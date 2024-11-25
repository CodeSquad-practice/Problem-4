def main():
    print("사각형 그리기 프로그램")
    paint=makePaint()
    print("명령을 입력하세요(help: 도움말)")
    while True:
        paint=getOrder(paint)


        # x,y,r=takeThreeNumbers()
        # result=drawCircle(paint,x,y,r)
        # if result[0]==False :
        #     print("잘못 입력하셨습니다.")
        #     continue
        # else:
        #     paint=result[1]
        printPaint(paint)
        # num1,num2=takeTwoNumbers(0)
        # num3,num4=takeTwoNumbers(1)
        # paint=drawRectangle(paint,num1,num2,num3,num4)
        print("프로그램을 종료합니다.")
        break

def getOrder(paint):
    while True:
        order=input().split(maxsplit=1)
        if order[0]=='help':
            help()
            continue
        elif order[0]=='line':
            pass
        elif order[0]=='circle':
            inputs=splitString(order[1])
            x,y,r,m=inputs
            x,y,r=int(x),int(y),int(r)

            if not canDrawCircle(x,y,r):
                print("잘못 입력하셨습니다.")
                continue
            paint=drawCircle(paint,x,y,r,m)
            return paint
        elif order[0]=='rectangle':
            pass
        elif order[0]=='quit':
            pass
        else:
            pass

def splitString(string):
    string=string.split(',')
    for i in range(len(string)):
        string[i]=string[i].strip()
    return string

def help():
    print("""help: 도움말, 지금 이 화면을 출력한다.
line x1, y1, x2, y2, m: 두 좌표를 지정한 모양으로 잇는 선을 그린다.
circle x, y, r, m: x,y 를 중점으로 하는 반지름 r인 원을 그린다.
rectangle x1, y1, x2, y2, m: 두 좌표를 양 끝점으로 하는 직사각형을 그린다.
quit: 프로그램을 종료한다.
          """)


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

def takeThreeNumbers(string):
    while True:
        # print("x,y,r을 입력하세요. (예: 10, 20, 5)")
        numbers=string.split(',')
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
        if num3<2 or num3>14:
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

def drawCircle(paint,x,y,r,m):
    for i in range(80):
        for j in range(30):
            if (x-i)**2+(y-j)**2<=r**2:
                paint[j][i]=m
    return paint

def canDrawCircle(x,y,r):
    for i in range(80):
        for j in range(30):
            if (x-i)**2+(y-j)**2<=r**2:
                 if i==0 or i==79 or j==0 or j==30:
                    return False
    return True


if __name__=="__main__":
    main()
