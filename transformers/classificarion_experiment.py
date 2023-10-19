number = [4, 13, 15, 70, 51, 23, 38, 9, 12, 5]
even = []
odd = []

for num in number:
    if num % 2 == 0:  # 짝수 판단
        even.append(num)
    else:
        odd.append(num)

even.sort()
odd.sort()

print("짝수 리스트:", even)
print("홀수 리스트:", odd)
