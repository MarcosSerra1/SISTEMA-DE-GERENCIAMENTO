from twilio.rest import Client
import mysql.connector
from mysql.connector import Error
from flask import Flask, request


# Em seguida, vamos configurar o cliente do Twilio e o banco de dados MySQL:
twilio_account_sid = 'ACcbaba24d9c7d9ff2b16a119da3e18791'
twilio_auth_token = '50a950719f6dcb91098ff69e0bf09d26'
twilio_phone_number = '+14179003290'
mysql_host = 'localhost'
mysql_database = 'gestao_lojas'
mysql_user = 'root'
mysql_password = ''

client = Client(twilio_account_sid, twilio_auth_token)

try:
    connection = mysql.connector.connect(
        host=mysql_host,
        database=mysql_database,
        user=mysql_user,
        password=mysql_password
    )
    cursor = connection.cursor()
except Error as e:
    print("Error connecting to MySQL:", e)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    message_body = data.get('Body')
    phone_number = data.get('From')
    
    # Verificar se a mensagem é um comando válido
    if message_body.lower() == 'chegada':
        registrar_chegada(phone_number)
        return 'Registrado com sucesso!'
    
    return 'Comando inválido.'

if __name__ == '__main__':
    app.run()

def registrar_chegada(phone_number):
    try:
        # Buscar o nome do funcionário com base no número de telefone
        query = "SELECT name FROM employees WHERE phone_number = %s"
        cursor.execute(query, (phone_number,))
        result = cursor.fetchone()
        if result is None:
            return 'Número de telefone não encontrado.'
        employee_name = result[0]
        
        # Inserir o registro de chegada no banco de dados
        query = "INSERT INTO arrivals (employee_name) VALUES (%s)"
        cursor.execute(query, (employee_name,))
        connection.commit()
        
        # Enviar uma mensagem de confirmação para o funcionário
        message = f'Olá, {employee_name}! Sua chegada ao serviço foi registrada com sucesso.'
        send_message(phone_number, message)
    except Error as e:
        print("Error registering arrival:", e)

def send_message(phone_number, message):
    try:
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
    except Exception as e:
        print("Error sending message:", e)

if __name__ == '__main__':
    app.run()

