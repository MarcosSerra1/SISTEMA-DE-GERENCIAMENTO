from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'zeus'
)

def inserir():

    nome = str(formulario.lineEdit_Nome.text())
    cpf = str(formulario.lineEdit_Cpf.text())
    nContato = str(formulario.lineEdit_NumeroContato.text())
    cargo = str(formulario.lineEdit_Cargo.text())
    dataAdmissao = str(formulario.lineEdit_Data.text())
    pix = str(formulario.lineEdit_Pix.text())

    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO funcionarios (nome, cpf, n_contato, cargo, data_admissao, pix) VALUES (%s, %s, %s, %s, %s, %s)'
    dados = (nome, cpf, nContato, cargo, dataAdmissao, pix)
    cursor.execute(comando_SQL, dados)
    conexao.commit()




app = QtWidgets.QApplication([])
formulario = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/cadastro.ui")

formulario.pushButton_Cadastrar.clicked.connect(inserir)

formulario.show()
app.exec()