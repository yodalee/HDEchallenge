#!/usr/bin/env python
#######################################################################
# Mission Description
#
# We want to calculate a sum of squares of some integers, excepting negatives
# * The first line of the input will be an integer N (1 <= N <= 100)
# * Each of the following N test cases consists of one line containing an integer X (0 < X <= 100),
#   followed by X integers (Yn, -100 <= Yn <= 100) space-separated on the next line
# * For each test case, calculate the sum of squares of the integers excepting negatives,
#   and print the calculated sum to the output. No blank line between test cases
# * (Take input from standard input, and output to standard output)
# 
# ##Rules
# * Choose your favorite language from either of these: C, Erlang, Go, Python, Ruby
# * Do not use loop statements like while/until/for/each/loop, and goto
#
# ## Sample Input
# 2
# 4
# 3 -1 1 14
# 5
# 9 6 -53 32 16
#
# ##Sample Output
# 206
# 1397
#######################################################################

import sys

# map function
square_map = lambda x : x*x
sum_map = lambda x: x

# filter function
pos_filter = lambda x: x>0

def get_iteration_times():
    """get the iteration times of input cases: N
    N is in the range: 1 <= N <= 100 """
    try:
        n = int(input())
        if n <= 0 or n > 100:
            sys.stderr.write("iteration times N (1 <= N <= 100)\n")
            sys.exit(1);
    except ValueError:
        sys.stderr.write("First input should be a integer N, that 1<= N <=100\n")
        sys.exit(1)
    return n

def get_data():
    """parse standard input, first get a integer X(0 < X <= 100)
    then followed by X integers Yn(-100 <= Yn <= 100) space-separated on next line"""
    try:
        X = int(input())
        if X <= 0 or X > 100:
            sys.stdin.readline() # dump the rest data
            raise ValueError
        Y = map(int, sys.stdin.readline().split())
    except ValueError:
        sys.stderr.write("Input Data Error: ")
        raise ValueError
    return Y

def calculate(times, map_func = sum_map, filter_fun = pos_filter):
    """get data, and calculate a """
    if times == 0:
        return 0
    try:
        result = sum(map(map_func, filter(filter_fun, get_data())))
        print(result)
    except ValueError:
        sys.stderr.write("at %d input dataset\n" % (times))
    return calculate(times-1, map_func, filter_fun)

n = get_iteration_times()
calculate(n, square_map, pos_filter)

