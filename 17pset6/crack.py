import crypt
import cs50
import string

while True:
    
    print('Please only input alphabet for Crack: ', end = "")
    _input = cs50.get_string()
    check_count = 0
    # check everything user type in
    # if everything is char then proceed
    for i in range(len(_input)):
        if _input[i].isalpha() is True:
            check_count+=1
            #print(check_count) # check if char qty is correct
    # if everythin is char and length is < 5, proceed        
    if check_count == len(_input) & len(_input) < 5:
        break

# generate hash for user input        
hash_input = crypt.crypt(_input,'abc')

# test data only consist lower and uppercase
test_list = string.ascii_lowercase + string.ascii_uppercase

# brute crack, use 4 nest loop 
for i in test_list:
    test = crypt.crypt(i,'abc')
    if test == hash_input:
        print('Found! Password is ' + i + '.')
        break
    
    for j in test_list:
        test = crypt.crypt(i+j,'abc')
        if test == hash_input:
            print('Found! Password is ' + i+j + '.')
            break
        
        for k in test_list:
            test = crypt.crypt(i+j+k,'abc')
            if test == hash_input:
                print('Found! Password is ' + i+j+k + '.')
                break
            
            for l in test_list:
                test = crypt.crypt(i+j+k+l,'abc')
                if test == hash_input:
                    print('Found! Password is ' + i+j+k+l + '.')
                    break
            
print('The hash password is ' + hash_input + '.')