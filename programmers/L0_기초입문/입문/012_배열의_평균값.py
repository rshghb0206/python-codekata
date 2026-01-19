# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 유승희
# 작성일: 2026. 01. 19. 20:51:20

def solution(numbers):
    nums = 0
    for num in numbers:
        nums += num
    return nums/len(numbers)