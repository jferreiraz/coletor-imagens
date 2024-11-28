import time
from botcity.web import WebBot, By

def clicar_elemento(bot: WebBot, selector, by, tempo_maximo=100, tempo_espera=2):
    elemento = bot.find_element(selector=selector, by=by)
    tempo_decorrido = 0

    while tempo_decorrido < tempo_maximo:
        try:
            elemento.click()  
            break 
        except:
            print("Elemento não clicado, tentando novamente...")
            time.sleep(tempo_espera) 
            tempo_decorrido += tempo_espera

    if tempo_decorrido >= tempo_maximo:
        print(f"Falha ao clicar no elemento após {tempo_maximo} segundos.")

def rolar_e_clicar(bot: WebBot, selector, by, tempo_maximo=20, tempo_espera=2, scroll='down'):
    tempo_decorrido = 0

    while tempo_decorrido < tempo_maximo:
        try:
            elemento = bot.find_element(selector=selector, by=by)
            elemento.click()  
            print("Elemento clicado com sucesso!")
            break  
        except Exception as e:
            print(f"Elemento não clicado, tentando novamente... Erro: {e}")
            if scroll == 'down':
                bot.execute_javascript("window.scrollBy(0, 300);")  
            elif scroll == 'up':
                bot.execute_javascript("window.scrollBy(0, -300);")  
            time.sleep(tempo_espera) 
            tempo_decorrido += tempo_espera

    if tempo_decorrido >= tempo_maximo:
        print(f"Falha ao clicar no elemento após {tempo_maximo} segundos de tentativa com rolagem.")

def realizar_login(bot: WebBot, usuario, senha):
    usuarioLogin = bot.find_element(selector="MainContent_txtUsuario", by=By.ID)
    usuarioLogin.send_keys(usuario)

    senhaLogin = bot.find_element(selector="MainContent_txtSenha", by=By.ID)
    senhaLogin.send_keys(senha)

    botaoLogin = bot.find_element(selector="MainContent_btnLogin", by=By.ID)
    botaoLogin.click()