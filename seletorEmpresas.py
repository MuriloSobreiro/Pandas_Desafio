import pandas as pd
import matplotlib.pyplot as plt

separador = "," #Separador dos dados csv
dec = "." #Separador decimal dos dados numéricos

#Importando os arquivos que se encontram na mesma pasta do script
dadosEmpresa = pd.read_csv("DadosEmpresa.csv", sep = separador, decimal = dec)
dadosEndereco = pd.read_csv("DadosEndereco.csv", sep = separador, decimal = dec)

#Gere um arquivo csv com todas as empresas que tem opção_pelo_simples como SIM;
#Filtrando as empresas desejadas
opSimples = dadosEmpresa[dadosEmpresa.opcao_pelo_simples == "SIM"]

#Gerando o arquivo
opSimples.to_csv("opPeloSimples.csv",sep =",", index = False)

#Gere outro arquivo csv que contenha todas as informações das empresas que 
# são de Curitiba ou de Londrina e que tenham capital social maior que 5000 reais.
#Vamos juntar as duas tabelas para facilitar o trabalho com os dados
dadosCompletos = pd.merge(dadosEmpresa,dadosEndereco, on = "cnpj")

#Selecionando os dados
empSelect = dadosCompletos[((dadosCompletos.municipio == "LONDRINA") | (dadosCompletos.municipio == "CURITIBA")) & (dadosCompletos.capital_social > 5000)]

#Gerando o aquivo
empSelect.to_csv("EmpresasGrandeCapital.csv", sep = ",", index = False)

#Faça um gráfico que mostre o total de empresas em cada bairro de Curitiba. (utilize uma biblioteca de sua escolha);
#Extrair os dados úteis
x = dadosEndereco[dadosEndereco.municipio == "CURITIBA"].groupby("bairro").size().sort_values()

#Utilizando a bibliotexa matplotlib faremos um gráfico de barras horizontais
plt.barh(x.index,x)
plt.title("Empresas por bairro de Curitiba")

#Observando os dois arquivos, qual outra analise de dados você faria? Implemente ela e escreva em um comentário o porque pensou nela.
#Olhando os dados disponíveis acho válido verificar se a opção pelo simples tem correlação com o capital social da empresa
#Pois essa escolha pode influenciar na capacidade da empresa de aumentar seu capital social
ys = dadosEmpresa[(dadosEmpresa.opcao_pelo_simples == "SIM")][["opcao_pelo_simples","capital_social"]]
yn = dadosEmpresa[(dadosEmpresa.opcao_pelo_simples == "NAO")][["opcao_pelo_simples","capital_social"]]

#Calculo das médias de capital social para as empresas
print(ys.mean(numeric_only= True)) #44434.725849
print(yn.mean(numeric_only= True)) #702432.535452

#Criando o gráfico de caixas para a visualização dos dados
data = [ys.capital_social,yn.capital_social]
fig, ax = plt.subplots()
ax.set_title('Comparação entre opção pelo simples e capital social')
ax.boxplot(data)
#Aqui utilizamos uma escala logaritimica para melhor visualização dos dados
plt.semilogy()

#Podemos ver pelas médias e pelo gráfico gerado que empresas que optam pelo simples tendem a ter um menor capital social

plt.show()