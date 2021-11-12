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

Ao final do código, foram colocadas considerações sobre uma análise de dados que eu faria junto com a sua implementação.
