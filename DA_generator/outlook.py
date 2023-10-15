# import os
# import win32com.client as win32   

# os.startfile("outlook")


# def email(text, subject, recipient, auto=True):
    

#     outlook = win32.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.To = recipient
#     mail.Subject = subject
#     mail.HtmlBody = text
#     if auto:
#         mail.Display(False)
#     else:
#         mail.open # or whatever the correct code is

#     email()

from django.core.mail import send_mail

send_mail(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
)

send_mail()