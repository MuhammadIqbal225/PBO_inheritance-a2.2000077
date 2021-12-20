class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health
    
class Hero_intellegent(Hero):
    pass

class Hero_strength(Hero):
    pass

yesi = Hero('yesi',100)
techies = Hero_intellegent('techies',50)
axe = Hero_strength('axe',200)

print(yesi.name)
print(techies.__dict__)
print(axe.__dict__)