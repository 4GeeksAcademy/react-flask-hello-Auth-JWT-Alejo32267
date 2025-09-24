import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from flask_jwt_extended import JWTManager

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
# Actualizamos la ruta para que apunte al archivo index.html correcto
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../')  # Ruta raíz del proyecto

app = Flask(__name__)
# ¡Cambia las palabras "super-secret" por otra cosa!
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

# Database Configuration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Setup
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# CORS Configuration
frontend_origin = os.getenv("FRONTEND_ORIGIN", "*")
CORS(app, supports_credentials=True, resources={
     r"/api/*": {"origins": frontend_origin}})

# Initialize DB
db.init_app(app)
Migrate(app, db, compare_type=True)

# Setup Admin and Commands
setup_admin(app)
setup_commands(app)

# Register API Blueprint
app.register_blueprint(api, url_prefix='/api')

# Handle/Serialize Errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)

    # En producción, sirvo el archivo estático index.html desde la ruta raíz del proyecto
    return send_from_directory(static_file_dir, 'index.html')

# Serve static files in production


@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    # Si el archivo no existe, intento devolver el 'index.html'
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'

    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0  # Evitar cache en producción
    return response


# Running the app only if directly executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
