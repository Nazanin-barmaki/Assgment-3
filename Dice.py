import random
sum = 0
while True:
    tas = random.randint(1,6)
    if tas == 6:
        print(tas)
        print(' yeah You are lucky dude:')
        sum += tas
        continue
    else:
        sum += tas
        print(tas)
        print('sum of number:',sum)

    if tas<6:
        break 
    else:
      continue