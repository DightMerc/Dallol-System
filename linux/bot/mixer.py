import client

orders = client.api_models.Order.objects.all()

a = 0
b = 0
print(orders.count())
for order in orders:
    if  str(client.api_models.TelegramUser.objects.get(telegram_id=1812687).phone)[3:] in str(order.contact):
        try:
            order.user = client.api_models.TelegramUser.objects.get(telegram_id=1812687)
            order.save()
            a += 1
        except Exception as e:
            b += 1
    elif str(client.api_models.TelegramUser.objects.get(telegram_id=74860394).phone)[3:] in str(order.contact):
        try:
            order.user = client.api_models.TelegramUser.objects.get(telegram_id=74860394)
            order.save()
            a += 1
        except Exception as e:
            b += 1

print(a)
print(b)

