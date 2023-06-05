from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'zeus'
)

def lista():
    lista.show()
    cursor = conexao.cursor()
    comando_SQL = 'SELECT * FROM funcionarios'
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()

    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(7)

    for i in range (0, len(leitura_banco)): # i = linhas
        for j in range (0, 7): # j = colunas
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))


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

    formulario.lineEdit_Nome.setText('')
    formulario.lineEdit_Cpf.setText('')
    formulario.lineEdit_NumeroContato.setText('')
    formulario.lineEdit_Cargo.setText('')
    formulario.lineEdit_Data.setText('')
    formulario.lineEdit_Pix.setText('')
    


app = QtWidgets.QApplication([])
formulario = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/formulario.ui")
formulario.pushButton_Cadastrar.clicked.connect(inserir)

formulario.pushButton_Relatorio.clicked.connect(lista)
lista = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/lista.ui")

editar = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/editar.ui")

formulario.show()
app.exec()