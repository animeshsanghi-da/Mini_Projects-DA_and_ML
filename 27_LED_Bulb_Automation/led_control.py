import serial
import time
import sys

# Configuration: Update these based on your specific setup
# On Windows, use 'COM3' or similar. On Linux/Pi, use '/dev/ttyUSB0' or '/dev/ttyACM0'
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

def initialize_connection():
    """Initializes the serial connection to the Arduino."""
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the connection to settle
        print(f"Connected to {SERIAL_PORT}")
        return ser
    except serial.SerialException as e:
        print(f"Error: Could not connect to {SERIAL_PORT}. {e}")
        return None

def send_command(ser, command):
    """Sends a byte command to the Arduino."""
    if ser:
        ser.write(command.encode('utf-8'))
        print(f"Command sent: {command}")

def main():
    ser = initialize_connection()
    if not ser:
        return

    print("--- LED Automation System ---")
    print("Commands: '1' for ON, '0' for OFF, 'q' to Quit")

    try:
        while True:
            user_input = input("Enter command: ").strip().lower()
            
            if user_input == '1':
                send_command(ser, '1')
            elif user_input == '0':
                send_command(ser, '0')
            elif user_input == 'q':
                print("Exiting...")
                break
            else:
                print("Invalid input. Use 1, 0, or q.")
    
    except KeyboardInterrupt:
        print("\nSystem interrupted by user.")
    finally:
        if ser:
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()

"""
Important Prerequisites
For this to function, you need two things:

1. Library: You must install the pyserial library in your environment:
    pip install pyserial

2. Arduino Logic: You need a simple sketch (C++) running on your Arduino to "read" these commands. If you don't have this, your Python script will send signals into the void.

    Quick Arduino C++ snippet (Reference):
        void setup() {
            Serial.begin(9600);
            pinMode(13, OUTPUT); // Built-in LED
        }

        void loop() {
            if (Serial.available() > 0) {
                char data = Serial.read();
                if (data == '1') digitalWrite(13, HIGH);
                else if (data == '0') digitalWrite(13, LOW);
            }
        }
"""