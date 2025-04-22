consonant = ['A', 'E', 'I', 'O', 'U']
def solution(word):
    answer = 0
    for n_1 in range(5):
        answer+=1
        t1 = consonant[n_1]
        if t1 == word:
            return answer
        for n_2 in range(5):
            answer +=1
            t2 = consonant[n_2]
            if t1+t2 ==word:
                return answer
            for n_3 in range(5):
                answer +=1
                t3 = consonant[n_3]
                if t1+t2+t3 ==word:
                    return answer
                for n_4 in range(5):
                    answer +=1
                    t4 = consonant[n_4]
                    if t1+t2+t3+t4 == word:
                        return answer
                    for n_5 in range(5):
                        answer +=1
                        t5 = consonant[n_5]
                        if t1+t2+t3+t4+t5 == word:
                            return answer
    return answer


print(solution("I"))