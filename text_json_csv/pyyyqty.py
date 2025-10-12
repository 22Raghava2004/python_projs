import sys   # importing sys module so we can access commandd line arguments anduse sys.exit(to cleanly exit the application)
from PyQt5.QtWidgets import QApplication, QMainWindow ,QLabel

from PyQt5.QtGui import QIcon #importing QIcon class to set the window icon
from PyQt5.QtGui import QFont #importing QFont class to set the font of the label
from PyQt5.QtCore import Qt #importing Qt module to access various constants and flags
from PyQt5.QtGui import QPixmap #importing QPixmap class to handle images   




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(700,300,600,600)
        self.setWindowIcon(QIcon("rag.jpeg")) #setting the window icon using an image file named "icon.png"
        label=QLabel("hello",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,300,300)
        label.setStyleSheet("color:blue;"
                            "background-color:yellow;"
                            "font-weight:bold;"
                            "text-decoration :underline;") 
                            
      
        pixmap=QPixmap("rag.jpeg")
        label.setPixmap(pixmap) 
        label.setScaledContents(True)
        label.setGeometry(self.width()//2 -150 ,self.height()//2 -150,300,300)
       # label.setAlignment(Qt.AlignTop) #aligning the text to the center of the label using Qt.AlignCenter constant
        #label.setAlignment( Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignRight)
       # label.setAlignment(Qt.AlignBottom ) #aligning the text to the bottom-right corner of the label using bitwise OR operator to combine two alignment flags
        #label.setAlignment(Qt.AlignHCenter)
        label.setAlignment(Qt.AlignCenter)






def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__ =="__main__":
    main()
    