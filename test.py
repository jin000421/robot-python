# num(순서)
num = 1

# (함수)
#  누구의 순서인가? 
j = 0
def who(j):
    if j % 2 == 0 :
        # user  
        return True
    # com    
    return False

# (함수)
#  3 6 9 인가? 
    # 369 0 -> ture
    # 369 x -> false

# while문
while num > 0:
    # user (j가 짝수) 
    if who:
        # input 받기 
        # num() == 369
            # o -> input == '짝' 
            j += 1
            # x -> break
        # num != 369 
            # o ->  input == num
            j += 1
            # x -> break
    # com (j가 홀수)
    else:
        # num == 369
            # 짝 
            j += 1
        # num != 369
            # num
            j += 1

# break -> game over
print("game over")