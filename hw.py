def permutations_dp(s):
    
    dp = [[]]   
    
    for char in s:
        new_dp = []
        
        for perm in dp:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [char] + perm[i:]
                new_dp.append(new_perm)
        
        dp = new_dp   
    
    for perm in dp:
        print("".join(perm))


string = input("Enter a string: ")
permutations_dp(string)
