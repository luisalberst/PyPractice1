from functools import reduce

def func_list(values): 
    res = list(filter((lambda x: x % 2), values)) 
    print(res)
    res = reduce( (lambda x, y: x + y), res) 
    print(res)

new_list = list(range(100))

func_list(new_list)