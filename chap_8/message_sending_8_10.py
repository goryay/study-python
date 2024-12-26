def print_message(messages, messages_send):
    for message in messages:
        print(message)
        messages_send.append(message)


def send_messages(messages, messages_send):
    for message in messages:
        print(f"Sending message: {message}")
        messages_send.append(message)


messages = ['Hello!', 'Hi', 'How are u?', 'How old are u?']
messages_send = []

messages_copy = messages[:]

print_message(messages, messages_send)
send_messages(messages_copy, messages_send)

print(f"\n{messages}")
print(messages_send)
print(f"\nOriginal messages: {messages}")
print(f"Sent messages: {messages_send}")
