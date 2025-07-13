import re
import locale
import argparse
import logging
from uuid import UUID

from domain.entidades.PosteoEntity import PosteoEntity 
from domain.interfaces.IUseCase import IUseCase
from application.DistribucionPreciosCategorias import DistribucionPreciosCategorias
from application.VariacionSemanalTipoArticulos import VariacionSemanalTipoArticulos
from application.GenerateIndex import GenerateIndex
from infraestructure.db.models import Session
from infraestructure.db.PostgresRepository import PostgresRepository
from config import OUTPUT_DIR, TITLE, LOG_LEVEL

locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')

def camel_to_snake(name):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '-', name).lower()

def generar_nombre_archivo(posteo: PosteoEntity):
    dia = posteo.fecha.day
    mes_nombre = posteo.fecha.strftime('%B').lower()  # ej: "julio"
    anio = posteo.fecha.year
    tipo_snake = camel_to_snake(posteo.tipo)
    return f"{tipo_snake}-{dia}-{mes_nombre}-{anio}.html"

def save(html: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

def main(posteo_id: UUID):

    logger = logging.getLogger(TITLE)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, LOG_LEVEL))

    repo = PostgresRepository(Session())
    posteo: PosteoEntity = repo.obtener_posteo(posteo_id)
    if not posteo: 
            raise Exception("Post Not Found")

    tipos = {
        "DistribucionPreciosCategorias": DistribucionPreciosCategorias,
        "VariacionSemanalTipoArticulos": VariacionSemanalTipoArticulos,
    }
    
    file=f"{OUTPUT_DIR}/posts/{generar_nombre_archivo(posteo)}"
    usecase: IUseCase = tipos[posteo.tipo](logger)
    post_page = usecase.run(posteo)
    save(post_page, file)
    logger.info(f"{file} generado.")

    index_page = GenerateIndex(logger).run("index")
    save(index_page, f"{OUTPUT_DIR}/index.html")
    logger.info("Index actualizado.")
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Crea una pagina para un posteo dado y actualiza el index")
    subparsers = parser.add_subparsers(dest='comando', required=True)
    parser_crear_posteo = subparsers.add_parser('crear_pagina', help='Crea una pagina para un posteo dado')
    parser_crear_posteo.add_argument('-i', '--id', type=UUID, required=True, help='ID del posteo')
    args, _ = parser.parse_known_args()

    main(args.id)