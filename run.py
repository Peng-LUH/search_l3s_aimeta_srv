"""Flask CLI/Application entry point."""
import os

from src.search_l3s_aimeta import create_app, db

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db}


print("update")