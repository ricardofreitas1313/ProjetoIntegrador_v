from  flask_restful import Resource,reqparse
from models.curriculo import CurriculoModel


curriculos =[{'curriculo_id':'1','nome':'Luiz de Freitas','email':'defreitasluiz1313@gmail.com','telefone ':'3199945281','endereco':'avenida amazonas 2554','cidade':'belo horizonte', 'idade':'43','resumo':'Programador dedicado com 5 anos de experiência. Tenho experiência em Java, Python e C#, programando diversos tipos de aplicações para os clientes da Empresa X, desde aplicativos bancários até softwares educativos. Focando em otimizar processos, consegui reduzir o tempo de testes dos produtos em 20%, sem comprometer a qualidade final. Na sua empresa, buscarei oportunidades semelhantes para otimizar processos.'},{

'curriculo_id':'2','nome':'ercilia esteves de freitas','email':'erciliaesteved@gmail.com','telefone ':'3199945589','endereco':'avenida augusto de lima 450','cidade':'belo horizonte', 'idade':'35','resumo':'Professora dedicada de inglês com 10 anos de experiência. Na minha carreira, ensinei em diversos países da América Latina, incluindo Argentina e Venezuela. Em 2018, recebi uma bolsa para ensinar português nos Estados Unidos por 6 meses. Todas as minhas viagens foram fundamentais para o meu desenvolvimento cultural e pretendo passar as minhas experiências para os alunos da Escola X'}]

class Curriculos(Resource):
    def get(self):
        return{'Curriculos':curriculos}

class Curriculo(Resource):
    argumentos =reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('telefone')
    argumentos.add_argument('endereco')
    argumentos.add_argument('cidade')
    argumentos.add_argument('idade')
    argumentos.add_argument('resumo')

    def find_curriculo(curriculo_id):
        for curriculo in curriculos:
            if curriculo['curriculo_id'] == curriculo_id:
                return curriculo
        return False

    def get(self, curriculo_id):
        curriculo = Curriculo.find_curriculo(curriculo_id)
        if curriculo:
            return curriculo
        return {'message':'Curriculo not found.'},404 #

    def post(self,curriculo_id):
        if Curriculo.find_curriculo(curriculo_id):
            return {"message": "Curriculo id '{}' already exists.".format(curriculo_id)},400 #Bad request
        dados = Curriculo.argumentos.parse_args()
        curriculo_objeto = CurriculoModel(curriculo_id,**dados)
        novo_curriculo =curriculo_objeto.json()
        curriculos.append(novo_curriculo)
        return novo_curriculo,200

    def put(self,curriculo_id):
        dados = Curriculo.argumentos.parse_args()
        curriculo_objeto = CurriculoModel(curriculo_id,**dados)
        novo_curriculo =curriculo_objeto.json()
        curriculo = Curriculo.find_curriculo(curriculo_id)
        if curriculo:
            curriculo.update(novo_curriculo)
            return novo_curriculo,200
        curriculos.append(novo_curriculo)
        return novo_curriculo,201 #created criado


    def delete(self,curriculo_id):
        global curriculos
        curriculos = [curriculo for curriculo in curriculos if curriculo ['curriculo_id'] !=  curriculo_id]
        return {'message':'Curriculo  deleted.'}