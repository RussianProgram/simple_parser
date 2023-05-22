from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from coindesk_parser import Parser
from config import URL, PAGES

def main():
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    try:
        driver = webdriver.Firefox(
            options=opts,
            keep_alive=False
            )
        
        print("Parser started")
        Parser(URL, PAGES).start_parser(driver)
        print("Parsing complete")
    except Exception as e:
        print(e)
    
    finally:
        print("Browser closed")
        driver.quit()
        


if __name__ == "__main__":
    main()
