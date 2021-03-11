def div_str(s):
    """
    균형잡힌 괄호와 아닌 문자 그룹 나누기
    :param s:
    :return:
    """
    u = ''
    left = 0
    right = 0
    for i, c in enumerate(s):
        u += c
        if c == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = s[i + 1:] if len(s) > i else ""
    return u, v


def check(s):
    """
    올바른 괄호인지 확인
    """
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    # 스택이 빈 경우 true, 아닌 경우 false
    return False if stack else True


def recursive(p):
    """
    재귀로 반복되는 구간
    """
    if not p:
        return ''
    u, v = div_str(p)  # 균형잡힌 괄호과 아닌 문자열 나누기

    # 올바른 괄호인 경우 v에 대해서 시작
    if check(u):
        return u + recursive(v)
    else:  # 올바른 괄호가 아닌 경우 수행
        x = ""
        for a in u[1:-1]:
            if a == "(":
                x += ")"
            else:
                x += "("
        return "(" + recursive(v) + ")" + x


def solution(p):
    return recursive(p)


print(solution(p="()))((()"))
