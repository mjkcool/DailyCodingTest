# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_list = [max(size) for size in sizes]
    min_list = [min(size) for size in sizes]
    return max(max_list) * max(min_list)