import crypt
import cs50

_input = cs50.get_string()

for i in range(len(_input)):
    if _input[i].isalpha() is False:
        print('Please only input alphabet.')
        _input = cs50.get_string()
    else:
        print('.',end="")

    
hash_input = crypt.crypt(_input,'abc')

print(hash_input)