#Python
Dies ist eine kurze Einführung in Python für Schüler, die an der Berufsorientierung für Realschulen (BORS) oder Gymnasien (BOGY) teilnehmen.
Insbesondere soll die Verwendung von Python auf dem Raspberry Pi erklärt werden.
## Programmiersprachen
Ein Computer muss programmiert werden, damit er das tut, was man von ihm will. Für diese Aufgabe gibt es Programmiersprachen. Diese Einleitung erklärt, welche Unterschiede es bei Programmiersprachen gibt und warum wir uns für Python entschieden haben.
### Maschinensprache
- Prozessoren führen Befehle / Berechnungen aus
- Prozessor versteht Maschinensprache
- Maschinensprache sind Zahlen, meist hexadezimal

Beispiel:
```
55
48 89 E5
C7 45 FC 02
C7 45 F8 03
```


Diese Art der Programmierung ist für Menschen nicht gut verständlich.

###Assembler
- Für tief eingestiegene Programmierer lesbare Form

Beispiel (Maschinensprache links, Assembler rechts)
```
55                push rbp
48 89 E5          mov rbp, rsp
C7 45 FC 02       mov DWORD PTR [rbp-4], 2
C7 45 F8 03       mov DWORD PTR [rbp-8], 3
```

Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Maschinensprache)

- mov: Daten verschieben
- r: Register
- DWORD: Anzahl der Bits (32)

###C
- Programmiersprache von 1972
- Gliederung in Methoden, Variablen, ...

Beispiel (Maschinensprache links, Assembler Mitte, C rechts)
```
55                push rbp                          int main()
48 89 E5          mov rbp, rsp                      {
C7 45 FC 02       mov DWORD PTR [rbp-4], 2              int a = 2;
C7 45 F8 03       mov DWORD PTR [rbp-8], 3              int b = 3;
```

Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Maschinensprache)

In C wird noch viel programmiert, insbesondere für Embedded-Systeme (z.B. Arduino).

### Wunsch-Programmiersprache
Auch wenn C für Menschen schon gut verständlich ist, müssen dem Computer noch viel zu viele Details beigebracht werden. Am liebsten wäre uns eine Programmiersprache, die gleich das tut, was wir vom Computer wollen.

Beispiel:
```
Computer, erkenne meine Gesten.
```

Eine solche Programmiersprache existiert leider noch nicht.

### Python

Für die Programmierung des Raspberry Pi verwenden wir Python. Aus folgenden Gründen haben wir Python ausgewählt:

- Python ist kostenlos verfügbar
 - für den Raspberry (unser Zielsystem)
 - auf dem PC (zum Üben)
 - online (zum Üben)
- Es handelt sich um eine Hochsprache
 - sie ist nicht so nah am Prozessor orientiert
 - und dadurch leichter verständlich
- Es ist eine Universalsprache ("general purpose language")
 - man kann sehr viele unterschiedliche Probleme damit lösen
- Es gibt viele Bibliotheken
 - man muss nicht alles selbst programmieren
 - man kommt schneller zum Ergebnis
 - Bibliotheken wurden bereits getestet und enthalten weniger Fehler
- Untersützt beide wesentlichen Paradigmen (Denkweisen)
 - objektorientierte Programmierung ("alles ist ein Ding", z.B. ein Bild)
 - prozedurale Programmierung ("alles ist ein Algorithmus", z.B. eine Funktion)
- Python ist interpretiert
 - im Gegensatz zu compiliert
 - dadurch plattformunabhängig
 - aber leider etwas langsam

Obwohl das Python Logo zwei Schlagen enthält, geht der Name Python auf Monty Python zurück.

## Installation

