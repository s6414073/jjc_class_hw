#!/usr/bin/env python

def hanoi1(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi1(n-1, A, C, B) + hanoi1(1, A, B, C) + hanoi1(n-1, B, A, C)

def hanoi2(n, a, b, c):
    param_stack_recursion2 = [[n, a, b, c]]

    while param_stack_recursion2:
        m, pa, pb, pc = param_stack_recursion2.pop()
        
        param_stack_recursion1 = []
        while True:
            if m == 1:
                print(pa, pc) # hanoi(1, A, B, C)
                
                # hanoi(m - 1, A, C, B) is completed
                leng = len(param_stack_recursion2)
                while param_stack_recursion1:
                    m = m + 1
                    sa, sb, sc = param_stack_recursion1.pop() 
                    
                    # hanoi(m - 1, B, A, C)
                    param_stack_recursion2.insert(leng, [m - 1, sb, sa, sc])
                      
                if param_stack_recursion2:
                    _, mb, ma, mc = param_stack_recursion2[-1] 
                    print(ma, mc) # move A to C
                
                break
            
            param_stack_recursion1.append([pa, pb, pc])
            # hanoi(m - 1, A, C, B)
            m = m - 1
            pa, pb, pc = pa, pc, pb

if __name__ == '__main__':

    print(hanoi1(4, 'A', 'B', 'C'))
    hanoi2(4, 'A', 'B', 'C')
