# Import the Python library for sending emails (SMTP)
import smtplib

# Prompt the user to enter their email details and the recipient's email
print("As of the new Google Update, you will need an App Password, which you can get from this link: https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4Phbu27B6xsRRbUamCF0frMSYox2B9By-7q-JKYzJh_21Zbh98ojcuiTZUkk2sVrCF9a-AUmfnZtOtAstRwdOEgAN0wqtaaqU6KDVM46fOhBBkmwqI. You will have to have 2-step verification on.")
Sender_Email = input("Please enter your email:  ")
Reciever_Email = input("Please enter the email of the receiver:  ")
Password = input('Enter your email account password:  ')

# Form the email content
Subject = "This is an automated email"
Body = "Template"
Message = f'Subject: {Subject}\n\n{Body}'

# Use smtplib to send the email through Gmail
# Line 14 specifies the SMTP server (for Gmail) and the port number (587).
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # Authenticate with Gmail using the provided email and password
    # Then send the email with the sender's email, recipient's email, and the composed message (subject and body)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_Email, Password)
    smtp.sendmail(Sender_Email, Reciever_Email, Message)

    # Print a confirmation message
    print("Done!")

# End of the script
