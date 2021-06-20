
#map function
myList = [1,2,3,4,5,6,7,8]
def square(num):
    return num*num
print(list(map(square, myList)))
#lambda function
l = lambda num: num*num
print(l(5))

print(list(map(lambda num: num*num, myList)))

#example
r = lambda x: x+15
print(r(5))
a = lambda x,y: x*y
print(a(8,5))

#example
def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))

#example
marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(marks)

#example
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2 , 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

#example
list = ["Python","Java","Physics","Android"]
print(list(map(lambda x: True if x.startswith('P') else False, list)))





#filter function
print(list(filter(lambda x : x%2 == 0, myList)))
#write a function to filter a list of integers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x : x**2, nums)))
print(list(map(lambda x : x**3, nums)))

