날짜=['4월 17일', '4월 18일', '4월 19일', '4월 20일', '4월 21일']
요일=['토', '일', '월', '화', '수']
싯가=[85000, 90000, 87500, 80000, 100100]

min_index=싯가.index(min(싯가))
max_index=싯가.index(max(싯가))

print('min', 요일[min_index], 날짜[min_index])
print('max', 요일[max_index], 날짜[max_index])

dic=dict(zip(날짜, 싯가))

dic.update({'4월 22일': 99000})
print(dic)