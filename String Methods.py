Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String methods
>>> name='Suyash Pawar'
>>> name
'Suyash Pawar'
>>> name.split()
['Suyash', 'Pawar']
>>> name.upper()
'SUYASH PAWAR'
>>> name.tite()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name.tite()
AttributeError: 'str' object has no attribute 'tite'. Did you mean: 'title'?
>>> name.title()
'Suyash Pawar'
>>> name.lower()
'suyash pawar'
>>> name.capitalize()
'Suyash pawar'
>>> a='AsHiSH'
>>> a.swapcase()
'aShIsh'
>>> #swapcase()converts smallcase into bigcase and similar vice versa
>>> name
'Suyash Pawar'
>>> name.replace('Pawar','Patil')
'Suyash Patil'
>>> a
'AsHiSH'
>>> A='   Vinay    '
>>> A.strip()
'Vinay'
>>> B='$yash'
>>> B.replace('$','')
'yash'
