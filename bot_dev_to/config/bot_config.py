from botcity.web import WebBot, Browser, PageLoadStrategy
from botcity.web.browsers.edge import default_options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def webbot_config(webbot:WebBot, headless:bool=False)-> None:
    """
    Configures the settings for a WebBot instance.

    Args:
        webbot (WebBot): The WebBot instance to configure.
        headless (bool, optional): Whether to run in headless mode. Defaults to False.

    Note:
        This function configures various settings for the WebBot instance, such as
        the browser type, WebDriver path, download folder path, and additional
        browser arguments.
    """
    
    
    # Configure whether or not to run on headless mode
    webbot.headless = headless

    webbot.browser = Browser.EDGE

    # set the WebDriver path
    webbot.driver_path = EdgeChromiumDriverManager().install()

    def_options = default_options(
        headless=webbot.headless,
        download_folder_path=r"bot_dev_to\results",
        user_data_dir=None,  # Informing None here will generate a temporary directory
        page_load_strategy=PageLoadStrategy.NORMAL
    )

    # Add your customized argument
    def_options.add_argument("--inprivate")
    # Update the options to use the customized Options.
    webbot.options = def_options
