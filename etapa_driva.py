import pandas as pd
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
#Plotagem de gráfico de barras via Pandas
bairros_cwb = enderecos[enderecos.municipio == "CURITIBA"]
bairros_cwb = bairros_cwb["bairro"].value_counts()
plot_cwb = bairros_cwb.plot.barh(figsize = (40,35), fontsize = 24, sort_columns = True,
                                 xticks = range(0, bairros_cwb.max()+1), grid = True)
plot_cwb.get_figure().savefig('plotted.pdf', format='pdf')






