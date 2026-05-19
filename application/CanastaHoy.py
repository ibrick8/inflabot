import shutil
from jinja2 import Environment, FileSystemLoader

from domain.interfaces.IUseCase import IUseCase
from domain.entidades.PosteoEntity import PosteoEntity
from config import TEMPLATE_DIR, IMAGE_INPUT_DIR, IMAGE_OUTPUT_DIR

class CanastaHoy(IUseCase):
    
    def __init__(self, logger):
        self.logger = logger

    def run(self, posteo: PosteoEntity, filename: str):
 
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{posteo.tipo}.html")

        composicion_por_categoria_plot_file = posteo.cuerpo['images']['composicion_por_categoria_plot_file']
        concentracion_acumulada_plot_file = posteo.cuerpo['images']['concentracion_acumulada_plot_file']

        origen = f"{IMAGE_INPUT_DIR}/{composicion_por_categoria_plot_file}"
        destino = f"{IMAGE_OUTPUT_DIR}/{composicion_por_categoria_plot_file}"
        shutil.copy(origen, destino)

        origen = f"{IMAGE_INPUT_DIR}/{concentracion_acumulada_plot_file}"
        destino = f"{IMAGE_OUTPUT_DIR}/{concentracion_acumulada_plot_file}"
        shutil.copy(origen, destino)

        return template.render(
            **posteo.cuerpo,
            canonical_url = f"https://ibrick8.github.io/inflabot/posts/{filename}",
            og_image_url = f"https://ibrick8.github.io/inflabot/assets/{composicion_por_categoria_plot_file}",
            graficas = {"concentracion_acumulada_plot_file": concentracion_acumulada_plot_file, 
                        "composicion_por_categoria_plot_file": composicion_por_categoria_plot_file }
        )