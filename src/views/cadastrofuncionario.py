from PyQt5 import uic, QtWidgets

def iniciar():

    nome = str(formulario.lineEdit_Nome.text())
    cpf = str(formulario.lineEdit_Cpf.text())
    nContato = str(formulario.lineEdit_NumeroContato.text())
    cargo = str(formulario.lineEdit_Cargo.text())
    dataAdmissao = str(formulario.lineEdit_Data.text())
    pix = str(formulario.lineEdit_Pix.text())

    print(nome, cpf, nContato, cargo, dataAdmissao, pix)




app = QtWidgets.QApplication([])
formulario = uic.loadUi("C:/Users/devse/OneDrive/Documentos/GitHub/SISTEMA-DE-GERENCIAMENTO/src/views/cadastro.ui")

formulario.pushButton_Cadastrar.clicked.connect(iniciar)

formulario.show()
app.exec()