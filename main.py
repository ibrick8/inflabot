import os
import re
import locale
import argparse
import logging
from uuid import UUID

from domain.entidades.PosteoEntity import PosteoEntity
from domain.interfaces.IUseCase import IUseCase
from application.CanastaHoy import CanastaHoy
from application.InflacionCanasta import InflacionCanasta
from application.CostoImpuestosCanasta import CostoImpuestosCanasta
from application.GenerateIndex import GenerateIndex
from infraestructure.db.models import Session
from infraestructure.db.PostgresRepository import PostgresRepository
from config import OUTPUT_DIR, TITLE, LOG_LEVEL, SITE_BASE_URL

try:
    locale.setlocale(locale.LC_TIME, "es_AR.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "Spanish_Argentina.1252")
    except locale.Error:
        pass


def camel_to_snake(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name).lower()


def generar_nombre_archivo(posteo: PosteoEntity) -> str:
    dia = posteo.fecha.day
    mes_nombre = posteo.fecha.strftime("%B").lower()
    anio = posteo.fecha.year
    tipo_snake = camel_to_snake(posteo.tipo)
    return f"{tipo_snake}-{dia}-{mes_nombre}-{anio}.html"


def save(html: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


TIPOS = {
    "CanastaHoy": CanastaHoy,
    "InflacionCanasta": InflacionCanasta,
    "CostoImpuestosCanasta": CostoImpuestosCanasta,
}


def crear_pagina(posteo_id: UUID, logger: logging.Logger):
    repo = PostgresRepository(Session())
    posteo: PosteoEntity = repo.obtener_posteo(posteo_id)
    if not posteo:
        raise ValueError(f"Posteo con id {posteo_id} no encontrado")

    if posteo.tipo not in TIPOS:
        raise ValueError(f"No existe renderer de blog para tipo '{posteo.tipo}'")

    filename = generar_nombre_archivo(posteo)
    file_path = os.path.join(OUTPUT_DIR, "posts", filename)

    usecase: IUseCase = TIPOS[posteo.tipo](logger)
    post_page = usecase.run(posteo, filename)
    save(post_page, file_path)
    logger.info(f"{file_path} generado.")

    post_url = f"{SITE_BASE_URL.rstrip('/')}/posts/{filename}"
    repo.actualizar_post_url(posteo_id, post_url)
    logger.info(f"post_url actualizado: {post_url}")

    index_page = GenerateIndex(logger).run("index")
    save(index_page, os.path.join(OUTPUT_DIR, "index.html"))
    logger.info("Index actualizado.")


def main():
    parser = argparse.ArgumentParser(
        description="Genera páginas HTML del blog a partir de posteos"
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_crear = subparsers.add_parser(
        "crear_pagina", help="Crea una página para un posteo dado y actualiza el index"
    )
    parser_crear.add_argument(
        "-i", "--id", type=UUID, required=True, help="ID del posteo"
    )

    args = parser.parse_args()

    logger = logging.getLogger(TITLE)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, LOG_LEVEL))

    if args.comando == "crear_pagina":
        crear_pagina(args.id, logger)


if __name__ == "__main__":
    main()
