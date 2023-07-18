import requests
import pyautogui
import time

def localiza_imagem(nome_arquivo):
    while not pyautogui.locateOnScreen(nome_arquivo):
        time.sleep(1)
    posicao = pyautogui.locateOnScreen(nome_arquivo)
    return posicao

# buscar o valor do dólar do dia

link = "http://economia.awesomeapi.com.br/json/last/USD-BRL"

req = requests.get(link).json()
valor_dolar = eval(req["USDBRL"]['high'])

# configurar o tempo de pausa entre cada comando do pyautogui
pyautogui.PAUSE = 1
# entrar na página do confluence, considerar que já esteja logado
# abrir a navegação do windows
pyautogui.press('win')
# abrir o navegador (digitar 'chrome' e apertar 'enter')
pyautogui.write('chrome')
pyautogui.press('enter')

# clicar na barra de endereço, escrever o endereço e clicar em 'enter
pyautogui.write('https://szalbuque.atlassian.net/wiki/spaces/TEAM/pages/edit-v2/557092')
pyautogui.press('enter')
pyautogui.hotkey('f11')

# localizar na tela a posição da imagem referente ao campo do valor do dólar
x,y,largura, altura = localiza_imagem('dolar.png')
 
# clicar logo após a imagem
pyautogui.click(x + largura + 4 , y + altura/2)

# selecionar o conteúdo para substituir
pyautogui.hotkey('shift','end')
valor_dolar_formatado = "US$ {:2.2f}".format(valor_dolar)
pyautogui.write(valor_dolar_formatado)

# clicar em publicar
x,y,largura, altura = localiza_imagem('publicar.png')
pyautogui.click(x + largura/2, y + altura/2)