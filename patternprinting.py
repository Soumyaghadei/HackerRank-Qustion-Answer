def door_mat_design(n, m):
    # Upper half pattern (excluding WELCOME)
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))
    
    # Middle row with WELCOME
    print('WELCOME'.center(m, '-'))
    
    # Lower half pattern (mirror of upper half)
    for i in range(n-2, 0, -2):
        print(('.|.' * i).center(m, '-'))

# Input
n, m = map(int, input().split())

# Function call to print the door mat
door_mat_design(n, m)
