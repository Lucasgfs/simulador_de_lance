import streamlit as st




# Inserindo dicionário de imagens

imagens = {
"Automóvel":"1.png",
"Imóvel": "2.png",
"Moto": "3.png",
"Serviço": "4.png",
"Caminhão": "5.png"
}

#função para buscar imagem
def exibir_imagem(produto):
    imagem_path = imagens.get(produto)
    if imagem_path:
         st.image(imagem_path, use_container_widht=True)
    else:
         st.write("Imagem não disponível")


#criando informaçãos na barra lateral:
st.sidebar.write("## Informações básicas:")



# Tabelas com os produtos e seus respectivos prazos, taxas e seguros
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

# Dicionário com os produtos e seus respectivos prazos
produtos_prazos = {
 "Automóvel": automovel,
 "Imóvel": imovel,
 "Moto": moto,
 "Serviço": servico,
 "Caminhão": caminhao
}

# Função para exibir a selectbox de prazos com base no produto selecionado
def exibir_prazos(produto):
    prazos = [item["Prazo"] for item in produtos_prazos[produto]]
    prazo_selecionado = st.sidebar.selectbox("Selecione o prazo", prazos)
    return prazo_selecionado



# Criação do segmentador de prazos
produto = st.sidebar.selectbox('Escolha um Produto:', list(produtos_prazos.keys()))

#Criação do header de imagens
header = exibir_imagem(produto)

#titulo do suimulador
st.write ("# Simulador de lance")

# Criação do segmentador de prazos
prazo_selecionado = exibir_prazos(produto)
prazo = prazo_selecionado

### ADEQUAR O SIMULADOR NO STREAMLIT
furo = st.sidebar.number_input("Parcelas furo:",min_value=0 ,max_value = 216)    

#Criando a condicional de Diluição do furo
diluicao = ['Diluir_Inicial', 'Diluir_lance']
diluir_furo = st.sidebar.selectbox ('Diluição do furo', diluicao) 



#calculando o prazo do cliente, 
def prazo_cliente (prazo, furo, diluir_furo):
    if furo > 0 and diluir_furo == "Diluir_lance":
        prazo = prazo
    elif furo > 0 and diluir_furo == "Diluir_Inicial":
        prazo = prazo - furo
    else:
        prazo = prazo
    return prazo


prazo_do_cliente = prazo_cliente(prazo, furo,diluir_furo)

#Calculando a parcela 
def calcular_parcela (credito, prazo_do_cliente, taxa, seguro,plano):
    valor_total = credito * (1+ taxa/100)
    seguro = valor_total * (seguro/100)

    if plano =="integral":
        parcela = valor_total/prazo_do_cliente + seguro
    elif plano == "reduzido":
        parcela = valor_total*0.7 / prazo_do_cliente + seguro
    elif plano == "meia_parcela":
        parcela = valor_total*0.5 / prazo_do_cliente + seguro
    return parcela


def parcela_integral (credito, prazo_do_cliente, taxa, seguro):
    valor_total = credito * (1+ taxa/100)
    seguro = valor_total * (seguro/100)
    parcela_int = valor_total/prazo_do_cliente + seguro
    
    return parcela_int

credito = st.number_input('Valor do Crédito')


# Função para buscar taxa e seguro
def obter_taxa_seguro(produto, prazo):
    for item in produtos_prazos[produto]:
         if item["Prazo"] == prazo:
            return item["Taxa"], item["Seguro"]
    return None, None

taxa, seguro = obter_taxa_seguro(produto, prazo)


#Criando box de seleção de planos de pagamento do cliente
planos = ['reduzido','integral','meia_parcela']
plano = st.sidebar.selectbox( 'Plano:', planos)

# Criando segmentação do seguro:
opcao_seguro = ["Sim", "Não"]
incluir_seguro = st.sidebar.selectbox("Opção de Seguro:", opcao_seguro)
if incluir_seguro == "Sim":
    seguro = seguro
else:
    seguro = 0

#parcela inicial do cliente até a contemplação
parcela_cliente = calcular_parcela(credito, prazo_do_cliente, taxa, seguro,plano) 

# para calcular lance na parcela integral
parcela_int = parcela_integral(credito, prazo_do_cliente, taxa, seguro) 

#Custo Efetivo total:
cet = (credito * (1+ (taxa/100))) + (credito * (1+ (taxa/100))) * seguro/100 * prazo_do_cliente


st.write('Parcela integral de: R$ {:.2f}'.format(parcela_int))
st.write('Parcela Reduzida de: R$ {:.2f}'.format(parcela_cliente))
st.write('Taxa:  {:.2f}'.format(taxa/prazo), "% ao mês")
st.write('Seguro:  {:.5f}'.format(seguro),"%")


st.write(f" Prazo do cliente :", format(prazo_do_cliente), ' meses.')
st.write(cet)





#--------------------------------------------------#
#Calculando a Oferta de Lance
st.write ('# Projeção de Lance:')



#CALCULANDO LANCE:

#Criando colunas para tipos de lance:
col1, col2, col3 = st.columns(3)
with col1:
    valor_lance = st.number_input("Valor Total de Lance R$ ", min_value=0, max_value = int(cet))
    if valor_lance > cet:
        st.write("Lance Maior que o Crédito")

with col2:
    parcela_de_lance = st.number_input("Quantidade Parcelas de Lance:", min_value=0, max_value=prazo)
    if parcela_de_lance> prazo:
        st.write("Lance Maior que o Prazo.")

with col3:
    embutido = st.number_input("Lance Embutido",min_value=0, max_value= int(credito*0.3))


def lance (qtd_plc,tipo_lance):
    if plano == "reduzido" and tipo_lance == "reduzida":
        valor_lance = parcela_cliente * qtd_plc
    elif plano == "meia_parcela" or plano =="reduzido" and tipo_lance =="parcela_integral":
        valor_lance = parcela_int* qtd_plc
    else:
        valor_lance = parcela_int * qtd_plc

    return valor_lance    

def valor_de_lance (valor_lance):
    try:
        return int(valor_lance/parcela_cliente)
    except ZeroDivisionError:
        return 0
  

lance_convertido = valor_de_lance(valor_lance)



#Criando Segmentador com tipo de lance
col4, col5 = st.columns(2)
escolhe_lance = ("Lance Parcela Integral","Lance Parcela Reduzida")
with col4:
    tipo_lance = st.selectbox("Tipo de Lace:",escolhe_lance ) #escolher reduzida ou parcela_integral

with col5:
    st.write("### Lance Convertido")
    st.write( format(lance_convertido))


qtd_plc = 30 #quantidade de parcelas ofertadas para o lance
tipo_lance = "reduzida" #escolher reduzida ou parcela_integral

total_lance = lance(qtd_plc, tipo_lance)










st.write ('# Parcela pós contemplação')
print (type(taxa))
print (type(seguro))