# OpenCV Homework (grüne Hand aus Bild ausschneiden)
Ziel der Hausaufgabe ist es alles außer dem Handschuh im Bild zu eliminieren.
Es werden Funktionen gebraucht, die ihr schon in den Übungen angewendet habt. Diese findet ihr
[hier!](https://github.com/BogyMitutoyoCTL/OpenCV-gesture-recognition/blob/master/Anleitungen/Bild-Verarbeitung-Manipulaltion/L%C3%B6sung.py)

![Grüner Handschuh](https://github.com/BogyMitutoyoCTL/OpenCV-gesture-recognition/blob/master/Hausaufgaben/Handschuh.jpg)

Als Ergebnis erwarten wir ein Schwarz-Weiß Bild (Handschuh weiß)

Solltet ihr Fragen haben kontaktiert uns per E-Mail.

Hinweis zur Lösung:
Die HSV Werte des Handschuhs könnt ihr mit einem Grafikprogramm wie GIMP auslesen. Allerdings müsst ihr darauf achten, dass die
meisten Grafikprogramme die "S" und "V" Werte in Prozent (also von 0 bis 100) auslesen aber die
inRange() Funktion von OpenCV die "S" und die "V" Werte als Hexadezimale Zahlen erwartet.

* Umrechnung: 
  * Ausgelesene HSV Werte mit GIMP: 
    * H:  61
    * S: 100
    * V:  26
  * HSV Werte für OpenCV:         
    * H:  61
    * S: 255  --> (255 X 1) = **255**
    * V:  66  --> (255 X 0,26) = **66,3**
