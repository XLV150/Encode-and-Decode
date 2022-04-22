import base64

userinput = input("Enter the message you want to be encoded here: ")

my_string = "{}".format(userinput).encode()
print()
print("Encoded string into bytes.")
secret_message = base64.b64encode(my_string)      # Encoding a string into bytes

print(secret_message)
print()
print("Decoding string from bytes into a string.")
print(secret_message.decode())        # Decodes string from bytes into a string
print()

print("Decoding the string from bytes back into a string which we can understand.")
secret_message_revealed = base64.decodebytes(secret_message)        # Decoding the secret message from bytes back into a string which we can understand
print(secret_message_revealed.decode())
