'''
Каждый пишет сумму списка при помощи for и while
'''

a = list(range(1, 101))
i = 0
total = 0

while i < len(a):
    total += a[i]
    i += 1

print(total)
