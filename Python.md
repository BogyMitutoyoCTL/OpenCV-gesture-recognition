#Python
Dies ist eine kurze Einführung in Python für Schüler, die an der Berufsorientierung für Realschulen (BORS) oder Gymnasien (BOGY) teilnehmen.
Insbesondere soll die Verwendung von Python auf dem Raspberry Pi erklärt werden.

Um diese Anleitung komplett durchzuarbeiten brauchst Du ca. 2 bis 3 Stunden Zeit. Du kannst Dir aber auch ein Kapitel pro Tag vornehmen. Die Anleitung geht nicht auf alle Details ein. Wenn Du etwas nicht verstehst, dann recherchiere ein bisschen im Internet.

Du kannst die Beispiele gern ausprobieren und solltest Dir auch Zeit für die Übungsaufgaben nehmen. Es hat sich bewiesen, dass man beim Ausprobieren viel mehr lernt als beim reinen Durchlesen.

## Programmiersprachen Übersicht
Ein Computer muss programmiert werden, damit er das tut, was man von ihm will. Für diese Aufgabe gibt es Programmiersprachen. Diese Einleitung erklärt, welche Unterschiede es bei Programmiersprachen gibt und warum wir uns für Python entschieden haben.
### Maschinensprache
Prozessoren (CPUs, Centrl Processing Unit) führen Befehle / Berechnungen aus. Ein Prozessor versteht Maschinensprache.  Maschinensprache sind Zahlen, für Menschen meist in hexadezimaler Schreibweise angegeben.

Beispiel:
```
55
48 89 E5
C7 45 FC 02
C7 45 F8 03
```


Diese Art der Programmierung ist für Menschen nicht gut verständlich. Oder weißt Du jetzt, was da berechnet wird?

###Assembler
Assembler ist die nächst höhere Stufe, aber immer noch sehr Prozessor-lastig. Für tief eingestiegene Programmierer handelt es sich jedoch schon um eine lesbare Form.

Beispiel (Maschinensprache links, Assembler rechts):
```
55                push rbp
48 89 E5          mov rbp, rsp
C7 45 FC 02       mov DWORD PTR [rbp-4], 2
C7 45 F8 03       mov DWORD PTR [rbp-8], 3
```

Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Maschinensprache)

- `mov`: Daten verschieben
- `rsp`: Das SP Register (das sind Datenspeicher im Prozessor)
- `DWORD`: Kennzeichnet die Größe des Speichers, nämlich 32 Bits
- `2`: Die Zahl 2
- `3`: Die Zahl 3

Hier werden also die Zahlen 2 und 3 irgendwo im Speicher (RAM) verschoben. Noch nicht sonderlich aufschlussreich, oder?

###C
C ist eine Programmiersprache von 1972. Sie erlaubt die Gliederung eines Programms in Methoden, Variablen, usw.

Beispiel (Maschinensprache links, Assembler Mitte, C rechts)
```
55                push rbp                          int main()
48 89 E5          mov rbp, rsp                      {
C7 45 FC 02       mov DWORD PTR [rbp-4], 2              int a = 2;
C7 45 F8 03       mov DWORD PTR [rbp-8], 3              int b = 3;
```

Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Maschinensprache)

`main()` ist eine Funktion, die einen Wert vom Typ `int` (das sind 32 Bit) zurückgibt. Darin gibt es zwei Variablen `a*`und `b`, die den Wert `2` bzw. `3` haben. Das kann man schon fast verstehen.

In C wird noch viel programmiert, insbesondere für Embedded-Systeme (z.B. Arduino), wo wenig Speicher zur Verfügung steht.

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

### Raspberry Pi

