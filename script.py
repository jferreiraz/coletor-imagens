from botcity.web import WebBot, By, PageLoadStrategy
from botcity.web.browsers.chrome import default_options
from selenium.webdriver.common.keys import Keys

from functions import *

class Bot(WebBot):
    def __init__(self):
        super().__init__()

    def on_start(self):
        self.headless = False

        def_options = default_options(
            headless=bot.headless,
            download_folder_path= "C:\MeusProjetos\coletor-imagens\Dados",
            user_data_dir=None,
            page_load_strategy=PageLoadStrategy.NORMAL
        )

        self.options = def_options
        self.driver_path = "Driver/chromedriver.exe"
        
        self.browse("https://www.linkedin.com/search/results/people/?origin=COMPANY_PAGE_CANNED_SEARCH&schoolFilter=%5B%222848413%22%5D&sid=_ih")
        self.maximize_window()
        self.realizar_download()

    def realizar_download(self):

        self.kb_type("email")
        self.tab()
        self.kb_type("senha")
        self.enter()

        clicar_elemento(self, selector="/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[1]/div/div/div/div[1]/div/a/div/div/div/img", by=By.XPATH)
       #clicar_elemento(self, selector="/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[1]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]", by=By.XPATH)
       #clicar_elemento(self, selector="/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[--(Variavel aqui)--]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]", by=By.XPATH)

        clicar_elemento(self, selector="/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[1]/div/button/img", by=By.XPATH)

        imagemPerfil = self.find_element("/html/body/div[4]/div/div/div[2]/div/img", By.XPATH)
        
        self.wait_for_element_visibility(element=imagemPerfil, visible=True, waiting_time=10000)

        screen_width, screen_height = self.display_size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        self.right_click_at(center_x, center_y)
        

        time.sleep(2)

        # Adding an image to the image map that is in a specific directory.

        # self.find(label="image", matching=0.6, waiting_time=10000)
        # #    print("image not found")
        # self.click()
        
        self.type_down()
        self.type_down()
        self.enter()

        self.kb_type("minha_imagem")
        self.enter()

        if not self.find(label="X", matching=0.8, waiting_time=10000):
            print("x not find")
        self.click()

        self.back()

        clicar_elemento(self, selector="/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[4]/div/div/button[2]/span", by=By.XPATH)

bot = Bot()
bot.on_start()