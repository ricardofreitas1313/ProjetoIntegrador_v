class EmpresaModel:
     def __init__(self, empresa_id, nome,cidade,cnpj,contato,telefone):
          self.empresa_id = empresa_id
          self.nome = nome
          self.cidade = cidade
          self.cnpj = cnpj
          self.contato=contato
          self.telefone = telefone

     def json(self):
        return {'empresa_id': self.empresa_id,'nome':self.nome,'cidade':self.cidade ,'cnpj': self.cnpj,'contato':self.contato,'telefone':self.telefone}
