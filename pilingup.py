n=int(input())

def isVertical(blocks):
    stk = [float('inf')]
    while len(blocks):
        if blocks[0] >= blocks[-1]:
            if stk[-1] >= blocks[0]:
                stk.append(blocks.pop(0))
            else:
                return 'No'
        else:
            if stk[-1] >= blocks[-1]:
                stk.append(blocks.pop(-1))
            else:
                return 'No'
    return 'Yes'
    
for i in range(n):
    size = int(input())
    blocks = list(map(int, input().split()))
    print(isVertical(blocks))
