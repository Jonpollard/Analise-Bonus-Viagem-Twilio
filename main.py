import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC02e9a9c000bf422cb447b74c0341619f"
# Your Auth Token from twilio.com/console
auth_token  = "ba7128bef0996ff236567c1cbc5e9740"
client = Client(account_sid, auth_token)


# Passo a Passo da solução
# Abrir os 6 arquivos em Excel
lista_nomes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_nomes:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor} e qtd em Vendas: {vendas}')
        message = client.messages.create(
            to="+5521988081512",
            from_="+12677133290",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor} e qtd em Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Se for maior do que 55.000 - > Envia um SMS com o Nome, o Mês e as vendas do vendedor
# Caso não seja maior do que 55.000 não quero fazer nada
