import random
answer1 = 99
answer2= 0
counter=1
answer_cmput=random.randint(0,99)
     print ('select a number between 0 to 99.)'
   guess = random.randint(answer1,answer2)

    while True:
     print('1) yeah body ,it correct''\n''2)nope my number is bigger''\n''3)nope my number is lower')

     resualt = int(input())

     if resualt==1:
        print('yea yoe gesess')


     elif resualt==2:
        answer2=answer_cmput
        answer=random.randint(answer1),(answer2)
        counter+=1
        print(answer)

     elif resualt==3:
        answer1=answer_cmput
        answer_cmput=random.randint(answer1),(answer2)
        counter+=1
        print(answer)

        