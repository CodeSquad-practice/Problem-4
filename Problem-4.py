def main():
    print("사각형 그리기 프로그램")
    paint=makePaint()
    x,y,r=takeThreeNumbers()
    print(x,y,r)


    # num1,num2=takeTwoNumbers(0)
    # num3,num4=takeTwoNumbers(1)
    # paint=drawRectangle(paint,num1,num2,num3,num4)
    printPaint(paint)
    print("프로그램을 종료합니다.")

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

def takeTwoNumbers(ordinal):
    dots=['첫 번째','두 번째']
    example=['10, 10','70, 20']
    while True:
        print(f"{dots[ordinal]} 점의 좌표를 입력하세요. (예: {example[ordinal]})")
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
    
def takeThreeNumbers():

    while True:
        print("x,y,r을 입력하세요. (예: 10, 20, 5)")
        numbers=input().split(',')
        # 3개가 아니면 다시 입력
        if len(numbers)!=3:
            print("잘못 입력하셨습니다.")
            continue
        # 2 번째 숫자가 공백으로 시작하면 그 공백 제거
        if numbers[1][0]==' ':
            numbers[1]=numbers[1][1:]
        # 3 번째 숫자가 공백으로 시작하면 그 공백 제거
        if numbers[2][0]==' ':
            numbers[2]=numbers[2][1:]
        # 입력받은 세 개가 모두 숫자가 아니면 다시 입력
        if not numbers[0].isdigit() or not numbers[1].isdigit() or not numbers[2].isdigit():
            print("잘못 입력하셨습니다.")
            continue
        num1=int(numbers[0])
        num2=int(numbers[1])
        num3=int(numbers[2])
        # 범위 밖이면 다시 입력
        if num1<1 or num1>=79:
            print("잘못 입력하셨습니다.")
            continue
        if num2<1 or num2>=29:
            print("잘못 입력하셨습니다.")
            continue
        if num3<0 or num3>28:
            print("잘못 입력하셨습니다.")
            continue
        return num1,num2,num3

def drawRectangle(paint,c1,r1,c2,r2):
    # r2,c2가 항상 더 크도록 함
    if c1>c2:
        c1,c2=c2,c1
    if r1>r2:
        r1,r2=r2,r1
    
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            paint[j][i]='*'
    return paint

if __name__=="__main__":
    main()

