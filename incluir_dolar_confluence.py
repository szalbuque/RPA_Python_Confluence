import requests
import pyautogui
import time

def find_image(filename):
    """Finds on screen the image contained in the file filename

    Args:
        filename (string): name of the file containing the image in PNG format

    Returns:
        tuple (x,y,width,height): position and dimensions of the image in the screen
    """
    while not pyautogui.locateOnScreen(filename):
        time.sleep(1)
    return pyautogui.locateOnScreen(filename)

# use an API to obtain the dolar of the day, in brazilian real

link = "http://economia.awesomeapi.com.br/json/last/USD-BRL"

req = requests.get(link).json()
dolar_value = eval(req["USDBRL"]['high'])

# sets the default pause interval between pyautogui commands
pyautogui.PAUSE = 1
# opens a Chrome window
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# opens the page that will be updated
pyautogui.write('https://szalbuque.atlassian.net/wiki/spaces/TEAM/pages/edit-v2/557092')
pyautogui.press('enter')
pyautogui.hotkey('f11')

# finds on screen the position of the image of the dolar value field
x,y,largura, altura = find_image('dolar.png')
 
# clicks just after the image
pyautogui.click(x + largura + 4 , y + altura/2)

# selects the text to be updated
pyautogui.hotkey('shift','end')
dolar_value_formated = "R$ {:2.2f}".format(dolar_value)
pyautogui.write(dolar_value_formated)

# publish the page updated
x,y,largura, altura = find_image('publicar.png')
pyautogui.click(x + largura/2, y + altura/2)