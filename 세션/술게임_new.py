import random


print("~"*80)
print("ALCOHOL GAME")
print("~"*80)

dictionary = {'고은': [7, 7], '용현': [6, 6],
              '태영': [5, 5], '수현': [5, 5], '현지': [4, 4]}
start_game = input("게임을 진행할까요? (y/n) : ")

if start_game == 'y':
    player_name = input("오늘 거하게 취해볼 당신의 이름은?(고은, 용현, 태영, 수현, 현지 중 선택) : ")
    print("당신의 주량은?")
    list.remove(player_name)


elif start_game == 'n':
    print("다음에 만나요")
