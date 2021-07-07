import csv
import pprint

with open('campling_items_list.csv') as file:
    items=list(csv.reader(file))

pprint.pprint(items)

#캠핑장비를 구매하는데 지출된 총 금액을 출력하고,
# 단가*수량이 낮은 물건부터 높은 순으로 정렬 후
# 그 결과를 sorted_campling_lists.csv파일로 저장

total=0
for i in items:
    total+=int(i[1])


for a in items:
    a.append(int(a[1])*int(a[2]))

pprint.pprint(items)
print()

sorted_list=sorted(items, key=lambda row:row[-1], reverse=True)

pprint.pprint(sorted_list)

with open('sorted_campling_lists.csv', 'w') as file:
    writer=csv.writer(file)
    writer.writerows(sorted_list)