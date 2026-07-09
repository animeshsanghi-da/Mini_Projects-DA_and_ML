"""
Prerequisites
    1. You will need to install the required libraries first:
        pip install bleak pandas
"""
import asyncio
import pandas as pd
from datetime import datetime
from bleak import BleakScanner

async def mark_attendance(csv_file):
    # Load the attendance log
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_file}'. Please ensure the file exists.")
        return
    
    print("Scanning for nearby Bluetooth Low Energy (BLE) devices. This may take a few seconds...")
    
    # Discover nearby BLE devices asynchronously
    nearby_devices = await BleakScanner.discover()
    
    # Extract the addresses (MAC on Win/Linux, UUID on macOS). 
    # Converted to uppercase to ensure string matching works correctly.
    found_macs = [device.address.upper() for device in nearby_devices]
    
    print(f"Found {len(found_macs)} devices.")
    
    # Update status for found devices
    for index, row in df.iterrows():
        target_mac = str(row['MAC_Address']).upper()
        if target_mac in found_macs:
            df.at[index, 'Status'] = 'Present'
            df.at[index, 'Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Marked {row['Student_Name']} as Present.")
    
    # Save the updated log
    df.to_csv(csv_file, index=False)
    print("Attendance updated successfully.")

if __name__ == "__main__":
    # Bleak requires an asyncio event loop to run
    asyncio.run(mark_attendance('attendance_log.csv'))

"""
How to use this script:
1. Setup: Ensure attendance_log.csv is in the same directory as this script.
2. Execution: Run python attendance_system.py.
3. Simulation: Since you may not have 30 physical devices to test against, you can temporarily add your own device's MAC address to the CSV file to verify the "Present" status updates correctly when the script runs.
"""