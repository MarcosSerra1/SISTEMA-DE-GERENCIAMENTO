from PyQt5 import uic, QtWidgets
import mysql.connector

# Estabelecendo uma conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'zeus'
)

numero_id = 0 # Uma variável global para armazenar o ID do item selecionado para edição

def excluir():
    # Função para excluir um registro do banco de dados e remover uma linha da tabela

    remover = lista.tableWidget.currentRow()
    lista.tableWidget.removeRow(remover)

    # Obtendo o ID do registro do banco de dados com base na linha selecionada
    cursor = conexao.cursor()
    cursor.execute('SELECT id_funcionarios FROM funcionarios')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [remover][0]

    # Excluindo o registro do banco de dados usando o ID obtido
    cursor.execute('DELETE FROM funcionarios WHERE id_funcionarioS= ' + str(valor_id))

    conexao.commit()


def editar():
    # Função para preencher o formulário de edição com os dados do registro selecionado para edição

    global numero_id

    dados = lista.tableWidget.currentRow()

    # Obtendo o ID do registro do banco de dados com base na linha selecionada
    cursor = conexao.cursor()
    cursor.execute('SELECT id_funcionarios FROM funcionarios')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dados][0]

    # Obtendo o registro completo do banco de dados com base no ID obtido
    cursor.execute('SELECT * FROM funcionarios WHERE id_funcionarios= ' + str(valor_id))
    leitura_banco = cursor.fetchall()

    editar.show() # Mostrando o formulário de edição
    numero_id = valor_id # Armazenando o ID para uso posterior na operação de atualização

    # Configurando os valores dos campos no formulário de edição com base no registro obtido
    editar.lineEdit_AlterarId.setText(str(leitura_banco[0][0]))
    editar.lineEdit_AlterarNome.setText(str(leitura_banco[0][1]))
    editar.lineEdit_AlterarCpf.setText(str(leitura_banco[0][2]))
    editar.lineEdit_AlterarContato.setText(str(leitura_banco[0][3]))
    editar.lineEdit_AlterarCargo.setText(str(leitura_banco[0][4]))
    editar.lineEdit_AlterarDataAdmissao.setText(str(leitura_banco[0][5]))
    editar.lineEdit_AlterarPix.setText(str(leitura_banco[0][6]))

def salvar_alteracao():
    # Função para salvar as alterações feitas no formulário de edição no banco de dados

    global numero_id

    # Obtendo os valores dos campos do formulário de edição
    id = editar.lineEdit_AlterarId.text()
    nome = editar.lineEdit_AlterarNome.text()
    cpf = editar.lineEdit_AlterarCpf.text()
    n_contato = editar.lineEdit_AlterarContato.text()
    cargo =  editar.lineEdit_AlterarCargo.text()
    data_admissao = editar.lineEdit_AlterarDataAdmissao.text()
    pix = editar.lineEdit_AlterarPix.text()

    # Atualizando o registro no banco de dados usando o ID obtido
    cursor = conexao.cursor()
    cursor.execute("UPDATE funcionarios SET id_funcionarios='{}', nome='{}', cpf='{}', n_contato='{}', cargo='{}', data_admissao='{}', pix='{}' WHERE id_funcionarios={}". format(id, nome, cpf, n_contato, cargo, data_admissao, pix, numero_id))

    editar.close() # Fechando o formulário de edição
    lista.close() # Fechando o formulário de listagem
    formulario.show() # Mostrando o formulário principal

    conexao.commit()

def lista():
    # Função para exibir a lista de registros em um widget de tabela

    lista.show() # Mostrando o formulário de listagem

    cursor = conexao.cursor()
    comando_SQL = 'SELECT * FROM funcionarios'
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()

    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(10)

    # Preenchendo o widget de tabela com os registros obtidos
    for i in range (0, len(leitura_banco)): # i = linhas
        for j in range (0, 10): # j = colunas 
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))


def inserir():
    # Função para inserir um novo registro no banco de dados

    # Obtendo os valores dos campos do formulário principal
    nome = str(formulario.lineEdit_Nome.text())
    cpf = str(formulario.lineEdit_Cpf.text())
    nContato = str(formulario.lineEdit_NumeroContato.text())
    cargo = str(formulario.lineEdit_Cargo.text())
    dataAdmissao = str(formulario.lineEdit_Data.text())
    pix = str(formulario.lineEdit_Pix.text())

    # Inserindo os valores no banco de dados
    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO funcionarios (nome, cpf, n_contato, cargo, data_admissao, pix) VALUES (%s, %s, %s, %s, %s, %s)'
    dados = (nome, cpf, nContato, cargo, dataAdmissao, pix)
    cursor.execute(comando_SQL, dados)
    conexao.commit()

    # Limpando os campos do formulário principal
    formulario.lineEdit_Nome.setText('')
    formulario.lineEdit_Cpf.setText('')
    formulario.lineEdit_NumeroContato.setText('')
    formulario.lineEdit_Cargo.setText('')
    formulario.lineEdit_Data.setText('')
    formulario.lineEdit_Pix.setText('')
    
# Carregando o formulário principal e conectando seus botões às funções correspondentes
app = QtWidgets.QApplication([])
formulario = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/tests/formulario_test.ui")
formulario.pushButton_Cadastrar.clicked.connect(inserir)
formulario.pushButton_Relatorio.clicked.connect(lista)

# Carregando o formulário de listagem e conectando seus botões às funções correspondentes
lista = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/tests/")
lista.pushButton_AlterarRegistro.clicked.connect(editar)
lista.pushButton_ApagarRegistro.clicked.connect(excluir)

# Carregando o formulário de edição e conectando seu botão à função correspondente
editar = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/tests/")
editar.pushButton_ConfirmarAlteracao.clicked.connect(salvar_alteracao)

formulario.show() # Mostrando o formulário principal
app.exec()