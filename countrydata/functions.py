import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import Subscriber, Data

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

def update_email(content):
    table_rows = """"""
    for each in content:
        row = f"""
        <tr>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.country}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.rank}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currconfirmed}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currdeath}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.curractive}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currrecovery}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.confirmed[len(each.confirmed)-1]-each.confirmed[len(each.confirmed)-2]}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.confirmed[-1] - each.confirmed[-2])/each.confirmed[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.death[-1] - each.death[-2])/each.death[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.recovery[-1] - each.recovery[-2])/each.recovery[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.active[-1] - each.active[-2])/each.active[-2])*100, 2)}%</td>
        </tr>
        """
        table_rows += row

    email_content = """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <h5 style="font-size: 20px;">My Watchlist</h5>
    <table style=" padding: 5px; background-color: #242526; color: #dadce1; border: 1px solid #dadce1; border-collapse: collapse;">
        <thead>
            <tr>
                <th style=" border: 1px solid #dadce1; padding: 5px">Country</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Rank</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Confirmed</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Deaths</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Active</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Recoveries</th>
                <th  style=" border: 1px solid #dadce1; padding: 5px; white-space: nowrap">New Cases</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Confirmed %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Death %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Recovery %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Active %</th>
            </tr>
        </thead>
        <tbody>"""+table_rows+"""</tbody>
    </table>
    <p>for detailed view visit: <a href='http://localhost:3000/' target='_blank'>COVIZ.com</a></p>
    """
    return email_content

def top5_content():
    table_rows = """"""
    for each in Data.objects.all()[:5]:
        row = f"""
        <tr>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.country}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.rank}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currconfirmed}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currdeath}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.curractive}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.currrecovery}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{each.confirmed[len(each.confirmed)-1]-each.confirmed[len(each.confirmed)-2]}</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.confirmed[-1] - each.confirmed[-2])/each.confirmed[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.death[-1] - each.death[-2])/each.death[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.recovery[-1] - each.recovery[-2])/each.recovery[-2])*100, 2)}%</td>
            <td style=" border: 1px solid #dadce1; padding: 5px">{round(((each.active[-1] - each.active[-2])/each.active[-2])*100, 2)}%</td>
        </tr>
        """
        table_rows += row
    top5 = """
    <h5 style="font-size: 20px;">Top 5 Countries</h5>
    <table style=" padding: 5px; background-color: #242526; color: #dadce1; border: 1px solid #dadce1; border-collapse: collapse;">
        <thead>
            <tr>
                <th style=" border: 1px solid #dadce1; padding: 5px">Country</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Rank</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Confirmed</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Deaths</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Active</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Recoveries</th>
                <th  style=" border: 1px solid #dadce1; padding: 5px; white-space: nowrap">New Cases</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Confirmed %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Death %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Recovery %</th>
                <th style=" border: 1px solid #dadce1; padding: 5px">Active %</th>
            </tr>
        </thead>
        <tbody>"""+table_rows+"""</tbody>
    </table>
    """
    return top5
    


def verify( email ):
    pre = get_random_string(5)
    suf = get_random_string(5)
    code = pre+'-'+suf
    send_verification_email(email, code)
    return code

def send_email_to_sub():
    res = 'success'
    for each in Subscriber.objects.all():
        content = []
        top5_c = ''
        countries = each.watchlist.split('%')
        for country in countries:
            c = Data.objects.filter(country=country)[0]
            content.append(c)
            if(each.top5):
                top5_c = top5_content()
        py_mail("Daily Update", top5_c+update_email(content), each.email, 'covizupdates@gmail.com')
    return res


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
