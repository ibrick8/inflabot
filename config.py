import os
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "docs"
SITE_BASE_URL = os.environ.get(
    "SITE_BASE_URL", "https://ibrick8.github.io/inflabot"
)

IMAGE_INPUT_DIR = os.environ.get("IMAGE_INPUT_DIR", r"C:\Users\emili\tmp")
IMAGE_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "assets")

POSTGRESQL_URL = os.environ.get(
    "POSTGRESQL_URL", "postgresql://mi_user:mi_pass@db/mi_db"
)

TITLE = "CreatePagePosts"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
