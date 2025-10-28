char_list = ["lancelot", "sir lancelot", "robin", "arthur"]

for item in char_list:
    if "sir lancelot of camelot".find(item) != -1:
        print("success")
    else:
        print("failure")