Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a=[1,2,3,4,5,6,7,8,9,10]
a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.pop()
10
a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#pop removes last value by default
#Set
C1={'DD','VN','HN','SK','AB'}
C2={'Ong','SP','GJ'}
C1.update(C2)
C1
{'AB', 'DD', 'HN', 'VN', 'SP', 'SK', 'GJ', 'Ong'}
C2
{'SP', 'GJ', 'Ong'}
a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
b=(10,20,30,40,50)
b
(10, 20, 30, 40, 50)
b==(1,2,56,65)
False
B=(1,2,3,11,25,36)
B
(1, 2, 3, 11, 25, 36)
>>> a.difference_update(B)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.difference_update(B)
AttributeError: 'list' object has no attribute 'difference_update'
>>> A={1,2,3,4,5}
>>> C={1,5,8,9}
>>> A.difference_update(C)
>>> A
{2, 3, 4}
>>> C
{8, 1, 5, 9}
>>> #symmetric_difference_update
>>> x={'reliance','JBL','Tata'}
>>> y={'Zebion','Dell','Lenovo'}
>>> x.symmetric_difference_update(y)
>>> y
{'Lenovo', 'Zebion', 'Dell'}
>>> x
{'Zebion', 'Tata', 'Lenovo', 'Dell', 'reliance', 'JBL'}
>>> #intersection_update
>>> p={'A','B','C'}
>>> q={'N','D','W'}
>>> r={'S','T','W'}
>>> p.intersection_update(q,r)
>>> p
set()
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b
(10, 20, 30, 40, 50)
>>> A
{2, 3, 4}
>>> B
(1, 2, 3, 11, 25, 36)
>>> B={2,8,9}
>>> A.intersection_update(B)
>>> A
{2}
