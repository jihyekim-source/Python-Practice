print('숫자를 입력하십시오: ', end='')
number = int(input())

def nSquareSum(n):
    total = 0
    for i in range(1, number+1):
        total+=i**i
    print(total)

nSquareSum(number)