
keys = ["/l096URcdqhqHvlP1deqIw==wBuBWG8rIXxFTpEM"]
index = 0
def get_key():
    global index
    key = keys[index]
    index += 1
    if index >= len(keys):
        index = 0
    return key