import os
import sys
import time
import copy
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
    def __init__(self, name=str('Empty'), dose=0, qty=0, expire=str(), dpd=None, ppd=None, timehour=None, timemin=None, ampm=None, timehour2=None, timemin2=None, ampm2=None):
        self.name = name
        self.dose = dose
        self.qty = qty
        self.expire = expire
        self.dpd = dpd
        self.ppd = ppd
        self.timehour = timehour
        self.timemin = timemin
        self.ampm = ampm
        self.timehour2 = timehour2
        self.timemin2 = timemin2
        self.ampm2 = ampm2

    def __str__(self):
        if self.timehour == None and self.timemin == None and self.ampm == None and self.timehour2 == None and self.timemin2 == None and self.ampm2 == None:
            return f"Medication Name:  {self.name}\n             Dosage:  {self.dose}\n            Quantity:  {self.qty}\n   Expiration Date:  {self.expire}\n   "
        elif self.timehour2 == None and self.timemin2 == None and self.ampm2 == None:
            return f"Medication Name:  {self.name}\n             Dosage:  {self.dose}\n            Quantity:  {self.qty}\n   Expiration Date:  {self.expire}\n   Time 1: {self.timehour}:{self.timemin} {self.ampm}"
        else:
            return f"Medication Name:  {self.name}\n             Dosage:  {self.dose}\n            Quantity:  {self.qty}\n   Expiration Date:  {self.expire}\n   Time 1: {self.timehour}:{self.timemin} {self.ampm}\n Time 2: {self.timehour2}:{self.timemin2} {self.ampm2}"

