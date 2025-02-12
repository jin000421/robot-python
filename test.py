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
#  NUM == 3 6 9 ?? 
def agree(num):
    str_num = str(num)
    for a in range(len(str_num)):
        # 369 0 -> ture         
        if str_num[a] == '3' or str_num[a] == '6' or str_num[a] == '9':
            num = int(str_num)
            return  True
        # 369 x -> false
        else:
            num = int(str_num)
            return False

# while문
while num > 0:
    # user (j가 짝수) 
    if who:
        # input 받기 
        user = input("사용자: ") #input은 str로 저장됨
        # num == 369
        if agree:
            # o -> user == '짝' 
            if user == "짝":
                j += 1
                num += 1
            # x -> break
            else:
                break
        # num != 369
        else: 
            # o ->  user == num
            int_user = int(user)
            if user == int_user:
                j += 1
                num += 1
            # x -> break
            else:
                break
    # com (j가 홀수)
    else:
        # num == 369
        if agree:
            # 짝 
            print("com: 짝")
            j += 1
            num += 1
        # num != 369
        else:
            # num
            print(f"com: {num}")
            j += 1
            num += 1

# break -> game over
print("game over")