from playwright.sync_api import sync_playwright
from src.models import Vaga
from src.logger import logger

def coletar_vagas(tecnologia):

    with sync_playwright() as p:

        

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="pt-BR"
        )

        page = context.new_page()

        page.goto("https://remoteok.com")
        
        vagas = page.locator("tr.job")


        lista_vagas = []

        for i in range(vagas.count()):

            try:
           

                vaga_atual = vagas.nth(i)

                tags_locators = vaga_atual.locator("div.tag")

                href = vaga_atual.locator(
                    'a[itemprop="url"]'
                ).get_attribute("href")
                link_completo = "https://remoteok.com" + href

                titulo = vaga_atual.locator('h2[itemprop="title"]').inner_text()
                empresa = vaga_atual.locator('h3[itemprop="name"]').inner_text()
                localizacao = vaga_atual.locator('.location').nth(0).inner_text()

                tags = []
                

                for indice_tag in range(tags_locators.count()):
                    
                    tags.append(tags_locators.nth(indice_tag).inner_text())
                    
                tags_normalizadas = [tag.capitalize()for tag in tags]



                if tecnologia in tags_normalizadas:

                    texto_tags = ", ".join(tags)

                    vaga = Vaga(
                        titulo=titulo,
                        empresa=empresa,
                        localizacao=localizacao,
                        link=link_completo,
                        tags=texto_tags
    )

                    lista_vagas.append(vaga)
            except Exception as erro:
                logger.exception(f"Erro ao processar a vaga {i}")
            
       
        
       

        return lista_vagas