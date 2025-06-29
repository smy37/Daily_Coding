import sys 

def mix_str(input_s):
    front = ""
    back = ""
    for i in range(len(input_s)//2):
        front += input_s[2*i]
        back = input_s[2*i+1] +back
    if len(input_s)%2 != 0:
        front += input_s[-1]
    front += back
    
    return front

N = int(sys.stdin.readline())
input_str = sys.stdin.readline().strip()


### First Approach
# for _ in range(N):
#     input_str = mix_str(input_str)
# print(input_str)


### Second Approach
order = [input_str]
mixed_str = mix_str(input_str)
while mixed_str!= input_str:
    order.append(mixed_str) 
    mixed_str = mix_str(mixed_str)

print(order[N%(len(order))])

explain = """
섞이는 규칙을 찾아 섞이기 이전의 문자열을 만드는 함수를 작성하는건 쉽게 할 수 있었다. 
그러나 문자가 섞이다가 원래 문자열과 같아짐을 이용해서 순열의 순서를 찾고 이 순서를 이용해서
더 빠르게 풀어내는 접근법이 필요하였다.
"""