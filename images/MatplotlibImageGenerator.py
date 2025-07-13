import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
from matplotlib.font_manager import FontProperties

from settings import IMAGE_OUTPUT_DIR
from domain.interfaces.IImageGenerator import IImageGenerator

mpl.rcParams['font.family'] = 'Segoe UI Emoji'
emoji_font = FontProperties(fname="C:/Windows/Fonts/seguiemj.ttf")  # Ruta completa a Segoe UI Emoji

class MatplotlibImageGenerator(IImageGenerator):
    def __init__(self):
        sns.set_theme(style="whitegrid")

    def generar_imagen_categoria(self, data: list[tuple[str, float]], fecha: str, filename: str):
        categorias, valores = zip(*data)

        iconos = {
            "lacteos": "🧀",
            "leche": "🥛",
            "leche entera": "🥛",
            "aceite": "🫒",
            "aceite de girasol": "🌻",
            "alimento": "🍽️",
            "almacen": "📦",
            "limpieza": "🧼",
            "carnes": "🥩",
            "bebidas": "🥤"
        }

        categorias_icono = [f"{iconos.get(cat.lower(), '')} {cat}" for cat in categorias]
        df = pd.DataFrame({"Categoría": categorias_icono, "Variación": valores})

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = sns.barplot(data=df, x="Categoría", y="Variación", hue="Categoría", dodge=False, palette="crest", ax=ax, legend=False)

        for bar, val, label in zip(bars.patches, valores, categorias_icono):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.2,
                f"{val:.1f}%",
                ha="center",
                va="bottom",
                fontsize=9,
                fontproperties=emoji_font  # Usa la fuente emoji
            )

        ax.set_title(f"Inflación por categoría - {fecha}", fontsize=14, weight='bold', fontproperties=emoji_font)
        ax.set_ylabel("% Variación")
        ax.set_xlabel("")
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        for label in ax.get_xticklabels():
            label.set_fontproperties(emoji_font)

        fig.tight_layout()
        output_path = os.path.join(IMAGE_OUTPUT_DIR, filename)
        plt.savefig(output_path, dpi=150)
        plt.close(fig)
        return output_path