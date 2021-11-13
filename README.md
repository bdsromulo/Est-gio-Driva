# data_analysis_driva

O projeto de análise de dados para a Driva, chamado por conveniência de "data_analysis_driva", tem por objetivo realizar as tarefas propostas pelo desafio da Driva
para o seu novo programa de estágio para 2022. O desafio é composto da seguinte forma:

"- Faça um pequeno código em Python utilizando a biblioteca Pandas que atenda os seguintes requisitos:

* Leia o arquivo "DadosEmpresa.csv";
* Leia o arquivo "DadosEndereco.csv";
* Gere um arquivo csv com todas as empresas que tem opção_pelo_simples como SIM;
* Gere outro arquivo csv que contenha todas as informações das empresas que são de Curitiba ou de Londrina e que tenham capital social maior que 5000 reais.
* Faça um gráfico que mostre o total de empresas em cada bairro de Curitiba. (utilize uma biblioteca de sua escolha);
* Observando os dois arquivos, qual outra analise de dados você faria? Implemente ela e escreva em um comentário o porque pensou nela."

Dessa forma, esse repositório veio cumprindo com todas as tarefas pedidas. Para as 4 primeiras tarefas, utilizei conforme pedido a bilioteca Pandas, executando
seus comandos e gerando os arquivos solicitados, localizados dentro da pasta "Data".

Utilizando o recurso "read" do pandas, os 2 arquivos fornecidos foram lidos e inseridos no programa como dataframes.

O primeiro arquivo csv pedido foi entregue com a simples realização de um dataframe a partir da planilha "DadosEmpresa.csv" com o recurso de filtragem do prórpio
framework. Esse dataframe por sua vez foi convertido e exportado para o arquivo "as_simples.csv", também por meio de ferramenta da Pandas.

O segundo arquivo csv pedido foi executado com o passo inicial sendo a junção dos dois arquivos fornecidos, sabendo que precisava-se filtrar índices que se
encontravam separados nas 2 planilhas que haviam sido lidas anteriormente, sendo eles as cidades (Curitiba e Londrina) e o capital social (superior a 5000).
A junção foi realizada a partir da análise e inserção externa das duas planilhas, utilizando como chave-comum o cnpj, que se encontrava nas duas planilhas.
A partir do dataframe formado com essa junção, pôde-se obter o .csv pedido realizando novamente um filtro com operadores lógicos, com os critérios que foram
fornecidos. Assim, exportou-se o arquivo "juncao_filtrada.csv", contendo as informações pedidas.

Para a realização do gráfico, gerei mais um dataframe a partir dos endereços originalmente fornecidos, sabendo que seria uma filtragem menor de dados que,
por não terem sofrido manipulação prévia, corriam menos risco de estarem comprometidos. Utilizando a função da Pandas "count.values()", obtive o dataframe que
continha a contagem de empresas por bairro.
Inicialmente, utilizei a própria biblioteca Pandas para plotar o gráfico. Com pouca dificuldade, o fiz, mas no entanto, não pude deixar de perceber a limitação da
biblioteca na ação de plotagem de gráficos, que permite poucas alterações estéticas e dinâmicas.
Por isso, abri outra branch, desta vez, me utilizando da biblioteca MatPlotLib. Por meio dela, pude realizar mais ações no gráfico, dentre deixá-lo mais organizado,
com um esquema de cores mais esteticamente agradável e com possibilidade de formatação condicional que torna a informação mais visível e "user-friendly".
Ao final, o gráfico plotado com Pandas ficou expresso em sua branch, a "master", com nome e formato "plotted.pdf", enquanto o plotado com MatPlotLib foi expresso com nome e
formato "graph.png" na branch "altered_plotting"

Ao final do código, foram colocadas considerações sobre uma análise de dados que eu faria junto com a sua implementação. A análise de dados, trazida diretamente do código, foi proposta da seguinte maneira:

"""
#####Minha análise de dados - Teoria#####

#Para a criação de estratégias de investimento, abordagem e expansão de um negócio, é necessário observar fontes de renda
#e capital. Por sua vez, é preferencial que a implementação dessas estratégias seja orientada por proximidade e distribuição
#capital regional, a fim de não dificultar a realização logística da estratégia ou mesmo de diminuir as chances de um
#desequilíbrio e concentração de investimentos.
 
#Logo, a análise de dados a seguir visa observar o capital social em relação panorama geral da Região Sul que foi apresentado.
#Essa análise buscará trazer os munícipios com maior concentração de capital e maior distribuição proporcional em relação a esse
#capital total. Essa distribuição pode ser medida à partir do cálculo de Desvio Padrão, e é relevante no princípio do ditado
#popular "Não se deve colocar todos os ovos no mesmo cesto", onde municípios com uma empresa de capital alto e as demais com
#capital comparativamente baixa nem sempre são a escolha mais adequada. Avaliando individualmente  cada município,
#pode-se chegar à partir destes dados se um determinado município tem pouca ou muita presença de serviço (quantidade),
#se seu capital social é alto ou baixo (capital_total) e se a distribuição deste capital dentre as unidades da cidade é
# igual ou desigual(desvio_padrão).

#É válido ressaltar que a medida de Desvio Padrão deve ser avaliada de acordo com o capital_total, sabendo-se que
#quanto mais baixa, mais igual é a distribuição da renda por entre as empresas(exceto quando se trata de desvio nulo
# em municípios de quantidade = 1, onde aí a concentração é total de uma empresa).

#Ao final, a exportação e a apresentação dos dados se encontra em formatos .csv e .xlsx. Essa escolha de formatos se deu
#por .csv ter sido o formato apresentado inicialmente e mais utilizado durante o projeto, enquanto o .xlsx permite uma
#visualização e manipulação dos dados de maneira mais user-friendly. Os documentos estão identificados por "dados_capital_municipal"
#na pasta "Data".
"""

E assim, o projeto dá-se por finalizado.
