#Writing an Email Spammer in Python

#First, Importing the Simple Mail Transfer Protocol Module

import smtplib

#Specifying the From and To addresses

fromaddress = "your email address" toaddress = "another email address"

#Now,Specifying the Gmail Login

username = "your user name" password = "your password"

#Writing the message which will appear in the mail

message = """ MESSAGE """

#Creating a connection with the Gmail server

server =smtplib.SMTP('smtp.gmail.com:587') server.starttls() server.login(username,password)

#Creating a for loop to send multiple mails

for i in range (0,10): server.sendmail(fromaddress,toaddress,message) print ("mail sent")

#closing the server server.quit()


