# Bluetooth Attendance System

## Overview
This project provides a simple, asynchronous Python-based solution to track attendance by detecting nearby Bluetooth Low Energy (BLE) devices. It utilizes the `bleak` library for BLE scanning and `pandas` for data manipulation, comparing detected device addresses against a predefined list in a CSV file to automatically mark attendance.

## Prerequisites
* Python 3.x
* `bleak` library (for asynchronous BLE scanning)
* `pandas` library (for reading and updating the CSV log)
* Hardware with Bluetooth capability (or a Bluetooth adapter)

## Setup Instructions

### 1. Install Dependencies
Run the following command in your terminal:

``` bash
pip install bleak pandas
```

### 2. Prepare Data
Ensure `attendance_log.csv` is in the same directory as the script. The file should maintain the following format:

``` csv
Student_Name,MAC_Address,Timestamp,Status
John Doe,AA:BB:CC:11:22:33,2026-06-26 08:00:00,Present
Jane Smith,DD:EE:FF:44:55:66,2026-06-26 08:05:00,Present
Mark Wilson,11:22:33:AA:BB:CC,2026-06-26 08:10:00,Absent
```

## How to Use
1. Open your terminal or command prompt.
2. Navigate to the project directory: `05_Bluetooth_Attendance`.
3. Execute the script:

``` bash
python attendance_system.py
```

## Important Notes
* **Device Visibility:** Ensure the devices you want to track are broadcasting via Bluetooth Low Energy (BLE).
* **Platform Differences (macOS vs. Windows/Linux):** On Windows and Linux, `bleak` returns standard MAC addresses. However, on macOS, it returns UUIDs due to Apple's privacy restrictions. If you are running this script on a Mac, you must populate the `MAC_Address` column in your CSV with device UUIDs instead of MAC addresses.
* **Permissions:** Depending on your operating system (e.g., Linux or macOS), you may need specific permissions (like Location/Bluetooth access, or root/sudo privileges) to perform Bluetooth discovery.
* **Testing:** To simulate and test the functionality, temporarily add your own device's MAC address (or UUID) to the CSV file and run the script to verify the "Present" status updates correctly.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.