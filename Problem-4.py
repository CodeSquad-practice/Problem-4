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

paint=makePaint()
printPaint(paint)
