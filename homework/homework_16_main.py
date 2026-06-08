from pywebio.input import input, input_group
from pywebio.output import put_success
from pywebio import start_server
from pywebio.session import run_js
import homework_16_utils

def main():
    data = input_group(
        "Аналіз довжини стрічки",
        [
            input("Ваше ім'я", name="name", required=True),
            input("Введіть стрічку", name="content", required=True),
            input("Ваш Email для результату", name="email", required=True),
        ]
    )

    content = data["content"].strip()

    email_body = homework_16_utils.create_string_report(
        {
            "name": data["name"],
            "content": content,
            "length": len(content),
        }
    )

    homework_16_utils.send_email(
        recipients=[data["email"]],
        mail_body=email_body,
        mail_subject="Результат обчислення довжини стрічки",
    )

    put_success("Лист успішно відправлено! Сторінка оновиться через 5 секунд...")

    run_js("setTimeout(() => { window.location.reload(); }, 5000);")


if __name__ == "__main__":
    start_server(
        main,
        host="0.0.0.0",
        port=8888,
        debug=True,
    )
