"""Flask CLI/Application entry point."""
import os
from flask import jsonify

import sys
# sys.path.append(os.getcwd())
sys.path.append("/home/rathee/search/aims/search_l3s_aimeta_srv/src")

from src.search_l3s_aimeta import create_app, db

app = create_app(os.getenv("FLASK_ENV", "development"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="9041")

@app.shell_context_processor
def shell():
    return {"db": db}




