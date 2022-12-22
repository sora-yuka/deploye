from django.core.mail import send_mail
from shop.celery import app

@app.task
def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        f'Ваш код сэр:  {full_link}',
        'sabyrkulov.nurmuhammed@gmail.com',
        [email]
    )


@app.task
def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'sabyrkulov.nurmuhammed@gmail.com',
        [email]
    )