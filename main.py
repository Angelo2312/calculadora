
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.zeroButton.clicked.connect(lambda: pressionado('0'))
        self.ui.oneButton.clicked.connect(lambda: pressionado('1'))
        self.ui.twoButton.clicked.connect(lambda: pressionado('2'))
        self.ui.threeButton.clicked.connect(lambda: pressionado('3'))
        self.ui.fourButton.clicked.connect(lambda: pressionado('4'))
        self.ui.fiveButton.clicked.connect(lambda: pressionado('5'))
        self.ui.sixButton.clicked.connect(lambda: pressionado('6'))
        self.ui.sevenButton.clicked.connect(lambda: pressionado('7'))
        self.ui.eightButton.clicked.connect(lambda: pressionado('8'))
        self.ui.nineButton.clicked.connect(lambda: pressionado('9'))
        self.ui.equalButton.clicked.connect(lambda: resultado())
        self.ui.clearButton.clicked.connect(lambda: clearOutput())
        self.ui.deleteButton.clicked.connect(lambda: delete())
        self.ui.plusButton.clicked.connect(lambda: pressionado('+'))
        self.ui.minusButton.clicked.connect(lambda: pressionado('-'))
        self.ui.timesButton.clicked.connect(lambda: pressionado('*'))
        self.ui.divisionButton.clicked.connect(lambda: pressionado('/'))
        self.ui.dotButton.clicked.connect(lambda: pressionado('.'))
        self.ui.percentageButton.clicked.connect(lambda: porcentagem())
        self.ui.negativeButton.clicked.connect(lambda: negativo())


        def negativo():
            saida = self.ui.outputLabel.text() 
            try:
                negativo = float(saida ) * -1
                self.ui.outputLabel.setText(str(negativo))
            except:
                self.ui.outputLabel.setText('SYNTAX ERROR')

        def porcentagem():
            saida = self.ui.outputLabel.text()  
            porcent = float(saida) / 100
            self.ui.outputLabel.setText(str(porcent))


        def resultado():
            saida = self.ui.outputLabel.text()  

            try:         
                resposta = eval(saida)
                if (resposta - int(resposta)) == 0:

                    resposta = int(resposta)
                    self.ui.outputLabel.setText(str(resposta))
                else:
                    self.ui.outputLabel.setText(str(f'{resposta:.2f}'))

            except:
                self.ui.outputLabel.setText('SYNTAX ERROR')

        def delete():
            saida = self.ui.outputLabel.text()
            self.ui.outputLabel.setText(saida[:-1])


        def clearOutput():
            self.ui.outputLabel.setText(" ")

        self.operacoes = ['+' , '-' , '*' , '/', ]
        self.ponto = '.'

        def pressionado(tecla):
            saida = self.ui.outputLabel.text()

            if tecla in self.operacoes and saida[-1] in self.operacoes:
                saida = saida[:-1]

            if tecla == self.ponto and saida[-1] == self.ponto:
                saida = saida[:-1]
            
            saida += tecla

            if saida[:-1] == 'SYNTAX ERROR':
                ultimo = saida[-1]
                saida = ' '
                saida += ultimo

            self.ui.outputLabel.setText(saida)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())