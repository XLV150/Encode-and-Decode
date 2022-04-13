import base64


my_string = "This is just a plain string.".encode()
secret_message = base64.b64encode(my_string)      # Encoding a string into bytes

print(secret_message)
print()
print(secret_message.decode())        # Decodes string from bytes into a string
print()

secret_message_revealed = base64.decodebytes(secret_message)        # Decoding the secret message from bytes back into a string which we can understand
print(secret_message_revealed.decode())