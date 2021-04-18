from flask import Flask
from flask_restful import Api
from resources.empresas import Empresas, Empresa
from resources.curriculos import Curriculos,Curriculo


app = Flask(__name__)
api = Api(app)

api.add_resource(Empresas, '/empresas')
api.add_resource(Empresa,'/empresas/<string:empresa_id>')
api.add_resource(Curriculos, '/curriculos')
api.add_resource(Curriculo,'/curriculos/<string:curriculo_id>')


if __name__ == '__main__':
    app.run(debug=True)


