import os, platform
import smtplib

def check_reachability(ip_address):
    hostname = ip_address
    response = os.system("ping " + ("-n 1 " if platform.system().lower()=="windows" else "-c 1 ") + hostname)

    # and then check the response...
    if response == 0:
        pingstatus = "Up"
    else:
        pingstatus = "Down"
        #try:
        #send_email()
        #Except Exception as e:
        #    print(str(e))

    return pingstatus


def send_email():
    sender = ''
    receivers = ['admin_email']

    message = """From: From Python script <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('')
        smtpObj.sendmail(sender, receivers, message)
        print
        "Successfully sent email"
    except smtplib.SMTPException as sm:
        print("Error: unable to send email" + str(sm))
#check_reachability("172.16.0.1")