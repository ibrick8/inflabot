import os
from jinja2 import Environment, FileSystemLoader

from config import TEMPLATE_DIR, OUTPUT_DIR


class GenerateIndex:
    def __init__(self, logger):
        self.logger = logger

    def extraer_nombre_y_fecha(self, nombre_archivo: str):
        nombre_sin_ext = nombre_archivo.replace(".html", "")
        partes = nombre_sin_ext.split("-")
        nombre_reporte = "-".join(partes[:-3])
        fecha_str = "-".join(partes[-3:])
        return nombre_reporte, fecha_str

    def run(self, template_file: str):
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(f"{template_file}.html")

        posts_dir = os.path.join(OUTPUT_DIR, "posts")
        os.makedirs(posts_dir, exist_ok=True)
        archivos = os.listdir(posts_dir)

        informes = []
        for archivo in sorted(archivos, reverse=True):
            if not archivo.endswith(".html"):
                continue
            nombre, fecha = self.extraer_nombre_y_fecha(archivo)
            informes.append(
                {
                    "fecha": fecha,
                    "titulo": nombre.replace("-", " ").title(),
                    "link": f"posts/{archivo}",
                }
            )

        return template.render(informes=informes)
