# -*- coding: utf-8 -*-
import sys
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import os

from mainwindowV2 import Ui_MainWindow  # Import the generated UI file
import json
import time

servo_min, servo_max = 500, 2500
motor_min, motor_max = 1000, 2000
servo_neutral = (servo_min + servo_max) / 2
motor_neutral = (motor_min + motor_max) / 2

# Initialize the serial connection (adjust the port and baud rate as needed)
ser = serial.Serial('COM6', 115200)  # Replace 'COM3' with your serial port


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.is_armed = False
        self.servoUsec = None
        self.motorUsec = None
        self.is_live_controlled = False
        self.opened_file = None
        self.is_file_loaded = False
        self.loose_active = False
        self.total_command_sequence_time = 0

        self.setupUi(self)
        # self.armButton.setCheckable(True)  # Make the button checkable to toggle its state
        self.armButton.clicked.connect(self.arm_button_clicked)
        self.liveButton.clicked.connect(self.live_button_clicked)
        self.motorMax.editingFinished.connect(self.update_motor_slider)
        self.motorMin.editingFinished.connect(self.update_motor_slider)
        self.servoMax.editingFinished.connect(self.update_servo_slider)
        self.servoMin.editingFinished.connect(self.update_servo_slider)
        self.motorSlider.valueChanged.connect(self.update_motor_counter)
        self.pitchSlider.valueChanged.connect(self.update_servo_counter)
        self.openFile.clicked.connect(self.open_file_dialog)
        self.looseButton.clicked.connect(self.loose)

        self.motorMax.setText(str(motor_max))
        self.motorMin.setText(str(motor_min))
        self.servoMax.setText(str(servo_max))
        self.servoMin.setText(str(servo_min))
        self.update_motor_slider()
        self.update_servo_slider()
        self.pitchSlider.setValue(int((servo_max + servo_min) / 2))

        self.commands = []
        self.command_index = 0

        self.last_time = time.time()
        self.last_command_time = 0
        self.next_command_time = 0
        self.command_sequence_start_time = 0

        self.UpdateTimer = QtCore.QTimer()
        self.UpdateTimer.timeout.connect(self.update)
        self.UpdateTimer.start(20)

        self.progressTimer = QtCore.QTimer(self)
        self.progressTimer.timeout.connect(self.updateProgressBar)
        self.progressTimer.start(100)  # Update every 100 milliseconds

        self.progress_value = 0

    def update(self):
        # Update the clock label
        self.clockLabel.setText("Time: " + str(time.strftime("%H:%M:%S", time.localtime())))

        # Update arm button state
        if self.is_armed:
            self.armButton.setStyleSheet("background-color: red; color: white;")
            self.armButton.setText("Click To Disarm")
            if self.is_live_controlled:
                self.servoUsec = int(self.pitchSlider.value())
                self.motorUsec = int(self.motorSlider.value())
                self.printToConsole(f"{self.servoUsec}, {self.motorUsec}")
        else:
            self.armButton.setStyleSheet("background-color: white; color: black;")
            self.armButton.setText("Click To Arm")

        # Send commands if armed
        if self.is_armed:
            self.send_commands()

        # Update live button state
        if self.is_live_controlled:
            self.liveButton.setStyleSheet("background-color: yellow; color: black;")
            self.liveButton.setText("LIVE CONTROL")
        else:
            self.liveButton.setStyleSheet("background-color: blue; color: white;")
            self.liveButton.setText("FILE CONTROL")

        # Update loose button state if file is loaded
        if self.is_file_loaded:
            if self.total_command_sequence_time > 0 and self.command_sequence_start_time > 0:
                self.progress_value = int(100*(time.time() - self.command_sequence_start_time) / self.total_command_sequence_time)
            else:
                self.progress_value = 0
            if not self.is_armed:
                self.looseButton.setStyleSheet(
                    "background-color: #e4ea67; color: black; font-weight: bold; font-size:12px")
                self.looseButton.setText("Need to Arm before sending commands")
            else:
                self.looseButton.setStyleSheet(
                    "background-color: green; color: white; font-weight: bold; font-size:16px")
                self.looseButton.setText("Click To Send Commands")
                if self.loose_active:
                    self.looseButton.setStyleSheet("background-color: red; color: white")
                    self.looseButton.setText("Click To Deactivate")

        # Update the last time
        self.last_time = time.time()

    def updateProgressBar(self):
        print("hello1")
        print("hello2")
        self.commandProgress.setValue(self.progress_value)
        print("hello3")

    def update_motor_slider(self):
        try:
            min_val = int(self.motorMin.text())
            max_val = int(self.motorMax.text())
            self.motorSlider.setMinimum(min_val)
            self.motorSlider.setMaximum(max_val)
        except ValueError:
            pass  # Handle the error as needed

    def update_servo_slider(self):
        try:
            min_val = int(self.servoMin.text())
            max_val = int(self.servoMax.text())
            self.pitchSlider.setMinimum(min_val)
            self.pitchSlider.setMaximum(max_val)
        except ValueError:
            pass  # Handle the error as needed

    def update_motor_counter(self):
        self.motorCounter.display(self.motorSlider.value())

    def update_servo_counter(self):
        self.pitchCounter.display(self.pitchSlider.value())

    def arm_button_clicked(self):
        self.is_armed = not self.is_armed

    def live_button_clicked(self):
        self.is_live_controlled = not self.is_live_controlled

    def open_file_dialog(self):
        self.reset_commands()
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                            options=options)
        if fileName:
            self.openFile.setText(fileName)
            self.opened_file = fileName
            print(f"Selected file: {fileName}")
            self.print_command_breakdown(self.load_commands(fileName))
            self.is_file_loaded = True
            self.commands = self.load_commands(self.opened_file)

    def printToConsole(self, inputstring):
        self.readout.append(inputstring)

    def loose(self):
        self.printToConsole("Loose Clicked")
        if self.is_armed:
            self.loose_active = not self.loose_active
            if not self.is_live_controlled:
                if self.opened_file is not None:
                    self.printToConsole(f"{self.opened_file} selected")
                    # if not self.check_file(self.opened_file):
                    #     return False, "File does not exist or is not a JSON file."
                    try:
                        self.printToConsole("Sending Commands...")
                        self.send_commands()
                    except Exception as e:
                        self.printToConsole(f"Error Loading File: {str(e)}")
                        return False, f"Error Loading File: {str(e)}"
        return True

    def print_command_breakdown(self, commands):
        print("Commands Breakdown:")
        self.printToConsole("Command Breakdown:")
        for index, (results, for_millis) in enumerate(commands):
            print(f"{index + 1}. {results}")
            command_str = (f"Command {index + 1}: Motor: {results[1]}, Servo: {results[0]},"
                           f"Arm Status: {results[2]}. (Hold for {for_millis / 1000:.3f} seconds)")
            print(command_str)
            self.printToConsole(command_str)

    def check_file(self, file_path):
        if self.opened_file is not None:
            self.printToConsole("File appears to be up to par.")
        if self.opened_file is None:
            self.printToConsole("There is no file loaded.")
        # if not os.path.isfile(file_path):
        #     self.printToConsole("File does not exist.")
        #     return False
        # if not file_path.endswith('.json'):
        #     self.printToConsole("File is not a JSON file.")
        #     return False

    def load_commands(self, file_path):
        self.printToConsole("Loading Commands...")
        try:

            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    self.printToConsole(f"Error decoding JSON: {str(e)}")
                    return []

            commands = []
            self.total_command_sequence_time = 0
            for index, entry in enumerate(data):
                if not isinstance(entry, dict):
                    self.printToConsole(f"Invalid entry at index {index}: Expected dict, got {type(entry).__name__}")
                    self.printToConsole(f"Entry content: {entry}")
                    continue

                try:
                    results, for_millis = self.readJSON(entry, index)
                    if results is None:
                        break
                    self.total_command_sequence_time += for_millis / 1000  # seconds
                    self.printToConsole(f"Total Time of Sequence: {self.total_command_sequence_time}")
                    commands.append((results, for_millis))
                except Exception as e:
                    self.printToConsole(f"Error processing entry at index {index}: {str(e)}")
                    continue

            return commands
        except Exception as e:
            self.printToConsole(f"Unexpected error: {str(e)}")
            return []

    def send_commands(self, commands=None):
        if self.is_armed:
            if self.is_live_controlled:
                input_str = f"{self.servoUsec},{self.motorUsec},{self.is_armed}\n"
                ser.write(input_str.encode())
            else:
                if self.loose_active:
                    if self.command_index < len(self.commands):
                        if self.command_index == 0:
                            self.command_sequence_start_time = time.time()
                        # self.printToConsole(f"Command Issuing...")
                        results, for_millis = self.commands[self.command_index]
                        current_time = time.time()  # Current time in seconds
                        if current_time >= self.next_command_time:
                            self.printToConsole(f"Command {self.command_index + 1} Issuing")
                            input_str = f"{results[0]},{results[1]},{results[2]}\n"
                            self.printToConsole(input_str)
                            # self.printToConsole(str(current_time))
                            ser.write(input_str.encode())
                            self.last_command_time = current_time  # Update the last command time
                            self.next_command_time = current_time + (for_millis / 1000)
                            self.command_index += 1  # Move to the next command
                    else:
                        self.printToConsole(f"Command Sequence Completed")
                        self.loose_active = False
                        self.is_armed = False
                        self.reset_commands()

    def reset_commands(self):
        self.total_command_sequence_time = 0
        self.command_index = 0
        self.last_command_time = 0
        self.next_command_time = 0
        self.progress_value = 0

    def readJSON(self, entry, index):
        try:
            servoUsec = entry['servoUsec']
            motorUsec = entry['motorUsec']
            for_millisecs = entry['for_millisecs']
            is_armed = entry['is_armed']
            results = servoUsec, motorUsec, is_armed
            return results, for_millisecs
        except KeyError as e:
            self.printToConsole(f"Missing key in entry at index {index}: {str(e)}")
            return None, None
        except Exception as e:
            self.printToConsole(f"Error processing entry at index {index}: {str(e)}")
            return None, None


# def send_signals(servo_usec, motor_usec, arm_active):
#     # Create the input string in the format expected by the Arduino code
#     input_str = f"{servo_usec},{motor_usec},{arm_active}\n"
#     # Send the input string over the serial connection
#     ser.write(input_str.encode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
