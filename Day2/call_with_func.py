def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("#map() 실행 결과")
print(output_a)
print(list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("#filter() 함수의 실행 결과")
print(output_b)
print(list(output_b))