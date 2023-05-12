


keys = [
    "5bc88ee9e9e94669b308500cd72e73c5",
    ]
index = 0
def get_key():
    global index
    key = keys[index]
    index += 1
    if index >= len(keys):
        index = 0
    return key