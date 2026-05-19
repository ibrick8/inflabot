import os
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "docs"


REDIS_CHANNEL = "metricas"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
IMAGE_INPUT_DIR = "C:\\Users\\emili\\tmp\\"
IMAGE_OUTPUT_DIR = f"{OUTPUT_DIR}\\assets"


POSTGRESQL_URL= os.environ.get("POSTGRESQL_URL", "postgresql://mi_user:mi_pass@db/mi_db")

TITLE = 'CreatePagePosts'
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")