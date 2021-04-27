menu={
    '아메리카노': 2000,
    '카페라떼': 2500,
    '블루레몬에이드': 3000
}


stamp=0

def order(drink):
    global stamp
    stamp+=1
    return menu.get(drink), stamp

print(order('아메리카노'))
print(order('카페라떼'))
print(order('블루레몬에이드'))