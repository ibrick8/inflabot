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


class CostoImpuestosCanasta(IUseCase):

    def __init__(self, logger):
        self.logger = logger

    def run(self, posteo: PosteoEntity, filename: str):
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{posteo.tipo}.html")

        images = posteo.cuerpo.get("images") or {}
        comparacion = _copiar_imagen(images.get("comparacion_impuestos_plot_file"))
        carga = _copiar_imagen(images.get("carga_impositiva_categoria_plot_file"))

        return template.render(
            **posteo.cuerpo,
            canonical_url=f"{SITE_BASE_URL}/posts/{filename}",
            og_image_url=f"{SITE_BASE_URL}/assets/{comparacion}" if comparacion else None,
            graficas={
                "comparacion_impuestos_plot_file": comparacion,
                "carga_impositiva_categoria_plot_file": carga,
            },
        )
