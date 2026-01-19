# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 유승희
# 작성일: 2026. 01. 19. 20:49:16

def solution(n):
    r_n=0
    for i in range(1, n+1):
        if i%2==0:
            r_n+=i
    return r_n
