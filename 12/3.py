def solution(s):
    answer = len(s)    # 중복이 없는 경우
    for step in range(1, len(s)//2 + 1):  # 1 ~ 문자열 절반 단위까지 쪼갬
        result = ''    # 압축결과
        pre = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if pre == s[i:i + step]:    # 이전 결과와 동일한 경우
                count += 1
            else:                      # 이전 결과와 다른 경우, 초기화 및 결과 저장
                result += str(count) + pre if count > 1 else pre
                pre = s[i:i + step]
                count = 1
        result += str(count) + pre if count > 1 else pre
        answer = min(answer, len(result))
    return answer


print(solution(s="cabab"))