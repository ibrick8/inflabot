from jinja2 import Environment, FileSystemLoader

from domain.interfaces.IUseCase import IUseCase
from domain.entidades.PosteoEntity import PosteoEntity
from config import TEMPLATE_DIR

class VariacionSemanalTipoArticulos(IUseCase):
    
    def __init__(self, logger):
        self.logger = logger

    def run(self, posteo: PosteoEntity):
 
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{posteo.tipo}.html")
        secciones = {
            "titulo": posteo.cuerpo[0],
            "pie": posteo.cuerpo[-1],
            "items": posteo.cuerpo[1:-1],
        }
        return template.render(fecha=posteo.fecha, secciones=secciones)
