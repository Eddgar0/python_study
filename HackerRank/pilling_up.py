from collections import deque 
T = int(input())

for t in range(T):
    block_size = int(input())
    blocks = list(map(int, input().split()))
    blocks_queue = deque(blocks)
    blocks_stack = deque()
    
    for _ in range(block_size):
        
        bl = blocks_queue.popleft() if blocks_queue[0] >= blocks_queue[-1] else blocks_queue.pop()
        
        if not blocks_stack:
            blocks_stack.append(bl)
        else:
            if bl <=  blocks_stack[-1]:
                blocks_stack.append(bl)
            else:
                break
            
    if len(blocks_stack) == block_size:
        print('Yes')
    else:
         print('No')
        