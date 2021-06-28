Bloods = []

for i in range(0,10,1):
    Bloods.append(input('헌열할 혈액형 (a, b, ab, o) : '))

print('\n저장된 혈액형')
for i in range(0,10,1):
    print(Bloods[i], end='    ')

print()
print('A   혈액형 수 : ', Bloods.count('a'))
print('B   혈액형 수 : ', Bloods.count('b'))
print('AB 혈액형 수 : ', Bloods.count('ab'))
print('O   혈액형 수 : ', Bloods.count('o'))
