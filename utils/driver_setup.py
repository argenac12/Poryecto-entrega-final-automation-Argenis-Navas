import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def create_driver():
    # Inicializar el navegador Chrome usando webdriver-manager
    chrome_options = Options()

    running_in_ci = os.environ.get("CI") == "true"

    if running_in_ci:
        # Configuraciones para CI/CD
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-software-rasterizer")
    else:
        # Iniciar maximizado y en incógnito
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")

    # Evitar popups de Chrome
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_leak_detection": False,
        "signin.allowed": False
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Evitar log
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver