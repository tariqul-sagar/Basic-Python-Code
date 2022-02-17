#SMTP-Simple Mail Transfer Protocol#
print("\nSMTP-Simple Mail Transfer Protocol")
import smtplib

smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login('your mail@gmail.com','your mail password')
smtObj.sendmail('sender mail','receiver mail','Subject: SMTP Check. \nThis is a test mail.')
smtObj.quit()