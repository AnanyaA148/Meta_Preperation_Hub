S = "abbc"
B = "babcabbecbabcbba"


for i in range(len(B)):
    
    if B[i] == S[0]:
        str1 = S[0:]
        num =i +1
        num1 =i -1
        if B[num] in str1:
            print("hi")
        # i am stuck. 
        

