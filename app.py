# Passo a passo:
# 1) Abrir os arquivos em excel
# 2) Para cada arquivo:
# 2.1) Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55K
# 2.1.1) SE for maior que 55K => Envia um SMS com o nome, mês e vendas do vendedor
# 2.1.2) Caso seja menor, fará nada.

# Instalar pandas, openpyxl e twilio
# Comando: pip install xxxx

import pandas as pd
from twilio.rest import Client
import os

'''
# Your Account SID from twilio.com/console
account_sid= os.getenv("TWILIO_ACCOUNT_SID")  # SID da conta Twilio, usado para autenticação
# Your Auth Token from twilio.com/console
auth_token = os.getenv("TWILIO_AUTH_TOKEN")  # Token de autenticação da conta Twilio
client = Client(account_sid, auth_token)  # Criação de uma instância do cliente Twilio
'''

# Função para enviar mensagem via Twilio
def enviar_mensagem(mes, vendedor, vendas):
    # Cria e envia a mensagem com os dados do vendedor e vendas
    message = client.messages.create(
        to="+5521999999999",  # Número de destino
        from_="seu_numero_twillio",  # Número Twilio que está enviando
        body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'  # Corpo da mensagem
    )
    print(message.sid)  # Imprime o SID da mensagem enviada para rastreamento


# 1) Abrir os arquivos em excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]  # Lista dos meses a serem processados

# Loop através da lista de meses
for mes in lista_meses:
    #print(mes)  # Imprime o nome do mês atual
    tabelas_vendas = pd.read_excel(f"{mes}.xlsx")  # Lê o arquivo Excel correspondente ao mês
    #print(tabelas_vendas)  # Exibe a tabela de vendas para verificação

    # Verifica se há alguma venda acima de 55000
    if (tabelas_vendas["Vendas"] > 55000).any():
        # Obtém o vendedor e as vendas que superaram 55000
        vendedor = tabelas_vendas.loc[tabelas_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas["Vendas"] > 55000, "Vendas"].values[0]
        
        #print(f"No mês {mes}, o vendedor {vendedor} vendeu {vendas}")  # Imprime a informação de vendas
        
        enviar_mensagem(mes, vendedor, vendas)  # Função que envia a notificação