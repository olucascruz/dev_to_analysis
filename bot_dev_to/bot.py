from botcity.web import WebBot
from scraping_data import devto_scraping_data
import json
import csv
from config.bot_config import webbot_config

def main():
    webbot = webbot_config(WebBot())
    # Opens the dev.to website.
    webbot.browse("https://dev.to/top/week")
    # Implement here your logic...
    webbot.maximize_window()
  
    list_dict_stories = devto_scraping_data(webbot)

    for story_dict in list_dict_stories:
        story_dict["tags"] = ', '.join(story_dict["tags"])

    json_file_path = "results/data.json"
    csv_file_path = "results/data.csv"

    with open(json_file_path, "w") as arquivo_json:
        json.dump(list_dict_stories, arquivo_json)

    header = list_dict_stories[0].keys()

    with open(csv_file_path, "w", newline="", encoding="utf-8") as arquivo_csv:
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
    webbot.wait(3000)
    webbot.stop_browser()
    

if __name__ == '__main__':
    main()
    