def makePaint():
    paint=[
        [' ']*80 for _ in range(30)
    ]

    for r in range(30):
        paint[r][0]='|'
        paint[r][79]='|'

    for c in range(80):
        paint[0][c]='-'
        paint[29][c]='-'
        if c==0 or c==79:
            paint[0][c]='+'
            paint[29][c]='+'

    return paint

def printPaint(paint):
    for elems in paint:
        for elem in elems:
            print(elem,end='')
        print()

def takeTwoNumbers():
    while True:
        print("첫 번째 점의 좌표를 입력하세요. (예: 10, 10)")
        numbers=input().split(',')
        # 2개가 아니면 다시 입력
        if len(numbers)!=2:
            print("잘못 입력하셨습니다.")
            continue
        # 2 번째 숫자가 공백으로 시작하면 그 공백 제거
        if numbers[1][0]==' ':
            numbers[1]=numbers[1][1:]
        # 입력받은 두 개가 모두 숫자가 아니면 다시 입력
        if not numbers[0].isdigit() or not numbers[1].isdigit():
            print("잘못 입력하셨습니다.")
            continue
        num1=int(numbers[0])
        num2=int(numbers[1])
        # 범위 밖이면 다시 입력
        if num1<1 or num1>=79:
            print("잘못 입력하셨습니다.")
            continue
        if num2<1 or num2>=29:
            print("잘못 입력하셨습니다.")
            continue
        return num1,num2

def main():
    paint=makePaint()
    printPaint(paint)

    num1,num2=takeTwoNumbers()
    print(num1,num2)

if __name__=="__main__":
    main()