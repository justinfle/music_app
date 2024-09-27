Musikverwaltung und Algorithmus-Analyse
##1. Einleitung
Dieses Projekt beschäftigt sich mit der Entwicklung einer textbasierten Musikverwaltungsanwendung, die eine umfangreiche Sammlung von Musiktiteln und Playlists ermöglicht. Der Fokus des Projekts liegt darauf, verschiedene Such- und Sortieralgorithmen zu implementieren und deren Leistung auf große Datenmengen zu testen. Die Anwendung bietet Funktionen zum Erstellen, Verwalten und Durchsuchen von Songs und Playlists sowie zur Analyse der Effizienz von Algorithmen. Die gesamte Benutzeroberfläche basiert auf einer textbasierten Menüführung, die für verschiedene Operationen der Musikverwaltung verwendet wird.

##2. Konzept und Vorgehensweise
Das Projekt besteht aus zwei Hauptkomponenten:

CSV-Datei mit Musiktiteln: Es wurde eine CSV-Datei (charts_renew_large.csv) erstellt, die 100.000 vollständig einzigartige Songtitel enthält. Diese Datei stellt die Grundlage der Musiksammlung dar. Jeder Songtitel hat individuelle Eigenschaften wie Name, Künstler, Album, Genre und Dauer. Diese Datei wurde speziell erstellt, um keine Dopplungen in den Songnamen zu enthalten.

Python-Code zur Verwaltung und Analyse: Der Hauptcode der Anwendung ist in Python geschrieben und enthält Klassen und Methoden für das Laden, Speichern und Verwalten der Musiktitel sowie für die Durchführung von Sortier- und Suchoperationen. Die Anwendung wird beim Starten der Datei music_app.py ausgeführt und lädt die Musiktitel aus der CSV-Datei in eine interne Datenstruktur. Anschließend bietet das Programm eine textbasierte Menüführung, um die verschiedenen Funktionen aufzurufen.

Die Vorgehensweise gliedert sich wie folgt:

Die Erstellung der CSV-Datei umfasst die Generierung von 100.000 einzigartigen Songtiteln durch eine speziell entwickelte Python-Funktion. Diese Funktion kombiniert zufällig ausgewählte Wörter, um individuelle Songnamen zu generieren und prüft dabei, dass keine Dopplungen in den Namen auftreten. Dadurch wird sichergestellt, dass jeder Songtitel in der Musiksammlung vollständig einzigartig ist.

Die Implementierung des Codes erfolgt durch die Definition mehrerer Klassen, darunter Song, Playlist und MusicApp. Jede dieser Klassen besitzt spezifische Methoden, um die Daten zu verwalten. Die Song-Klasse repräsentiert einen einzelnen Musiktitel, während die Playlist-Klasse Sammlungen von Songs speichert und verwaltet. Die Hauptklasse MusicApp koordiniert alle Interaktionen und Funktionalitäten der Anwendung, wie das Laden und Speichern von Daten, das Erstellen von Playlists und die Implementierung von Sortier- und Suchalgorithmen.

Die Einbindung der Sortier- und Suchalgorithmen erfolgt durch die Integration verschiedener Algorithmen, die speziell für die Verwaltung der Musiksammlung optimiert wurden. Es wurden Algorithmen wie Quicksort, Mergesort und Blocksort zur Sortierung, sowie lineare und binäre Suche für das effiziente Durchsuchen der Musiksammlung implementiert.

Zur abschließenden Leistungsbewertung wurden detaillierte Laufzeitmessungen für jeden implementierten Algorithmus durchgeführt. Diese Messungen ermöglichen es, die Effizienz der einzelnen Verfahren auf großen Datenmengen zu analysieren und zu vergleichen, wodurch klar wird, welche Algorithmen in verschiedenen Anwendungsfällen die besten Ergebnisse erzielen.

##3. Architektur und Nutzerführung
Der Code ist modular aufgebaut und besteht aus den folgenden Hauptklassen:

Song: Repräsentiert einen einzelnen Musiktitel mit den Attributen name, artist, album, genre und duration.
Playlist: Verwaltet eine Sammlung von Songs unter einem bestimmten Playlist-Namen.
MusicApp: Die Hauptklasse, die alle Funktionalitäten der Anwendung koordiniert, darunter das Laden von Songs aus der CSV-Datei, das Verwalten von Playlists und die Implementierung der Sortier- und Suchalgorithmen.
Nutzerführung
Die Benutzeroberfläche ist eine textbasierte Konsole, in der der Benutzer durch Eingabe von Menüoptionen navigiert. Das Hauptmenü bietet die folgenden Optionen:

