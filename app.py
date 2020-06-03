import os
import sys
import time
from PyQt5.QtGui import QPixmap
from huff import HuffmanCoding
from PyQt5.QtCore import Qt
from PIL import Image
import img as im
import design
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, \
    QComboBox
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Compressor'
        self.left = 400
        self.top = 50
        self.width = 400
        self.height = 500
        self.image_width = 0
        self.i = 1
        self.setFixedSize(self.width, self.height)
        self.setObjectName("main_window")
        self.setStyleSheet(design.stylesheet)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # -------------------------------heading-----------------------------------------------------------
        self.headr = QFrame(self)  # frame=Text
        self.headr.setObjectName("Header")
        self.headr.move(25, 20)
        self.headr_heading = QLabel(self.headr)
        self.headr_heading.setObjectName("Header_Text")
        self.headr_heading.setText("COMPRESSOR")

        # ------------------------------main_window--------------------------------------------------------
        self.frame = QFrame(self)  # frame=Text
        self.frame.setObjectName("Text_button")
        self.frame.move(50, 120)
        self.frame.mousePressEvent = self.frame_clicked
        self.frame_heading = QLabel(self.frame)
        self.frame_heading.setObjectName("Heading")
        self.frame_heading.move(108, 40)
        self.frame_heading.setText("TEXT")

        self.frame1 = QFrame(self)  # frame1==Image
        self.frame1.setObjectName("Text_button")
        self.frame1.move(50, 295)
        self.frame1.mousePressEvent = self.frame1_clicked
        self.frame1_heading = QLabel(self.frame1)
        self.frame1_heading.setObjectName("Heading")
        self.frame1_heading.move(95, 40)
        self.frame1_heading.setText("IMAGE")

        # ------------------------------frame-cliked-expand--------------------------------------------------------
        self.frame_expanded = QFrame(self)  # frame_expanded=single Text file
        self.frame_expanded.setObjectName("Text_button")
        self.frame_expanded.move(50, 120)
        self.frame_expanded.setVisible(False)
        self.frame_expanded.mousePressEvent = self.frame_expanded_clicked
        self.frame_expanded_heading = QLabel(self.frame_expanded)
        self.frame_expanded_heading.setVisible(False)
        self.frame_expanded_heading.move(25, 40)
        self.frame_expanded_heading.setObjectName("Heading")
        self.frame_expanded_heading.setText("Single File")

        self.frame_expanded1 = QFrame(self)  # frame_expanded1= multiple text file
        self.frame_expanded1.setObjectName("Text_button")
        self.frame_expanded1.move(50, 295)
        self.frame_expanded1.setVisible(False)
        self.frame_expanded1.mousePressEvent = self.frame_expanded1_clicked
        self.frame_expanded1_heading = QLabel(self.frame_expanded1)
        self.frame_expanded1_heading.setVisible(False)
        self.frame_expanded1_heading.move(25, 40)
        self.frame_expanded1_heading.setObjectName("Heading")
        self.frame_expanded1_heading.setText("Multi  File")
        self.back_arrow_frame_t = QFrame(self)  # frame1_expanded=single Img file
        self.back_arrow_frame_t.setObjectName("Back_arrow_Frame")
        self.back_arrow_frame_t.move(5, 90)
        self.back_arrow_frame_t.setVisible(False)
        self.back_arrow_frame1_t = QLabel(self.back_arrow_frame_t)
        self.back_arrow_frame1_t.move(0, 0)
        self.back_arrow_frame1_t.setObjectName("Frame_Backarrow")
        self.back_arrow_frame1_t.setTextFormat(Qt.RichText)
        self.back_arrow_frame1_t.setText("&#8592;")
        self.back_arrow_frame1_t.mousePressEvent = self.back_arrow_frame1_t_clicked

        # ------------------------------frame1-cliked-expand--------------------------------------------------------

        self.frame1_expanded = QFrame(self)  # frame1_expanded=single Img file
        self.frame1_expanded.setObjectName("Text_button")
        self.frame1_expanded.move(50, 120)
        self.frame1_expanded.setVisible(False)
        self.frame1_expanded.mousePressEvent = self.frame1_expanded_clicked
        self.frame1_expanded_heading = QLabel(self.frame1_expanded)
        self.frame1_expanded_heading.setVisible(False)
        self.frame1_expanded_heading.move(25, 40)
        self.frame1_expanded_heading.setObjectName("Heading")
        self.frame1_expanded_heading.setText("Single File")

        self.frame1_expanded1 = QFrame(self)  # frame1_expanded1= multiple text file
        self.frame1_expanded1.setObjectName("Text_button")
        self.frame1_expanded1.move(50, 295)
        self.frame1_expanded1.setVisible(False)
        self.frame1_expanded1.mousePressEvent = self.frame1_expanded1_clicked
        self.frame1_expanded1_heading = QLabel(self.frame1_expanded1)
        self.frame1_expanded1_heading.setVisible(False)
        self.frame1_expanded1_heading.move(25, 40)
        self.frame1_expanded1_heading.setObjectName("Heading")
        self.frame1_expanded1_heading.setText("Multi  File")
        self.back_arrow_frame = QFrame(self)
        self.back_arrow_frame.setObjectName("Back_arrow_Frame")
        self.back_arrow_frame.move(5, 90)
        self.back_arrow_frame.setVisible(False)
        self.back_arrow_frame1 = QLabel(self.back_arrow_frame)
        self.back_arrow_frame1.move(0, 0)
        self.back_arrow_frame1.setObjectName("Frame_Backarrow")
        self.back_arrow_frame1.setTextFormat(Qt.RichText)
        self.back_arrow_frame1.setText("&#8592;")
        self.back_arrow_frame1.mousePressEvent = self.back_arrow_frame1_clicked

        # ----------------------------------------------Frame expand single text file clicked--------------------------------------------------
        self.Single_text_clicked_frame = QFrame(self)  # frame1_expanded=single Img file
        self.Single_text_clicked_frame.setObjectName("Big_Frame")
        self.Single_text_clicked_frame.move(25, 120)
        self.Single_text_clicked_frame.setVisible(False)
        self.back_arrow_s = QLabel(self.Single_text_clicked_frame)
        self.back_arrow_s.move(5, 2)
        self.back_arrow_s.setObjectName("Backarrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_s_clicked
        self.single_file_text_heading = QLabel(self.Single_text_clicked_frame)
        self.single_file_text_heading.setObjectName("Heading1")
        self.single_file_text_heading.move(50, 10)
        self.single_file_text_heading.setText("Single Text Compress")

        self.single_file_text_chose = QLabel(self.Single_text_clicked_frame)
        self.single_file_text_chose.setObjectName("chose")
        self.single_file_text_chose.move(20, 90)
        self.single_file_text_chose.setText("Choose Text File")

        self.single_file_text_path = QLineEdit(self.Single_text_clicked_frame)
        self.single_file_text_path.setObjectName("path")
        self.single_file_text_path.move(45, 121)

        self.single_file_text_path_bt = QPushButton(self.Single_text_clicked_frame)
        self.single_file_text_path_bt.setText("Browse")
        self.single_file_text_path_bt.setObjectName("path_bt")
        self.single_file_text_path_bt.move(250, 120)
        self.single_file_text_path_bt.clicked.connect(self.st_path_bt)

        self.single_file_text_chose1 = QLabel(self.Single_text_clicked_frame)
        self.single_file_text_chose1.setObjectName("chose")
        self.single_file_text_chose1.move(20, 190)
        self.single_file_text_chose1.setText("Destination Dir")

        self.single_file_text_path1 = QLineEdit(self.Single_text_clicked_frame)
        self.single_file_text_path1.setObjectName("path")
        self.single_file_text_path1.move(45, 221)

        self.single_file_text_path_bt1 = QPushButton(self.Single_text_clicked_frame)
        self.single_file_text_path_bt1.setText("Browse")
        self.single_file_text_path_bt1.setObjectName("path_bt")
        self.single_file_text_path_bt1.move(250, 220)
        self.single_file_text_path_bt1.clicked.connect(self.st_path_bt1)

        self.single_file_text_com = QPushButton(self.Single_text_clicked_frame)
        self.single_file_text_com.setText("Compress")
        self.single_file_text_com.setObjectName("com")
        self.single_file_text_com.move(25, 275)
        self.single_file_text_com.clicked.connect(self.st_com)

        self.single_file_text_decom = QPushButton(self.Single_text_clicked_frame)
        self.single_file_text_decom.setText("Decompress")
        self.single_file_text_decom.setObjectName("decom")
        self.single_file_text_decom.move(200, 275)
        self.single_file_text_decom.clicked.connect(self.st_decom)
        self.message_text = QMessageBox()

        # ----------------------------------------------Frame expand1 Multiple text file clicked--------------------------------------------------
        self.Multiple_text_clicked_frame = QFrame(self)
        self.Multiple_text_clicked_frame.setObjectName("Big_Frame")
        self.Multiple_text_clicked_frame.move(25, 120)
        self.Multiple_text_clicked_frame.setVisible(False)
        self.back_arrow_m = QLabel(self.Multiple_text_clicked_frame)
        self.back_arrow_m.move(5, 2)
        self.back_arrow_m.setObjectName("Backarrow")
        self.back_arrow_m.setTextFormat(Qt.RichText)
        self.back_arrow_m.setText("&#8592;")
        self.back_arrow_m.mousePressEvent = self.back_arrow_m_clicked
        self.mult_file_text_heading = QLabel(self.Multiple_text_clicked_frame)
        self.mult_file_text_heading.setObjectName("Heading1")
        self.mult_file_text_heading.move(50, 10)
        self.mult_file_text_heading.setText("Multiple Text Compress")

        self.mult_file_text_chose = QLabel(self.Multiple_text_clicked_frame)
        self.mult_file_text_chose.setObjectName("chose")
        self.mult_file_text_chose.move(20, 90)
        self.mult_file_text_chose.setText("Source Directory")

        self.mult_file_text_path = QLineEdit(self.Multiple_text_clicked_frame)
        self.mult_file_text_path.setObjectName("path")
        self.mult_file_text_path.move(45, 121)

        self.mult_file_text_path_bt = QPushButton(self.Multiple_text_clicked_frame)
        self.mult_file_text_path_bt.setText("Browse")
        self.mult_file_text_path_bt.setObjectName("path_bt")
        self.mult_file_text_path_bt.move(250, 120)
        self.mult_file_text_path_bt.clicked.connect(self.mt_path_bt)

        self.mult_file_text_chose1 = QLabel(self.Multiple_text_clicked_frame)
        self.mult_file_text_chose1.setObjectName("chose")
        self.mult_file_text_chose1.move(20, 190)
        self.mult_file_text_chose1.setText("Destination Dir")

        self.mult_file_text_path1 = QLineEdit(self.Multiple_text_clicked_frame)
        self.mult_file_text_path1.setObjectName("path")
        self.mult_file_text_path1.move(45, 221)

        self.mult_file_text_path_bt1 = QPushButton(self.Multiple_text_clicked_frame)
        self.mult_file_text_path_bt1.setText("Browse")
        self.mult_file_text_path_bt1.setObjectName("path_bt")
        self.mult_file_text_path_bt1.move(250, 220)
        self.mult_file_text_path_bt1.clicked.connect(self.mt_path_bt1)

        self.mult_file_text_com = QPushButton(self.Multiple_text_clicked_frame)
        self.mult_file_text_com.setText("Compress")
        self.mult_file_text_com.setObjectName("com")
        self.mult_file_text_com.move(25, 280)
        self.mult_file_text_com.clicked.connect(self.mt_com)

        self.mult_file_text_decom = QPushButton(self.Multiple_text_clicked_frame)
        self.mult_file_text_decom.setText("Decompress")
        self.mult_file_text_decom.setObjectName("decom")
        self.mult_file_text_decom.move(200, 280)
        self.mult_file_text_decom.clicked.connect(self.mt_decom)
        self.message_text1 = QMessageBox()

        # ----------------------------------------------Frame1 expand single IMG file clicked--------------------------------------------------
        self.Single_img_clicked_frame = QFrame(self)  # frame1_expanded=single Img file
        self.Single_img_clicked_frame.setObjectName("Big_Frame")
        self.Single_img_clicked_frame.move(25, 120)
        self.Single_img_clicked_frame.setVisible(False)
        self.back_arrow_si = QLabel(self.Single_img_clicked_frame)
        self.back_arrow_si.move(5, 2)
        self.back_arrow_si.setObjectName("Backarrow")
        self.back_arrow_si.setTextFormat(Qt.RichText)
        self.back_arrow_si.setText("&#8592;")
        self.back_arrow_si.mousePressEvent = self.back_arrow_si_clicked

        self.Single_file_img_heading = QLabel(self.Single_img_clicked_frame)
        self.Single_file_img_heading.setObjectName("Heading1")
        self.Single_file_img_heading.move(50, 10)
        self.Single_file_img_heading.setText("Single Img Compress")

        self.Single_file_img_chose = QLabel(self.Single_img_clicked_frame)
        self.Single_file_img_chose.setObjectName("chose")
        self.Single_file_img_chose.move(20, 50)
        self.Single_file_img_chose.setText("Choose IMG File")

        self.Single_file_img_path = QLineEdit(self.Single_img_clicked_frame)
        self.Single_file_img_path.setObjectName("path")
        self.Single_file_img_path.move(45, 81)

        self.Single_file_img_path_bt = QPushButton(self.Single_img_clicked_frame)
        self.Single_file_img_path_bt.setText("Browse")
        self.Single_file_img_path_bt.setObjectName("path_bt")
        self.Single_file_img_path_bt.move(250, 80)
        self.Single_file_img_path_bt.clicked.connect(self.si_path_bt)

        self.Single_file_img_chose1 = QLabel(self.Single_img_clicked_frame)
        self.Single_file_img_chose1.setObjectName("chose")
        self.Single_file_img_chose1.move(20, 120)
        self.Single_file_img_chose1.setText("Destination Dir")

        self.Single_file_img_path1 = QLineEdit(self.Single_img_clicked_frame)
        self.Single_file_img_path1.setObjectName("path")
        self.Single_file_img_path1.move(45, 151)

        self.Single_file_img_path_bt1 = QPushButton(self.Single_img_clicked_frame)
        self.Single_file_img_path_bt1.setText("Browse")
        self.Single_file_img_path_bt1.setObjectName("path_bt")
        self.Single_file_img_path_bt1.move(250, 150)
        self.Single_file_img_path_bt1.clicked.connect(self.si_path_bt1)

        self.Single_file_img_q = QLabel(self.Single_img_clicked_frame)
        self.Single_file_img_q.setObjectName("chose")
        self.Single_file_img_q.move(20, 190)
        self.Single_file_img_q.setText("Quality")

        self.Single_file_img_qt = QLineEdit(self.Single_img_clicked_frame)
        self.Single_file_img_qt.setObjectName("qt")
        self.Single_file_img_qt.move(45, 220)

        self.Single_file_img_qt_cb = QComboBox(self.Single_img_clicked_frame)
        self.Single_file_img_qt_cb.move(200, 220)
        self.Single_file_img_qt_cb.addItem("High")
        self.Single_file_img_qt_cb.addItem("Medium")
        self.Single_file_img_qt_cb.addItem("Low")
        self.Single_file_img_qt_cb.currentIndexChanged.connect(self.cb_value)
        self.Single_file_img_qt_cb.resize(96, 20)
        self.Single_file_img_qt_cb.setObjectName("cb")

        self.Single_file_img_com = QPushButton(self.Single_img_clicked_frame)
        self.Single_file_img_com.setText("Compress")
        self.Single_file_img_com.setObjectName("com")
        self.Single_file_img_com.move(105, 275)
        self.Single_file_img_com.clicked.connect(self.si_com)

        self.message_text2= QMessageBox()

        # ----------------------------------------------Frame1 expand1 Multiple IMG file clicked--------------------------------------------------
        self.Multiple_img_clicked_frame = QFrame(self)  # frame1_expanded=single Img file
        self.Multiple_img_clicked_frame.setObjectName("Big_Frame")
        self.Multiple_img_clicked_frame.move(25, 120)
        self.Multiple_img_clicked_frame.setVisible(False)
        self.back_arrow_mi = QLabel(self.Multiple_img_clicked_frame)
        self.back_arrow_mi.move(5, 2)
        self.back_arrow_mi.setObjectName("Backarrow")
        self.back_arrow_mi.setTextFormat(Qt.RichText)
        self.back_arrow_mi.setText("&#8592;")
        self.back_arrow_mi.mousePressEvent = self.back_arrow_mi_clicked

        self.Single_file_img_heading = QLabel(self.Multiple_img_clicked_frame)
        self.Single_file_img_heading.setObjectName("Heading1")
        self.Single_file_img_heading.move(50, 10)
        self.Single_file_img_heading.setText("Multiple Img Compress")

        self.Multiple_file_img_chose = QLabel(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_chose.setObjectName("chose")
        self.Multiple_file_img_chose.move(20, 50)
        self.Multiple_file_img_chose.setText("Choose Source Directory")

        self.Multiple_file_img_path = QLineEdit(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_path.setObjectName("path")
        self.Multiple_file_img_path.move(45, 81)

        self.Multiple_file_img_path_bt = QPushButton(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_path_bt.setText("Browse")
        self.Multiple_file_img_path_bt.setObjectName("path_bt")
        self.Multiple_file_img_path_bt.move(250, 80)
        self.Multiple_file_img_path_bt.clicked.connect(self.mi_path_bt)

        self.Multiple_file_img_chose1 = QLabel(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_chose1.setObjectName("chose")
        self.Multiple_file_img_chose1.move(20, 120)
        self.Multiple_file_img_chose1.setText("Destination Directory")

        self.Multiple_file_img_path1 = QLineEdit(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_path1.setObjectName("path")
        self.Multiple_file_img_path1.move(45, 151)

        self.Multiple_file_img_path_bt1 = QPushButton(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_path_bt1.setText("Browse")
        self.Multiple_file_img_path_bt1.setObjectName("path_bt")
        self.Multiple_file_img_path_bt1.move(250, 150)
        self.Multiple_file_img_path_bt1.clicked.connect(self.mi_path_bt1)

        self.Multiple_file_img_q = QLabel(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_q.setObjectName("chose")
        self.Multiple_file_img_q.move(20, 190)
        self.Multiple_file_img_q.setText("Quality")

        self.Multiple_file_img_qt = QLineEdit(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_qt.setObjectName("qt")
        self.Multiple_file_img_qt.move(45, 220)

        self.Multiple_file_img_qt_cb = QComboBox(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_qt_cb.move(200, 220)
        self.Multiple_file_img_qt_cb.addItem("High")
        self.Multiple_file_img_qt_cb.addItem("Medium")
        self.Multiple_file_img_qt_cb.addItem("Low")
        self.Multiple_file_img_qt_cb.currentIndexChanged.connect(self.cb_value)
        self.Multiple_file_img_qt_cb.resize(96, 20)
        self.Multiple_file_img_qt_cb.setObjectName("cb")

        self.Multiple_file_img_com = QPushButton(self.Multiple_img_clicked_frame)
        self.Multiple_file_img_com.setText("Compress")
        self.Multiple_file_img_com.setObjectName("com")
        self.Multiple_file_img_com.move(105, 275)
        self.Multiple_file_img_com.clicked.connect(self.mi_com)

        self.message_text3 = QMessageBox()






        self.show()

    # --------------------------------functions---------------------------------------------------------

    def frame_clicked(self, event):
        self.back_arrow_frame_t.setVisible(True)
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame1_expanded.setVisible(False)
        self.frame_expanded.setVisible(True)
        self.frame_expanded_heading.setVisible(True)
        self.frame_expanded1.setVisible(True)
        self.frame_expanded1_heading.setVisible(True)
        print("frame-clicked")

    def frame1_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame_expanded.setVisible(False)
        self.frame1_expanded.setVisible(True)
        self.frame1_expanded_heading.setVisible(True)
        self.frame1_expanded1.setVisible(True)
        self.frame1_expanded1_heading.setVisible(True)
        self.back_arrow_frame.setVisible(True)

    def frame_expanded_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame_expanded.setVisible(False)
        self.frame_expanded1.setVisible(False)
        print("clicked Text Single file")
        self.Single_text_clicked_frame.setVisible(True)
        self.back_arrow_frame_t.setVisible(False)

    def frame1_expanded_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame1_expanded.setVisible(False)
        self.frame1_expanded1.setVisible(False)
        print("img single")
        self.Single_img_clicked_frame.setVisible(True)
        self.back_arrow_frame_t.setVisible(False)
        self.back_arrow_frame.setVisible(False)

    def frame_expanded1_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame_expanded.setVisible(False)
        self.frame_expanded1.setVisible(False)
        self.Multiple_text_clicked_frame.setVisible(True)
        print("clicked Text multi file")
        self.back_arrow_frame_t.setVisible(False)
        self.back_arrow_frame.setVisible(False)

    def frame1_expanded1_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.frame1_expanded.setVisible(False)
        self.frame1_expanded1.setVisible(False)
        self.Multiple_img_clicked_frame.setVisible(True)
        print("img multi")
        self.back_arrow_frame_t.setVisible(False)
        self.back_arrow_frame.setVisible(False)

    def back_arrow_s_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.Single_text_clicked_frame.setVisible(False)
        self.frame_expanded.setVisible(True)
        self.frame_expanded_heading.setVisible(True)
        self.frame_expanded1.setVisible(True)
        self.frame_expanded1_heading.setVisible(True)
        self.back_arrow_frame_t.setVisible(True)
        print("clicked")

    def back_arrow_m_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.Multiple_text_clicked_frame.setVisible(False)
        self.frame_expanded.setVisible(True)
        self.frame_expanded_heading.setVisible(True)
        self.frame_expanded1.setVisible(True)
        self.frame_expanded1_heading.setVisible(True)
        self.back_arrow_frame_t.setVisible(True)
        print("clicked")

    def back_arrow_si_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.Single_img_clicked_frame.setVisible(False)
        self.frame1_expanded.setVisible(True)
        self.frame1_expanded_heading.setVisible(True)
        self.frame1_expanded1.setVisible(True)
        self.frame1_expanded1_heading.setVisible(True)
        print("clicked")
        self.back_arrow_frame.setVisible(True)

    def back_arrow_mi_clicked(self, event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.Multiple_img_clicked_frame.setVisible(False)
        self.frame1_expanded.setVisible(True)
        self.frame1_expanded_heading.setVisible(True)
        self.frame1_expanded1.setVisible(True)
        self.frame1_expanded1_heading.setVisible(True)
        print("clicked")
        self.back_arrow_frame.setVisible(True)

    def back_arrow_frame1_clicked(self, event):
        self.frame.setVisible(True)
        self.frame1.setVisible(True)
        self.back_arrow_frame.setVisible(False)
        self.frame1_expanded.setVisible(False)
        self.frame1_expanded_heading.setVisible(False)
        self.frame1_expanded1.setVisible(False)
        self.frame1_expanded1_heading.setVisible(False)
        print("clicked")

    def back_arrow_frame1_t_clicked(self, event):
        self.frame.setVisible(True)
        self.frame1.setVisible(True)
        self.back_arrow_frame_t.setVisible(False)
        self.frame_expanded.setVisible(False)
        self.frame_expanded_heading.setVisible(False)
        self.frame_expanded1.setVisible(False)
        self.frame_expanded1_heading.setVisible(False)
        print("clicked")

    def st_path_bt(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select text file", "",
                                                  "All Files (*);;Text (.txt)")
        if fileName:
            self.single_file_text_path.setText(fileName)

    def st_com(self):
        path = self.single_file_text_path.text()
        des = self.single_file_text_path1.text()
        if path == "":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if des == "":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        h = HuffmanCoding()
        h.compress(path, des)
        self.message_text.setText(h.msg)
        self.message_text.exec()
        self.single_file_text_path.clear()
        self.single_file_text_path1.clear()

    def st_path_bt1(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if direc:
            self.single_file_text_path1.setText(direc)

    def st_decom(self):
        path = self.single_file_text_path.text()
        des = self.single_file_text_path1.text()
        if path=="":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if des=="":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        h = HuffmanCoding()
        h.decompress(path, des)
        self.single_file_text_path.clear()
        self.message_text.setText(h.msg)
        self.message_text.exec()
        self.single_file_text_path.clear()
        self.single_file_text_path1.clear()

    def mt_path_bt(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Source Directory"))
        if direc:
            self.mult_file_text_path.setText(direc)

    def mt_path_bt1(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Destination Directory"))
        if direc:
            self.mult_file_text_path1.setText(direc)

    def mt_com(self):

        spath = self.mult_file_text_path.text()
        dpath = self.mult_file_text_path1.text()
        if spath == "":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if dpath == "":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        files = os.listdir(spath)
        start=time.time()
        for file in files:
            h = HuffmanCoding()
            old_file = spath + "/" + file
            new_file = dpath
            h.compress(old_file, new_file)
        end = time.time()
        self.mult_file_text_path1.clear()
        self.mult_file_text_path.clear()
        self.message_text.setText('Compression Done!  And time take is ' + str(
                round((end - start),
                      3)) + "s")
        self.message_text.exec()

    def mt_decom(self):
        spath = self.mult_file_text_path.text()
        dpath = self.mult_file_text_path1.text()
        if spath=="":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if dpath=="":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        files = os.listdir(spath)
        start=time.time()
        for file in files:
            h = HuffmanCoding()
            old_file = spath + "/" + file
            new_file = dpath
            h.decompress(old_file, new_file)
        end=time.time()
        self.mult_file_text_path1.clear()
        self.mult_file_text_path.clear()

        self.message_text1.setText("Decompression Done! in "+str(
                round((end - start),
                      3)) + "s")
        self.message_text1.exec()

    def si_path_bt(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*)")
        if fileName:
            self.Single_file_img_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.Single_file_img_qt.setText(str(self.image_width))

    def cb_value(self):
        if self.Single_file_img_qt_cb.currentText() == "High":
            self.Single_file_img_qt.setText(str(self.image_width))
        if self.Single_file_img_qt_cb.currentText() == "Medium":
            self.Single_file_img_qt.setText(str(int(self.image_width / 2)))
        if self.Single_file_img_qt_cb.currentText() == "Low":
            self.Single_file_img_qt.setText(str(int(self.image_width / 4)))

        if self.Multiple_file_img_qt_cb.currentText() == "High":
            self.i = 1
            self.Multiple_file_img_qt.setText(str(self.image_width))
        if self.Multiple_file_img_qt_cb.currentText() == "Medium":
            self.i= 2
            self.Multiple_file_img_qt.setText(str(int(self.image_width / 2)))
        if self.Multiple_file_img_qt_cb.currentText() == "Low":
            self.i = 4
            self.Multiple_file_img_qt.setText(str(int(self.image_width / 4)))

    def si_path_bt1(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if direc:
            self.Single_file_img_path1.setText(direc)

    def si_com(self):
        spath = self.Single_file_img_path.text()
        dpath = self.Single_file_img_path1.text()
        if spath=="":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if dpath=="":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        filename = spath.split("/")
        start = time.time()
        im.compress_img(spath, dpath + "/" + filename[-1], int(self.Single_file_img_qt.text()))
        self.Single_file_img_path.clear()
        self.Single_file_img_path1.clear()
        self.Single_file_img_qt.clear()
        get_original_filesize1 = os.path.getsize(spath)
        get_compressed_filesize1 = os.path.getsize(dpath + "/" + filename[-1])
        percentage1 = (get_compressed_filesize1 / get_original_filesize1) * 100
        print(round(percentage1, 3), "%")
        end = time.time()
        print(round((end - start), 3), "s")

        self.message_text2.setDetailedText(
            'Compression Done! with Ratio ' + str(round(percentage1, 3)) + "% And time take is " + str(
                round((end - start),
                      3)) + "s")
        self.message_text2.setIconPixmap(QPixmap(dpath + "/" + filename[-1]))
        self.message_text2.exec()

    def mi_path_bt(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Source Directory"))
        if direc:
            self.Multiple_file_img_path.setText(direc)
            files = os.listdir(direc)
            print(files[0])
            img = Image.open(direc+"/"+files[0])
            self.image_width = img.width
            self.Multiple_file_img_qt.setText(str(self.image_width))

    def mi_path_bt1(self):
        direc = str(QFileDialog.getExistingDirectory(self, "Select Destination Directory"))
        if direc:
            self.Multiple_file_img_path1.setText(direc)

    def mi_com(self):
        spath = self.Multiple_file_img_path.text()
        dpath = self.Multiple_file_img_path1.text()
        if spath=="":
            self.message_text.setText("Please Enter the source path")
            self.message_text.exec()
            exit()
        if dpath=="":
            self.message_text.setText("Please Enter destination path")
            self.message_text.exec()
            exit()
        files = os.listdir(spath)
        start = time.time()
        for file in files:
            old_img = spath + "/" + file
            new_img = dpath + "/" + file
            img = Image.open(old_img)
            self.image_width = img.width
            im.compress_img(old_img, new_img, int(self.image_width/self.i))
        end = time.time()
        self.message_text3.setText("Compression Done! in " + str(round((end - start), 3)) + "s")
        self.message_text3.exec()
        self.Multiple_file_img_path1.clear()
        self.Multiple_file_img_path.clear()
        self.Multiple_file_img_qt.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
