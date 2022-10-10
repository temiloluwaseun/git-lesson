anime=input("Favourite anime character")

def a():
    return anime.replace("a"," ")
def e():
    return a().replace("e","0")
def i():
    return e().replace("i","1")
def o():
    return i().replace("o","2")
def u():
    return o().replace("u","3")

print(u())