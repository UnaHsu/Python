print("hello world")
a = 30
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
f = int(f)
print(f, type(f))

list = [1, 2, 'w']
print('第二個字', list[1], '最後一個字', list[-1])
print('第二個字{0}，最後一個字{1}'.format(list[1], list[-1]))

list1 = [[1, 2, [3, 4]], "hello"]
print(list1[1][0])
print(list1[0][2][1])

d1 = {'fish': [100, 200, 300], 'soup': {'big': 100, 'small': 50}, 'meat': 150}
print(d1['fish'][1]);
print(d1['soup']['big']);
