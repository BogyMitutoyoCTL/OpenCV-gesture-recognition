# Python Hausaufgaben 1/2
Dies sind Hausaufgaben zur Festigung der Python Grundlagen, bevor wir mit Klassen, Objekten, Exceptions und anderen Möglichkeiten von Python fortfahren.
Bei diesen Hausaufgaben handelt es sich um die ersten zehn Probleme von [Project Euler](https://projecteuler.net). Wir haben Sie ins Deutsche übersetzt und ggf. etwas anders erklärt als auf der Originalseite.
Die Lösungen oder Lösungsprogramme bitte nicht ins Git hochladen. Wer mag, kann bei Project Euler einen Account anlegen und die Lösungen dort überprüfen.

## Aufgabe 1: Summe aller Vielfachen von 3 oder 5
Vielfache von 3 oder 5 sind 3, 5, 6, 9, 10, 12, 15, ... 
Addiere all diese Zahlen solange sie kleiner als 1000 sind.

## Aufgabe 2: Summe von Fibunacci-Zahlen
Beginnend mit den Zahlen 1 und 2 addieren wir jeweils die letzten beiden Zahlen und bekommen eine neue. Die Zahlenreihe lautet also 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
Addiere all diese Zahlen solange sie kleiner als 4.000.000 und nur wenn sie gerade sind.

## Aufgabe 3: Größter Primfaktor
Zahlen lassen sich in Primfaktoren zerlegen z.B. ist 13195 die Multiplikation aus 5, 7, 13 und 29.
Ermittle den größten Primfaktor von 600.851.475.143

## Aufgabe 4: Palindromprodukt
Eine Palindromzahl kann man von vorn und von hinten lesen. Manche Produkte ergeben Palindromzahlen. Die größte Palindromzahl, die sich als Produkt aus zwei zweistelligen Zahlen ergibt ist 9009, nämlich 91*99.
Finde die größte Palindromzahl, die sich bei der Multiplikation von zwei dreistelligen Zahlen ergibt.

## Aufgabe 5: Teilen ohne Rest
Die Zahl 2520 lässt sich durch alle Zahlen von 1 bis 10 ohne Rest teilen. Es handelt sich um die kleinste Zahl, bei der dies möglich ist.
Finde die kleinste Zahl, die sich durch alle Zahlen von 1 bis 20 ohne Rest teilen lässt.

Diese Aufgabe ist nicht ganz einfach. Wenn Du nicht weiterkommst, versuche erst einmal die Aufgaben 6 bis 10.

## Aufgabe 6: Quadratsummen
Die Summe der Quadrate der Zahlen von 1 bis 10 ist 385 (1²+2²+...+10²). Das Quadrat der Summe der Zahlen von 1 bis 10 ist 3025 ([1+2+...+10]²). Der Unterschied zwischen beiden ist 2640 (3025-385).
Finde den Unterschied der Summe der Quadrate und des Quadrats der Summe für die Zahlen 1 bis 100.

## Aufgabe 7: Die 10001. Primzahl
Die ersten Primzahlen sind 2, 3, 5, 7, 11, 13. Die sechste Primzahl ist 13.
Welches ist die 10001. Primzahl?

## Aufgabe 8: Prudukt von aufeinanderfolgenden Ziffern
In der folgenden 1000-stelligen Zahl befinden sich hintereinander die Ziffern 9, 9, 8 und 9.
```
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
```
Das Produkt dieser Ziffern ist 5832. Es handelt sich dabei um das größte Produkt aus 4 aufeinanderfolgenden Ziffern in dieser Zahl.
Finde das größte Produkt von 13 aufeinanderfolgenden Ziffern in dieser 1000-stelligen Zahl.

Tipp: ein langer Text lässt sich in Python folgendermaßen schreiben:
```
text = "Langer text\
der über eine Zeile\
hinausgeht."
```

## Aufgabe 9: Pythagoras-Produkt
Pythagoras fand die Gleichung a²+b²=c² für rechtwinklige Dreiecke. Wir schränken ein auf a < b < c. Bei natürlichen Zahlen gibt es z.B. 3²+4²=5². Die Summe aus a, b und c ist hier 12 und das Produkt aus a, b und c ist in diesem Fall 60.
Es gibt genau eine Lösung für a²+b²=c², für die Summe der natürlichen Zahlen a, b und c genau 1000 ergibt und a < b < c gilt. Wie lautet in diesem Fall das Produkt a\*b\*c?

## Aufgabe 10: Summe von Primzahlen
Die Primzahlen unter 10 sind 2, 3, 5 und 7. Die Summe dieser Primzahlen ist 17.
Finde die Summe aller Primzahlen unter 2.000.000.
