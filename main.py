import logging.config
import os
import traceback

import yaml
from domain.error import CoviLifeException
from flask_cors import CORS

from app import blueprint
from app.containers import Container
from app.main import create_app

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

# app = create_app('dev')
logging.config.dictConfig(yaml.load(open('logging.yaml'), yaml.FullLoader))
app = create_app('prod')
CORS(app)
app.register_blueprint(blueprint)
app.container = Container()
app.app_context().push()


@app.errorhandler(Exception)
def handle_exception(e):
    traceback.print_exc()
    if isinstance(e, CoviLifeException):
        return e.to_dict(), 500
    else:
        return {
                   "code": 5000,
                   "message": "Internal Server Error"
               }, 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))