"""
Prerequisites:
    1. Before running this script, you must install the library:
       pip install bleak
"""
import asyncio
from bleak import BleakScanner

async def find_bluetooth_devices():
    print("Searching for nearby Bluetooth LE devices...")
    print("Scanning for 8 seconds. Please wait...\n")

    # discover() searches for devices in range
    nearby_devices = await BleakScanner.discover(timeout=8.0)

    if not nearby_devices:
        print("No devices found.")
    else:
        print(f"Found {len(nearby_devices)} device(s):")
        for device in nearby_devices:
            # Bleak devices return a 'name' and 'address' attribute
            # Some devices hide their name, so we provide a fallback
            device_name = device.name if device.name else "Unknown Device"
            
            print(f"  Device Name: {device_name}")
            print(f"  MAC Address: {device.address}")
            print("-" * 30)

if __name__ == "__main__":
    try:
        # asyncio.run() is required to run the asynchronous function
        asyncio.run(find_bluetooth_devices())
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure your Bluetooth is turned on and the library is correctly installed.")

"""
Steps to test this file:
1. Enable Bluetooth: Ensure your computer's Bluetooth is turned on.
2. Run the script: python bluetooth_finder.py
3. Validation: Ensure at least one other Bluetooth-enabled device (like your phone) is set to "discoverable" mode nearby.
"""