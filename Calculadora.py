import pyautogui as pg
import time

# Aguardar 1 segundo para dar tempo do sistema reagir
time.sleep(1)

# Mover o mouse até o botão do Windows na parte inferior da tela
pg.moveTo(22, 1052)
time.sleep(1)

# Clicar no botão do Windows para abrir o menu iniciar
pg.click(22, 1056)
time.sleep(1)

# Digitar "calc" para buscar a calculadora no menu iniciar
pg.typewrite("calc")
time.sleep(1)

# Mover o mouse para o ícone da calculadora e clicar
pg.moveTo(221, 522)
pg.click()
