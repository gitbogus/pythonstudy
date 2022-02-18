# n = int(input('n을 입력허시오 : '))

# for i in range(1, n+1):
#     print('*'*i)
    
# n = int(input('n을 입력허시오 : '))

# for i in range(1, n+1):
#     print(' '*(n-i), end=' ')
#     print('*'*i)

# n = int(input('n을 입력허시오 : '))

# for i in range(1, n):
#     print('*'*(n-i))

# n = int(input('n을 입력허시오 : '))

# for i in range(1, n):
#     print(' '*i, end=' ')
#     print('*'*(n-i))

n = int(input('n을 입력허시오 : '))

for i in range(n): 
    print(' '*(n-i-1), end=' ')
    print('*'*(i*2+1))
    
print('Fun Programming!')
print('item').rjust(10)
