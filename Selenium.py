from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializa o navegador Chrome com o gerenciador automático de driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abre o site
driver.get("https://www.hashtagtreinamentos.com/")

# Maximiza a janela
driver.maximize_window()

# Encontra e clica no botão verde
botao_verde = driver.find_element("class name", "botao-verde")
botao_verde.click()

# Dentro de todos os elementos com a classe "header__titulo", clica no que contém "Assinatura"
botoes_header = driver.find_elements("class name", "header__titulo")

for botao in botoes_header:
    if "Assinatura" in botao.text:
        botao.click()
        break

# Troca para a nova janela/aba aberta
abas = driver.window_handles
driver.switch_to.window(abas[1])

# Abre o link diretamente (opcional, já que ele clicou no botão anteriormente)
driver.get("https://www.hashtagtreinamentos.com/curso-python?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=programacao")

# Preenche o campo de nome
driver.find_element("id", "firstname").send_keys("Vinicius Camargo")

# Preenche o campo de email
campo_email = driver.find_element("id", "email")
campo_email.send_keys("viniciusc.2005@gmail.com")

# Aguarda 20 segundos antes de encerrar ou seguir
time.sleep(20)
