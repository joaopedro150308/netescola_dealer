from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def navegar_ate_o_site(driver):
    driver.get('https://portalnetescola.educacao.go.gov.br/')
    
def logar_netescola(matricula, senha, wait):
    campo_usuario = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Usuário']")))
    sleep(1)
    campo_usuario.click()
    sleep(1)
    campo_usuario.send_keys(matricula)
    sleep(1)
    campo_senha = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Senha']")))
    campo_senha.click()
    sleep(1)
    campo_senha.send_keys(senha)
    sleep(1)
    driver.execute_script('scrollBy(0, 200)')
    botao_logar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Logar']")))
    sleep(1)
    botao_logar.click()

def acessar_sergoias(wait, driver, original_handle):
    botao_link_sergoias = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-bcXHqe fcTwxh']/a[1]")))
    sleep(1)
    botao_link_sergoias.click()
    wait.until(EC.number_of_windows_to_be(2))
    janelas = driver.window_handles
    print(original_handle)
    print(janelas)
    for janela in janelas:
        if janela != original_handle:
            driver.switch_to.window(janela)
            break
    print(driver.current_window_handle)


def selecionar_nova_atividade(wait, driver):
    # input("Aperte qualquer tecla")
    perfil_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='nui-avatar-text']")))
    print(perfil_buttons)
    sleep(2)
    driver.execute_script('window.scrollBy(0, 1000);')
    sleep(2)
    proxima_atividade = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mt-8']/ul//a[@class='nui-button-icon nui-button-curved nui-button-small nui-button-default flex w-[50px] items-center justify-center']")))
    print(proxima_atividade)
    sleep(1)
    proxima_atividade.click()


# --- Executing ---
matricula = str(input('Digite sua matricula do net escola: '))
senha = str(input('Digite sua senha do net escola: '))
from selenium_starting import driver, wait
original_handle = driver.current_window_handle
navegar_ate_o_site(driver)
logar_netescola(matricula, senha, wait)
sleep(5)
acessar_sergoias(wait, driver, original_handle)
sleep(30)
selecionar_nova_atividade(wait, driver)
input()
