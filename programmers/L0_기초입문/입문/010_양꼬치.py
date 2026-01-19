# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 유승희
# 작성일: 2026. 01. 19. 20:19:13

def solution(n, k):
    n_f=n//10
    return 12000*n + 2000*(k-n_f)