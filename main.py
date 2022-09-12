from acesso_cep import BuscaEndereco
import requests


cep = '13506569'
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)