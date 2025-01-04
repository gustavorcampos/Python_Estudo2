"""
Dicionário

Exemplos referente ao método setdefault() e update()

"""
# Inicializando dicionário
dicionario_estudo = {

    "dados_gerais": {
        "nome": "Gustavo",
        "Idade": 35
    },

    "trabalho": {
        "nome": "Bridge",
        "cidade": "SP"
    }

}

# Print do dicionário sem alterações
print(f"Dicionário sem alterações: {dicionario_estudo}")

# Exemplo do método setdefault()
# Irá inserir uma nova chave e valor

dicionario_estudo["dados_gerais"].setdefault("Altura", 180)
print(f"Dicionário com método setdefacult(): {dicionario_estudo}")

# Exemplo do método update()
# Irá atualizar um valor
atualizacoes = {
    "dados_gerais": {
        "nome": "GRC"
    }
}

dicionario_estudo["dados_gerais"].update(atualizacoes["dados_gerais"])
print(f"Dicionário com método update(): {dicionario_estudo}")
