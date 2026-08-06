import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QSlider, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

class ColorTester(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(460, 240, 1000, 600)
        self.setMinimumSize(400, 200)
        self.setWindowTitle("colorpicker") 
        
        self.button1 = QPushButton("COLOR 1")
        self.button2 = QPushButton("COLOR 2")
        self.button3 = QPushButton("COLOR 3")
        
        self.color1 = QLabel("", self)
        self.color2 = QLabel("", self)
        self.color3 = QLabel("", self)
        
        for color_label in [self.color1, self.color2, self.color3]:
            color_label.setMinimumSize(50, 50)
            color_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.color_value1_label = QLabel("0", self)
        self.color_value2_label = QLabel("0", self)
        self.color_value3_label = QLabel("0", self)
        
        self.color_value1_label.setFixedWidth(30)
        self.color_value2_label.setFixedWidth(30)
        self.color_value3_label.setFixedWidth(30)
        
        self.slider1 = QSlider(Qt.Orientation.Horizontal)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(255)
        
        self.slider2 = QSlider(Qt.Orientation.Horizontal)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(255)
        
        self.slider3 = QSlider(Qt.Orientation.Horizontal)
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(255)
        
        self.color1_red = 0
        self.color1_green = 0
        self.color1_blue = 0
        
        self.color2_red = 0
        self.color2_green = 0
        self.color2_blue = 0
        
        self.color3_red = 0
        self.color3_green = 0
        self.color3_blue = 0
        
        self.current_color = "1"
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        hbox_colors = QHBoxLayout()
        hbox_colors.addWidget(self.color1)
        hbox_colors.addWidget(self.color2)
        hbox_colors.addWidget(self.color3)
        
        hbox_slider1 = QHBoxLayout()
        hbox_slider1.addWidget(self.slider1)
        hbox_slider1.addWidget(self.color_value1_label)
        
        hbox_slider2 = QHBoxLayout()
        hbox_slider2.addWidget(self.slider2)
        hbox_slider2.addWidget(self.color_value2_label)
        
        hbox_slider3 = QHBoxLayout()
        hbox_slider3.addWidget(self.slider3)
        hbox_slider3.addWidget(self.color_value3_label)
        
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.button1)
        hbox_buttons.addWidget(self.button2)
        hbox_buttons.addWidget(self.button3)
        
        main_layout.addLayout(hbox_colors, stretch=4)
        main_layout.addLayout(hbox_slider1, stretch=1)
        main_layout.addLayout(hbox_slider2, stretch=1)
        main_layout.addLayout(hbox_slider3, stretch=1)
        main_layout.addLayout(hbox_buttons, stretch=1)
        
        self.setLayout(main_layout)
        
        self.button1.setStyleSheet("background-color: rgb(0,185,255)")
        self.button2.setStyleSheet("background-color: rgb(240,240,240)")
        self.button3.setStyleSheet("background-color: rgb(240,240,240)")
        
        self.slider1.valueChanged.connect(self.update_slider1)
        self.slider2.valueChanged.connect(self.update_slider2)
        self.slider3.valueChanged.connect(self.update_slider3)
        
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        
        self.update_preview()

    def update_preview(self):
        self.color1.setStyleSheet(f"background-color: rgb({self.color1_red}, {self.color1_green}, {self.color1_blue});")
        self.color2.setStyleSheet(f"background-color: rgb({self.color2_red}, {self.color2_green}, {self.color2_blue});")
        self.color3.setStyleSheet(f"background-color: rgb({self.color3_red}, {self.color3_green}, {self.color3_blue});")

    def update_slider1(self, value):
        if self.current_color == "1":
            self.color1_red = value
        elif self.current_color == "2":
            self.color2_red = value
        else:
            self.color3_red = value
        self.color_value1_label.setText(str(value))
        self.update_preview()

    def update_slider2(self, value):
        if self.current_color == "1":
            self.color1_green = value
        elif self.current_color == "2":
            self.color2_green = value
        else:
            self.color3_green = value
        self.color_value2_label.setText(str(value))
        self.update_preview()

    def update_slider3(self, value):
        if self.current_color == "1":
            self.color1_blue = value
        elif self.current_color == "2":
            self.color2_blue = value
        else:
            self.color3_blue = value
        self.color_value3_label.setText(str(value))
        self.update_preview()

    def button1_clicked(self):
        self.current_color = "1"
        self.slider1.setValue(self.color1_red)
        self.slider2.setValue(self.color1_green)
        self.slider3.setValue(self.color1_blue)
        self.color_value1_label.setText(str(self.color1_red))
        self.color_value2_label.setText(str(self.color1_green))
        self.color_value3_label.setText(str(self.color1_blue))
        self.button1.setStyleSheet("background-color: rgb(0,185,255)")
        self.button2.setStyleSheet("background-color: rgb(240,240,240)")
        self.button3.setStyleSheet("background-color: rgb(240,240,240)")

    def button2_clicked(self):
        self.current_color = "2"
        self.slider1.setValue(self.color2_red)
        self.slider2.setValue(self.color2_green)
        self.slider3.setValue(self.color2_blue)
        self.color_value1_label.setText(str(self.color2_red))
        self.color_value2_label.setText(str(self.color2_green))
        self.color_value3_label.setText(str(self.color2_blue))
        self.button1.setStyleSheet("background-color: rgb(240,240,240)")
        self.button2.setStyleSheet("background-color: rgb(0,185,255)")
        self.button3.setStyleSheet("background-color: rgb(240,240,240)")

    def button3_clicked(self):
        self.current_color = "3"
        self.slider1.setValue(self.color3_red)
        self.slider2.setValue(self.color3_green)
        self.slider3.setValue(self.color3_blue)
        self.color_value1_label.setText(str(self.color3_red))
        self.color_value2_label.setText(str(self.color3_green))
        self.color_value3_label.setText(str(self.color3_blue))
        self.button1.setStyleSheet("background-color: rgb(240,240,240)")
        self.button2.setStyleSheet("background-color: rgb(240,240,240)")
        self.button3.setStyleSheet("background-color: rgb(0,185,255)")

def main():
    app = QApplication(sys.argv)
    color_tester = ColorTester()
    color_tester.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
