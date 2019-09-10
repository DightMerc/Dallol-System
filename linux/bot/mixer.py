import client

messages = client.bot_models.Message.objects.all()

a = 33

for message in messages:
    new_message = client.bot_models.Message()
    new_message.number = a
    new_message.title = "UZ " + str(message.title)
    new_message.text = message.text
    new_message.save()

    a += 1

