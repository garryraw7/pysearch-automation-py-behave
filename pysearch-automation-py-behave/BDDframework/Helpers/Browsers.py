from selenium import webdriver  # pip install selenium==3.5.0
import os

chromeDriverExe = 'Files\Resources\Drivers\chrome\chromedriver.exe'


class Browser:
    # Class variable should be used for driver. It will create one value of it.
    driver = None
    

    def __init__(self):
        print("\n\nInstantiate Driver via Browser Class\n\n")
        
        if 'nt' in os.name:			# windows users
            ## For Windows - rmeove comment on below line
            driver = webdriver.Chrome(executable_path=chromeDriverExe)
            #Below only works for Windows
            Browser.driver.maximize_window()
        else:  # linux, mac users

            # For Mac -
            # Download chromedriver from official link (notice version of Chrome browser)
            # Unpack *.zip file and file chromedriver copy to location usr/local/bin/
            # Remove any path you put in file and just go with driver = webdriver.Chrome()
            # For Mac - remove comment on below code
            Browser.driver=webdriver.Chrome()

        #Common code for All OS.    

        Browser.driver.implicitly_wait(30)
        Browser.driver.set_page_load_timeout(30)


    def close(self):
        Browser.driver.close()

    def quit(self):
        Browser.driver.quit()


if __name__=="__main__":
    "For testing purpose, if driver is launching properly or not"
    B = Browser()
    B.driver.get("https://google.com")
    B.quit()

