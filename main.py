# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_main import Ui_MainWindow
import getMagnet,downloadTorrent
from threading import Thread
import threading
import os,time
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        url = self.lineEditUrl.text()     
        
        try:            
            magnet = getMagnet.getMagent(getMagnet.getHtml(url))
            text = '\n'.join(magnet)
            self.textBrowserMagnet.setText(text)
            self.statusBarDisplay.showMessage("")
        except Exception as e:
            self.statusBarDisplay.showMessage(str(e),2000)
        
        try:
            
            basepath = os.getcwd()
            now = time.strftime("%Y-%m-%d-%H%M",time.localtime(time.time()))
            dirpath = os.path.join(basepath,now)
            if not os.path.exists(dirpath):
                print(dirpath)
                os.makedirs(dirpath)
            
            turl = getMagnet.getSomething(getMagnet.getHtml(url),r'(http://www.rmdown.com/link.php\?hash=.*?)<')
            text = '\n'.join(turl)
            self.textBrowserMagnet.setText(text)
            downloader = downloadTorrent.downloadTorrent()
            index = 1
            self.Tcount = len(turl)
            
            for i in turl:
                try:
                    #self.statusBarDisplay.showMessage("%s doing %d of %d" % (i,index,count))
                    #downloader.getTorrent(i)
                    #self.statusBarDisplay.showMessage("%s done %d of %d" % (i,index,count))
                    a = Thread(target=downloader.getTorrent,args=(i,dirpath))
                    a.setDaemon(True)
                    a.start()
                    pass
                except Exception as e:
                    self.statusBarDisplay.showMessage(str(e),2000)   
            Thread(target=self.display).start() 
        except Exception as e:
            self.statusBarDisplay.showMessage(str(e),2000)        
        #self.statusBarDisplay.showMessage(url)
        
    def display(self):
        while True:
            count = threading.activeCount() - 2
            if count != 0:
                self.statusBarDisplay.showMessage("%d/%d" % (count,self.Tcount), 1000)
                time.sleep(1)
            else:
                self.statusBarDisplay.showMessage('All Done!', 1000)
                break


            

#if __name__ == "__main__":
    #import sys
    #app = QApplication(sys.argv)
    #mainwindow = MainWindow()
    #mainwindow.show()
    #sys.exit(app.exec_())
    