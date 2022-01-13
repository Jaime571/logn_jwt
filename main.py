from flask import Flask
from flask_cors import CORS
from routes.authorization import routes_autorization
from routes.signUp import signUp
from dotenv import load_dotenv

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
with app.app_context():
    
    """ Declaración de las Blueprint """
app.register_blueprint(routes_autorization, url_prefix="/api")
app.register_blueprint(signUp, url_prefix="/api/registro")

if __name__ == '__main__':
    """ Carga el entorno virtual de manera automática """
    load_dotenv()
    app.run(debug=True, port="4000", host="127.0.0.1")
