def get_key():
    key_file = open("api_key.txt", "r")
    return key_file.read().rstrip()
