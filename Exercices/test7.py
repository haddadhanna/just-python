input_cmd = ''
while input_cmd != 'exit':
    input_cmd = input("> ").lower()
    if input_cmd == "start":
        print("started")
    elif input_cmd == "stop":
        print("stoped")
    else:
        print("i dont understand")
else:
    print("exit")