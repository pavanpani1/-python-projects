#This is a simple text based Rock-paper-scissor
#game
import random

l=['Rock','Paper','Scissor']
while True:
    print('-'*45)
    r=random.randint(0,2)
    for i in range(0,len(l)):
        print(f'Enter {i+1}: ',l[i])

    print(' ')
    ch=int(input('Enter your choice: '))
    print(' ')
    print('you: ',l[ch-1])
    print('computer: ',l[r])
    print(' ')

    if l[ch-1]==l[r]:
        print('Hay!! its a Draw')
    elif l[ch-1]=='Scissor' and l[r]=='Paper':
        print('yayyy you won!!!...')
    elif l[ch-1]=='Rock' and l[r]=='Scissor':
        print('Wow nice! you won....')
    elif l[ch-1]=='Paper' and l[r]=='Rock':
        print('Nice keep it up...')
    else:
        print('Better Luck next time computer won..')
    print(' ')
    a=input('Do you want to Play (y/n): ')
    if a.lower()=='y':
        continue
    else:
        print('Thanks for playing')
        break





    
