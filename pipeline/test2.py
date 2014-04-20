
def even_filter(nums):
    return filter(lambda x: x%2==0, nums)

def multiply_by_three(nums):
    return map(lambda x: x*3, nums)

def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)

#fn(fn-1(.....(init_data)))))
def pipeline_func(init_data, functions):
    return reduce(lambda ret, f: f(ret),
                  functions,
                  init_data)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print pipeline_func(nums, [even_filter, multiply_by_three, convert_to_string])
