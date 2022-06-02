inp = input()

def is_uppercase(inp):
    if inp.find(inp.upper()):
        return False
    else:
        return True

print(is_uppercase(inp))
