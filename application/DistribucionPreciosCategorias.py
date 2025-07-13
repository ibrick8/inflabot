from jinja2 import Environment, FileSystemLoader

from domain.interfaces.IUseCase import IUseCase
from domain.entidades.PosteoEntity import PosteoEntity
from config import TEMPLATE_DIR

class DistribucionPreciosCategorias(IUseCase):
    
    def __init__(self, logger):
        self.logger = logger

    def run(self, posteo: PosteoEntity):
 
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{posteo.tipo}.html")
        secciones = [(posteo.cuerpo[i], posteo.cuerpo[i+1]) for i in range(0, len(posteo.cuerpo), 2)]

        return template.render(fecha=posteo.fecha, secciones=secciones)
