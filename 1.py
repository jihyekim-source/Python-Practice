street=(199000*0.89)+2500
carrot=180000-2500

if street>carrot:
    print('carrot is cheaper')
elif street<carrot:
    print('street is cheaper')
else:
    print('same')

print(abs(street-carrot))