class MedicationDispenser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.prescription1 = MedicationInformation()
        self.prescription2 = MedicationInformation()
        self.prescription3 = MedicationInformation()
        self.prescription4 = MedicationInformation()
        self.prescriptiontemp = MedicationInformation()
        self.addmed = None

        self.setWindowTitle("Medication Dispenser")
        self.setGeometry(0, 0, 800, 480)  # Set window dimensions
        # self.setupGPIO()
        self.initUI()

        self.clock = QTimer()
        self.clock.timeout.connect(self.update_time)
        self.clock.timeout.connect(self.check_med_time)
        self.clock.start(100)

        # Initialize previous screen and button label variables
        self.previous_screen = None
        self.previous_button_label = None

    def update_time(self):
        if self.current_screen == "main_menu":
            current_time = time.localtime()
            formatted_hour = time.strftime("%I", current_time).lstrip('0')  # Format hour and remove leading zero
            formatted_time = formatted_hour + time.strftime(":%M %p", current_time)  # Concatenate formatted hour with the rest of the time
            self.time_label.setText(formatted_time)
            self.time_label.setAlignment(Qt.AlignCenter)

    def check_med_time(self):
        hour = int(time.strftime("%I"))
        min = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        ampm = str(time.strftime("%p"))
        if hour == self.prescription1.timehour and min == self.prescription1.timemin and sec == 0 and ampm == self.prescription1.ampm or hour == self.prescription1.timehour2 and min == self.prescription1.timemin2 and sec == 0 and ampm == self.prescription1.ampm2:
            if self.prescription1.ppd == 2:
                if self.prescription1.qty > 1:
                    print("Time to take your medication!")
                    self.prescription1.qty -= 1
                    time.sleep(30)
                    print("Time to take your medication!")
                    self.prescription1.qty -= 1
                else:
                    print("Time to take your medication!")
                    self.prescription1.qty -= 1
                    time.sleep(1)
            else:
                if self.prescription1.qty > 0:
                    print("Time to take your medication!")
                    self.prescription1.qty -= 1
                    time.sleep(1)
        elif hour == self.prescription2.timehour and min == self.prescription2.timemin and sec == 0 and ampm == self.prescription2.ampm or hour == self.prescription2.timehour2 and min == self.prescription2.timemin2 and sec == 0 and ampm == self.prescription2.ampm2:
            if self.prescription2.ppd == 2:
                if self.prescription2.qty > 1:
                    print("Time to take your medication!")
                    self.prescription2.qty -= 1
                    time.sleep(30)
                    print("Time to take your medication!")
                    self.prescription2.qty -= 1
                else:
                    print("Time to take your medication!")
                    self.prescription2.qty -= 1
                    time.sleep(1)
            else:
                if self.prescription2.qty > 0:
                    print("Time to take your medication!")
                    self.prescription2.qty -= 1
                    time.sleep(1)
        elif hour == self.prescription3.timehour and min == self.prescription3.timemin and sec == 0 and ampm == self.prescription3.ampm or hour == self.prescription3.timehour2 and min == self.prescription3.timemin2 and sec == 0 and ampm == self.prescription3.ampm2:
            if self.prescription3.ppd == 2:
                if self.prescription3.qty > 1:
                    print("Time to take your medication!")
                    self.prescription3.qty -= 1
                    time.sleep(30)
                    print("Time to take your medication!")
                    self.prescription3.qty -= 1
                else:
                    print("Time to take your medication!")
                    self.prescription3.qty -= 1
                    time.sleep(1)
            else:
                if self.prescription3.qty > 0:
                    print("Time to take your medication!")
                    self.prescription3.qty -= 1
                    time.sleep(1)
        elif hour == self.prescription4.timehour and min == self.prescription4.timemin and sec == 0 and ampm == self.prescription4.ampm or hour == self.prescription4.timehour2 and min == self.prescription4.timemin2 and sec == 0 and ampm == self.prescription4.ampm2:
            if self.prescription4.ppd == 2:
                if self.prescription4.qty > 1:
                    print("Time to take your medication!")
                    self.prescription4.qty -= 1
                    time.sleep(30)
                    print("Time to take your medication!")
                    self.prescription4.qty -= 1
                else:
                    print("Time to take your medication!")
                    self.prescription4.qty -= 1
                    time.sleep(1)
            else:
                if self.prescription4.qty > 0:
                    print("Time to take your medication!")
                    self.prescription4.qty -= 1
                    time.sleep(1)

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
                26: "Take Picture"
            },
            "screen_2": {
                23: "Retake",
                26: "Confirm"      
            },
            "screen_3": {
                0: "%s 1" % self.prescription1.name if self.prescription1.name == "Empty" else None,
                1: "%s 2" % self.prescription2.name if self.prescription2.name == "Empty" else None,
                5: "%s 3" % self.prescription3.name if self.prescription3.name == "Empty" else None,
                6: "%s 4" % self.prescription4.name if self.prescription4.name == "Empty" else None,
                23: "Home"
            },
            "screen_4": {
                0: "1",
                5: "2"
            },
            "screen_5": {
                0: "1",
                5: "2",
            },
            "screen_6": {
                0: "Hour Up",
                1: "Hour Down",
                23: "AM/PM",
                5: "Min Up",
                6: "Min Down",
                26: "Ok"
            },
            "screen_7": {
                0: "Hour Up",
                1: "Hour Down",
                23: "AM/PM",
                5: "Min Up",
                6: "Min Down",
                26: "Ok"
            },
            "screen_8": {
                23: "Home",
            },
            "screen_9": {
                0: "%s" % self.prescription1.name if self.prescription1.name != "Empty" else "%s 1" % self.prescription1.name,
                1: "%s" % self.prescription2.name if self.prescription2.name != "Empty" else "%s 2" % self.prescription1.name,
                5: "%s" % self.prescription3.name if self.prescription3.name != "Empty" else "%s 3" % self.prescription1.name,
                6: "%s" % self.prescription4.name if self.prescription4.name != "Empty" else "%s 4" % self.prescription1.name,
                23: "Home"
            },
            "screen_10": {
                23: "Home"
            },
            "screen_11": {
                23: "Home"
            },
            "screen_12": {
                23: "Home"
            },
            "screen_13": {
                23: "Home"
            },
            "screen_14": {
                22: "ON",
                23: "Home",
                16: "OFF",
            },
            "screen_15": {
                23: "Home"
            },
            "screen_16": {
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
                    
                if label == "Hour Up":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Up.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Hour Down":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Down.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Min Up":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Up.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)

                if label == "Min Down":  # Check if the label is "1"
                    icon_path = os.path.join(os.path.dirname(__file__), "Down.png")
                    pixmap = QPixmap(icon_path)
                    pixmap_resized = pixmap.scaled(25, 25)  # Resize the icon
                    icon = QIcon(pixmap_resized)
                    button.setIcon(icon)
                
                button.clicked.connect(partial(self.onButtonClick, screen_name, button.text())) # Connect button click to screen update
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
            textbox = QLabel("%s" % self.prescriptiontemp)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_4":
            textbox = QLabel("Doses Per Day")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 60px; font-weight: bold; padding-top: 60px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns
        
        if screen == "screen_5":
            textbox = QLabel("Pills Per Day")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 60px; font-weight: bold; padding-top: 60px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns
            
        if screen == "screen_6":
            if self.addmed == 1:
                prescription = self.prescription1
            elif self.addmed == 2:
                prescription = self.prescription2
            elif self.addmed == 3:
                prescription = self.prescription3
            elif self.addmed == 4:
                prescription = self.prescription4
            textbox = QLabel("Time 1: %s:%s %s" % (prescription.timehour, prescription.timemin, prescription.ampm))
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 60px; font-weight: bold;")
            self.grid_layout.addWidget(textbox, 2, 0, 1, 2)  # Span over two columns

        if screen == "screen_7":
            if self.addmed == 1:
                prescription = self.prescription1
            elif self.addmed == 2:
                prescription = self.prescription2
            elif self.addmed == 3:
                prescription = self.prescription3
            elif self.addmed == 4:
                prescription = self.prescription4
            textbox = QLabel("Time 2: %s:%s %s" % (prescription.timehour2, prescription.timemin2, prescription.ampm2))
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 60px; font-weight: bold;")
            self.grid_layout.addWidget(textbox, 2, 0, 1, 2)  # Span over two columns

        if screen == "screen_8":
            self.addmed = None
            self.prescriptiontemp = MedicationInformation()
            textbox = QLabel("Pour Bottle")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_10":
            textbox = QLabel("%s" % self.prescription1)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_11":
            textbox = QLabel("%s" % self.prescription2)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_12":
            textbox = QLabel("%s" % self.prescription3)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_13":
            textbox = QLabel("%s" % self.prescription4)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setStyleSheet("font-size: 40px; padding-left: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_14":
            textbox = QLabel("Text to speech option")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_15":
            textbox = QLabel("Text to speech ON")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

        if screen == "screen_16":
            textbox = QLabel("Text to speech OFF")
            textbox.setAlignment(Qt.AlignCenter)
            textbox.setStyleSheet("font-size: 40px;")
            self.grid_layout.addWidget(textbox, 1, 0, 1, 2)  # Span over two columns

    def getButtonLabels(self, screen):

        if self.addmed == 1:
            prescription = self.prescription1
        elif self.addmed == 2:
            prescription = self.prescription2
        elif self.addmed == 3:
            prescription = self.prescription3
        elif self.addmed == 4:
            prescription = self.prescription4

        button_labels = []
        if screen == "main_menu":
            button_labels = [("Add Med", "screen_1"), ("Med Info", "screen_9"), (None, None), (None, None), (None, None), (None, None), ("Delete Med", None), ("Sound", "screen_14")]
        elif screen == "screen_1":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), ("Take picture","screen_2")]
        elif screen == "screen_2":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Retake", "screen_1"), ("Confirm","screen_3")] 
        elif screen == "screen_3":
            button_labels = [("%s 1" % self.prescription1.name if self.prescription1.name == "Empty" else None, "screen_4"), ("%s 3" % self.prescription3.name if self.prescription3.name == "Empty" else None, "screen_4"), ("%s 2" % self.prescription2.name if self.prescription2.name == "Empty" else None, "screen_4"), ("%s 4" % self.prescription4.name if self.prescription4.name == "Empty" else None, "screen_4"), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_4":
            button_labels = [("1", "screen_5"), ("2", "screen_5"), (None, None), (None, None), (None, None), (None, None), (None, None), (None,None)]
        elif screen == "screen_5":
            button_labels = [("1", "screen_6"), ("2", "screen_6"), (None, None), (None, None), (None, None), (None, None), (None, None), (None,None)]
        elif screen == "screen_6":
            if prescription.dpd == 2:
                button_labels = [("Hour Up", "screen_6"), ("Min Up", "screen_6"), ("Hour Down", "screen_6"), ("Min Down", "screen_6"), (None, None), (None, None), ("AM/PM", "screen_6"), ("Ok", "screen_7")]
            else:
                button_labels = [("Hour Up", "screen_6"), ("Min Up", "screen_6"), ("Hour Down", "screen_6"), ("Min Down", "screen_6"), (None, None), (None, None), ("AM/PM", "screen_6"), ("Ok", "screen_8")]
        elif screen == "screen_7":
            button_labels = [("Hour Up", "screen_7"), ("Min Up", "screen_7"), ("Hour Down", "screen_7"), ("Min Down", "screen_7"), (None, None), (None, None), ("AM/PM", "screen_7"), ("Ok", "screen_8")]
        elif screen == "screen_8":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_9":
            button_labels = [("%s" % self.prescription1.name if self.prescription1.name != "Empty" else "%s 1" % self.prescription1.name, "screen_10"), ("%s" % self.prescription3.name if self.prescription3.name != "Empty" else "%s 3" % self.prescription3.name, "screen_12"), ("%s" % self.prescription2.name if self.prescription2.name != "Empty" else "%s 2" % self.prescription2.name, "screen_11"), ("%s" % self.prescription4.name if self.prescription4.name != "Empty" else "%s 4" % self.prescription4.name, "screen_13"), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_10":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_11":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_12":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_13":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_14":
            button_labels = [(None, None), (None, None), (None, None), (None, None), ("ON", "screen_15"), ("OFF", "screen_16"), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_15":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        elif screen == "screen_16":
            button_labels = [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None), ("Home", "main_menu"), (None,None)]
        return button_labels

    def clearLayout(self, layout):
        """Remove all widgets from the layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def onButtonClick(self, screen, button_label):
        """Updates the screen when a button is clicked."""
        # Store the previous screen and button label
        self.previous_screen = self.current_screen
        self.previous_button_label = button_label

        # Update the screen
        self.updateScreen(screen)

        # Put OCR Info into self.prescription
        if self.previous_screen == 'screen_3' and self.previous_button_label == 'Empty 1' and self.current_screen == 'screen_4':
            self.prescription1 = copy.copy(self.prescriptiontemp)
            self.addmed = 1
        elif self.previous_screen == 'screen_3' and self.previous_button_label == 'Empty 2' and self.current_screen == 'screen_4':
            self.prescription2 = copy.copy(self.prescriptiontemp)
            self.addmed = 2
        elif self.previous_screen == 'screen_3' and self.previous_button_label == 'Empty 3' and self.current_screen == 'screen_4':
            self.prescription3 = copy.copy(self.prescriptiontemp)
            self.addmed = 3
        elif self.previous_screen == 'screen_3' and self.previous_button_label == 'Empty 4' and self.current_screen == 'screen_4':
            self.prescription4 = copy.copy(self.prescriptiontemp)
            self.addmed = 4

        if self.previous_screen == 'screen_4' and self.previous_button_label == '1' and self.current_screen == 'screen_5':
            if self.addmed == 1:
                self.prescription1.dpd = 1
                self.prescription1.timehour, self.prescription1.timemin, self.prescription1.ampm = 0, 0, 'AM'
            elif self.addmed == 2:
                self.prescription2.dpd = 1
                self.prescription2.timehour, self.prescription2.timemin, self.prescription2.ampm = 0, 0, 'AM'
            elif self.addmed == 3:
                self.prescription3.dpd = 1
                self.prescription3.timehour, self.prescription3.timemin, self.prescription3.ampm = 0, 0, 'AM'
            elif self.addmed == 4:
                self.prescription4.dpd = 1
                self.prescription4.timehour, self.prescription4.timemin, self.prescription4.ampm = 0, 0, 'AM'
        elif self.previous_screen == 'screen_4' and self.previous_button_label == '2' and self.current_screen == 'screen_5':
            if self.addmed == 1:
                self.prescription1.dpd = 2
                self.prescription1.timehour, self.prescription1.timemin, self.prescription1.ampm = 0, 0, 'AM'
                self.prescription1.timehour2, self.prescription1.timemin2, self.prescription1.ampm2 = 0, 0, 'AM'
            elif self.addmed == 2:
                self.prescription2.dpd = 2
                self.prescription2.timehour, self.prescription2.timemin, self.prescription2.ampm = 0, 0, 'AM'
                self.prescription2.timehour2, self.prescription2.timemin2, self.prescription2.ampm2 = 0, 0, 'AM'
            elif self.addmed == 3:
                self.prescription3.dpd = 2
                self.prescription3.timehour, self.prescription3.timemin, self.prescription3.ampm = 0, 0, 'AM'
                self.prescription3.timehour2, self.prescription3.timemin2, self.prescription3.ampm2 = 0, 0, 'AM'
            elif self.addmed == 4:
                self.prescription4.dpd = 2
                self.prescription4.timehour, self.prescription4.timemin, self.prescription4.ampm = 0, 0, 'AM'
                self.prescription4.timehour2, self.prescription4.timemin2, self.prescription4.ampm2 = 0, 0, 'AM'

        if self.previous_screen == 'screen_5' and self.previous_button_label == '1' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                self.prescription1.ppd = 1
            elif self.addmed == 2:
                self.prescription2.ppd = 1
            elif self.addmed == 3:
                self.prescription3.ppd = 1
            elif self.addmed == 4:
                self.prescription4.ppd = 1
        elif self.previous_screen == 'screen_5' and self.previous_button_label == '2' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                self.prescription1.ppd = 2
            elif self.addmed == 2:
                self.prescription2.ppd = 2
            elif self.addmed == 3:
                self.prescription3.ppd = 2
            elif self.addmed == 4:
                self.prescription4.ppd = 2

        if self.previous_screen == 'screen_6' and self.previous_button_label == 'Hour Up' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                if self.prescription1.timehour < 12:
                    self.prescription1.timehour += 1
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timehour < 12:
                    self.prescription2.timehour += 1
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timehour < 12:
                    self.prescription3.timehour += 1
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timehour < 12:
                    self.prescription4.timehour += 1
                else:
                    pass
        elif self.previous_screen == 'screen_6' and self.previous_button_label == 'Hour Down' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                if self.prescription1.timehour > 0:
                    self.prescription1.timehour -= 1
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timehour > 0:
                    self.prescription2.timehour -= 1
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timehour > 0:
                    self.prescription3.timehour -= 1
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timehour > 0:
                    self.prescription4.timehour -= 1
                else:
                    pass
        elif self.previous_screen == 'screen_6' and self.previous_button_label == 'Min Up' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                if self.prescription1.timemin < 45:
                    self.prescription1.timemin += 15
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timemin < 45:
                    self.prescription2.timemin += 15
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timemin < 45:
                    self.prescription3.timemin += 15
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timemin < 45:
                    self.prescription4.timemin += 15
                else:
                    pass
        elif self.previous_screen == 'screen_6' and self.previous_button_label == 'Min Down' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                if self.prescription1.timemin > 0:
                    self.prescription1.timemin -= 15
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timemin > 0:
                    self.prescription2.timemin -= 15
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timemin > 0:
                    self.prescription3.timemin -= 15
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timemin > 0:
                    self.prescription4.timemin -= 15
                else:
                    pass
        elif self.previous_screen == 'screen_6' and self.previous_button_label == 'AM/PM' and self.current_screen == 'screen_6':
            if self.addmed == 1:
                if self.prescription1.ampm == 'AM':
                    self.prescription1.ampm = 'PM'
                elif self.prescription1.ampm == 'PM':
                    self.prescription1.ampm = 'AM'
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.ampm == 'AM':
                    self.prescription2.ampm = 'PM'
                elif self.prescription2.ampm == 'PM':
                    self.prescription2.ampm = 'AM'
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.ampm == 'AM':
                    self.prescription3.ampm = 'PM'
                elif self.prescription3.ampm == 'PM':
                    self.prescription3.ampm = 'AM'
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.ampm == 'AM':
                    self.prescription4.ampm = 'PM'
                elif self.prescription4.ampm == 'PM':
                    self.prescription4.ampm = 'AM'
                else:
                    pass

        if self.previous_screen == 'screen_7' and self.previous_button_label == 'Hour Up' and self.current_screen == 'screen_7':
            if self.addmed == 1:
                if self.prescription1.timehour2 < 12:
                    self.prescription1.timehour2 += 1
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timehour2 < 12:
                    self.prescription2.timehour2 += 1
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timehour2 < 12:
                    self.prescription3.timehour2 += 1
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timehour2 < 12:
                    self.prescription4.timehour2 += 1
                else:
                    pass
        elif self.previous_screen == 'screen_7' and self.previous_button_label == 'Hour Down' and self.current_screen == 'screen_7':
            if self.addmed == 1:
                if self.prescription1.timehour2 > 0:
                    self.prescription1.timehour2 -= 1
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timehour2 > 0:
                    self.prescription2.timehour2 -= 1
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timehour2 > 0:
                    self.prescription3.timehour2 -= 1
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timehour2 > 0:
                    self.prescription4.timehour2 -= 1
                else:
                    pass
        elif self.previous_screen == 'screen_7' and self.previous_button_label == 'Min Up' and self.current_screen == 'screen_7':
            if self.addmed == 1:
                if self.prescription1.timemin2 < 45:
                    self.prescription1.timemin2 += 15
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timemin2 < 45:
                    self.prescription2.timemin2 += 15
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timemin2 < 45:
                    self.prescription3.timemin2 += 15
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timemin2 < 45:
                    self.prescription4.timemin2 += 15
                else:
                    pass
        elif self.previous_screen == 'screen_7' and self.previous_button_label == 'Min Down' and self.current_screen == 'screen_7':
            if self.addmed == 1:
                if self.prescription1.timemin2 > 0:
                    self.prescription1.timemin2 -= 15
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.timemin2 > 0:
                    self.prescription2.timemin2 -= 15
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.timemin2 > 0:
                    self.prescription3.timemin2 -= 15
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.timemin2 > 0:
                    self.prescription4.timemin2 -= 15
                else:
                    pass
        elif self.previous_screen == 'screen_7' and self.previous_button_label == 'AM/PM' and self.current_screen == 'screen_7':
            if self.addmed == 1:
                if self.prescription1.ampm2 == 'AM':
                    self.prescription1.ampm2 = 'PM'
                elif self.prescription1.ampm2 == 'PM':
                    self.prescription1.ampm2 = 'AM'
                else:
                    pass
            elif self.addmed == 2:
                if self.prescription2.ampm2 == 'AM':
                    self.prescription2.ampm2 = 'PM'
                elif self.prescription2.ampm2 == 'PM':
                    self.prescription2.ampm2 = 'AM'
                else:
                    pass
            elif self.addmed == 3:
                if self.prescription3.ampm2 == 'AM':
                    self.prescription3.ampm2 = 'PM'
                elif self.prescription3.ampm2 == 'PM':
                    self.prescription3.ampm2 = 'AM'
                else:
                    pass
            elif self.addmed == 4:
                if self.prescription4.ampm2 == 'AM':
                    self.prescription4.ampm2 = 'PM'
                elif self.prescription4.ampm2 == 'PM':
                    self.prescription4.ampm2 = 'AM'
                else:
                    pass

        # Update the screen
        self.updateScreen(screen)

        print(self.previous_screen, self.previous_button_label, self.current_screen)

    def ocr_function(self):
        # imageocr(self.prescriptiontemp)
        print("OCR Done")

def main():
    app = QApplication(sys.argv)
    window = MedicationDispenser()
    window.show()
    sys.exit(app.exec())

main()
