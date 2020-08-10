import bl_message

bl_message.send_message.seed("hello")
print(bl_message.receive_message.receive())
