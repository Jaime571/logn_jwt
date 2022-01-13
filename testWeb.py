from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.cedulaprofesional.sep.gob.mx/cedula/presidencia/indexAvanzada.action')
time.sleep(2)

nameBox = driver.find_element(By.XPATH, '//*[@id="nombre"]')
nameBox.send_keys("Manuel")

paternoBox = driver.find_element(By.XPATH, '//*[@id="paterno"]')
paternoBox.send_keys("Avila")

maternoBox = driver.find_element(By.XPATH, '//*[@id="materno"]')
maternoBox.send_keys("Hernandez")

continuarBtnBox = driver.find_element(By.XPATH, '//div[@class="pull-right text-muted text-vertical-align-button"]//span[@id="dijit_form_Button_0_label"]')
continuarBtnBox.click()

time.sleep(5)
#Resultados de las cédulas
def busqueda():
    cedulasNumero = driver.find_elements(By.XPATH, '//div[@class="dojoxGridRow" or @class="dojoxGridRow dojoxGridRowOdd"]//td[@idx = 0]')
    cedulasNombre = driver.find_elements(By.XPATH, '//div[@class="dojoxGridRow" or @class="dojoxGridRow dojoxGridRowOdd"]//td[@idx = 1]')

    for cedula, nombre in zip(cedulasNumero, cedulasNombre):
        #En las pruebas realizadas, el nombre a analizar debe estar en mayúsculas
        if(cedula.text == "839464" and nombre.text == "VICTOR MANUEL"):
            return print(f'{cedula.text} {nombre.text}')

    #En este bloque se prevee que el botón cambie de clase y elemento HTML por lo que el elemento no se encotraría
    #dando una excepción, por lo que primero se verifica y en caso de no poder encontrarla, se sale del ciclo
    try:
        siguienteBtn = driver.find_element(By.XPATH, '//div[@class="bottom-buffer"]/ul[@class = "pagination"]//a[@class="pager-next"]')
        siguienteBtn.click()
        #Recursividad que cura
        busqueda()
    except NoSuchElementException:
        return None

resultado = busqueda()
print (resultado)
driver.close()
