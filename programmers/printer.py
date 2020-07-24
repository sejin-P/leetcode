def max_count(priorities):
    max_num = 0
    max_idx = 0
    length = len(priorities)
    for i in range(length):
        if priorities[i] > max_num:
            max_num = priorities[i]
            max_idx = i
    return max_num, max_idx
def solution(priorities, location):
    answer = 0
    while True:
        max_num, max_idx = max_count(priorities)
        if location > max_idx:
            priorities = priorities[max_idx+1:] + priorities[:max_idx]
            location = location - max_idx - 1
            answer += 1
            continue
        elif location < max_idx:
            priorities = priorities[max_idx+1:] + priorities[:max_idx]
            location = len(priorities) + location - max_idx
            answer += 1
            continue
        else:
            answer += 1
            break
        
    return answer