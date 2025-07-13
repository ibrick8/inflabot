import os
from jinja2 import Environment, FileSystemLoader

from config import TEMPLATE_DIR, OUTPUT_DIR

class GenerateIndex():
    
    def __init__(self, logger):
        self.logger = logger

    def extraer_nombre_y_fecha(self, nombre_archivo):
        partes = nombre_archivo.split('-')
        nombre_reporte = '-'.join(partes[:-3])
        fecha_str = '-'.join(partes[-3:])
        return nombre_reporte, fecha_str

    def run(self, template_file:str):
 
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{template_file}.html")
        
        archivos = os.listdir(f"{OUTPUT_DIR}/posts")

        informes = []
        for archivo in sorted(archivos, reverse=True):
            if archivo != "index.html":
                
                nombre, fecha = self.extraer_nombre_y_fecha(archivo)
                informes.append({
                    "fecha": f"📅 {fecha}",
                    "titulo": nombre,
                    "link": f"posts/{archivo}"
                })
            
        return template.render(informes=informes)
