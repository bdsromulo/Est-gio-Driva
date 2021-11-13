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
#plt.show()

#Salvamento do gráfico em png
plt.savefig(r"graph.png")

#####Minha análise de dados - Teoria#####

#Para a criação de estratégias de investimento, abordagem e expansão de um negócio, é necessário observar fontes de renda
#e capital. Por sua vez, é preferencial que a implementação dessas estratégias seja orientada por proximidade e distribuição
#capital regional, a fim de não dificultar a realização logística da estratégia ou mesmo de diminuir as chances de um
#desequilíbrio e concentração de investimentos.
 
#Logo, a análise de dados a seguir visa observar o capital social em relação panorama geral da Região Sul que foi apresentado.
#Essa análise buscará trazer os munícipios com maior concentração de capital e maior distribuição proporcional em relação a esse
#capital total. Essa distribuição pode ser medida à partir do cálculo de Desvio Padrão, e é relevante no princípio do ditado
#popular "Não se deve colocar todos os ovos no mesmo cesto", onde municípios com uma empresa de capital alto e as demais com
#capital comparativamente baixo nem sempre são a escolha mais adequada. Avaliando individualmente  cada município,
#pode-se chegar a partir destes dados se um determinado município tem pouca ou muita presença de serviço (quantidade),
#se seu capital social é alto ou baixo (capital_total) e se a distribuição deste capital dentre as unidades da cidade é
#igual ou desigual(desvio_padrão).

#É válido ressaltar que a medida de Desvio Padrão deve ser avaliada de acordo com o capital_total, sabendo-se que
#quanto mais baixa, mais igual é a distribuição da renda por entre as empresas(exceto quando se trata de desvio nulo
#em municípios de quantidade = 1, onde aí a concentração é total de uma empresa).

#Ao final, a exportação e a apresentação dos dados se encontra em formatos .csv e .xlsx. Essa escolha de formatos se deu
#por .csv ter sido o formato apresentado inicialmente e mais utilizado durante o projeto, enquanto o .xlsx permite uma
#visualização e manipulação dos dados de maneira mais user-friendly. Os documentos desta análise estão identificados por "dados_capital_municipal"
#na pasta "Data".

#####Minha análise de dados - Implementação#####

#DataFrame para obtenção do capital total
valores = junction.groupby("municipio").capital_social.sum()

#DataFrame para obtenção do desvio padrão por cidade
variancias = junction.groupby("municipio").capital_social.std()

#Junção e organização das categorias de valor p/cidade (Capital total da cidade, Desvio Padrão
#e quantidade de empresas estabelecidas na cidade)
dados_capital = pd.merge(valores, variancias, on = "municipio", how = "outer")
dados_capital = dados_capital.merge(enderecos["municipio"].value_counts().to_frame(), left_on="municipio",
                    right_index = True, suffixes=('', 'x'))

#Renomeação a fim de organizar os títulos e tópicos da planilha final
dados_capital = dados_capital.rename(columns={'capital_social_x':'capital_total','capital_social_y':'desvio_padrão',
'municipio':'quantidade'})

#Exportação do  DataFrame para arquivo .csv e .xlsx
dados_capital.to_csv(r"Data\dados_capital_municipal.csv")
dados_capital.to_excel(r"Data\dados_capital_municipal.xlsx")


