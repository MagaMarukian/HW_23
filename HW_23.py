# 1․ Գրել հետևյալ ծրագիրը․
#    - բացել jupyter notebook-ը,
#    - գեներացնել list, որը կպարունակի 1-ից 1_000_000 միջակայքում գտնվող կենտ թվերը,
#    - պահել գեներացված list-ը համապատասխան ֆորմատով համակարգչի մեջ data անունով,
#    - բացել pycharm-ը,
#    - pycharm-ում կարդալ data ֆայլը,
#    - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
#    - կտպի ստացված list-ի արժեքների միջին թվաբանականը։

# file1 = open('data.json', 'r')
# l = file1.read()
# file1.close()
# l1 = [i.strip(' ') for i in l.split(',')]
# l2 = []
# for i in l1:
#     if i == l1[0]:
#         l2.append(i.strip('['))
#     elif i == l1[-1]:
#         l2.append(i.strip(']'))
#     else: 
#         l2.append(i)
# list_three = []
# for i in range(1, len(list(l2)), 3):
#     list_three.append(int(l2[i]))
# print(list_three)
# print(sum(list_three) / len(list_three))


# 2․ Գրել ծրագիր, որը․
#    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները, իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
#    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
#    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:

# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
# for i, j in dict_1.items():
#     dict_2.update({j: len(j)})
# print(dict_2)

# 3. Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,
#    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
#    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:

# dict_1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# def dict_odd(d: dict) -> dict:
#     d2 = {}
#     for i, j in d.items():
#         new_j = []
#         for x in j:
#             if x % 2 != 0:
#                 new_j.append(x)
#         d2.update({i: new_j})
#     return d2
# print(dict_odd(dict_1)) 
