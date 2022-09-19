def solution(genres, plays):
    hash_map = {}
    play_cnt = {}
    for i in range(len(genres)):
        if genres[i] not in hash_map:
            hash_map[genres[i]] = [[plays[i], i]]
            play_cnt[genres[i]] = plays[i]
        else:
            hash_map[genres[i]].append([plays[i], i])
            play_cnt[genres[i]] += plays[i]
    hash_map = dict(sorted(hash_map.items(), key=lambda x: len(x[1]), reverse=True))
    play_cnt = dict(sorted(play_cnt.items(), key=lambda x: x[1], reverse=True))

    answer = []

    for i in play_cnt:
        temp = sorted(hash_map[i], key=lambda x: x[0], reverse=True)
        if len(temp) >= 2:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            answer.append(temp[0][1])
    return answer