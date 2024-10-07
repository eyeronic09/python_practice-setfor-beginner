a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def lessThanTen(a):
    return a < 10

filtered_num = list(filter(lessThanTen,a))
print(filtered_num)