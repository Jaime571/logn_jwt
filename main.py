from flask import Flask
from routes.authorization import routes_autorization
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(routes_autorization, url_prefix="/api" )

if __name__ == '__main__':
    load_dotenv()
    app.run(debug = True, port = "4000", host = "localhost")