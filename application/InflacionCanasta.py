import os
import shutil
from jinja2 import Environment, FileSystemLoader

from domain.interfaces.IUseCase import IUseCase
from domain.entidades.PosteoEntity import PosteoEntity
from config import TEMPLATE_DIR, IMAGE_INPUT_DIR, IMAGE_OUTPUT_DIR, SITE_BASE_URL


def _copiar_imagen(filename: str):
    if not filename:
        return None
    os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)
    origen = os.path.join(IMAGE_INPUT_DIR, filename)
    destino = os.path.join(IMAGE_OUTPUT_DIR, filename)
    if not os.path.isfile(origen):
        raise FileNotFoundError(f"No se encontró la imagen {origen}")
    shutil.copy(origen, destino)
    return filename


class InflacionCanasta(IUseCase):

    def __init__(self, logger):
        self.logger = logger

    def run(self, posteo: PosteoEntity, filename: str):
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{posteo.tipo}.html")

        images = posteo.cuerpo.get("images") or {}
        inflacion_plot = _copiar_imagen(images.get("inflacion_por_categoria_plot_file"))
        comparacion_plot = _copiar_imagen(images.get("comparacion_gastos_plot_file"))

        return template.render(
            **posteo.cuerpo,
            canonical_url=f"{SITE_BASE_URL}/posts/{filename}",
            og_image_url=f"{SITE_BASE_URL}/assets/{inflacion_plot}" if inflacion_plot else None,
            graficas={
                "inflacion_por_categoria_plot_file": inflacion_plot,
                "comparacion_gastos_plot_file": comparacion_plot,
            },
        )
