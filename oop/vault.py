#Overloading
class Vault:
    def __init__(self, g, s, k) -> None:
        self.g = g
        self.s = s
        self.k = k

    def __str__(self):
        return f"{self.g},{self.s},{self.k}"
    
    def __add__(self, other):
        g = self.g + other.g
        s = self.s + other.s
        k = self.k + other.k
        return Vault(g, s, k)

p = Vault(10,20,30)
x = Vault(40,50,60)

print(p + x)
