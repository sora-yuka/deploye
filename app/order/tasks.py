from django.core.mail import send_mail
from shop.celery import app

@app.task
def send_confirmation_email(email, code, title, price,):
    full_link = f'Подтверди заказ на продукт {title} на {price} сумму \n\n http://localhost:8000/api/v1/order/confirm/{code}'
    
    send_mail(
        'Order',
        full_link,
        'sabyrkulov.nurmuhammed@gmail.com',
        [email],
    )