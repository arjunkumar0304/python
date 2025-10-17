Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/arjun/Desktop/py.py
10
<class 'list'>
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4]
>>> 
===================== RESTART: C:/Users/arjun/Desktop/py.py ====================
10
<class 'list'>
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4]
>>> 
========================================================================= RESTART: C:/Users/arjun/Desktop/py.py ========================================================================
10
<class 'list'>
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4]
Traceback (most recent call last):
  File "C:/Users/arjun/Desktop/py.py", line 6, in <module>
    a.expend(4,5,6,7,8)
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
>>> 
========================================================================= RESTART: C:/Users/arjun/Desktop/py.py ========================================================================
10
<class 'list'>
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4]
Traceback (most recent call last):
  File "C:/Users/arjun/Desktop/py.py", line 6, in <module>
    a.expend([4,5,6,7,8])
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
>>> 
========================================================================= RESTART: C:/Users/arjun/Desktop/py.py ========================================================================
10
<class 'list'>
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4]
[1, 2, 3, 4, '5', 10.6, [1, 2, 3], {'one': 1, 'two': 2, 'three': 3}, (1, 2, 3), {0, 9, 5}, 4, 4, 5, 6, 7, 8]
