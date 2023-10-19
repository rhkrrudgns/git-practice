slist = []

while True:
    item = input("항목을 입력하거나 'quit'을 입력하여 종료하세요: ")
    
    if item == "quit":
        break
    
    slist.append(item)
    slist.sort()
    print("현재 리스트 (오름차순 정렬):")
    
    for idx, value in enumerate(slist):
        print(f"{idx+1}: {value}")

print("프로그램을 종료합니다.")
