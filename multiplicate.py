def multiplicate(a):
    product = [1] * len(a)

    # calculate product of prefix
    for i in range(1, len(a)):
        product[i] = product[i - 1] * a[i - 1]

    temp = 1 # in loop will contains product of suffix
    for i in range(len(a) - 2, -1, -1):
        temp *= a[i + 1]
        product[i] *= temp
    
    return product


input_array = [int(i) for i in input('Input array: ').split()]
print('Array of products: ' + ' '.join([str(i) for i in multiplicate(input_array)]))