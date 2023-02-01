import smtplib
from email.message import EmailMessage

def alert_system(product, link):
    email_id = 'yudhishthirpbl@gmail.com'
    email_pass = 'firstpandav'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'yudhishthirpbl@gmail.com' # receiver address
    msg.set_content(f'boss, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)