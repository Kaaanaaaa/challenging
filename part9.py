#1
with open('st.txt', 'r') as f:
    print(f.read())

#2
question = input('好きな色は？：')
with open('question.txt', 'w') as f:
    f.write(question)

#3
import csv
movies = [['Top Gun', 'Risky Business', 'Minority Report'],
          ['Titanic', 'The Revenant', 'Inception'],
          ['Training Day', 'Man on Fire', 'Flight']]
with open('data.txt', 'w') as f:
    moviefile = csv.writer(f, delimiter=',')
    for list in movies:
        moviefile.writerow(list)

#4
import csv
movies = [['トップガン', '危険なビジネス', 'マイノリティ・リポート'],
          ['タイタニック', 'レヴェナント', 'インセプション'],
          ['トレーニングの日', '燃える男', 'フライト']]
with open('data.txt', 'w') as f:
    moviefile = csv.writer(f, delimiter=',')
    for list in movies:
        moviefile.writerow(list)