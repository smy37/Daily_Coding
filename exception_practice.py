class Myerror(Exception):
    def __str__(self):
        return '사람수가 제한을 초과합니다'
    pass



def select_variable(n : int):
    if n > 1000:
        raise Myerror

    else:
        print(f'초기 사람수: {n}')

try:
    select_variable(500)
    select_variable(5000)
except Myerror as e:
    print(e)

test = [1,2,3,4,5]

try:
    test[9]
except IndexError:
    print('인덱스를 다시 설정해주십시오')
finally:
    print('끝')
