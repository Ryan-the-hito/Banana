class CustomDialog_warn(QDialog):  # save to banana
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.center()
        self.resize(300, 300)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

    def setUpMainWindow(self):
        l0 = QLabel('Save to Banana🍌?', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(30)
        l0.setFont(font)

        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('banana.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setFixedSize(150, 150)
        l1.setScaledContents(True)

        self.choose_folder = QComboBox(self)
        self.choose_folder.setCurrentIndex(0)
        home_dir = str(Path.home())
        tarname1 = "BananaAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        tarname2 = "Folder.txt"
        self.fullfolder = os.path.join(fulldir1, tarname2)
        textc = codecs.open(self.fullfolder, 'r', encoding='utf-8').read()
        if textc == '':
            with open(self.fullfolder, 'w', encoding='utf-8') as f0:
                f0.write('Default folder')
            self.choose_folder.addItems(['Default folder'])
        if textc != '':
            listc = textc.split('\n')
            while '' in listc:
                listc.remove('')
            self.choose_folder.addItems(listc)
        self.choose_folder.setFixedWidth(260)

        btn_no = QPushButton('Cancel', self)
        btn_no.clicked.connect(self.choosenot)
        btn_no.setFixedWidth(120)

        btn_can = QPushButton('Yes!', self)
        btn_can.clicked.connect(self.cancel)
        btn_can.setFixedWidth(120)

        w0 = QWidget()
        blay0 = QHBoxLayout()
        blay0.setContentsMargins(0, 0, 0, 0)
        blay0.addStretch()
        blay0.addWidget(l0)
        blay0.addStretch()
        w0.setLayout(blay0)

        w1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(l1)
        blay1.addStretch()
        w1.setLayout(blay1)

        w2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(self.choose_folder)
        blay2.addStretch()
        w2.setLayout(blay2)

        w2_1 = QWidget()
        blay2_1 = QHBoxLayout()
        blay2_1.setContentsMargins(0, 0, 0, 0)
        blay2_1.addStretch()
        blay2_1.addWidget(btn_no)
        blay2_1.addWidget(btn_can)
        blay2_1.addStretch()
        w2_1.setLayout(blay2_1)

        w3 = QWidget()
        blay3 = QVBoxLayout()
        blay3.setContentsMargins(20, 20, 20, 20)
        blay3.addStretch()
        blay3.addWidget(w1)
        blay3.addStretch()
        blay3.addWidget(w0)
        blay3.addStretch()
        blay3.addWidget(w2)
        blay3.addWidget(w2_1)
        w3.setLayout(blay3)
        w3.setObjectName("Main")

        blayend = QHBoxLayout()
        blayend.setContentsMargins(0, 0, 0, 0)
        blayend.addWidget(w3)
        self.setLayout(blayend)

    def center(self):  # 设置窗口居中
        # Get the primary screen's geometry
        screen_geometry = self.screen().availableGeometry()

        # Calculate the centered position
        x_center = int((screen_geometry.width() / 2) - (self.width() / 4))
        y_center = (screen_geometry.height() - self.height()) // 2

        # Move the window to the center position
        self.setGeometry(QRect(x_center, y_center, self.width(), self.height()))

    def choosenot(self):
        with open('choose.txt', 'w', encoding='utf-8') as f0:
            f0.write('0')
        self.close()

    def cancel(self):  # 设置取消键的功能
        with open('tarfolder.txt', 'w', encoding='utf-8') as f0:
            f0.write(self.choose_folder.currentText())
        with open('choose.txt', 'w', encoding='utf-8') as f0:
            f0.write('1')
        self.close()