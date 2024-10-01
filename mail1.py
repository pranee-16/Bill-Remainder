import smtplib
from datetime import datetime
from email.mime.text import MIMEText

def send_email(to_email, subject, message):
    # Email configuration
    from_email = "binatibasanthi@gmail.com"
    from_password = "jylo euoc fckw pmuc"  # Replace with your generated app password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def bill_reminder(bill_name, due_date_str, reminder_days=3, user_phone=None):
    # Convert due_date from string to datetime
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    current_date = datetime.now()  # Get current date

    if current_date >= due_date:
        print(f"Bill '{bill_name}' is overdue!")
        send_email("reddybinatibasanthi@gmail.com", f"Reminder: {bill_name} is overdue", f"Please pay your bill for {bill_name}.")
    
    elif (due_date - current_date).days <= reminder_days:
        print(f"Reminder: Your bill '{bill_name}' is due soon!")
        send_email("reddybinatibasanthi@gmail.com", f"Reminder: {bill_name} due soon", f"Your bill for {bill_name} is due on {due_date_str}.")

        if user_phone:
            # Update carrier_gateway based on the user's carrier
            carrier_gateway = "tmomail.net"  # Change this based on the user's carrier
            send_email(f"{user_phone}@{carrier_gateway}", f"Reminder: {bill_name} due soon", f"Your bill for {bill_name} is due on {due_date_str}.")

if __name__ == "__main__":
    # Example usage
    bill_name = "Electricity"
    due_date = "2024-10-05"  # Replace with actual due date
    user_phone = "8790576498"  # Replace with the user's phone number
    bill_reminder(bill_name, due_date, user_phone=user_phone)
