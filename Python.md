#Python
Dies ist eine kurze Einführung in Python für Schüler, die an der Berufsorientierung für Realschulen (BORS) oder Gymnasien (BOGY) teilnehmen.
Insbesondere soll die Verwendung von Python auf dem Raspberry Pi erklärt werden.
## Programmiersprachen
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

- **mov**: Daten verschieben
- **r**: Register (das sind Datenspeicher im Prozessor)
- **DWORD**: Kennzeichnet die Größe des Speichers, nämlich 32 Bits
- **2**: Die Zahl 2
- **3**: Die Zahl 3

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

**main()** ist eine Funktion, die einen Wert vom Typ **int** (das sind 32 Bit) zurückgibt. Darin gibt es zwei Variablen **a** und **b**, die den Wert **2** bzw. **3** haben. Das kann man schon fast verstehen.

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

Auf unserem Raspberry Pi ist das Betriebssystem [Raspbian](https://www.raspbian.org/) installiert. Bei den derzeitigen Versionen von Raspbian ist Python schon installiert. Im Menü findet ihr sogar zwei Editoren, nämlich IDLE fpr Python 2 und IDLE für Python 3. IDLE steht für Integrated Development and Learning Environment.

Für die Programmierung werden wir IDLE verwenden.

### Windows

Falls ihr zu Hause Python ausprobieren wollt, könnt ihr Python auch für Windows installieren. Den offiziellen Download gibt es auf [python.org](https://www.python.org/downloads/). Wir verwenden Python 3, d.h. ihr müsst Python 3.6.0 herunterladen und installieren.

Es gibt jedoch auch Installtionen, die noch mehr Bibliotheken mitbringen. Eine davon ist [Anaconda](https://www.continuum.io/downloads#windows). Allerdings ist der Download mit über 400 MB auch etwas größer und auf der Festplatte braucht es fast 2 GB.

## Entwicklungsumgebung

Um ein Programm zu schreiben braucht man einen Editor. Ein ganz normaler Texteditor wie Notepad würde schon genügen. Allerdings ist der Text dort immer schwarz-weiß. Es hat sich herausgestellt, dass eine farbige Hervorhebung praktisch ist. So können Probleme erkannt werden, ohne dass das Programm ausprobiert werden muss.

Um ein Programm von Text in Maschinensprache zu übersetzen braucht man einen Compiler oder Interpreter. Dabei handelt es sich meist um ein Kommandozeilen-Programm, das umständlich zu bedienen ist.

Damit man den Vorteil von "buntem" Text hat und den Compiler oder Interpreter bequem benutzen kann, hat es sich durchgesetzt, dass man zum Programmieren eine Entwicklungsumgebung verwendet. Im Fachjargon nennt sich das IDE und steht für Integrated Development Environment.

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

Python verwendet eine Anweisung pro Zeile. Andere Sprachen trennen Anweisungen mit einem Strichpunkt (;) und ein Umbruch ist nur empfohlen.

Die Einrückung ist bei Python wichtig. Bei anderen Programmiersprachen ist die Einrückung oft egal, aber empfohlen.

Variablen existieren ab der ersten Verwendung. Die meisten anderen Programmiersprachen erfordern eine Deklaration von Variablen.

### Kommentare

Kommentare und Anmerkungen werden mit einer Raute (auch "Lattenzaun") eingeleitet. Dies kann z.B. für die Aufgabenbeschreibung bei den Hausaufgaben verwendet werden. Ein Kommentar kann auch hinter einer Anweisung stehen.

Beispiel:
```
# Aufgabe 1: Summe aller Vielfachen von 3 oder 5
# Vielfache von 3 oder 5 sind 3, 5, 6, 9, 10, 12, 15, ... 
# Addiere all diese Zahlen solange sie kleiner als 1000 sind.
```

### Rechnen

Eine Variable existiert ab ihrer ersten Zuweisung. Die Zuweisung eines Werts erfolgt mit einem Gleichheitszeichen (=). Die mathematischen Operationen +, -, \* und / funktionieren wie aus der Mathematik bekannt unter Berücksichtigung der Regel "Punkt vor Strich".

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
- Ganzzahl Division mit **//**, z.B. 5//2 = 2
- Rest (Modulo) mit **%**, z.B. 5%2 = 1
- Potenz mit \*\*, z.B. 2\*\*3 = 2³ = 8
- Klammern mit **(** und **)**, z.B. (3+1)*2 = 8

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

Bei anderen Rechenoperationen geht das auch (z.B. **\*\*=**, **%=** oder **//=**), wird dort aber seltener angewandt.

### Text

Text (auch "Zeichenketten" oder "Strings" genannt) kann bei Python in Anführungszeichen (") (engl. "quotation marks" oder "double quotes") oder in Hochkomma (') (engl. "apostrophe") geschrieben werden.

Beispiel:
```
print("Hello world.")
print('Hello world.')
```

Wenn das einleitende Zeichen im Text selbst vorkommen soll, muss es dem Interpreter entrinnen (engl. "escape"). Dies geschieht durch einen umgekehrten Schrägstrich (engl. "backslash").

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
- **\n** für einen Zeilenumbruch (neue Zeile, line feed, LF)
- **\\\\** für einen Backslash
- **\"** für ein Anführungszeichen
- **\'** für einen Apostroph
- **\xhh** für ein Sonderzeichen aus der Sonderzeichentabelle (wobei hh durch eine hexadezimale Zahl ersetzt wird)

Ansonsten lassen sich dank UTF-8 Sonderzeichen auch direkt in das Programm einfügen:

```
print("Zeile 1\nZeile 2")
print("∞♫")
```

Python kann auch mit Text "rechnen", z.B. kann eine Variable Text enthalten. Texte können mit Plus (+) aneinandergehängt werden. Witzig: auch multiplizieren klappt mit Mal (\*). Probier es mal aus:

```
omg = "OMG"
print(omg + "Wow")
print(omg * 5)
```

Wie eine Zeitung mit einer Schere lässt sich Text in Python auch zerschnipseln (engl. "slice") mit eckigen Klammern und Angabe einer Position an der begonnen bzw. aufgehört werden soll zu schneiden. Achtung: die Zählung startet für einen Computer bei 0.

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
- Text in Ganzzahl mit **int(...)**
- Text in Kommazahl mit **float(...)**
- Zahl in Text mit **str(...)**

```
zahl = int("5")
kommazahl = float("5.1")
text = str(zahl)
print(zahl, text, kommazahl)
```