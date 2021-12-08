import sys

start = list(map(int, sys.stdin.readline().split(':')))
end = list(map(int, sys.stdin.readline().split(':')))

start_time = start[0]*3600 + start[1]*60 + start[2]
end_time = end[0]*3600 + end[1]*60 + end[2]

if start_time > end_time:
    end_time += 3600*24

print(end_time - start_time)