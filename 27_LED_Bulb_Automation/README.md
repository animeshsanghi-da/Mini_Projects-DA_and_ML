# 27_LED_Bulb_Automation

This project enables real-time control of an LED (or any component connected to an Arduino pin) directly from your computer using a Python script. It utilizes serial communication to send commands from Python to an Arduino/Microcontroller.

## Features
- Interactive CLI to toggle LED state.
- Real-time communication via Serial port.
- Easy to extend for home automation projects (e.g., relay modules for 220V bulbs).

## Prerequisites

### 1. Hardware
- Arduino Board (Uno, Nano, etc.).
- LED and a 220-ohm resistor.
- USB Cable (A-to-B).

### 2. Software
- Python 3.x installed.
- Arduino IDE (to upload the sketch).

## Setup Instructions

### Step 1: Install Dependencies
Create a `requirements.txt` file in your project folder with the following content:
```text
pyserial==3.5
```

Then, run the following command in your terminal:
```bash
pip install -r requirements.txt
```

### Step 2: Configure Arduino
Upload the following sketch to your Arduino using the Arduino IDE:

```cpp
void setup() {
    Serial.begin(9600);
    pinMode(13, OUTPUT); // Uses the built-in LED on most boards
}

void loop() {
    if (Serial.available() > 0) {
        char data = Serial.read();
        if (data == '1') digitalWrite(13, HIGH);
        else if (data == '0') digitalWrite(13, LOW);
    }
}
```

### Step 3: Configure Python Script
1. Open `led_control.py`.
2. Update the `SERIAL_PORT` variable to match your connected device.
   - **Windows:** 'COM3', 'COM4', etc. (Check Device Manager).
   - **Linux/Mac:** '/dev/ttyUSB0' or '/dev/ttyACM0'.
3. Run the script:
```bash
python led_control.py
```

## Usage
- Enter `1` to turn the LED **ON**.
- Enter `0` to turn the LED **OFF**.
- Enter `q` to close the connection and exit.

## Troubleshooting
- **Permission Denied:** On Linux, you might need to run `sudo chmod 666 /dev/ttyUSB0`.
- **Port Not Found:** Ensure your Arduino is plugged in and the correct COM port is specified in `led_control.py`.
- **Baud Rate Mismatch:** Ensure the baud rate in the Python script (9600) matches the `Serial.begin(9600)` in the Arduino sketch.

## Portfolio Note
This project demonstrates the intersection of software and hardware (IoT). In a professional data analyst/engineering setting, this represents the ability to handle I/O data streams and basic M2M (Machine-to-Machine) communication.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.