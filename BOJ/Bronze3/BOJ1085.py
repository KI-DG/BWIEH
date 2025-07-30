x, y, w, h = map(int, input().split())

left = (0, 0)
right = (w, h)
start = (x, y)

x_start = min(abs(0 - x), abs(w - x))
y_start = min(abs(0 - y), abs(h - y))
print(min(x_start, y_start))
