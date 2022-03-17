import random
boys = ["AmirHossein", "Hamed", "Benyamin", "Moshteba", "Ali", "Saeed"]
girls = ["Shirin", "Sahar", "Negin", "Fahime", "Mary", "Mona"]
marriage = []
boy_marrid = []
girl_marrid = []
for name in boys:
    flag = False
    while flag == False:
        boy = boys[random.randint(0,5)]
        girl = girls[random.randint(0,5)]
        if boy not in boy_marrid:
            if girl not in girl_marrid:
                tuple = (boy, girl)
                boy_marrid.append(boy)
                girl_marrid.append(girl)
                flag =True
    marriage.append(tuple)
print(marriage)
