## Einrichtung einer Remotedesktopverbindung von Windows zu RasPi

Voraussetzungen:

	Raspi mit SSH-Zugriff
	Windows mit Remotedesktopverbindung

Zuerst muss über die „raspi-config“ festgelegt werden, dass Raspbian in die eingeloggte, graphische Benutzeroberfläche bootet.

Außerdem muss für Raspbian-Pixel zunächst der RealVNC-Server deinstalliert werden:

	$ sudo apt-get purge realvnc-vnc-server
	
Dann kann xrdp installiert werden:

	$ sudo apt-get install xrdp
	
Anschließend muss der RasPi neu gestartet werden.

Mit der eingebauten Windows- Remotedesktopverbindung kann nun auf den Raspberry zugegriffen werden. Der Benutzername und das Passwort entsprechen den default-Login-Daten, sofern diese nicht verändert wurden.
