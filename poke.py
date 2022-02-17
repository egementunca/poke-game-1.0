
class Pokemon:
    def __init__(self,i):

        with open("modified.csv","r") as file:
            for line_number,line in enumerate(file):
                if line_number == i:
                    info = line.split(",")
                    self.name = info[1]
                    self.type = info[2]
                    self.hp = info[4]   # this will be increase and decrease
                    self.max_hp = info[4]   
                    self.attack_power = info[5]
                    self.defense_power = info[6]   
                    self.total = int(info[8])

    def __str__(self):
        return "Name: %s\nType: %s\nHP: %s/%s\nAttack Power: %s\nDefense Power: %s"%(self.name,self.type,self.hp,self.max_hp,self.attack_power,self.defense_power)            


    def increase_attack_power(self):
        pass

    def increase_defense_power(self):
        pass


    def feed(self,amount):
        if not (self.hp + amount) > self.max_hp:
            self.hp += amount
            used = amount
        else:
            self.hp += (self.max_hp-self.hp)
            used = (self.max_hp-self.hp)

        return used #To determine how much coin this will cost
