from flask import Flask
from flask_jwt_extended import JWTManager 
from flask_restful import Api
from config import Config

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)
# JWT 매니저를 초기화 
jwt = JWTManager(app)


api = Api(app)


if __name__ == '__main__':
    app.run()