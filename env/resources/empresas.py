from  flask_restful import Resource,reqparse
from models.empresa import EmpresaModel


empresas =[{'empresa_id':'1','nome':'Delta Empresa','cidade':'Belo Horizonte','cnpj ':'11524853458798','contato':'Ricardo Luiz de Freitas ','telefone':'3199945213'},   {'empresa_id':'2','nome':'Fox Empresa','cidade':'Belo Horizonte','cnpj ':'11524853458799','contato':'Rafaela Neri','telefone':'3199945280'},{'empresa_id':'3','nome':'Lima Empresa','cidade':'Tiradentes','cnpj ':'11524853458100','contato':'Renato','telefone':'3199945281'}]

class Empresas(Resource):
    def get(self):
        return{'Empresas':empresas}

class Empresa(Resource):
    argumentos =reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('cidade')
    argumentos.add_argument('cnpj')
    argumentos.add_argument('contato')
    argumentos.add_argument('telefone')

    def find_empresa(empresa_id):
        for empresa in empresas:
            if empresa['empresa_id'] == empresa_id:
                return empresa
        return False

    def get(self, empresa_id):
        empresa = Empresa.find_empresa(empresa_id)
        if empresa:
            return empresa
        return {'message':'Empresa not found.'},404 #

    def post(self,empresa_id):
        if Empresa.find_empresa(empresa_id):
            return {"message": "Empresa id '{}' already exists.".format(empresa_id)},400 #Bad request
        dados = Empresa.argumentos.parse_args()
        empresa_objeto = EmpresaModel(empresa_id,**dados)
        nova_empresa =empresa_objeto.json()
        empresas.append(nova_empresa)
        return nova_empresa,200

    def put(self,empresa_id):
        dados = Empresa.argumentos.parse_args()
        empresa_objeto = EmpresaModel(empresa_id,**dados)
        nova_empresa =empresa_objeto.json()
        empresa = Empresa.find_empresa(empresa_id)
        if empresa:
            empresa.update(nova_empresa)
            return nova_empresa,200
        empresas.append(nova_empresa)
        return nova_empresa,201 #created criado


    def delete(self,empresa_id):
        global empresas
        empresas = [empresa for empresa in empresas if empresa ['empresa_id'] !=  empresa_id]
        return {'message':'Empresa  deleted.'}


