from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Acessa o site do desafio
driver.get("https://rpachallengeocr.azurewebsites.net")

# Localiza a tabela pelo XPath
tabela = driver.find_element(By.XPATH, '//*[@id="tableSandbox"]')

# Pega todas as linhas da tabela (incluindo o cabeçalho)
linhas = tabela.find_elements(By.TAG_NAME, "tr")

# Itera sobre as linhas e imprime o texto de cada uma
linha = 1 
for linha_atual in linhas:
    print(f"Linha {linha}: {linha_atual.text}")
    linha += 1