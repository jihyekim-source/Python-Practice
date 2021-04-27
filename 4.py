def money():
    payment=int(input())
    price=int(input())
    remain=payment-price
    coin_500=remain//500
    coin_100=(remain-(coin_500*500))//100
    print(coin_500+coin_100)

money()