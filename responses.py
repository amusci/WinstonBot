def responseHandler(message) -> str:
    process = message.lower()


    if process == 'hello':
        return 'Yeo'

    if process == 'ping':
        return 'pong!'