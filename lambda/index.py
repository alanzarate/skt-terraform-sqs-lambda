import logging
import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handler(event, context):
    
    print("============================= this is event ==============================")
    print(event)
    records = event['Records']
    for record in records:
      body = record['body'] 
      dat = json.loads(body)
      send_email(dat['message'], dat['emailReceiver'], dat['subject'])
    

# =============================================================================
# SEND EMAIL FUNCTION
# =============================================================================
def send_email(mes, receiver , subject):
  sender_email = "alnzarate@gmail.com"
  receiver_email = receiver
  password = "plmkkamxkozuapsf"

  message = MIMEMultipart("alternative")
  message["Subject"] = subject
  message["From"] = sender_email
  message["To"] = receiver_email

  # Create the plain-text and HTML version of your message
  text = """\
  Hi,
  How are you?
  """+ mes

  html = """\
  <html>
    <body>
      <p>Hi,<br>
        How are you?<br>
        <a href="http://www.google.com">"""+mes+"""</a>  
      </p>
    </body>
  </html>
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )

# =============================================================================
# END OF: SEND EMAIL FUNCTION
# =============================================================================