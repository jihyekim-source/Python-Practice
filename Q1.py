import random

random.seed(10)

print('지불 금액: ', end='')
money=int(input())

game_num=money//1000


#6개 숫자 생성하는 함수
def generateLottoNumber(game_num):
    for games in range(game_num):
        lotto_1 = random.sample(range(46), 6)
        lotto_2 = []
        couple=0
        for i in lotto_1:
            lotto_2.append('{0:02}'.format(i))
            if i % 2 == 0:
                couple += 1
                single = 6 - couple  # 홀수
        print('로또 당첨 번호:', sorted(lotto_2))
        print('홀수: {}, 짝수: {}'.format(str(single), str(couple)))
        print('----------------------------------------------------')

generateLottoNumber(game_num)