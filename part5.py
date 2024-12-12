#1
artists = ['UVERworld', 'BE:FIRST', 'SUPER BEAVER']

#2
places = [(140.8693, 38.2682), (141.3543, 43.062), (125.2811, 24.8054)]

#3
my = {'height': 166, 'color': 'black'}

#4
question = input('私について何が知りたいですか？：')
if question in my:
    print(my[question])
else:
    print('選択されなかった')

#5
my_favorite = {'UVERworld': ['ビタースウィート',
                             ' 0 chiro',
                             'WANNA BE BRILLIANT'],
                'BE:FIRST': ['Sailling',
                            'Message',
                            'Shining One'],
                'SUPER BEAVER': ['ひたむき',
                                '儚くない',
                                '切望']
                }