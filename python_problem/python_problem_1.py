import random


def brGame():
    while (True):
        player_num = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        try:
            player_num = int(player_num)
            if player_num < 1 or player_num > 3:
                print('1,2,3 중 하나를 입력하세요')
            else:
                player_num = int(player_num)
                return player_num
        except ValueError:
            print('정수를 입력하세요')


num = 0

while (num < 31):
    computer_num = random.randint(1, 3)
    for i in range(computer_num):
        num += 1
        print(f'computer : {num}')
        if num == 31:
            print('player win!')
            break
    if num >= 31:
        break
    player_num = brGame()
    for i in range(player_num):
        num += 1
        print(f'Player : {num}')
        if num == 31:
            print('computer win!')
            break
        elif num > 31:
            break