Auf unserem Raspberry Pi ist das Betriebssystem [Raspbian](https://www.raspbian.org/) installiert. Bei den derzeitigen Versionen von Raspbian ist Python schon installiert. Im Menü findet ihr sogar zwei Editoren, nämlich IDLE für Python 2 und IDLE für Python 3. IDLE steht für **I**ntegrated **D**evelopment and **L**earning **E**nvironment.

Für die Programmierung der Raspberry Gestensteuerung werden wir IDLE verwenden.

### Windows

Falls ihr zu Hause Python ausprobieren wollt, könnt ihr Python auch für Windows installieren. Den offiziellen Download gibt es auf [python.org](https://www.python.org/downloads/). Wir verwenden Python 3, d.h. ihr müsst Python 3.6.0 herunterladen und installieren.

Es gibt jedoch auch Installtionen, die noch mehr Bibliotheken mitbringen. Eine davon ist [Anaconda](https://www.continuum.io/downloads#windows). Allerdings ist der Download mit über 400 MB auch etwas größer und auf der Festplatte braucht es fast 2 GB.

## Entwicklungsumgebung

Um ein Programm zu schreiben braucht man einen Editor. Ein ganz normaler Texteditor wie Notepad würde schon genügen. Allerdings ist der Text dort immer schwarz-weiß. Es hat sich herausgestellt, dass eine farbige Hervorhebung praktisch ist. So können Probleme erkannt werden, ohne dass das Programm ausprobiert werden muss.

Um ein Programm von Text in Maschinensprache zu übersetzen braucht man einen Compiler oder Interpreter. Dabei handelt es sich meist um ein Kommandozeilen-Programm, das umständlich zu bedienen ist.

Damit man den Vorteil von "buntem" Text hat und den Compiler oder Interpreter bequem benutzen kann, hat es sich durchgesetzt, dass man zum Programmieren eine Entwicklungsumgebung verwendet. Im Fachjargon nennt sich das IDE und steht für **I**ntegrated **D**evelopment **E**nvironment.

Eine solche IDE unterstützt sämtliche Arbeitsschritte eines Entwicklers:
- Programm in einem Editor schreiben
- Befehle farblich hervorheben
- Programm compilieren
- Programm ausführen
- Bei einem Fehler anhalten ("Debugger")
- Aufgaben verwalten
- Versionskontrolle (z.B. Git) verwenden
- ...

### IDE für Raspberry

Auf dem Betriebssystem Raspbian ist die Entwicklungsumgebung IDLE schon installiert. Diese werden wir verwenden. Sie ist nicht besonders komfortabel, aber für unsere Zwecke ausreichend.

### IDE für Windows

Für Windows gibt es [PyCharm](https://www.jetbrains.com/pycharm/) in der kostenlosen Community Edition. Es braucht ca. 500 MB Festplattenplatz. Es hat viele Funktionen, was aber für Anfänger schon wieder zu viel sein kann. Achtet darauf, dass ihr beim Anlegen eines Projekts Python 3 als Interpreter auswählt.

### Online

Zum Üben kann man auch auf Online-Entwicklungsumgebungen zurückgreifen. Beispiele sind:
- [IDEone](https://ideone.com/) (Achtung: Sprache muss auf *Python 3 nbc* umgestellt werden)
- [PythonTutor](http://www.pythontutor.com/visualize.html#mode=edit) 
- [Blockly](https://developers.google.com/blockly/): Programmierung mit Klötzchen, Programm kann als Python angezeigt werden

Die Nachteile von Online-IDEs sind:
- sie können oft nur mit einer Datei umgehen
- das Programm ist ggf. für alle Menschen sichtbar
- keine Anbindung an eine Versionskontrolle wie Git
- nicht alle haben einen Debugger

## Python Grundlagen

### Dateiformat

Programme werden als PY Datei abgelegt. Es handelt sich um eine Textdatei mit UTF-8 Encoding (bei Python 3), d.h. ihr könnt auch Sonderzeichen verwenden.

Python verwendet eine Anweisung pro Zeile. Andere Sprachen trennen Anweisungen mit einem Strichpunkt (`;`) und ein Umbruch ist nur empfohlen.

Die Einrückung ist bei Python wichtig. Bei anderen Programmiersprachen ist die Einrückung oft egal, aber empfohlen. Damit einheitlich eingerückt wird, hat man sich auf 4 Leerzeichen geeinigt.

Variablen existieren ab der ersten Verwendung. Die meisten anderen Programmiersprachen erfordern eine Deklaration von Variablen.

### Kommentare

Kommentare und Anmerkungen werden mit einer Raute (`#`, auch "Lattenzaun") eingeleitet. Dies kann z.B. für die Aufgabenbeschreibung bei den Hausaufgaben verwendet werden. Ein Kommentar kann auch hinter einer Anweisung stehen.

Beispiel:
```
# Aufgabe 1: Summe aller Vielfachen von 3 oder 5
# Vielfache von 3 oder 5 sind 3, 5, 6, 9, 10, 12, 15, ... 
# Addiere all diese Zahlen solange sie kleiner als 1000 sind.
```

### Rechnen

Eine Variable existiert ab ihrer ersten Zuweisung. Die Zuweisung eines Werts erfolgt mit einem Gleichheitszeichen (`=`). Die mathematischen Operationen `+`, `-`, `*` (Multiplikation) und `/` (Division) funktionieren wie aus der Mathematik bekannt unter Berücksichtigung der Regel "Punkt vor Strich".

In Python werden Ganzzahlen automatisch in Kommazahlen umgewandelt.

Beispiel:
```
x = 5
y = x + x / 6
print(y)
```

Weil Variablen mehrere Buchstaben haben dürfen, muss die Multiplikation immer explizit angegeben werden. Im folgenden Beispiel gibt es drei Variablen mit den Namen **a**, **b** und **ab**:
```
a = 2
b = 3
ab = a*b
print(a, b, ab)
```

Es gibt noch weitere Rechenoperationen:
- Ganzzahl Division mit `//`, z.B. 5//2 = 2
- Rest (Modulo) mit `%`, z.B. 5%2 = 1
- Potenz mit `**`, z.B. 2\*\*3 = 2³ = 8
- Klammern mit `(` und `)`, z.B. (3+1)*2 = 8

Die Regel "Punkt vor Strich" ist sicherlich bekannt. Mit den zusätzlichen Rechenoperationen ist die Reihenfolge nicht mehr ganz so klar. Folgender Merkspruch kann helfen:

**K**ein **P**rogramm **m**acht **d**iese **a**bwegigen **S**achen

Die Anfangsbuchstaben stehen für
- **K**lammern (haben die höchste Priorität)
- **P**otenz
- **M**ultiplikation und **D**ivision (Punkt-Operationen)
- **A**ddition und **S**ubtraktion (Strich-Operationen)

Beim Programmieren ändert sich der Wert einer Variablen oft abhängig von ihrem eigenen Wert. Dafür gibt es eine eigene Schreibweise:

```
i += 1   # i = i + 1, d.h. i wird um eins erhöht
i -= 1   # i = i - 1, d.h. i wird um eins verringert
i *= 2   # i = i * 2, d.h. i wird verdoppelt
i /= 2   # i = i / 2, d.h. i wird halbiert
```

Bei anderen Rechenoperationen geht das auch (z.B. `**=`, `%=` oder `//=`), wird dort aber seltener angewandt.

### Übungsaufgabe zum Rechnen

Berechne 356*4³.

### Text

Text (auch "Zeichenketten" oder "Strings" genannt) kann bei Python in Anführungszeichen (`"`) (engl. "quotation marks" oder "double quotes") oder in Hochkomma (`'`) (engl. "apostrophe" oder "single quote") geschrieben werden.

Beispiel:
```
print("Hello world.")
print('Hello world.')
```

Wenn das einleitende Zeichen im Text selbst vorkommen soll, muss es dem Interpreter entrinnen (engl. "escape"). Dies geschieht durch einen umgekehrten Schrägstrich (`\`, engl. "backslash").

Beispiel:
```
print("\"Huch\", sagte er.")
print('"Huch", sagte er.')
print('\'Huch\', sagte er.')
print("'Huch', sagte er.")
```

Durch die Einführung des Backslashes als Sonderzeichen gibt es ein neues Problem: der Backslash selbst kann nicht mehr im Text verwendet werden. Lösung: der Backslash escaped sich selbst. Dies sieht man oft bei Pfadangaben von Windows, weil diese ebenfalls den Backslash nutzen.

```
print("Wow \\ ist \\ das \\ abgefahren...")
```

Einige Sonderzeichen, die mit dem Backslash escaped werden:
- `\n` für einen Zeilenumbruch (neue Zeile, line feed, LF)
- `\\` für einen Backslash
- `\"` für ein Anführungszeichen
- `\'` für einen Apostroph
- `\xhh` für ein Sonderzeichen aus der Sonderzeichentabelle (wobei hh durch eine hexadezimale Zahl ersetzt wird)

Ansonsten lassen sich dank UTF-8 Sonderzeichen auch direkt in das Programm einfügen:

```
print("Zeile 1\nZeile 2")
print("∞♫")
```

Python kann auch mit Text "rechnen", z.B. kann eine Variable Text enthalten. Texte können mit Plus (`+`) aneinandergehängt werden. Witzig: auch multiplizieren klappt mit Mal (`*`). Probier es mal aus:

```
omg = "OMG"
print(omg + "Wow")
print(omg * 5)
```

Wie eine Zeitung mit einer Schere lässt sich Text in Python auch zerschnipseln (engl. "slice") mit eckigen Klammern und Angabe einer Position an der begonnen bzw. aufgehört werden soll zu schneiden. Achtung: die Zählung startet für einen Computer bei 0 — daran gewöhnt man sich mit der Zeit.

Beispiel:
```
halloWelt = "Hallo Welt."
hallo = halloWelt[0:5]
print(hallo)
```

Beim Zerschnipseln gibt es viele Sonderfunktionen. Probiere mal aus, was in folgenden Fällen passiert:
```
halloWelt = "Hallo Welt."
print(halloWelt[5])
print(halloWelt[:5])
print(halloWelt[6:])
print(halloWelt[-5:-1])
```

Eine Aufgabe, die oft vorkommt, ist die Umwandlung von Text in Zahlen und umgekehrt. Das liegt daran, dass ein Benutzer auch Zahlen per Tastatur und damit als Text eingibt. Es gibt folgende Umwandlungsfunktionen:
- Text in Ganzzahl mit `int(...)`
- Text in Kommazahl mit `float(...)`
- Zahl in Text mit `str(...)`

```
zahl = int("5")
kommazahl = float("5.1")
text = str(zahl)
print(zahl, text, kommazahl)
```
### Übungsaufgabe zu Text

Was ist das Quadrat der mittleren beiden Ziffern von 36²?

Lösung: 36² = 1296. Die mittleren beiden Ziffern sind 2 und 9, also 29. 29² = 841. Die Lösung lautet also 841.

Tipp: Wandle die Zahl in Text um, schneide dann die Stellen aus und wandle den zweistelligen Text wieder in eine Zahl um.

###Listen

In Listen kann man mehrere Werte ablegen, um sie später nacheinander zu verarbeiten. In Python wird eine Liste mit eckigen Klammern (engl. "brackets") angelegt und die einzelnen Werte durch Komma getrennt. Ähnlich wie beim Text kann man die Liste auch zerschnipseln ("slice"). Wichtig ist, dass die Zählung bei 0 beginnt (wie beim Text auch) und die letzte Zahl nicht mehr dazu gehört.

```
list = [11, 13, 15, 17]
print(list)        # [11, 13, 15, 17]
print(list[0])     # 11
print(list[1:3])   # [13, 15]
print(list[1:])    # [13, 15, 17]
print(list[:3])    # [11, 13, 15]
```

Listen können auch geändert werden, z.B. lassen sich Listen mit `+` aneinanderhängen. Ebenfalls lässt sich der Listeninhalt mit `*` vervielfachen:

```
listA = [11, 13, 15]
listB = [17, 19]
listC = listA + listB
listD = listB * 3
print(listC)      # [11, 13, 15, 17, 19]
print(listD)      # [17, 19, 17, 19, 17, 19]
```

Einem Slice (Ausschnitt) können auch neue Werte zugewiesen werden, d.h. die betroffenen Teile der Liste werden entfernt und durch den zugewiesenen Teil ersetzt. Man kann einen Slice einer Liste löschen, indem man ihm eine leere Liste (`[]`) zuweist.

```
listA = [11, 13, 15]
listA[0:2] = [1, 5, 9]
print(listA)
listA[0:2] = []
print(listA)
```

Eine Liste kann beliebige Dinge enthalten, z.B. Text und Zahlen gemischt. Aber Achtung: da Listen meist in einer Schleife verarbeitet werden, wird die Rechenoperation (der Algorithmus) auf alle Einträge angewandt. Eine solcher Algorithmus kann z.B. bei Bildern funktionieren, aber bei Excel-Dateien nicht. Eine Mischung von unterschiedlichen Dingen wird eher selten benötigt.

```
beliebig = [3.14, "Text", 5]
print(beliebig)
```

Die Anzahl der Einträge in einer Liste lässt sich mit `len(...)` ermitteln.

```
list = [11, 13, 15]
einträge = len(list)
print(einträge)
```

### Übungsaufgabe zu Listen

Gib die ersten drei Einträge der Liste [2, 3, 5, 7, 11, 13, 17] aus.

### Wahrheitswerte

Der Vergleich zweier Zahlen, zweier Texte oder Buchstaben ergibt einen Wahrheitswert. Ein Wahrheitswert kann nur zwei Werte annehmen, nämlich wahr(`True`) oder falsch (`False`).

Übliche Vergleichsoperatoren sind:
- Kleiner: `<`
- Kleiner oder gleich: `<=`
- Größer: `>`
- Größer oder gleich: `>=`
- Gleich: `==` (beachte bitte, dass das einfache Gleichheitszeichen (`=`) verwendet wird, um Variablen einen Wert zuzuweisen)
- Ungleich: `!=`

```
print(3 < 5)   # True
print(3 <= 5)  # True
print(5 > 3)   # True
print(5 >= 3)  # True
print(5 == 5)  # True
print(3 != 5)  # True
```

Wahrheiten können auch miteinander verknüpft werden. Verknüpfungsoperatoren sind:
- `and`: beide Aussagen müssen wahr sein, damit das Gesamtergebnis wahr ist
- `or`: mindestens eine Aussage muss wahr sein, damit das Gesamtergebnis wahr ist

Wenn `and` und `or` gemeinsam verwendet werden, hat `and` Vorrang. Hier sind ein paar logische Verknüpfungen:

```
print(5 > 3 and 7 < 9)     # True
print(True and True)       # True
print(5 > 3 or 9 < 7)      # True
print(True or False)       # True
print(5 < 3 and 7 < 9)     # False
print(False and True)      # False
print(True or False and False)
```

### Übungsaufgabe zu Wahrheitswerten

Finde heraus, ob die Aussage a ≤ b ≥ c wahr oder falsch ist für die Werte
- a=3, b=9 und c=17
- a=1, b=2 und c=2

### Wiederholungen

Bei einer einzelnen mathematischen Berechnung ist man im Kopf oder mit dem Taschenrechner meist schneller als wenn man ein Programm schreibt. Ein Computer ist dann sinnvoll, wenn viele gleichartige Berechnungen hintereinander ausgeführt werden müssen, also wiederholt werden.

Für die Wiederholung einer Rechnung bei einer unbekannten Anzahl an Rechenschritten eignet sich die `while` Schleife. Die `while`-Schleife rechnet so lange, bis eine bestimmte Bedingung erfüllt ist. Nach dem Doppelpunkt der Schleife wird so lange eingerückt programmiert, bis alle Rechenschritte fertig sind. Alles was danach folgen soll, wird wieder ausgerückt.

Beispiel: es soll berechnet werden, wie viele Quadratzahlen es unter 1000 gibt. Da wir noch nicht wissen, wie viele das sein werden, bietet sich eine `while`-Schleife an.

```
i = 1
while i * i < 1000:
    i += 1
print("Es gibt " + str(i - 1) + " Quadratzahlen unter 1000")
```

Ist die Anzahl der Wiederholungen schon bekannt, bietet sich die `for`-Schleife an. Auch nach dem Doppelpunkt der `for`-Schleife muss solange eingerückt programmiert werden, bis die Rechnung abgeschlossen ist. Erst danach geht es wieder ausgerückt weiter.

Beispiel: da schon bekannt ist, wie viele Einträge eine Liste hat, werden Listen meist mit `for`-Schleife bearbeitet:

```
for i in [1, 2, 13, 47, 501]:
    print(i)
print("fertig")
```

Sehr beliebt ist hier auch __range(__...__)__:

```
for i in range(1, 100):
    print(i * i)
print("fertig")
```

### Übungsaufgabe zu Wiederholungen

Wie viele Zahlen zwischen 100 (einschließlich) und 999 (einschließlich) enthalten die Ziffer 3?

Lösung: 252

Tipp: wandle die Zahl in einen Text um und prüfe dann, ob an erster, zweiter oder dritter Stelle der Buchstabe 3 steht.

### Verzweigungen

In einigen Fällen muss ein Computer Entscheidungen fällen, z.B. wenn es dunkel ist, mach das Licht an, andernfalls mach das Licht aus.

Der Aufbau von Verzweigungen ist folgendermaßen:
```
if bedingung1:
    # wenn die Bedingung wahr ist
elif bedingung2:
    # wenn bedingung1 nicht wahr war, aber bedingung2 wahr ist
elif ...:
    # ...
else:
    # wenn keine der vorherigen Bedingungen zutraf
```

Nach dem Doppelpunkt geht es eingerückt weiter. An Stelle der Kommentare stehen natürlich Anweisungen. `elif` und `else` sind nicht unbedingt erforderlich.

Beispiel:
```
if 3 < 7:
    print("3 ist kleiner als 7")
else:
    print("3 ist nicht kleiner als 7")
```

### Methoden

Methoden werden verwendet, damit man Teile eines Programms mehrmals wieder verwenden kann. Eine Methode beginnt mit `def` und einem beliebigen Namen, dann runde Klammern und ein Doppelpunkt. Nach dem Doppelpunkt geht es (wie immer) solange eingerückt weiter, bis alle Rechnungen, die wiederverwendet werden sollen, enthalten sind. Danach geht es ausgerückt weiter.

Eine Methode wird verwendet über ihren Namen und runde Klammern, wie im Beispiel:

```
def Wahnsinn():
    print("OMG! Wow! Das ist irre")

Wahnsinn()
Wahnsinn()
```

Einer Methode können auch Werte zur Verarbeitung mitgegeben werden:
```
def Wahnsinn(anzahl):
	for i in range(1, anzahl):
        print("OMG! Wow! Das ist irre")

Wahnsinn(2)
Wahnsinn(5)
```

### Funktionen

Funktionen sind so ähnlich wie eine Methode, nur dass sie ein Ergebnis zurückgeben können, das wiederum einer Variablen zugewiesen werden kann. Das zurückgeben des Werts geschieht mit `return`.

```
def Unglaublich(a, b):
    c = a + b
    d = a * b
    return c * d

x = Unglaublich(2, 4)
print(x)
```

Der Wert 2 wird an die Funktion übergeben und hat innerhalb der Funktion den Namen `a`. Der Wert 4 wird als `b` übergeben. Die Funktion kann dann mit den Variablen a und b rechnen. Schließlich wird das ausgerechnete Ergebnis mit `return` wieder zurückgegeben und dann der Variable `x` zugeweisen.

### Eingabe und Ausgabe

Die Ausgabe haben wir schon oft verwendet: __print(__...__)__. Möchte man die Ausgabe hübsch gestalten, lassen sich Werte folgendermaßen in den Text einfügen:
```
wert1 = 7
wert2 = 13
print("Wert 1: {}, Wert 2: {}".format(wert1, wert2))
```

Eine Eingabe von der Tastatur lässt sich mit __input(__...__)__ erreichen. Beispiel:
```
name = input("Wie heisst Du?")
print("Der Benutzer {} ist jetzt da.".format(name))
```

Wenn es sich um größere Datenmengen handelt, dann ist die Ausgabe auf dem Bildschirm und die Eingabe per Tastatur nicht mehr praktikabel. In solchen Fällen können Dateien verwendet werden, um die Ausgangswerte einzulesen und die Ergebnisse abzuspeichern. Folgende Operationen sind mit Dateien nützlich:

- Eine Datei zum Lesen öffnen: `datei = open(dateiname, "r")`
- Die ganze Datei lesen: `inhalt = datei.read()`
- Eine Zeile lesen: `zeile = datei.readline()`
- Datei schließen: `datei.close()`
- Datei zum Schreiben öffnen: `datei = open(dateiname, "w")`
- Daten schreiben: `datei.write(text)`
- Datei schließen: `datei.close()`

### Übungsaufgabe zu Ein- und Ausgabe

Schreibe ein Programm, das die Zahlen 1 bis 10 und deren Quadrat sowie deren dritte Potenz ausgibt, aber nur wenn das Quadrat größer 8 und die dritte Potenz kleiner als eine vom Benutzer eingegebene Zahl ist.

## Ausblick

Python kann noch ganz viele Dinge mehr, die wir in einem zweiten Python Kurs besprechen:
- Tupel, Mengen, Wörterbücher
- Ausnahmen ("Exceptions")
- Klassen und Objekte
- Funktionen und Methoden der Standardbibliothek
- ...