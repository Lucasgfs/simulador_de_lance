# Tabelas
automovel = [
    {"Prazo": 96, "Taxa": 19.5, "Seguro": 0.086970},
    {"Prazo": 84, "Taxa": 18.0, "Seguro": 0.086970},
    {"Prazo": 72, "Taxa": 16.5, "Seguro": 0.086970},
    {"Prazo": 60, "Taxa": 15.0, "Seguro": 0.086970},
    {"Prazo": 48, "Taxa": 13.5, "Seguro": 0.086970},
    {"Prazo": 36, "Taxa": 12.5, "Seguro": 0.086970},
    {"Prazo": 24, "Taxa": 9.5, "Seguro": 0.086970},
    {"Prazo": 12, "Taxa": 6.0, "Seguro": 0.086970}
]

imovel = [
    {"Prazo": 216, "Taxa": 28.5, "Seguro": 0.032450},
    {"Prazo": 180, "Taxa": 26.0, "Seguro": 0.032450},
    {"Prazo": 144, "Taxa": 22.5, "Seguro": 0.032450},
    {"Prazo": 120, "Taxa": 19.0, "Seguro": 0.032450},
    {"Prazo": 96, "Taxa": 15.5, "Seguro": 0.032450},
    {"Prazo": 72, "Taxa": 13.5, "Seguro": 0.032450},
    {"Prazo": 60, "Taxa": 12.5, "Seguro": 0.032450},
    {"Prazo": 48, "Taxa": 11.5, "Seguro": 0.032450},
    {"Prazo": 36, "Taxa": 10.5, "Seguro": 0.032450},
    {"Prazo": 24, "Taxa": 9.5, "Seguro": 0.032450}
]

caminhao = [
    {"Prazo": 120, "Taxa": 19.0, "Seguro": 0.040200},
    {"Prazo": 108, "Taxa": 18.5, "Seguro": 0.040200},
    {"Prazo": 96, "Taxa": 14.5, "Seguro": 0.040200},
    {"Prazo": 84, "Taxa": 14.0, "Seguro": 0.040200},
    {"Prazo": 72, "Taxa": 13.5, "Seguro": 0.040200},
    {"Prazo": 60, "Taxa": 13.0, "Seguro": 0.040200},
    {"Prazo": 48, "Taxa": 12.5, "Seguro": 0.040200},
    {"Prazo": 36, "Taxa": 12.0, "Seguro": 0.040200},
    {"Prazo": 24, "Taxa": 9.0, "Seguro": 0.040200}
]

moto = [
    {"Prazo": 60, "Taxa": 21.5, "Seguro": 0.086900}
]

servico = [
    {"Prazo": 48, "Taxa": 26.5, "Seguro": 0.151960}
]

# Função para buscar taxa e seguro
def buscar_taxa_seguro(produto, prazo):
    tabelas = {
        "automovel": automovel,
        "imovel": imovel,
        "caminhao": caminhao,
        "moto": moto,
        "servico": servico
    }
    
    tabela = tabelas.get(produto.lower())
    if tabela:
        for item in tabela:
            if item["Prazo"] == prazo:
                return item["Taxa"], item["Seguro"]
    return None, None

# Exemplo de uso
produto = "automovel"
prazo = 84
taxa, seguro = buscar_taxa_seguro(produto, prazo)
if taxa is not None and seguro is not None:
    print(f"Produto: {produto.capitalize()}, Prazo: {prazo}, Taxa: {taxa}%, Seguro: {seguro}%")
else:
    print("Informações não encontradas para o produto e prazo especificados.")

print (type(taxa))
print (taxa)
print (type(seguro))
print (seguro)

print(150000 * (1+taxa))