from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = 'hadgagierh@^&$^*TUGYG*^Thfshug^%'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledbduyen?charset=utf8mb4' % quote('12345678')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

cloudinary.config(cloud_name='dwhnp2hsa', api_key='422672812142572', api_secret='IvSWkIQDax32lByzdZOD09HLUSA')

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return 'vi'


