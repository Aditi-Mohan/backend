import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def send_verification_email(email, code):
    email_content = """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
      div {
        width: 200px;
        margin: auto;
        padding: 10%;
        border: 2px #484a4d solid;
      }
      p {
        clear: both;
        text-align: center;
        background-color: #dadce1;
        color: #484a4d;
        padding: 10px;
      }
    </style>
    <div style="width: 200px; margin: auto; padding: 10%; border: 2px #dadce1 solid;">
        <p style="clear: both; text-align: center; background-color: #dadce1; color: #484a4d; padding: 10px;">
        CODE: """+code+"""</p>
    </div>
    """
    py_mail("Email verification", email_content, email, 'covizupdates@gmail.com')

def update_email(email):
    return


def verify( email ):
    pre = get_random_string(5)
    suf = get_random_string(5)
    code = pre+'-'+suf
    send_verification_email(email, code)
    return code


def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our HTML email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """Your mail reader does not support the report format.
    Please visit us <a href="http://www.mysite.com">online</a>!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    server = smtplib.SMTP('smtp.gmail.com:587')

    password = "coviz1234"

    server.starttls()
    server.login(FROM, password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()