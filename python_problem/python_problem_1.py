num = 0

while (num < 32):
    while (True):
        player_num = float(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if player_num % 1 != 0:
            print('정수를 입력하세요')
        elif player_num < 1 or player_num > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            player_num = int(player_num)
            break
    for i in range(player_num):
        num += 1
        if num > 31:
            break
        print(f'PlayerA : {num}')
        Player_A = num
    while (True):
        player_num = float(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if player_num % 1 != 0:
            print('정수를 입력하세요')
        elif player_num < 1 or player_num > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            player_num = int(player_num)
            break
    for i in range(player_num):
        num += 1
        if num > 31:
            break
        print(f'PlayerB : {num}')
        Player_B = num
