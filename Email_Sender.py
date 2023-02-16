import smtplib

Sender_Email = input("Please enter your email:  ")
Reciever_Email = input("Please enter the email of the receiver:  ")
Password = input('Enter your email account password:  ')

Subject = "This is a automated email"
Body = "Hi Father, This is only the begginging of what I can do."
Message = f'Subject: {Subject}\n\n{Body}'


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_Email, Password)
    smtp.sendmail(Sender_Email, Reciever_Email, Message)

    print("Done!")
