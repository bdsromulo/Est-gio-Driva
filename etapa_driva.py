from numpy import diag
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts


#####Leitura das Planilhas#####
empresa = pd.read_csv(r"Data\DadosEmpresa.csv")
enderecos = pd.read_csv(r"Data\DadosEndereco.csv")

#####Formulação da nova planilha com empresas que possuem "opcao_pelo_simples"#####
#Criação e Exportação do DataFrame
as_simples = empresa[empresa.opcao_pelo_simples == "SIM"]
as_simples.to_csv(r"Data\as_simples.csv")

#####Formulação da nova planilha com empresas que são de Curitiba ou de Londrina e que tenham capital social maior que 5000 reais#####
#Criação do DataFrame com a união das 2 planilhas tendo o CNPJ como chave
junction = pd.merge(empresa, enderecos, on = "cnpj", how = "outer")

#Filtragem final do DataFrame baseado em cidade (Curitiba e Londrina) e capital social (Superior a 5000)
capital_e_sede = junction[(junction.municipio == "CURITIBA") | (junction.municipio == "LONDRINA") & (junction.capital_social > 5000)]

#Eliminação de Index numérico bruto
capital_e_sede = capital_e_sede.set_index("cnpj")

#Exportação para CSV
capital_e_sede.to_csv(r"Data\juncao_filtrada.csv")

#####Criação de Gráfico de sedes p/bairro em Curitiba#####
#Plotagem de gráfico de barras via MatPlotLib
#Dataframe com os CNPJs em Curitiba
bairros_cwb = enderecos[enderecos.municipio == "CURITIBA"]
bairros_cwb = bairros_cwb["bairro"].value_counts()

#Configuração de tamanho da imagem
plt.figure(figsize=(12,55))
#Cores Condicionais baseadas em quantidade de sedes por bairro acima ou abaixo de 12 
colors = ["lightcoral" if i < 12 else "yellowgreen" for i in bairros_cwb]
#Configuração de dados do gráfico
plt.barh(range(len(bairros_cwb)), bairros_cwb.values, align='center', color = colors)
plt.yticks(range(len(bairros_cwb)), bairros_cwb.index.values, size='small', rotation = 'horizontal',fontsize = 6)
plt.title("Quantidade de Sedes em Curitiba (p/Bairro)")
for index, value in enumerate(bairros_cwb):
    plt.text(value, index, str(value), fontsize = 7.5)
#Display de gráfico por meio de ferramenta do Python
plt.show()
#Salvamento do gráfico em png
plt.savefig(r"graph.png")






