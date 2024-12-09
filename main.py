######### OBSERVAÇÃO #########
'''
Esse Código Precisa de Tratamento, já que não consegue acessar empresas como a S E I.
'''
######### OBSERVAÇÃO #########


from playwright.sync_api import Playwright, sync_playwright
import time
import json
import pandas as pd

#with open("cookies2.json", "r") as f:
    #cookies = json.load(f) #

'''Cookies não foram disponibilizados no Github, mas podem ser utilizados novos cookies, 
basta criar um arquivo json e colocá-los nele.'''

empresas = []
urls_acessadas = [] 
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  # Browser
    context = browser.new_context()  # Window
    page = context.new_page()  # Tab
    #page.context.add_cookies(cookies)

    
    page.goto("https://www.econodata.com.br/empresas/pa-belem/servicos")
    #time.sleep(2)
    page.click('text=Ver ranking completo')
    #time.sleep(2000)

    num_pagina = 0
    url_template = "https://www.econodata.com.br/maiores-empresas/pa-belem/servicos?pagina={num_pagina}"
    base_url = "https://www.econodata.com.br"
    aux = 0

    while len(empresas) < 20:#50  
        num_pagina += 1
        url_pagina = url_template.format(num_pagina=num_pagina)
        print(f"Acessando página {num_pagina}...")

        #time.sleep(2000)


        try:
            page.goto(url_pagina, wait_until="load")
            time.sleep(2)   
        except Exception as e:
            print(f"Erro ao acessar {url_pagina}: {e}")
            #continue
            break

        empresa_links = page.locator("div#maiores-empresas-card-tabela a").all()

        for link in empresa_links:
            if len(empresas) >= 20:
                break

            href = link.get_attribute("href")
            
            if href.startswith("/"):  
                href = base_url + href  

            if href in urls_acessadas:
                continue  
            '''
            try:
                page.goto(href, wait_until='load')
            except:
                print('Erro. Pulando Empresa.')
                urls_acessadas.append(href)
                continue
            '''

            page.goto(href, wait_until='load')
            #time.sleep(2)
    
            dados = {
                "atividade_economica": page.locator("#item-detalhe-valor-com-link-tooltip-ativ-economica").inner_text() if page.locator("#item-detalhe-valor-com-link-tooltip-ativ-economica") else None,
                "razao_social": page.locator("#item-detalhe-valor-razao-social").inner_text() if page.locator("#item-detalhe-valor-razao-social") else None,
                "cnpj": page.locator("#item-detalhe-valor-cnpj").inner_text() if page.locator("#item-detalhe-valor-cnpj") else None,
                "situacao": page.locator("#item-detalhe-valor-situacao").inner_text() if page.locator("#item-detalhe-valor-situacao") else None,
                "endereco": page.locator("div.my-auto.w-full.subitem-subtext.flex.flex-col").first.inner_text() if page.locator("div.my-auto.w-full.subitem-subtext.flex.flex-col").first.inner_text() else None,
            }

            empresas.append(dados)
            print(empresas[aux])
            aux = aux + 1
            urls_acessadas.append(href) 

            page.goto(url_pagina, wait_until='load')
            #page.go_back(wait_until='load')
            #time.sleep(2)

        #num_pagina += 1

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

df_empresas = pd.DataFrame(empresas)
df_empresas.to_csv('empresas.csv')

with open("empresas.json", "w", encoding="utf-8") as f:
    json.dump(empresas, f, ensure_ascii=False, indent=4)





#----------------------- Código pra Logar Sem Cookies -----------------------#

'''
page.click("#user-account-mini-menu-botao-entrar-desktop", force=True)
page.click("#user-account-mini-menu-botao-entrar-desktop", force=True)
time.sleep(2)
page.wait_for_selector("#emailInput", timeout=5000)
page.fill("#emailInput", 'email_here')
time.sleep(2)
#page.click('text=Continuar')
'''
#----------------------- Código pra Logar Sem Cookies -----------------------#
