class Pokemon:
    def __init__(self, name,owener,skills):
        self.name = name
        self.owner = owener
        self.skills = skills.split('/')
        print(f"포켓몬 {name}객체 생성됨")

    def info(self):
        print(f'{self.owner} have a pokemon {self.name}')
        for skill in self.skills:
            print(skill)

class Pikachu(Pokemon):  #inheritance
    pass
pi1 = Pikachu('피카류','덴트','번개')
pi1.info()

p1 = Pokemon('피카츄','한지우','50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기','오바람','고속스핀/거품/몸통박치기/하이드로펌프')


