#1
def number(int):
    '''
    int型を受け取り２倍にして返す関数
    :param int: int型
    :return: intを2倍
    '''
    return int ** 2
number(3)

#2
def print_str(str):
    '''
    渡された文字列を出力
    :param str: str型
    '''
    print(str)
print_str('Python')

#3
def numbers(num1, num2, num3, num4=4, num5=5):
    '''
    必須パラメータを３つ、オプションパラメータを２つ加算して返す
    :param num1: int型
    :param num2: int型
    :param num3: int型
    :param num4: int型
    :param num5: in5型
    :return: intを加算
    '''
    return num1 + num2 + num3 + num4 + num5
result = numbers(1, 2, 3)
print(result)

#4
def func(x):
    return x / 2
def function(y):
    return y * 4
int = func(100)
result = function(int)
print(result)

#5
def change_float(str):
    '''
    渡されたstrをfloatに変換
    :param str: str型
    :return: float型に変換
    '''
    try:
        return float(str)
    except ValueError:
        return ('float型に変換できない文字列です')
result = change_float('3.14')
print(result)

#6
#1~5までに追加でdocstring記述