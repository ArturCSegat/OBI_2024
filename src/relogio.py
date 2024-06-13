h = int(input())
m = int(input())
s = int(input())
delay = int(input())

new_s = (s+delay) % 60
new_m = m + (s+delay) // 60

new_h = h + new_m // 60
new_m = new_m % 60

new_h = new_h % 24

print(int(new_h))
print(int(new_m))
print(int(new_s))