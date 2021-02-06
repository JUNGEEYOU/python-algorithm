from collections import defaultdict
def solution(tickets):
    answer = []
    arr = defaultdict(list)
    stack = []      # 가야하는 곳을 넣기

    for a, b in tickets:
        arr[a].append(b)   # 인접 리스트

    for k, v in arr.items():         # 알파벳 정렬 > 스택이니 거꾸로 정렬
        arr[k].sort(reverse=True)

    stack.append("ICN")
    while stack:
        x = stack[-1]    # 맨 뒤에 있는 값
        if x not in arr or len(arr[x]) == 0:   # 표가 원래 없거나. 표를 다 쓴 경우. 결과에 넣어 경로를 저장한다.
            answer.append(stack.pop())
        else:
            stack.append(arr[x].pop())         # 표가 존재하는 경우, 스택에 추가 > 다음 갈 곳을 조회해야함

    answer.reverse()
    return answer


print()