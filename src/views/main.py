from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'zeus'
)

numero_id = 0

def excluir():
    remover = lista.tableWidget.currentRow()
    lista.tableWidget.removeRow(remover)

    cursor = conexao.cursor()
    cursor.execute('SELECT id_funcionarios FROM funcionarios')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [remover][0]
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionarioS= ' + str(valor_id))

    conexao.commit()


def editar():
    global numero_id
    dados = lista.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute('SELECT id_funcionarios FROM funcionarios')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dados][0]
    cursor.execute('SELECT * FROM funcionarios WHERE id_funcionarios= ' + str(valor_id))
    leitura_banco = cursor.fetchall()

    editar.show()
    numero_id = valor_id

    editar.lineEdit_AlterarId.setText(str(leitura_banco[0][0]))
    editar.lineEdit_AlterarNome.setText(str(leitura_banco[0][1]))
    editar.lineEdit_AlterarCpf.setText(str(leitura_banco[0][2]))
    editar.lineEdit_AlterarContato.setText(str(leitura_banco[0][3]))
    editar.lineEdit_AlterarCargo.setText(str(leitura_banco[0][4]))
    editar.lineEdit_AlterarDataAdmissao.setText(str(leitura_banco[0][5]))
    editar.lineEdit_AlterarPix.setText(str(leitura_banco[0][6]))
    editar.lineEdit_Alterar_Camisa.setText(str(leitura_banco[0][7]))
    editar.lineEdit_Alterar_Calca.setText(str(leitura_banco[0][8]))
    editar.lineEdit_Alterar_Bota.setText(str(leitura_banco[0][9]))

def salvar_alteracao():
    global numero_id

    id = editar.lineEdit_AlterarId.text()
    nome = editar.lineEdit_AlterarNome.text()
    cpf = editar.lineEdit_AlterarCpf.text()
    n_contato = editar.lineEdit_AlterarContato.text()
    cargo =  editar.lineEdit_AlterarCargo.text()
    data_admissao = editar.lineEdit_AlterarDataAdmissao.text()
    pix = editar.lineEdit_AlterarPix.text()
    camisa = editar.lineEdit_Alterar_Camisa.text()
    calca = editar.lineEdit_Alterar_Calca.text()
    bota = editar.lineEdit_Alterar_Bota.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE funcionarios SET id_funcionarios='{}', nome='{}', cpf='{}', n_contato='{}', cargo='{}', data_admissao='{}', pix='{}', camisa='{}', calca='{}', bota='{}' WHERE id_funcionarios={}". format(id, nome, cpf, n_contato, cargo, data_admissao, pix, camisa, calca, bota, numero_id))

    editar.close()
    lista.close()
    formulario.show()

    conexao.commit()

def lista():
    lista.show()
    cursor = conexao.cursor()
    comando_SQL = 'SELECT * FROM funcionarios'
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()

    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(10)

    for i in range (0, len(leitura_banco)): # i = linhas
        for j in range (0, 10): # j = colunas 
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))


def inserir():

    nome = str(formulario.lineEdit_Nome.text())
    cpf = str(formulario.lineEdit_Cpf.text())
    nContato = str(formulario.lineEdit_NumeroContato.text())
    cargo = str(formulario.lineEdit_Cargo.text())
    dataAdmissao = str(formulario.lineEdit_Data.text())
    pix = str(formulario.lineEdit_Pix.text())
    camisa = str(formulario.lineEdit_Camisa.text())
    calca = str(formulario.lineEdit_Calca.text())
    bota = str(formulario.lineEdit_Bota.text())

    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO funcionarios (nome, cpf, n_contato, cargo, data_admissao, pix, camisa, calca, bota) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    dados = (nome, cpf, nContato, cargo, dataAdmissao, pix, camisa, calca, bota)
    cursor.execute(comando_SQL, dados)
    conexao.commit()

    formulario.lineEdit_Nome.setText('')
    formulario.lineEdit_Cpf.setText('')
    formulario.lineEdit_NumeroContato.setText('')
    formulario.lineEdit_Cargo.setText('')
    formulario.lineEdit_Data.setText('')
    formulario.lineEdit_Pix.setText('')
    formulario.lineEdit_Camisa.setText('')
    formulario.lineEdit_Calca.setText('')
    formulario.lineEdit_Bota.setText('')
    


app = QtWidgets.QApplication([])
formulario = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/formulario_test.ui")
formulario.pushButton_Cadastrar.clicked.connect(inserir)
formulario.pushButton_Relatorio.clicked.connect(lista)

lista = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/lista.ui")
lista.pushButton_AlterarRegistro.clicked.connect(editar)
lista.pushButton_ApagarRegistro.clicked.connect(excluir)

editar = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/telas/editar.ui")
editar.pushButton_ConfirmarAlteracao.clicked.connect(salvar_alteracao)

formulario.show()
app.exec()