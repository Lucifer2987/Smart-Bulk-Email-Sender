import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils import load_config, load_recipients, log_result
import time

# Load config and recipients
config = load_config()
recipients = load_recipients()

# Load HTML template
with open("templates/email_template.html") as f:
    html_template = f.read()

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(config['smtp_server'], config['port'], context=context)
server.login(config['username'], config['password'])

for recipient in recipients:
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = config['sender_email']
        msg['To'] = recipient['email']
        msg['Subject'] = "Welcome Email"

        personalized_html = html_template.replace("{{name}}", recipient['name'])
        text_part = MIMEText(f"Hello {recipient['name']},\nThis is a fallback plain-text version.", 'plain')
        html_part = MIMEText(personalized_html, 'html')

        msg.attach(text_part)
        msg.attach(html_part)

        server.sendmail(config['sender_email'], recipient['email'], msg.as_string())
        print(f"Email sent to {recipient['email']}")
        log_result(recipient['email'], "Success")
        time.sleep(3)  # Throttle sending rate

    except Exception as e:
        print(f"Failed to send to {recipient['email']}: {e}")
        log_result(recipient['email'], f"Failed: {e}")

server.quit()
