import os
import sys
import time
# import serial
# import RPi.GPIO as GPIO
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt,QTimer
from functools import partial
# from OCR import imageocr

# Define the serial port
# arduino_port = '/dev/ttyACM0'  # Change this to match your Arduino port
# arduino_baudrate = 9600  # Make sure this matches the baud rate in your Arduino code

# Initialize serial communication with the Arduino
# arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

class MedicationInformation:
    def __init__(self, name=str('Empty'), dose=0, qty=0, expire=str(), dpd=None, ppd=None, timehour=None, timehour2=None, timemin=None, timemin2=None):
        self.name = name
        self.dose = dose
        self.qty = qty
        self.expire = expire
        self.dpd = dpd
        self.ppd = ppd
        self.timehour = timehour
        self.timehour2 = timehour2
        self.timemin = timemin
        self.timemin2 = timemin2

    def check_time(self):
        hour = int(time.strftime("%H"))
        min = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        if hour == self.timehour and min == self.timemin and sec == 0 or hour == self.timehour2 and min == self.timemin2 and sec == 0:
            if self.ppd == 2:
                if self.qty > 1:
                    print("Time to take your medication!")
                    self.qty -= 1
                    time.sleep(30)
                    print("Time to take your medication!")
                    self.qty -= 1
                else:
                    print("Time to take your medication!")
                    self.qty -= 1
                    time.sleep(1)
            else:
                if self.qty > 0:
                    print("Time to take your medication!")
                    self.qty -= 1
                    time.sleep(1)

    def __str__(self):
        return f"Medication Name:  {self.name}\n             Dosage:  {self.dose}\n            Quantity:  {self.qty}\n   Expiration Date:  {self.expire}"

prescription1 = MedicationInformation()
prescription2 = MedicationInformation()
prescription3 = MedicationInformation()
prescription4 = MedicationInformation()

