#Here it imports the Python Library for Smtplib, which we use in this python file
import smtplib
#Here is where the use enters there details and their receiver
Sender_Email = input("Please enter your email:  ")
Reciever_Email = input("Please enter the email of the receiver:  ")
Password = input('Enter your email account password:  ')
#Here is where the email is formed
Subject = "This is a automated email"
Body = "Hi Father, This is only the begginging of what I can do."
Message = f'Subject: {Subject}\n\n{Body}'

#Line 14 shows smtplib what email you are using and the port number. For gmail it is 587.
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #This is where the computed logs onto gmail with your email and password
    #and then is sends the email with your email, the receiver email and the message, which is the subject and body
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_Email, Password)
    smtp.sendmail(Sender_Email, Reciever_Email, Message)

    print("Done!")
#And that is all
