import os

from flask_cors import CORS

from app import blueprint
from app.main import create_app

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

app = create_app('dev')
# app = create_app('prod')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(blueprint)

app.app_context().push()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)