>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)
...
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)

>>> for i, v in enumerate(t):
...     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52

![enumerate](/image/enumerate.png)