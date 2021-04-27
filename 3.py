def baesu(range):
    print(sum(range)/len(range))
    list_range=(list(range)[-10::1])
    print(sum(list_range)/len(list_range))

baesu(range(0, 1000, 31))

