#1
movies = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for movie in movies:
    print(movie)

#2
for i in range(25, 51):
    print(i)

#3
movies = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for index, movie in enumerate(movies):
    print('{}. {}'.format(index, movie))

#4
numbers = [1, 100, 24, 30, 55, 61, 22, 98]
while True:
    int = input('数字もしくはqを入力：')
    if numbers == 'q':
        break
    try:
        int = int(int)
    except ValueError:
        print('数字を入力するか、qで終了します')
    if int in numbers:
        print('正解')
    else:
        print('不正解')

#5
num1 = [8, 19, 128, 4]
num2 = [9, 1, 33, 83]
numbers = []
for i in num1:
    for j in num2:
        list = i * j
        numbers.append(list)
print(numbers)