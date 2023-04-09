style_sheet_ori = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QTableWidget{
        border: 1px solid grey;  
        border-radius:4px;
        background-clip: border;
        background-color: #FFFFFF;
        color: #000000;
        font: 14pt Helvetica;
}
    QWidget#Main {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QPushButton{
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QTableWidget#small{
        border: 1px solid grey;  
        border-radius:4px;
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QLineEdit{
        border-radius:4px;
        border: 1px solid gray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QListWidget{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
    w1 = window_about()  # about
    w2 = window_update()  # update
    w3 = window3()  # main1
    w3.setAutoFillBackground(True)
    p = w3.palette()
    p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
    w3.setPalette(p)
    w4 = window4()  # CUSTOMIZING
    action1.triggered.connect(w1.activate)
    action2.triggered.connect(w2.activate)
    action3.triggered.connect(w3.activate)
    action4.triggered.connect(w3.archivethis)
    action5.triggered.connect(w3.embeditem)
    action6.triggered.connect(w3.showchat)
    action7.triggered.connect(w4.activate)
    action8.triggered.connect(w3.showdelbutton)
    btna4.triggered.connect(w3.activate)
    btna5.triggered.connect(w3.archivethis)
    app.setStyleSheet(style_sheet_ori)
    app.exec()
