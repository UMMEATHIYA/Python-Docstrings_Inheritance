"""
>>> from csc242hw5 import *

# ShortFilm class example usage
>>> f1 = ShortFilm()
>>> f1
ShortFilm(The Last Repair Shop, Ben Proudfoot/Kris Bowers, 2023, 39 min)

>>> print(f1)
The Last Repair Shop directed by Ben Proudfoot/Kris Bowers has these awards: []

>>> f1.addAward('best documentary short film', 'academy awards')
>>> print(f1)
The Last Repair Shop directed by Ben Proudfoot/Kris Bowers has these awards: [Best Documentary Short Film from Academy Awards]

>>> f1.addAward('outstanding short film', 'black reel')
>>> print(f1)
The Last Repair Shop directed by Ben Proudfoot/Kris Bowers has these awards: [Best Documentary Short Film from Academy Awards, Outstanding Short Film from Black Reel]

>>> lst = [awd for awd in f1]
>>> lst
[Outstanding Short Film from Black Reel, Best Documentary Short Film from Academy Awards]

>>> print(f1)
The Last Repair Shop directed by Ben Proudfoot/Kris Bowers has these awards: [Best Documentary Short Film from Academy Awards, Outstanding Short Film from Black Reel]

>>> num1 = f1.getSales()
>>> num1
0.0

>>> f1.registerSales(10000)
>>> num2 = f1.getSales()
>>> num2
10000.0

>>> f2 = ShortFilm('two distant strangers', 'Travon Free/Martin Desmond Roe', 2020, 32)
>>> f2
ShortFilm(Two Distant Strangers, Travon Free/Martin Desmond Roe, 2020, 32 min)

>>> print(f2)
Two Distant Strangers directed by Travon Free/Martin Desmond Roe has these awards: []

>>> f2.addAward('best live action short film', 'academy awards')
>>> print(f2)
Two Distant Strangers directed by Travon Free/Martin Desmond Roe has these awards: [Best Live Action Short Film from Academy Awards]

>>> num3 = f2.getSales()
>>> num3
0.0

# scoreQueue class example usage
>>> q1 = scoreQueue()
>>> q1
[]

>>> q1.enqueue(91, 'larue elam')
>>> q1
[(91, 'Larue Elam')]

>>> q1.enqueue(85, 'jojo settle')
>>> q1
[(85, 'Jojo Settle'), (91, 'Larue Elam')]

>>> q1.enqueue(78, 'hugin bryant')
>>> q1
[(78, 'Hugin Bryant'), (85, 'Jojo Settle'), (91, 'Larue Elam')]

>>> val1 = q1.dequeue()
>>> val1
'Hugin Bryant has a 78'

>>> q1
[(85, 'Jojo Settle'), (91, 'Larue Elam')]

>>> val2 = q1.dequeue()
>>> val2
'Jojo Settle has a 85'

>>> q1
[(91, 'Larue Elam')]

>>> q2 = scoreQueue()
>>> q2
[]

>>> q2.enqueue(89, 'pru sammons')
>>> q2
[(89, 'Pru Sammons')]

>>> q2.enqueue(77, 'trudy miles')
>>> q2
[(77, 'Trudy Miles'), (89, 'Pru Sammons')]

>>> q2.enqueue(65, 'cookie berthiaume')
>>> q2
[(65, 'Cookie Berthiaume'), (77, 'Trudy Miles'), (89, 'Pru Sammons')]

>>> lst1 = [item for item in q2]
>>> lst1
['Cookie Berthiaume has a 65', 'Trudy Miles has a 77', 'Pru Sammons has a 89']

>>> val3 = q2.dequeue()
>>> val3
'Cookie Berthiaume has a 65'

>>> lst2 = [item for item in q2]
>>> lst2
['Trudy Miles has a 77', 'Pru Sammons has a 89']


"""