class MedicationDispenser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Medication Dispenser")
        self.setGeometry(0, 0, 800, 480)  # Set window dimensions
        # self.setupGPIO()
        self.initUI()

        self.clock = QTimer()
        self.clock.timeout.connect(self.update_time)
        self.clock.timeout.connect(self.check_all_medications)
        self.clock.start(100)

    def update_time(self):
        if self.current_screen == "main_menu":
            current_time = time.localtime()
            formatted_hour = time.strftime("%I", current_time).lstrip('0')  # Format hour and remove leading zero
            formatted_time = formatted_hour + time.strftime(":%M %p", current_time)  # Concatenate formatted hour with the rest of the time
            self.time_label.setText(formatted_time)
            self.time_label.setAlignment(Qt.AlignCenter)

    def check_all_medications(self):
        # Check all instances of MedicationInformation
        prescription1.check_time()
        prescription2.check_time()
        prescription3.check_time()
        prescription4.check_time()

    # def setupGPIO(self):
    #     """Configures the GPIO pins for the Raspberry Pi."""
    #     GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbers
    #     self.button_pins = [0, 1, 22, 23, 5, 6, 16, 26]  # Update to your specific GPIO pin setup
    #     for pin in self.button_pins:
    #         GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.checkButtonPresses)
    #     self.timer.start(100)

    # def checkButtonPresses(self):
    #     """Checks for button presses."""
    #     for pin in self.button_pins:
    #         if GPIO.input(pin) == GPIO.LOW:
    #             self.button_pressed(pin)
    #             time.sleep(0.2)  # Debounce delay

    def button_pressed(self, pin):
        label = self.get_button_label(pin, self.current_screen)
        if label is not None:
            self.trigger_button_click(label)

    def get_button_label(self, pin, screen):
        labels = {
            "main_menu": {
                0: "Add Med",
                23: "Delete Med",
                5: "Med Info",
                26: "Sound"
            },
            "screen_1": {
                23: "Home",
                26: "Take picture"
            },
            "screen_2": {
                23: "Retake",
                26: "Confirm"      
            },
            "screen_3": {
                0: "Time 1",
                1: "Time 2",
                23: "Home", 
            },
            "screen_4": {
                0: "Hour Up",
                1: "Hour Down",
                23: "Home",
                5: "Min Up",
                6: "Min Down",
                26: "Ok"
            },
            "screen_5": {
                0: "Hour Up",
                1: "Hour Down",
                23: "Home",
                5: "Min Up",
                6: "Min Down",
                26: "Ok"
            },
            "screen_6": {
                23: "Home",
            },
            "screen_7": {
                0: "Delete med 1",
                1: "Delete med 2",
                23: "Home",
            },
            "screen_8": {
                23: "Home",
                26: "Delete"
            },
            "screen_9": {
                23: "Home",
                26: "Delete"
            },
            "screen_10": {
                0: "%s" % prescription1.name,
                1: "%s" % prescription2.name,
                5: "%s" % prescription3.name,
                6: "%s" % prescription4.name,
                23: "Home"
            },
            "screen_11": {
                23: "Home"
            },
            "screen_12": {
                23: "Home"
            },
            "screen_13": {
                22: "ON",
                23: "Home",
                16: "OFF",
            },
            "screen_14": {
                23: "Home"
            },
            "screen_15": {
                23: "Home"
            },
            "screen_16": {
                23: "Home"
            },
            "screen_17": {
                23: "Home"
            }
        }
        return labels.get(screen, {}).get(pin)

    def trigger_button_click(self, label):
        for widget in self.centralWidget().findChildren(QPushButton):
            if widget.text() == label:
                widget.click()
                break

    def initUI(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(200)  # Set horizontal spacing between columns
        self.grid_layout.setVerticalSpacing(20)  # Set vertical spacing between rows
        self.grid_layout.setContentsMargins(20, 20, 20, 20)  # Set margins to 20
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

        self.current_screen = "main_menu"
        self.updateScreen(self.current_screen)

    def updateScreen(self, screen):
        """Updates the displayed options based on the current screen context."""
        self.current_screen = screen
        self.clearLayout(self.grid_layout)
        button_labels = self.getButtonLabels(screen)
        row, col = 0, 0
        for label, screen_name in button_labels:
            if label is None:
                empty_widget = QWidget()  # Create an empty widget
                self.grid_layout.addWidget(empty_widget, row, col)
            else:
                button = QPushButton(label)
                button.setFixedSize(250, 90)  # Set button size
                button.setStyleSheet("""
                    QPushButton {
                        font-weight: bold;
                        font-size: 40px;
                        color: black;
                        border: 4px solid black;
                        background-color: white;  /* Set normal background color */
                    }
                    QPushButton:pressed {
                        background-color: lightgrey;  /* Set pressed background color */
                    }
                """)

                if label == "Add Med":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Plus.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)
                    button.setIconSize(pixmap_resized.size())  # Set icon size to match pixmap size

                if label == "Take picture":  # Check if the label is "1"
                    button.clicked.connect(self.ocr_function)  # Connect button click to function
                    
                if label == "Hour up":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Up.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Hour down":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Down.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Min up":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Up.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Min down":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Down.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)
                
                button.clicked.connect(partial(self.onButtonClick, screen_name)) # Connect button click to screen update
                self.grid_layout.addWidget(button, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        if screen == "main_menu":
            self.time_label = QLabel()
            self.time_label.setStyleSheet("font-size: 80px; font-weight: bold; padding-top: 60px;")
            self.grid_layout.addWidget(self.time_label, 1, 0, 1, 2) 
                
        if screen == "screen_1":
            textbox = QLabel("OCR Instructions")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2) 
                           
        if screen == "screen_2":
            textbox = QLabel("%s" % prescription1)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns
            
        if screen == "screen_4":
            textbox = QLabel("Time 1")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_5":
            textbox = QLabel("Time 2")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_6":
            textbox = QLabel("Pour Bottle")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_8":
            textbox = QLabel("Medication 1 Delete")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_9":
            textbox = QLabel("Medication 2 Delete")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_11":
            textbox = QLabel("%s" % prescription1)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_12":
            textbox = QLabel("%s" % prescription2)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_13":
            textbox = QLabel("%s" % prescription3)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_14":
            textbox = QLabel("%s" % prescription4)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_15":
            textbox = QLabel("Text to speech option")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_16":
            textbox = QLabel("Text to speech ON")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_17":
            textbox = QLabel("Text to speech OFF")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

    def getButtonLabels(self, screen):
        button_labels = []
        if screen == "main_menu":
            button_labels = [("Add Med", "screen_1"), ("Med Info", "screen_10"), (None, None), (None, None), (None, None), (None, None), ("Delete Med", "screen_7"), ("Sound", "screen_15")]
        elif screen == "screen_1":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), ("Take picture","screen_2")]
        elif screen == "screen_2":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Retake", "screen_1"), ("Confirm","screen_3")] 
        elif screen == "screen_3":
            button_labels = [("Time 1", "screen_4"), (None, None), ("Time 2", "screen_5"), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_4":
            button_labels = [("Hour Up", "screen_4"), ("Min Up", "screen_4"), ("Hour Down", "screen_4"), ("Min Down", "screen_4"), (None, None), (None, None), ("Home", "main_menu"), ("Ok", "screen_6")]
        elif screen == "screen_5":
            button_labels = [("Hour Up", "screen_5"), ("Min Up", "screen_5"), ("Hour Down", "screen_5"), ("Min Down", "screen_5"), (None, None), (None, None), ("Home", "main_menu"), ("Ok", "screen_6")]
        elif screen == "screen_6":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_7":
            button_labels = [("Delete med 1", "screen_8"), (None, None), ("Delete med 2", "screen_9"), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_8":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), ("Delete","main_menu")]
        elif screen == "screen_9":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), ("Delete","main_menu")]
        elif screen == "screen_10":
            button_labels = [("%s"%prescription1.name, "screen_11"), ("%s"%prescription3.name, "screen_13"), ("%s"%prescription2.name, "screen_12"), ("%s"%prescription4.name, "screen_14"), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_11":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_12":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_13":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_14":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_15":
            button_labels = [(None, None), (None, None), (None, None), (None, None), ("ON", "screen_16"), ("OFF", "screen_17"), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_16":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_17":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        return button_labels

    def clearLayout(self, layout):
        """Remove all widgets from the layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def onButtonClick(self, screen):
        """Updates the screen when a button is clicked."""
        self.updateScreen(screen)

    def ocr_function(self):
        # imageocr(prescription1)
        print("OCR Done")

def main():
    app = QApplication(sys.argv)
    window = MedicationDispenser()
    window.show()
    sys.exit(app.exec())

main()