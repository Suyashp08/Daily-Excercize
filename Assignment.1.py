Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3,'py',5]
>>> #add Aj before 1
>>> a.insert(0,'AJ')
>>> a
['AJ', 1, 2, 3, 'py', 5]
>>> #Add 4 through negative indexing
>>> a.insert(-1,4)
>>> a
['AJ', 1, 2, 3, 'py', 4, 5]
>>> ['AJ', 1, 2, 3, 'py', 4, 5]
['AJ', 1, 2, 3, 'py', 4, 5]
>>> a.insert(2,'Python')
>>> a
['AJ', 1, 'Python', 2, 3, 'py', 4, 5]
