nick=''
while nick!='quit':
    nick=input("Введите никнейм:")
    greet=f'Greetings my friend {nick}\n'
    print(greet)
    with open('guest_book.txt','a') as login:
        login.write(greet)