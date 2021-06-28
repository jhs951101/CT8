mylist = []

while True:
    print('*'*19)
    print('1. 이름 추가')
    print('2. 이름 삭제')
    print('3. 이름 수정')
    print('4. 종료')
    menu = input('메뉴 선택 : ')

    if menu == '4':
        break
    elif menu >= '1' and menu <= '3':
        name = input('이름 : ')
        error = False

        if menu == '1':
            if mylist.count(name) >= 1:
                print('이미 있는 이름')
                error = True
            else:
                 mylist.append(name)
        elif menu == '2' or menu == '3':
            if mylist.count(name) <= 0:
                print('해당 이름 없음')
                error = True
            else:
                if menu == '2':
                    mylist.remove(name)
                elif menu == '3':
                    newName = input('새 이름 : ')
                    mylist[mylist.index(name)] = newName

        if not error:
            print(mylist)
            
    else:
        print('메뉴에 없는 번호')

    print()
