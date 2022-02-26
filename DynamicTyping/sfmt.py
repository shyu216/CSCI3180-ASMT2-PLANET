# single function multiple type
def check_type(target1, target2):
    if type(target1) == type(target2):
        return True
    else:
        return False

if check_type("you", "me"):
    print("same")
if not check_type(3.14, 3):
    print("different")