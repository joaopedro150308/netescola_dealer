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

def acessar_sergoias(wait):
    botao_link_sergoias = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-bcXHqe fcTwxh']/a[1]")))
    sleep(1)
    botao_link_sergoias.click()


# --- Executing ---
matricula = str(input('Digite sua matricula do net escola: '))
senha = str(input('Digite sua senha do net escola: '))
from selenium_starting import driver, wait
navegar_ate_o_site(driver)
logar_netescola(matricula, senha, wait)
sleep(5)
acessar_sergoias(wait=wait)
input()