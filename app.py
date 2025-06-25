from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import TimeoutException


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
    descer_ate_o_fim_da_pagina(driver)
    sleep(2)
    proxima_atividade = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mt-8']/ul//a[@class='nui-button-icon nui-button-curved nui-button-small nui-button-default flex w-[50px] items-center justify-center']")))
    print(proxima_atividade)
    sleep(1)
    proxima_atividade.click()

def descer_ate_o_fim_da_pagina(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def avancar_button_click(wait):
    botao_avancar = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[text()='Avançar']")))
    print(botao_avancar)
    sleep(2)
    botao_avancar.click()


def verificar_button_click(wait):
    botao_verificar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='h5p-question-check-answer h5p-joubelui-button']")))
    print(botao_verificar)
    sleep(1)
    botao_verificar.click()

def e_uma_questao(wait):
    '''Verifica se o usuário está respondendo uma questão, ou se é apenas uma vídeo aula.'''
    try:
        texto_questao = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Questões']")))
        print('É uma questão')
        return True
    except TimeoutException:
        print('Não é uma questão')
        return False


def selecionar_alternativa(wait, index_da_alternativa):
    alternativas = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='h5p-answers']//li")))
    print(alternativas[index_da_alternativa])
    sleep(1)
    alternativas[index_da_alternativa].click()


def responder_questao(driver, wait):
    # Espera até o quadro de questões aparecer
    # input()

    # --- Entrar no Iframe ---
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//div//iframe")))
    sleep(2)
    driver.switch_to.frame(iframe)
    sleep(2)

    quadro_questoes = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='h5p-answers']//li")))
    print(quadro_questoes)
    driver.switch_to.default_content()
    sleep(2)
    descer_ate_o_fim_da_pagina(driver)
    sleep(2)
    driver.switch_to.frame(iframe)

    # Seleciona uma alternativa
    selecionar_alternativa(wait, 0)
    verificar_button_click(wait)

    # Verifica se o usuario acertou a questão
    acertou = False
    try:
        mensagem_de_erro = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Ops, não foi dessa vez... tente novamente!']")))
    except TimeoutException:
        mensagem_de_acerto = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Muito bem! Siga para o próximo desafio.']")))
        acertou = True
    print('Acertou: ',acertou)

    # Avança ou tenta novamente a questão
        # atributo class do botao conluir_atividade: nui-button nui-button-medium nui-button-curved nui-button-solid nui-button-primary
    driver.switch_to.default_content()
    if acertou == False:
        try:
            # tentar_novamente_button_click() -> Função
            tentar_novamente_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[text()=' Tentar novamente ']")))
            print(tentar_novamente_button)
            sleep(1)
            tentar_novamente_button.click()
        except TimeoutException:
            avancar_button_click(wait)
    else:
        avancar_button_click(wait)


def completar_atividade_ativa(driver, wait):
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Atividade concluída ']")))
    descer_ate_o_fim_da_pagina(driver)
    sleep(1)

    #--- Verifica se a div do video carregou ---
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='nui-card nui-card-curved nui-card-white relative p-4 sm:p-6']")))
    sleep(2)

    # --- Algoritmo que completa as atividades ---

    e_questao = e_uma_questao(wait)
    print(e_questao)
    if e_questao == True:
        sleep(1)
        responder_questao(driver, wait)
        print('Uma questão concluída')

    else:
        avancar_button_click(wait)
        print('Um vídeo concluído')
        sleep(2)


# --- Executing ---
matricula = str(input('Digite sua matricula do net escola: '))
senha = str(input('Digite sua senha do net escola: '))
from selenium_starting import driver, wait
original_handle = driver.current_window_handle
navegar_ate_o_site(driver)
logar_netescola(matricula, senha, wait)
sleep(5)
acessar_sergoias(wait, driver, original_handle)
sleep(10)

selecionar_nova_atividade(wait, driver)
sleep(5)
completar_atividade_ativa(driver, wait)
input()