Add New Song: Fügt einen neuen Song zur Musiksammlung hinzu.
Create Playlist: Erstellt eine neue Playlist.
Add Song to Playlist: Fügt einen bestehenden Song zu einer Playlist hinzu.
Search Songs: Durchsucht die Songsammlung basierend auf einem Suchbegriff.
Advanced Search with Time Measurement: Führt eine erweiterte Suche durch und misst die Zeit für die lineare oder binäre Suche.
Sort Songs with Time Measurement: Sortiert die Songsammlung und misst die Zeit für verschiedene Sortieralgorithmen.
Display All Songs: Zeigt alle Songs in der Sammlung an.
Display Playlists: Zeigt alle vorhandenen Playlists an.
Exit: Beendet die Anwendung und speichert die Daten.
Die Menüführung ist einfach und benutzerfreundlich gestaltet, um eine schnelle Navigation zwischen den Optionen zu ermöglichen. Der Benutzer erhält nach jeder Aktion eine Bestätigung und kann so den aktuellen Zustand der Daten leicht nachvollziehen.

##4. Implementierte Such- und Sortieralgorithmen
Sortieralgorithmen:
Quicksort: Ein effizienter Sortieralgorithmus mit einer durchschnittlichen Laufzeit von O(n log n). Er wählt ein Pivot-Element und teilt die Liste rekursiv in kleinere Teillisten auf.
Bubblesort: Ein einfacher, aber ineffizienter Algorithmus mit einer Laufzeit von O(n²). Er vertauscht benachbarte Elemente, bis die gesamte Liste sortiert ist.
Mergesort: Ein stabiler Sortieralgorithmus mit einer garantierten Laufzeit von O(n log n). Er teilt die Liste rekursiv und fügt die Teillisten wieder zusammen.
Blocksort: Sortiert die Liste in Blöcken und hat eine Laufzeit von O(n log n) bei geeigneter Blockgröße.
Suchalgorithmen:
Lineare Suche: Durchläuft die gesamte Liste, um das gewünschte Element zu finden. Die Laufzeit beträgt im Durchschnitt O(n).
Binäre Suche (Iterative Version): Durchsucht eine sortierte Liste effizient durch wiederholte Teilung der Liste in zwei Hälften. Die Laufzeit beträgt O(log n).

##5. Laufzeitanalyse der Algorithmen
Die Laufzeitanalyse für die Algorithmen wurde unter Verwendung einer großen Sammlung von 100.000 Songs durchgeführt. Die Ergebnisse sind wie folgt:

Quicksort: 0.3058 Sekunden
Bubblesort: 1011.8155 Sekunden
Mergesort: 8.3915 Sekunden
Blocksort: 0.0891 Sekunden
Lineare Suche: 0.0257 Sekunden
Binäre Suche: 1.0579 Sekunden
Analyse:
Sortieralgorithmen: Quicksort und Blocksort sind deutlich schneller als Bubblesort, was bei großen Datenmengen zu erwarten ist. Mergesort zeigt ebenfalls eine gute Performance, ist aber langsamer als Quicksort aufgrund der zusätzlichen Speicheranforderungen. Bubblesort zeigt eine extrem lange Laufzeit, was seine Verwendung für große Listen unpraktisch macht.
Suchalgorithmen: Die lineare Suche zeigt eine geringere Laufzeit im Vergleich zur binären Suche, weil die Binärsuche zunächst die Liste sortiert, bevor sie die Suche durchführt. Bei einer bereits sortierten Liste wäre die binäre Suche effizienter.

##6. Zusammenfassung
Dieses Projekt zeigt, wie Such- und Sortieralgorithmen auf eine große Menge an Musiktiteln angewendet werden können, um deren Effizienz und Leistung zu evaluieren. Die Anwendung bietet eine umfassende Verwaltung von Songs und Playlists und ermöglicht es dem Benutzer, die Algorithmen direkt zu testen und zu vergleichen. Die Laufzeitanalyse verdeutlicht die Unterschiede zwischen verschiedenen Algorithmen und zeigt auf, welche Methoden für große Datensätze geeignet sind.

