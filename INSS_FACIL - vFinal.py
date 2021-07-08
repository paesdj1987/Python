import math

# Parâmetros para o Cálculo
# 62 anos (mulher) ou 65 anos (homem) -> tem direito a 60% da média salarial
# Mulheres: ganham mais 2% a cada ano trabalhado depois de 15 anos de contribuição. Se tiver 16 anos de contribuição, tem direito 62%.
# se tiver 17 anos de contribuição, terá direito 64%, e assim por diante.
# Homens: ganham mais 2% a cada ano trabalhado depois de 20 anos de contribuição. De 15 a 20 anos de contribuição há direito a 60% da média salarial.
# Se tiver 21 anos, terá 62% da média. Se tiver 22 anos terá 64%, e assim por diante.


salMin='1.100'
salMax='6.430,00'
cadastro=[]
somaTotal=0
somando=0
soma1=0
soma2=0
soma3=0
soma4=0
soma5=0
soma6=0
soma7=0
s1=1100
s2=2200
s3=3300
s4=4400
s5=5500
s6=6430
calculoFinal=0
indice=0.02
meses=0


texto_inicial = ''' *** BEM VINDO AO SISTEMA - INSS FACIL *** \n
Este sistema só atende:
\n a) quem contribuiu por mais de 15 anos de INSS.\n
\n b) Homem com mais de 65 anos.\n
\n b) Mulheres com mais de 62 anos.\n
Este Sistema não atende:
\n a) Quem contribui por menos de 15 anos ou nunca contribuiu.
Logo, este sistema não calcula o BPC;
\n b) Quem se aposentou por invalidez;
\n c) Quem se aposentou proporcionalmente;
\n d) Cálculo da Aposentadoria Rural;\n '''

menuFaixaSalarial = '''\n ***PRÓXIMA ETAPA*** \n
Insira a quantidade de meses que recebeu salário de acordo com as faixas salarias abaixo:\n
\n a) Quantidade de Meses que recebeu até R$1.100,00 --- até 1 salário mínimo; \n
b) Quantidade de Meses que recebeu entre R$1.100,01 até R$2.200,00 --- de 1 a 2 salários mínimo; \n
c) Quantidade de Meses que recebeu entre R$2.200,01 até R$3.300,00 --- de 2 a 3 salários mínimo; \n
d) Quantidade de Meses que recebeu entre R$3.300,01 até R$4.400,00 --- de 3 a 4 salários mínimo; \n
e) Quantidade de Meses que recebeu entre R$4.400,01 até R$5.500,00 --- de 4 a 5 salários mínimo; \n
f) Quantidade de Meses que recebeu entre R$5.500,01 até R$6.430,00 --- de 5 salários mínimo até o teto do INSS; \n
g) Quantidade de Meses que recebeu mais de R$6.430,00; \n'''

print(texto_inicial)
print('\n Ano Atual: 2021')
print('\n Salário Mínimo vigente: R$', salMin)
print('\n Salário Máximo vigente: R$', salMax)

nome = str(input("\nInsira o seu nome: \n"))
sexo = str(input("Insira o seu sexo >>> masculino ou feminino: \n"))
idade = int(input("Insira a sua idade: \n"))
mes = int(input("Insira a quantidade de meses de contribuição: \n")) 
profissão = str(input("Insira a sua profissão: \n"))
  
       
print('*** Dados do Cadastro ***\n')
print('Nome: %s \n' %nome)
print('Sexo: %s \n' %sexo)
print('Idade: %d \n' %idade)
print('Nº de Meses Contribuídos: %d\n' %mes)
print('Profissão: %s \n' %profissão)


op = input("\n insira [1] para saber se você está apto para se APOSENTAR: \n")


while (op=='1'):
     
        if (sexo=="masculino") and (mes>=180) and (idade>=65):
            print("\n PARABÉNS! Você possui requisitos NECESSÁRIOS para se aposentar \n")
            break

        elif (sexo=="feminino") and (mes>=180) and (idade>=62):
            print("\n PARABÉNS! Você possui requisitos NECESSÁRIOS para se aposentar \n")
            break

        else:
            print("\n VOCÊ NÃO PODE SE APOSENTAR! \n")
            break


print(menuFaixaSalarial)

op1=float(input("\n a) até R$1.100,00 \n"))
op2=float(input("\n b) entre R$1.100,01 até R$2.200,00 \n"))
op3=float(input("\n c) entre R$2.200,01 até R$3.300,00 \n"))
op4=float(input("\n d) entre R$3.300,01 até R$4.400,00 \n"))
op5=float(input("\n e) entre R$4.400,01 até R$5.500,00 \n"))
op6=float(input("\n g) entre R$5.500,01 até R$6.430,00 \n"))
op7=float(input("\n h) acima de R$6.430,00 \n"))

somaTotal=op1+op2+op3+op4+op5+op6+op7

if op1>0:   
    med1=(op1*1100)/somaTotal
    soma1=1100*op1
else:
    soma1=0

if op2>0:
    med2=(op2*2200)/somaTotal
    soma2=2200*op2
else:
    soma2=0

if op3>0:
    med3=(op3*3300)/somaTotal
    soma3=3300*op3
else:
    soma3=0

if op4>0:
    med4=(op4*4400)/somaTotal
    soma4=4400*op4
else:
    soma=4

if op5>0:
    med5=(op5*5500)/somaTotal
    soma5=5500*op5
else:
    soma5=0

if op6>0:
    med6=(op6*6430)/somaTotal
    soma6=6430*op6
else:
    soma6=0

if op7>0:
    med7=(op7*6430)/somaTotal
    soma7=6430*op7
else:
    soma7=0


somando=soma1+soma2+soma3+soma4+soma5+soma6+soma7
mediaGeral=somando/somaTotal
calculo1=mediaGeral*(60/100)


print("*** Info geral ***")
print("O valor total pago ao INSS durante todo o período foi de: R$ %.2f \n" %somando)
print("Média Geral foi de: R$ %.2f \n" %mediaGeral)
print("Cálculo da Aposentadoria por Tempo Mínimo de Contribuição: 60 por cento da Média Salarial -> R$ %.2f \n" %calculo1)

op = input("\n insira [1] OBTER O RESULTADO FINAL DA SUA CONSULTA: \n")

while (sexo=="masculino") and (mes>=300) and (idade>=65):     
                calculoFinal += calculo1 + calculo1*0.02
                mes+=12
                break


while (sexo=="feminino") and (mes>=180) and (idade>=62):        
                calculoFinal += calculo1 + calculo1*0.02
                mes+=12
                break



print("\n *** RELATÓRIO FINAL *** \n")
print("NOME DO BENEFICIÁRIO: %s \n" %nome)
print("SEXO DO BENEFICIÁRIO: %s \n" %sexo)
print("IDADE DO BENEFICIÁRIO: %d anos \n" %idade)
print("VALOR APROXIMADO DA APOSENTADORIA: R$ %.1f \n" %calculoFinal)












                        
                        
