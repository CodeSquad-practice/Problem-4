# Problem-4
## 빈 종이 만들기
```python
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
```
우선 공백으로 가득 찬 배열을 만들고, 배열의 테두리는 문자들로 치환했다.

## 종이 print하기
```python
def printPaint(paint):
    for elems in paint:
        for elem in elems:
            print(elem,end='')
        print()
```
종이를 출력할 일이 많을 것 같아, 종이를 출력하는 함수를 따로 구현했다.

## 숫자 두개 받기
```python

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
```
1번 문제에서 숫자를 받았던 것과 비슷하게 숫자를 받는다.   
두 번째 숫자는 공백으로 시작하면 공백을 지워주도록 했다.  
첫 번쨰 입력인지, 두 번째 입력인지에 따라 print하는 내용이 다르니, 몇 번째 입력인지를 인수로 받고, 그에 따라 출력문을 다르게 했다.

## 사각형 그리기
```python
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
```
사각형을 그리는 함수이다. 위 takeTwoNumbers 함수를 통해 두 좌표를 받고, 두 좌표 사이에 있는 모든 공백을 별표로 치환하는 함수이다.

## 메인함수
```python 
def main():
    print("사각형 그리기 프로그램")
    paint=makePaint()
    num1,num2=takeTwoNumbers(0)
    num3,num4=takeTwoNumbers(1)
    paint=drawRectangle(paint,num1,num2,num3,num4)
    printPaint(paint)
    print("프로그램을 종료합니다.")
```
우선 빈 종이를 생성하고, 두 좌표를 받아 사각형을 그린 후 그림을 print 한후 종료한다.
## 실행결과

```
사각형 그리기 프로그램
첫 번째 점의 좌표를 입력하세요. (예: 10, 10)
10,10
두 번째 점의 좌표를 입력하세요. (예: 70, 20)
70,210
잘못 입력하셨습니다.
두 번째 점의 좌표를 입력하세요. (예: 70, 20)
70,20
+------------------------------------------------------------------------------+
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|         *************************************************************        |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
+------------------------------------------------------------------------------+
프로그램을 종료합니다.
```

# Problem-4 2단계
## 숫자 세 개 받기
숫자 두 개를 받는 함수를 숫자 세 개를 받는 함수로 변경했다.   
마지막 숫자는 반지름을 받는데, 그에 맞는 조건도 따로 추가했다.
## 원 그리기
```python
def drawCircle(paint,x,y,r):
    for i in range(80):
        for j in range(30):
            if (x-i)**2+(y-j)**2<=r**2:
                if i==0 or i==79 or j==0 or j==30:
                    return (False,paint)
                paint[j][i]='*'
    return (True,paint)
``` 
원을 그리는 함수는 중심으로 부터의 거리가 반지름보다 작거나 같을 때 점을 그린다.  
따라서 모든 점들을 대상으로 한번씩 돌면서 중심으로 부터의 거리, 즉 x좌표의 차이의 제곱 + y좌표의 차이의 제곱이 반지름의 제곱보다 작거나 같은지, 혹은 큰지를 확인한다.  
점을 그려야할 때, 그 점이 그림판의 테두리라면 원을 그릴 수 없기에, paint와 함께 false를 return 한다.   
main함수에서 False를 return 받으면 다시 입력을 받도록 구현했다.

# Problem-4 3단계 
## 입력받기
```python
def getOrder(paint):
    while True:
        print("명령을 입력하세요(help: 도움말)")
        order=input().split(maxsplit=1)
        if order[0]=='help':
            help()
            continue
        elif order[0]=='line':
            inputs=splitString(order[1])
            x1,y1,x2,y2,m=inputs
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            paint=drawLine(paint,x1,y1,x2,y2,m)
            return paint
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
            inputs=splitString(order[1])
            x1,y1,x2,y2,m=inputs
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            paint=drawRectangle(paint,x1,y1,x2,y2,m)
            return paint
        elif order[0]=='quit':
            print('프로그램을 종료합니다.')
            sys.exit()
        else:
            print("잘못 입력하셨습니다.")
```
입력받기를 통해 처음 입력의 시작이 무엇이냐에 따라 실행하는 것을 다르게 했다.
문자를 입력받아 그 문자로 그리게 하는 것은 어렵지 않아 바로 수정했다.

## 직선 그리기
```python
def drawLine(paint,x1,y1,x2,y2,m):
    # x1이 무조건 왼쪽에 
    if x1>x2:
        x2,x1=x1,x2
        y2,y1=y1,y2
    x,y=x1,y1
    if y2>y1:
        sy=1
    elif y2==y1:
        sy=0
    else:
        sy=-1
    paint[y][x]=m
    while True:
        if x!=x2:
            x+=1
        if y!=y2:
            y+=sy
        paint[y][x]=m
        if x==x2 and y==y2:
            break
    return paint
```
직선을 그리는 것은 실패했다.   
정 대각선이나 수평선은 긋기 쉽지만 x좌표의 차이와 y좌표의 차이가 다른 것은 어려웠다.   
아마 x좌표의 차이와 y좌표의 차이를 비교하여 더 큰 차이를 분배하는 것이라고 생각했는데 구현을 해내지는 못했다.  
대신 단순히 대각선으로 긋고, 남은 차이는 그냥 수평선으로 긋는 것으로 구현했다.