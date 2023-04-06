
keys = [
    "/l096URcdqhqHvlP1deqIw==wBuBWG8rIXxFTpEM",
    "PuWfrGNzlLPuTaEYcVe3sA==nXcKWvOY5N11HVhi",
    "MSDc3jQ7MOn9FekXhM0vDg==ljchUcbmecoKPHL9",
    "xRDXkfk+7HRuvg2V3/KtYg==FGE9EJGyo9n4leDO"
    ]
index = 0
def get_key():
    global index
    key = keys[index]
    index += 1
    if index >= len(keys):
        index = 0
    return key