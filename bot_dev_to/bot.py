from botcity.web import WebBot, Browser, PageLoadStrategy
from botcity.web.browsers.edge import default_options
from scraping_data import devto_scraping_data
import json
import csv
def main():
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.EDGE

    # Uncomment to set the WebDriver path
    bot.driver_path = r"msedgedriver.exe"

    def_options = default_options(
        headless=bot.headless,
        download_folder_path=r"bot_dev_to\results",
        user_data_dir=None,  # Informing None here will generate a temporary directory
        page_load_strategy=PageLoadStrategy.NORMAL
    )

    # Add your customized argument
    def_options.add_argument("--inprivate")
    # Update the options to use the customized Options.
    bot.options = def_options
    
    # Opens the dev.to website.
    bot.browse("https://dev.to/top/week")
    # Implement here your logic...
    bot.maximize_window()
  
    list_dict_stories = devto_scraping_data(bot)

    for story_dict in list_dict_stories:
        story_dict["tags"] = ', '.join(story_dict["tags"])
    json_string = json.dumps(list_dict_stories)


    path_json = "results/data.json"
    path_csv = "results/data.csv"

    with open(path_json, "w") as arquivo_json:
        json.dump(json_string, arquivo_json)

    header = list_dict_stories[0].keys()
    with open(path_csv, "w", newline="", encoding="utf-8") as arquivo_csv:
        writer_csv = csv.DictWriter(arquivo_csv, fieldnames=header)
        
        # Escrever o cabeçalho
        writer_csv.writeheader()
        
        # Escrever os dados
        for dictionary in list_dict_stories:
            try:
                writer_csv.writerow(dictionary)
            except:
                continue

    print(list_dict_stories)
    print(len(list_dict_stories))
    
    # Wait 3 seconds before closing
    bot.wait(3000)
    bot.stop_browser()
    

if __name__ == '__main__':
    main()
    