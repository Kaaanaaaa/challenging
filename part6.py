#1
str = 'カミュ'
for i in str:
    print(i)

#2
x = input('何を：')
y = input('何処へ：')
print('私は昨日{}を書いて、{}に送った！'.format(x, y))

#3
a = 'aldous Hexley was born in 1894.'
print(a.capitalize())

#4
www = 'どこで？　だれが？　いつ？'
www.split(' ')

#5
a = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
a = ' '.join(a[:6] + a[6])
print(a)

#6
a = 'A screaming comes across the sky.'
a = a.replece('s', '$')
print(a)

#7
h = 'Hemingway'
print(h.index('m'))

#8
"'海賊王'に俺はなる！"

#9
t = 'three'
print(t + t + t)
print(t * 3)

#10
a = '四月の晴れた寒い日で、時計がどれも十三時を打っていた。'
comma = a.index('、')
print(a[:comma])