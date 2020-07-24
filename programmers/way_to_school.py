# previous sol
def solution(m, n, puddles):
    answer = 0
    path = []
    for i in range(m):
        arr = []
        for j in range(n):
            arr.append(0)
        path.append(arr)
    for i in range(m):
        if [i + 1, 1] in puddles:
            break
        else:
            path[i][0] = 1
    for i in range(n):
        if [1, i+1] in puddles:
            break
        else:
            path[0][i] = 1
        
    for i in range(1,m):
        for j in range(1,n):
            if [i+1, j+1] in puddles:
                path[i][j] = 0
            else:
                path[i][j] = (path[i-1][j] + path[i][j-1])%1000000007
    answer = path[-1][-1]
    return answer