# Project 01: Python Email Automation System

## Overview
This project is a lightweight, efficient Python script designed to automate the process of sending personalized mass emails. Utilizing the built-in `smtplib` and `csv` libraries, it reads recipient data from a structured CSV file and dynamically injects details (such as name, company, and target role) into a customized email template.

## Business Use Case
Automation of repetitive communication tasks is a core operational efficiency. In this specific implementation, the script is tailored for a professional outreach and job application campaign. It allows for contacting multiple hiring managers and HR directors simultaneously while maintaining a strict level of personalization for each recipient, demonstrating both technical capability and operational workflow automation.

## Technologies Used
* **Language:** Python 3.x
* **Core Libraries:** `smtplib`, `csv`, `email.mime`, `time`, `os`, `getpass`, `textwrap`
* **Protocol:** SMTP (Simple Mail Transfer Protocol) via Gmail

## File Structure
* `email_automation.py`: The main execution script containing the SMTP connection logic, secure password handling, and email generation pipeline.
* `contacts.csv`: The structured dataset containing target recipient information (Name, Email, Company, Role).
* `README.md`: Project documentation.

## Prerequisites & Security Note
To run this script using a Gmail account, standard passwords will be blocked by Google's security policies. You must use an **App Password**. 

**Important:** You must generate this App Password from the **same Google Account** that you have set as the `SENDER_EMAIL` in the script (e.g., `animeshsanghi.da@gmail.com`).

1. Log into the correct Google Account and navigate to your Google Account Settings.
2. Go to **Security** > **2-Step Verification** (ensure 2FA is turned on).
3. Search for or select **App passwords**.
4. Generate a new 16-character app password. It will usually display with spaces (e.g., `abcd efgh ijkl mnop`).
5. **Crucial:** When copying and pasting this code into your terminal, **do not include any spaces** (e.g., `abcdefghijklmnop`).

## How to Execute
1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed. No additional `pip` installations are required as this utilizes Python's standard library.
3. Update the `contacts.csv` file with your target recipient data. Ensure your headers exactly match: `Name`, `Email`, `Company`, `Role`.
4. Open your terminal and navigate to the project directory:
```bash
cd 01_Email_Automation
```
5. Run the script:
```bash
python email_automation.py
```
6. When prompted in the terminal, paste your 16-character Google App Password (without spaces). *Note: Because the script uses the `getpass` module for security, your keystrokes/pasted text will remain completely hidden on the screen.*

## Author
**Animesh Sanghi** | *Google Certified Data Analyst* [LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.