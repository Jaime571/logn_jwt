from flask import Flask
from flask_cors import CORS
from routes.authorization import routes_autorization
from dotenv import load_dotenv

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(routes_autorization, url_prefix="/api" )

if __name__ == '__main__':
    load_dotenv()
    app.run(debug = True, port = "4000", host = "localhost")