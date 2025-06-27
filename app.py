from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
    sleep(1)
    driver.execute_script('window.scrollBy(0, -100)')
    sleep(2)
    proxima_atividade = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mt-8']/ul//a[@class='nui-button-icon nui-button-curved nui-button-small nui-button-default flex w-[50px] items-center justify-center']")))
    print(proxima_atividade)
    sleep(1)
    proxima_atividade.click()

def descer_ate_o_fim_da_pagina(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def avancar_button_click(wait):
    botao_avancar = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[text()='Avançar']")))
    sleep(2)
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
    e_uma_questao_value = None
    titulo_texto = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-2xl font-normal']"))).text
    print('Texto do título: ',titulo_texto)
    if 'Quest' in titulo_texto:
        e_uma_questao_value = True
    else:
        e_uma_questao_value = False
    return e_uma_questao_value


def selecionar_alternativa(wait, index_da_alternativa):
    alternativas = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='h5p-answers']//li")))
    print(alternativas[index_da_alternativa])
    sleep(1)
    alternativas[index_da_alternativa].click()


def tentar_novamente_button_click(wait):
    # tentar_novamente_button_click() -> Função
    tentar_novamente_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[text()=' Tentar novamente ']")))
    print(tentar_novamente_button)
    sleep(1)
    tentar_novamente_button.click()


def acertou_a_questao(wait):
    '''Verifica se acertou ou não a questão'''
    acertou = None

    mensagens_possiveis = {'erro': ['Ops, não foi dessa vez... tente novamente!', 'Ops, não foi dessa vez... Tente novamente!'], 'acerto': ['Parabéns pelo seu desempenho, siga para o próximo desafio.', 'Muito bem! Siga para a próxima questão.']}
    mensagem_de_feedback = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='h5p-question-feedback-content-text']"))).text
    print('Mensagem de feedback:', mensagem_de_feedback)

    for key, lista_mensagens in mensagens_possiveis.items():
        if mensagem_de_feedback in lista_mensagens:
            if key == 'erro':
                acertou = False
            else:
                acertou = True

    print('Acertou: ',acertou)
    return acertou


def tentar_denovo_avancar_ou_concluir_button_click(wait):
    botao_em_questao = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[@class='me-2 text-sm font-medium']")))
    texto_do_botao = botao_em_questao.text
    print('Texto do botao:[',texto_do_botao,']')
    
    opcoes = ['Avançar', 'Tentar novamente', 'Concluir atividade']
    if texto_do_botao in opcoes:
        sleep(2)
        botao_em_questao.click()
    else:
        print('Texto não encontrado')
        sleep(2)
        botao_em_questao.click()
        opcoes.append(texto_do_botao)
        print('Novo possível texto de botão adicionado')

    return texto_do_botao


def responder_questao(driver, wait):
    # Espera até o quadro de questões aparecer

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
    sleep(2)
    verificar_button_click(wait)

    # Verifica se o usuario acertou a questão
    acertou = acertou_a_questao(wait)
    sleep(1)
    
    # Avança ou tenta novamente a questão
        # atributo class do botao conluir_atividade: nui-button nui-button-medium nui-button-curved nui-button-solid nui-button-primary
        # Xpath botao concluir atividade: //div//span[text()='Concluir atividade']
        # XPATH div de conteúdos: //div//span[text()[contains(.,' Conteúdos: 6/6')]]
    driver.switch_to.default_content()
    sleep(1)
    texto_do_botao = tentar_denovo_avancar_ou_concluir_button_click(wait)
    sleep(2)
    return texto_do_botao


def voltar_para_home_sergoias(driver):
    driver.get('https://sergoias.portal.sagreseduca.com.br/dashboards/home-student/')


def completar_atividade_ativa(driver, wait):
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Atividade concluída ']")))
    descer_ate_o_fim_da_pagina(driver)
    sleep(1)

    #--- Verifica se a div do video carregou ---
    sleep(2)

    # --- Algoritmo que completa as atividades ---
    texto_do_botao = ''
    while texto_do_botao != 'Concluir atividade':
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='nui-card nui-card-curved nui-card-white relative p-4 sm:p-6']")))
        e_questao = e_uma_questao(wait)
        print('É questão: ',e_questao)
        if e_questao == True:
            sleep(1)
            texto_do_botao = responder_questao(driver, wait)
            print('Uma questão concluída')

        else:
            sleep(2)
            avancar_button_click(wait)
            print('Um vídeo concluído')
            sleep(2)
    print('Atividade concluída')


# --- Executing ---
matricula = str(input('Digite sua matricula do net escola: '))
senha = str(input('Digite sua senha do net escola: '))
from selenium_starting import driver, wait
original_handle = driver.current_window_handle

# -- Acessando o ser Goiás --
navegar_ate_o_site(driver)
logar_netescola(matricula, senha, wait)
sleep(5)
acessar_sergoias(wait, driver, original_handle)
sleep(10)

# - Selecionando e concluíndo próxima atividade
for c in range(0, 10):
    selecionar_nova_atividade(wait, driver)
    sleep(5)
    completar_atividade_ativa(driver, wait)
    voltar_para_home_sergoias(driver)
print('Atividades concluídas: ', c)
# input()
driver.close()
