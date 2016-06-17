__author__ = 'Anurag'
import sys
from PyQt4 import Qt

# We instantiate a QApplication passing the arguments of the script to it:
a = Qt.QApplication(sys.argv)
hello = Qt.QLabel("Hello, World")
hello.show()
a.exec_()
