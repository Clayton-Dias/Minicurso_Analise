# Sistema de Notificação de Vendas

Este projeto utiliza a API Twilio para enviar notificações via SMS quando um vendedor atinge uma meta de vendas mensal.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `twilio`
- Conta Twilio (com número de telefone configurado)

## Configuração

1. **Instale as dependências:**

   ```bash
   pip install pandas twilio
   ```

2. **Configuração do Ambiente:**
   
   Configure suas credenciais do Twilio como variáveis de ambiente:

   ```bash
   export TWILIO_ACCOUNT_SID='sua_account_sid'
   export TWILIO_AUTH_TOKEN='seu_auth_token'
   ```

3. **Crie os arquivos de vendas:**

   Prepare arquivos Excel (`.xlsx`) para cada mês desejado, com as seguintes colunas:
   - `Vendedor`
   - `Vendas`

   Exemplo de estrutura do arquivo:

   | Vendedor      | Vendas |
   |---------------|--------|
   | Vendedor A    | 60000  |
   | Vendedor B    | 45000  |
   | Vendedor C    | 70000  |

4. **Altere o número de telefone no código:**

   No arquivo de código, substitua `seu_numero_twillio` pelo seu número Twilio.

## Execução

Para executar o script, utilize o seguinte comando:

```bash
python seu_script.py
```

O script irá ler os arquivos de vendas de cada mês especificado na lista `lista_meses`, verificar se algum vendedor ultrapassou a meta de 55.000 vendas e, se houver, enviar uma notificação via SMS.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
