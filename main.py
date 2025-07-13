import re
import locale
import datetime
from uuid import UUID

from domain.entidades.PosteoEntity import PosteoEntity 
from domain.interfaces.IUseCase import IUseCase
from application.DistribucionPreciosCategorias import DistribucionPreciosCategorias
from application.GenerateIndex import GenerateIndex
from infraestructure.db.models import Session
from infraestructure.db.PostgresRepository import PostgresRepository
from config import OUTPUT_DIR

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
    repo = PostgresRepository(Session())
    posteo: PosteoEntity = repo.obtener_posteo_con_metrica(posteo_id)
    if not posteo: 
            raise Exception("Post Not Found")

    tipos = {
        "DistribucionPreciosCategorias": DistribucionPreciosCategorias,
    }
    
    usecase: IUseCase = tipos[posteo.tipo](None)
    
    print("Generando archivo de posteo")
    post_page = usecase.run(posteo, "post_inflacion")
    save(post_page, f"{OUTPUT_DIR}/posts/{generar_nombre_archivo(posteo)}")
    
    print("Regenerando index.html")
    index_page = GenerateIndex(None).run("index")
    save(index_page, f"{OUTPUT_DIR}/index.html")

    print("Hecho")

if __name__ == "__main__":

    main(UUID('bf8486f9-daf1-4a75-b8d5-4b71e7602bdb'))