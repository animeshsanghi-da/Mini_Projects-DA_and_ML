import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import time
import os
import getpass
import textwrap

def send_mass_emails(csv_file_path, sender_email, sender_password):
    # Setup the SMTP server for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    try:
        # Establish a secure connection using a context manager ('with')
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            print("Successfully connected to the SMTP server.\n")
            
            # Read contacts from the CSV file
            with open(csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    name = row['Name']
                    recipient_email = row['Email']
                    company = row['Company']
                    role = row['Role']
                    
                    # Construct the email message
                    msg = MIMEMultipart()
                    msg['From'] = formataddr(("Animesh Sanghi", sender_email))
                    msg['To'] = recipient_email
                    msg['Subject'] = f"Application for Data Analytics Opportunities at {company}"
                    
                    # textwrap.dedent removes leading whitespace from the code indentation
                    body = textwrap.dedent(f"""\
                        Dear {name},
                        
                        I hope this email finds you well. 
                        
                        I am writing to express my interest in potential {role} or Data Analyst positions at {company}. With a strong background in business operations and a specialization in Analytics and Data Science, I am eager to bring my expertise in Python, SQL, and Power BI to your team.
                        
                        Please find my portfolio on GitHub: https://github.com/animeshsanghi-da
                        
                        I would welcome the opportunity to discuss how my data-driven approach and operational experience can add value to {company}.
                        
                        Best regards,
                        
                        Animesh Sanghi
                        Email: animeshsanghi.da@gmail.com
                        Location: Madhya Pradesh
                    """)
                    
                    msg.attach(MIMEText(body, 'plain'))
                    
                    # Send the email
                    server.send_message(msg)
                    print(f"[*] Email successfully sent to {name} ({recipient_email}).")
                    
                    # 2-second delay to avoid triggering spam filters
                    time.sleep(2)
                    
            print("\nAll emails processed and sent successfully!")
            
    except smtplib.SMTPAuthenticationError:
        print("\n[ERROR] Authentication failed. Ensure you are using a 16-character Google App Password, not your standard email password.")
    except FileNotFoundError:
        print(f"\n[ERROR] The file {csv_file_path} was not found. Make sure it is in the same directory as this script.")
    except KeyError as e:
        print(f"\n[ERROR] Missing expected column in CSV: {e}. Ensure headers are: Name, Email, Company, Role.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Python Email Automation System ---")
    
    # Configuration
    SENDER_EMAIL = "animeshsanghi.da@gmail.com"
    CSV_FILE = "contacts.csv"
    
    # Prompt for password securely
    print(f"Sending as: {SENDER_EMAIL}")
    SENDER_PASSWORD = getpass.getpass("Enter your Google App Password: ")
    
    if os.path.exists(CSV_FILE):
        send_mass_emails(CSV_FILE, SENDER_EMAIL, SENDER_PASSWORD)
    else:
        print(f"Error: Cannot find '{CSV_FILE}'. Please verify your directory structure.")

"""
Important Execution Note
Because you are using Gmail (smtp.gmail.com), standard account passwords will not work due to Google's security policies. Before running the script, you must generate an App Password:

1. Go to your Google Account management settings.
2. Navigate to Security > 2-Step Verification.
3. Scroll to the bottom and select App passwords.
4. Generate a new app password (it will be a 16-letter code). Paste that code into the terminal when the script prompts you.
"""