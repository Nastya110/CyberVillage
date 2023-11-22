farmer_1 = [4, 3, 5, 2, 1, 3, 33, 0, 52]
farmer_2 = [2, 5, 5, 1, 52, 3]
for i in range(len(farmer_2)):
    if farmer_1[i]==farmer_2[i]:
        print('в', i+1,'день собрали одинаковое количество яиц равное', farmer_1[i])
