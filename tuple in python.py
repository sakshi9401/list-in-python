#tuple is immutable i.e, unchangeable
tp = (1, 3, 5, 6)
tp1 =('a','b','c')
print(tp)
print(type(tp))
print(tp[1])#acecss tuple item
print(tp[-1])#negative index
y = list(tp)
print(y)
y[1] = 9
print(y)
print(len(tp))
tp2 = tp + tp1
print(tp2)
"""
del #removes complete tuple but then tuple is no more exit
tp1 = (4)# this is integer
print(type(tp1))
tp2 = (1,)# this is tuple
print(type(tp2))
tp3 = ("3")# this is string
print(type(tp3))
"""