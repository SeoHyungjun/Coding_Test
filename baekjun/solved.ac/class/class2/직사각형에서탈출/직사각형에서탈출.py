x, y, w, h = map(int, input().split())

print(min(min(x, y), min(w-x, h-y))) 