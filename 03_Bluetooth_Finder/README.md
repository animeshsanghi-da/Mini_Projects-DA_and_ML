# Bluetooth LE Device Finder

This script is a simple utility designed to asynchronously scan for and list nearby Bluetooth Low Energy (BLE) devices using the `bleak` library. 

## Features
- Discovers nearby Bluetooth LE (Low Energy) devices.
- Retrieves and displays device names and their unique MAC/UUID addresses.
- Handles asynchronous scanning for modern cross-platform compatibility.
- Provides fallback names for devices that hide their broadcast name.

## Prerequisites

### Hardware
- A computer with an active Bluetooth adapter (internal or USB dongle).

### Software
- Python 3.7+ installed (required for modern `asyncio` features).
- `bleak` library.

## Installation

1. Install the required dependency via pip:

```bash
pip install bleak
```

## How to Run

1. **Enable Bluetooth:** Ensure your computer's Bluetooth is toggled **ON**.
2. **Set Device to Discoverable:** Ensure the Bluetooth LE device you want to find (e.g., a smartphone, smartwatch, or BLE beacon) is set to "Discoverable" or broadcasting mode.
3. **Execute the script:**

```bash
python bluetooth_finder.py
```

*Note: The script is configured to scan for exactly 8 seconds before outputting the results. Please wait for the scan to complete.*

## Troubleshooting

- **Permissions:** Depending on your OS configuration (especially Linux), you might need elevated privileges to access Bluetooth hardware. If you encounter permission errors, try running with `sudo`.
- **Classic Bluetooth vs. BLE:** The `bleak` library is specifically designed for Bluetooth Low Energy (BLE). Older "Classic" Bluetooth devices (like older audio headsets or legacy game controllers) may not show up in this scan.
- **No Devices Found:** Bluetooth devices often stop broadcasting their presence after a few minutes to save battery. Toggle the Bluetooth setting on your target device off and on again to restart the discovery broadcast.

## Disclaimer
This script is for educational and experimental purposes. Please ensure you have permission to scan and interact with Bluetooth devices in your environment.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com  

## License

This project is open-source and free to use.