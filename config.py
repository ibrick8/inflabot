import os
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "docs"


REDIS_CHANNEL = "metricas"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
IMAGE_OUTPUT_DIR = "C:\\Users\\emili\\tmp\\"

POSTGRESQL_URL= os.environ.get("POSTGRESQL_URL", "postgresql://mi_user:mi_pass@db/mi_db")

ICONOS_CATEGORIAS = {
    "chocolates": "🍫",
    "leches": "🥛",
    "aceites": "🧴",
    "aguas": "💧",
    "gaseosas": "🥤",
    "carnes": "🥩",
    "cerveza": "🍺",
    "vino": "🍷",
    "jugos": "🧃",
    "arroz": "🍚",
    "legumbres": "🫘",
    "pastas listas y rellenas": "🥟",
    "pastas secas": "🍝",
    "harina de trigo": "🌾",
    "harina de maiz": "🌽",
    "azucar": "🍬",
    "condimentos": "🧂",
    "detergente": "🧼",
    "jabon liquido y en polvo": "🧴",
    "lavandinas liquidas": "🧪",
    "galletitas": "🍪",
    "panificados": "🍞",
    "frutas": "🍎",
    "verduras": "🥦",
    "shampoo": "🧴",
    "jabon": "🧼",
    "papel higienico": "🧻",
    "conservados": "🥫",
    "yougurt": "🥣",
    "manteca": "🧈",
    "queso": "🧀",
    "pollo": "🍗",
    "cerdo": "🐖",
    "huevos blancos": "🥚",
    "huevos color": "🥚",
    "cafe": "☕",
    "mate": "🧉",
    "te": "🍵",
    "cacao": "🍫",
    "enteros": "📦",
    "filete": "🍽️",
    "conserva": "🥫"
}
