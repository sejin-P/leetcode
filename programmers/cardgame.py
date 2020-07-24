# previous solution
def solution(left, right):
    answer = 0
    score = [[0 for i in range(len(left) + 1)] for j in range(len(left) + 1)]
    for i in range(len(left)):
        for j in range(len(right)):
            if right[j] < left[i]:
                score[i][j+1] = max(score[i][j+1], score[i][j] + right[j])
            else:
                score[i+1][j+1] = max(score[i+1][j+1], score[i][j])
                score[i+1][j] = max(score[i+1][j], score[i][j])
    arr1 = [score[-1][i] for i in range(len(left) + 1)]
    arr2 = [score[i][-1] for i in range(len(left) + 1)]
    answer = max(arr1 + arr2)
    
    return answer


