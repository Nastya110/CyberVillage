chicken = [15, 35, 11, 15, 52, 515, 151, 9, 56, 55, 76, 5, 2, 84, 90, 17, 525]
print('Новый список для фермера в котором значения делятся на пять:', end=' ')
for i in range(len(chicken)):
    if chicken[i]%5==0:
       print(chicken[i], end=' ')
