import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import jinja2
import homework_16_config


def create_string_report(data: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath="./templates")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("homework_string.html")

    return template.render(data)


def send_email(recipients: list[str], mail_body: str, mail_subject: str):
    TOKEN = homework_16_config.TOKEN_UKR_NET
    USER = homework_16_config.USER_UKR_NET
    SMTP_SERVER = homework_16_config.SMTP_SERVER

    msg = MIMEMultipart("alternative")
    msg["Subject"] = mail_subject
    msg["From"] = f"PyWebIO Service <{USER}>"
    msg["To"] = ", ".join(recipients)
    msg["Reply-To"] = USER

    text_to_send = MIMEText(mail_body, "html", "utf-8")
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER, 465)

    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()
