#전체 좌표

print('table_x: ', end='')
table_x=int(input())
print('table_y: ', end='')
table_y=int(input())

table=[]

for x in range(table_x):
    for y in range(table_y):
        table.append([x, y])

#장애물 리스트

inputlist=[]
obstacle=None

while True:
    obstacle=input('장애물: ').split()
    inputlist.append(obstacle)
    if inputlist[-1]==['stop']:
        inputlist.remove(['stop'])
        break

for i in inputlist:
    i[0]=int(i[0])
    i[1]=int(i[1])

#길 리스트 만들기(테이블-장애물)

way=[]

for a in table:
    if a not in inputlist:
        way.append(a)

print(way)