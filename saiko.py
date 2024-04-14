anime = input("Favourite name character")
x = input("name =")

class Replace:
    def __init__(self, name):
        self.name = name

    def replace_a(self):
        self.name = self.name.replace("a"," ")

    def replace_e(self):
        self.name = self.name.replace("e","0")

    def replace_i(self):
        self.name = self.name.replace("i","1")

    def replace_o(self):
        self.name = self.name.replace("o","2")

    def replace_u(self):
        self.name = self.name.replace("u","3")



word = Replace(anime)
word.replace_a()
word.replace_e()
word.replace_i()
word.replace_o()
word.replace_u()
print(word.name)

name2 = Replace(x)
name2.replace_a()
name2.replace_e()
name2.replace_i()
name2.replace_o()
name2.replace_u()
print(name2.name)