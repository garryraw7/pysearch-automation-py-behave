from selenium import webdriver  # pip install selenium==3.5.0

chromeDriverExe = 'Files\Resources\Drivers\chrome\chromedriver.exe'


class Browser(object):
    print("\n\nInstantiate Driver via Browser Class\n\n")
    driver = webdriver.Chrome(executable_path=chromeDriverExe)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def quit(context):
        context.driver.quit()

