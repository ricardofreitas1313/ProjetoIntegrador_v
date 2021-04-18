class CurriculoModel:
     def __init__(self, curriculo_id, nome,email,telefone,endereco,cidade,idade,resumo):
          self.curriculo_id = curriculo_id
          self.nome = nome
          self.email = email
          self.telefone = telefone
          self.endereco=endereco
          self.cidade = cidade
          self.idade = idade
          self.resumo = resumo

     def json(self):
        return {'curriculo_id': self.curriculo_id,'nome':self.nome,'email':self.email ,'telefone': self.telefone,'endereco':self.endereco,'cidade':self.cidade,'idade':self.idade,'resumo':self.resumo}