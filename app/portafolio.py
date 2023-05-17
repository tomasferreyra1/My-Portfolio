from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)
import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('portafolio', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))


def send_email(name, email, message):
    my_email = 'tomy2002.tf@gmail.com'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    from_email = Email(my_email)
    to_email = To(my_email, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message
    })

    html_content = """
        <p>Hi Tomas, you have a new contact from the web:</p>
        <p>Name: -name-</p>
        <p>Mail: -email-</p>
        <p>Message: -message-</p>
    """
    mail = Mail(my_email, to_email, 'New contact from the web',
                html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())
