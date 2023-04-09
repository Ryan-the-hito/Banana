class window4(QWidget):  # Customization settings
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.setUpMainWindow()
        self.resize(350, 150)
        self.center()
        self.setWindowTitle('Customization settings')
        self.setFocus()

    def setUpMainWindow(self):
        self.widgeten = QComboBox(self)
        self.widgeten.setEditable(False)
        defalist = ['ChatGPT (Official module)', 'ChatGPT (httpx)']
        self.widgeten.addItems(defalist)
        Which = codecs.open('which.txt', 'r', encoding='utf-8').read()
        if Which == '0':
            self.widgeten.setCurrentIndex(0)
        if Which == '1':
            self.widgeten.setCurrentIndex(1)
        self.widgeten.currentIndexChanged.connect(self.IndexChange)

        self.leapi = QLineEdit(self)
        self.leapi.setPlaceholderText('API here...')
        Apis = codecs.open('api.txt', 'r', encoding='utf-8').read()
        if Apis != '':
            self.leapi.setText(Apis)

        self.lemaxtokens = QLineEdit(self)
        self.lemaxtokens.setPlaceholderText('Maxtokens here...(0~1024)')
        maxto = codecs.open('maxtokens.txt', 'r', encoding='utf-8').read()
        if maxto != '':
            self.lemaxtokens.setText(maxto)

        self.letemp = QLineEdit(self)
        self.letemp.setPlaceholderText('Temperature here...(0~1)')
        temp = codecs.open('temperature.txt', 'r', encoding='utf-8').read()
        if temp != '':
            self.letemp.setText(temp)

        btn_1 = QPushButton('Save', self)
        btn_1.clicked.connect(self.SaveAPI)
        btn_1.setFixedSize(80, 20)

        qw2 = QWidget()
        vbox2 = QHBoxLayout()
        vbox2.setContentsMargins(0, 0, 0, 0)
        vbox2.addStretch()
        vbox2.addWidget(btn_1)
        vbox2.addStretch()
        qw2.setLayout(vbox2)

        vbox1 = QVBoxLayout()
        vbox1.setContentsMargins(20, 20, 20, 20)
        vbox1.addWidget(self.widgeten)
        vbox1.addWidget(self.leapi)
        vbox1.addWidget(self.lemaxtokens)
        vbox1.addWidget(self.letemp)
        vbox1.addWidget(qw2)
        self.setLayout(vbox1)

    def IndexChange(self, i):
        if i == 0:
            with open('which.txt', 'w', encoding='utf-8') as f0:
                f0.write('0')
        if i == 1:
            with open('which.txt', 'w', encoding='utf-8') as f0:
                f0.write('1')

    def SaveAPI(self):
        with open('api.txt', 'w', encoding='utf-8') as f1:
            f1.write(self.leapi.text())
        with open('maxtokens.txt', 'w', encoding='utf-8') as f1:
            f1.write(self.lemaxtokens.text())
        with open('temperature.txt', 'w', encoding='utf-8') as f1:
            f1.write(self.letemp.text())
        self.close()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def activate(self):  # 设置窗口显示
        self.show()
        self.setFocus()
        self.raise_()
        self.activateWindow()

    def cancel(self):  # 设置取消键的功能
        self.close()