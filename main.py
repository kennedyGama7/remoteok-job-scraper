from src.scraper import coletar_vagas
from src.excel import salvar_excel
from src.logger import logger


logger.info("Programa iniciado")

try:

    tecnologia = input("Digite a tecnologia: ").capitalize().strip()

    logger.info(f"Tecnologia pesquisada: {tecnologia}")

    lista_vagas = coletar_vagas(tecnologia)

    print("Salvando planilha...")
    salvar_excel(lista_vagas, tecnologia)

    logger.info(f"{len(lista_vagas)} vagas encontradas")
    logger.info("Planilha salva com sucesso")

    print(f"Foram encontradas {len(lista_vagas)} vagas.")
    print("Arquivo salvo com sucesso!")


except Exception as erro:
    logger.exception("Erro durante a execução")
    print("Ocorreu um erro durante a execução.")
    print("Consulte o arquivo logs/app.log para mais detalhes.")
finally:
    logger.info("Programa encerrado")
