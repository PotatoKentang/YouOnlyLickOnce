


keys = [
<<<<<<< HEAD
    "5bc88ee9e9e94669b308500cd72e73c5",
=======
    "d435f6da0b66438f9f4f76edbf4e895e",
>>>>>>> ebc6270c23692be6defca00669fa32c260254bec
    ]
index = 0
def get_key():
    global index
    key = keys[index]
    index += 1
    if index >= len(keys):
        index = 0
    return key