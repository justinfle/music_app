# Musikverwaltung und Algorithmus-Analyse
## 1. Einleitung
Dieses Projekt beschäftigt sich mit der Entwicklung einer textbasierten Musikverwaltungsanwendung, die eine umfangreiche Sammlung von Musiktiteln und Playlists ermöglicht. Der Fokus des Projekts liegt darauf, verschiedene Such- und Sortieralgorithmen zu implementieren und deren Leistung auf große Datenmengen zu testen. Die Anwendung bietet Funktionen zum Erstellen, Verwalten und Durchsuchen von Songs und Playlists sowie zur Analyse der Effizienz von Algorithmen. Die gesamte Benutzeroberfläche basiert auf einer textbasierten Menüführung, die für verschiedene Operationen der Musikverwaltung verwendet wird.

## 2. Konzept und Vorgehensweise
### Das Projekt besteht aus zwei Hauptkomponenten:

CSV-Datei mit Musiktiteln: Es wurde eine CSV-Datei (charts_renew_large.csv) erstellt, die 100.000 vollständig einzigartige Songtitel enthält. Diese Datei stellt die Grundlage der Musiksammlung dar. Jeder Songtitel hat individuelle Eigenschaften wie Name, Künstler, Album, Genre und Dauer. Diese Datei wurde speziell erstellt, um keine Dopplungen in den Songnamen zu enthalten.

Python-Code zur Verwaltung und Analyse: Der Hauptcode der Anwendung ist in Python geschrieben und enthält Klassen und Methoden für das Laden, Speichern und Verwalten der Musiktitel sowie für die Durchführung von Sortier- und Suchoperationen. Die Anwendung wird beim Starten der Datei music_app.py ausgeführt und lädt die Musiktitel aus der CSV-Datei in eine interne Datenstruktur. Anschließend bietet das Programm eine textbasierte Menüführung, um die verschiedenen Funktionen aufzurufen.

### Die Vorgehensweise gliedert sich wie folgt:

Die Erstellung der CSV-Datei umfasst die Generierung von 100.000 einzigartigen Songtiteln durch eine speziell entwickelte Python-Funktion. Diese Funktion kombiniert zufällig ausgewählte Wörter, um individuelle Songnamen zu generieren und prüft dabei, dass keine Dopplungen in den Namen auftreten. Dadurch wird sichergestellt, dass jeder Songtitel in der Musiksammlung vollständig einzigartig ist.

Die Implementierung des Codes erfolgt durch die Definition mehrerer Klassen, darunter Song, Playlist und MusicApp. Jede dieser Klassen besitzt spezifische Methoden, um die Daten zu verwalten. Die Song-Klasse repräsentiert einen einzelnen Musiktitel, während die Playlist-Klasse Sammlungen von Songs speichert und verwaltet. Die Hauptklasse MusicApp koordiniert alle Interaktionen und Funktionalitäten der Anwendung, wie das Laden und Speichern von Daten, das Erstellen von Playlists und die Implementierung von Sortier- und Suchalgorithmen.

Die Einbindung der Sortier- und Suchalgorithmen erfolgt durch die Integration verschiedener Algorithmen, die speziell für die Verwaltung der Musiksammlung optimiert wurden. Es wurden Algorithmen wie Quicksort, Mergesort und Blocksort zur Sortierung, sowie lineare und binäre Suche für das effiziente Durchsuchen der Musiksammlung implementiert.

Zur abschließenden Leistungsbewertung wurden detaillierte Laufzeitmessungen für jeden implementierten Algorithmus durchgeführt. Diese Messungen ermöglichen es, die Effizienz der einzelnen Verfahren auf großen Datenmengen zu analysieren und zu vergleichen, wodurch klar wird, welche Algorithmen in verschiedenen Anwendungsfällen die besten Ergebnisse erzielen.


## 3. Architektur und Nutzerführung
Der Code der Anwendung ist modular aufgebaut und besteht aus drei Hauptklassen, die jeweils unterschiedliche Funktionalitäten abdecken und die Struktur der Anwendung klar voneinander trennen:

- Song: Diese Klasse repräsentiert die grundlegende Einheit der Musiksammlung – einen einzelnen Musiktitel. Jeder Song ist durch die Attribute name, artist, album, genre und duration charakterisiert. Die Song-Klasse dient dazu, die wesentlichen Informationen über jeden Titel strukturiert zu speichern und darzustellen. Diese Attribute sind entscheidend für die spätere Verwaltung, Suche und Sortierung der Titel.

- Playlist: Diese Klasse ist dafür zuständig, Sammlungen von Song-Objekten zu organisieren. Jede Playlist hat einen eindeutigen Namen und kann beliebig viele Songs enthalten. Die Playlist-Klasse bietet Methoden, um Songs zur Playlist hinzuzufügen oder daraus zu entfernen. Sie ermöglicht außerdem das Umbenennen der Playlists. Dadurch wird es einfach, benutzerdefinierte Gruppen von Songs zu erstellen und zu pflegen, was eine bessere Verwaltung und Strukturierung der Musiksammlung ermöglicht.

- MusicApp: Die MusicApp-Klasse ist das zentrale Steuerelement der Anwendung, das alle Funktionalitäten koordiniert und die Hauptlogik der Software implementiert. Sie ist für das Laden und Speichern der Daten aus und in die CSV-Datei zuständig, verwaltet Playlists und integriert die verschiedenen Sortier- und Suchalgorithmen. Zusätzlich stellt die MusicApp-Klasse die Benutzeroberfläche bereit und bietet alle Funktionen der Anwendung über ein interaktives Menü an. Dies erleichtert die Interaktion mit der Anwendung und sorgt für eine klare Trennung zwischen der Datenverarbeitung und der Benutzerinteraktion.

### Nutzerführung
Die gesamte Benutzerinteraktion erfolgt über eine textbasierte Konsole, in der der Benutzer durch Eingabe von numerischen Menüoptionen navigieren kann. Beim Start der Anwendung wird ein Hauptmenü angezeigt, das die verschiedenen Funktionen der Anwendung übersichtlich präsentiert. Jede Option des Menüs führt den Benutzer zu einer spezifischen Funktionalität, die in einem separaten Untermenü ausgeführt wird. Dabei sind alle Eingabemöglichkeiten mit einer kurzen Beschreibung versehen, um den Nutzer intuitiv durch die verschiedenen Schritte zu leiten.

Das Hauptmenü bietet die folgenden Optionen:

- Add New Song: Diese Option ermöglicht es dem Benutzer, einen neuen Song zur bestehenden Musiksammlung hinzuzufügen. Der Benutzer wird dabei durch eine Reihe von Eingabeaufforderungen geführt, bei denen die Details des neuen Songs abgefragt werden. Dies umfasst den Songtitel, den Namen des Interpreten, das Album, das Genre und die Länge des Titels.

- Create Playlist: Mit dieser Funktion kann der Benutzer eine neue Playlist erstellen. Hierzu gibt der Benutzer einen Namen für die Playlist ein. Die neu erstellte Playlist kann anschließend bearbeitet und verwaltet werden, indem Songs hinzugefügt oder entfernt werden.

- Add Song to Playlist: Diese Option ermöglicht es, einen bestehenden Song aus der Musiksammlung zu einer bereits vorhandenen Playlist hinzuzufügen. Der Benutzer muss den Namen der Playlist und den Titel des hinzuzufügenden Songs eingeben. Sollte der eingegebene Titel oder die Playlist nicht existieren, wird eine Fehlermeldung ausgegeben.

- Search Songs: Mit dieser Option kann der Benutzer die Musiksammlung durchsuchen, indem er einen Suchbegriff eingibt. Die Suche berücksichtigt sowohl den Songtitel als auch den Künstlernamen. Alle übereinstimmenden Titel werden anschließend in der Konsole angezeigt.

- Advanced Search with Time Measurement: Diese Funktion bietet eine erweiterte Suchmöglichkeit, bei der der Benutzer zwischen der linearen und der binären Suche wählen kann. Nach Auswahl des Suchalgorithmus wird die Zeit gemessen, die für die Suche benötigt wird, und das Ergebnis zusammen mit der Laufzeit in der Konsole ausgegeben.

- Sort Songs with Time Measurement: Hier kann der Benutzer zwischen verschiedenen Sortieralgorithmen wählen, um die Musiksammlung neu zu ordnen. Zur Verfügung stehen Quicksort, Mergesort, Bubblesort und Blocksort. Nach der Auswahl wird der ausgewählte Algorithmus auf die gesamte Sammlung angewendet und die Zeit gemessen, die für die Sortierung benötigt wird. Die Laufzeit und das sortierte Ergebnis werden dem Benutzer angezeigt.

- Display All Songs: Diese Option zeigt alle aktuell in der Musiksammlung enthaltenen Songs in der Konsole an. Der Benutzer erhält eine vollständige Liste der Songs mit allen Details wie Titel, Interpret, Album und Genre.

- Display Playlists: Mit dieser Funktion kann der Benutzer alle vorhandenen Playlists anzeigen. Jede Playlist wird mit ihrem Namen und einer Liste der darin enthaltenen Songs dargestellt. Diese Ansicht bietet dem Benutzer eine schnelle Übersicht über die Struktur und den Inhalt der Playlists.

- Exit: Beendet die Anwendung und speichert automatisch alle Änderungen an der Musiksammlung und den Playlists. Der Benutzer wird darüber informiert, dass die Daten erfolgreich gespeichert wurden, bevor das Programm geschlossen wird.

Die Menüführung ist bewusst einfach und benutzerfreundlich gestaltet, um eine schnelle und intuitive Navigation zwischen den verschiedenen Funktionen zu ermöglichen. Nach jeder durchgeführten Aktion erhält der Benutzer eine Bestätigung, damit er stets den aktuellen Zustand der Daten nachvollziehen kann. Fehlerhafte Eingaben werden durch entsprechende Fehlermeldungen abgefangen, sodass der Benutzer problemlos zu einem vorherigen Menü zurückkehren kann, um seine Eingabe zu korrigieren.

Durch diese klare Struktur und die durchdachte Navigation bietet die Anwendung eine hohe Benutzerfreundlichkeit, selbst bei großen Datenmengen. Die textbasierte Benutzeroberfläche ist einfach gehalten, sorgt aber dennoch für eine reibungslose Interaktion und einen klaren Überblick über die gesamte Musiksammlung und die Playlists.

## 4. Implementierte Such- und Sortieralgorithmen
### Sortieralgorithmen
1. Quicksort: Quicksort ist ein sehr effizienter und weit verbreiteter Sortieralgorithmus, der eine durchschnittliche Laufzeit von 𝑂(𝑛log⁡𝑛) besitzt. Der Algorithmus folgt dem Prinzip des Teile-und-Herrsche-Ansatzes, bei dem die zu sortierende Liste rekursiv in kleinere Teile zerlegt wird. Zunächst wird ein sogenanntes Pivot-Element aus der Liste gewählt, das als Referenzpunkt dient. Alle Elemente, die kleiner als das Pivot-Element sind, werden in eine Teilliste links vom Pivot und alle größeren Elemente in eine Teilliste rechts vom Pivot verschoben. Danach wird dieser Vorgang rekursiv auf beide Teillisten angewendet, bis die gesamte Liste sortiert ist. Da der Algorithmus nur sehr wenig zusätzlichen Speicher benötigt und im Allgemeinen sehr schnell ist, wird Quicksort häufig als einer der effizientesten Sortieralgorithmen betrachtet. In bestimmten Fällen, z.B. wenn das Pivot-Element schlecht gewählt wird, kann die Laufzeit im Worst-Case jedoch auf 𝑂(𝑛2) ansteigen. Durch die richtige Wahl des Pivot-Elements kann dies aber meist vermieden werden.

2. Bubblesort: Bubblesort ist einer der einfachsten Sortieralgorithmen und hat eine Laufzeit von 𝑂(𝑛2), was ihn für größere Datenmengen ineffizient macht. Der Name leitet sich von der Idee ab, dass größere Elemente wie Blasen nach oben aufsteigen. Bei jedem Durchlauf der Liste werden benachbarte Elemente miteinander verglichen und vertauscht, wenn das linke Element größer ist als das rechte. Dadurch wandert das größte Element in jeder Iteration "nach oben" und wird an der richtigen Position abgelegt. Dieser Prozess wird so lange wiederholt, bis keine Vertauschungen mehr notwendig sind. Da jeder Durchlauf maximal ein Element korrekt platziert, benötigt Bubblesort in der Regel viele Iterationen, was bei großen Listen sehr ineffizient ist. Aus diesem Grund wird Bubblesort in der Praxis kaum verwendet und dient häufig nur zu Lehrzwecken, um die Funktionsweise von Sortieralgorithmen zu veranschaulichen.

3. Mergesort: Mergesort ist ein stabiler Sortieralgorithmus, der ebenfalls nach dem Teile-und-Herrsche-Prinzip arbeitet. Er hat eine garantierte Laufzeit von 𝑂(𝑛log𝑛), unabhängig von der ursprünglichen Anordnung der Liste. Der Algorithmus teilt die Liste rekursiv in immer kleinere Teillisten, bis jede Teilliste nur noch ein einziges Element enthält. Danach werden die Teillisten in aufsteigender Reihenfolge wieder zusammengeführt (Merge-Phase), wobei jedes Element nacheinander in die richtige Reihenfolge gebracht wird. Mergesort ist besonders vorteilhaft, wenn Stabilität eine wichtige Rolle spielt, d.h. wenn gleiche Elemente in ihrer Reihenfolge erhalten bleiben sollen. Im Gegensatz zu Quicksort benötigt Mergesort jedoch zusätzlichen Speicher, um die Teillisten während der Zusammenführung zu speichern, was ihn für speicherintensive Anwendungen weniger geeignet macht.

4. Blocksort: Blocksort ist ein auf die Blockweise aufgeteiltes Verfahren, das besonders dann effizient ist, wenn die Liste in größere Blöcke unterteilt werden kann. Die Idee hinter Blocksort ist, die Liste zunächst in kleinere Blöcke fester Größe zu unterteilen und jeden dieser Blöcke separat zu sortieren. Anschließend werden die sortierten Blöcke durch ein effizientes Merging zusammengeführt. Diese Methode hat eine Laufzeit von 𝑂(𝑛log⁡𝑛), wenn die Blockgröße geeignet gewählt wird. Ein großer Vorteil von Blocksort besteht darin, dass er bei bereits teilweise sortierten Daten sehr schnell arbeiten kann, da nur innerhalb der Blöcke sortiert wird und die vorhandene Ordnung weitgehend erhalten bleibt.

### Suchalgorithmen
1. Lineare Suche: Die lineare Suche ist der einfachste Suchalgorithmus, der eine Laufzeit von 𝑂(𝑛) aufweist. Der Algorithmus durchläuft die Liste von Anfang bis Ende und vergleicht jedes Element mit dem gesuchten Wert. Sobald das gewünschte Element gefunden wird, wird die Suche beendet und das Element zurückgegeben. Falls das gesuchte Element nicht in der Liste vorhanden ist, wird die gesamte Liste einmal durchlaufen. Obwohl die lineare Suche bei kleinen Listen effizient sein kann, ist sie für große Datensätze eher ungeeignet, da die Anzahl der Vergleiche linear zur Listenlänge ansteigt. Daher eignet sich die lineare Suche besonders in Fällen, bei denen die Liste unsortiert ist oder keine zusätzlichen Vorbereitungen (z.B. Sortierung) durchgeführt werden sollen.

2. Binäre Suche (Iterative Version): Die binäre Suche ist ein effizienter Suchalgorithmus mit einer durchschnittlichen Laufzeit von 𝑂(log⁡𝑛), der jedoch nur auf sortierten Listen angewendet werden kann. Der Algorithmus arbeitet nach dem Prinzip des wiederholten Teilens: Er vergleicht das gesuchte Element mit dem mittleren Element der Liste. Ist das gesuchte Element kleiner als das mittlere Element, wird die Suche auf die linke Hälfte der Liste beschränkt; ist es größer, auf die rechte Hälfte. Dieser Vorgang wird solange wiederholt, bis entweder das gesuchte Element gefunden oder die verbleibende Liste leer ist. Da die binäre Suche die Anzahl der zu durchsuchenden Elemente bei jedem Schritt halbiert, wächst die Laufzeit logarithmisch zur Größe der Liste, was sie besonders bei großen sortierten Datenmengen sehr effizient macht. In diesem Projekt wurde die binäre Suche als iterative Version implementiert, um eine zu große Rekursionstiefe zu vermeiden, die bei sehr großen Listen zu Fehlern führen könnte.

## 5. Laufzeitanalyse der Algorithmen
Die Laufzeitanalyse für die Algorithmen wurde unter Verwendung einer großen Sammlung von 100.000 Songs durchgeführt. Die Ergebnisse sind wie folgt:

- Quicksort: 0.3058 Sekunden
- Bubblesort: 1011.8155 Sekunden
- Mergesort: 8.3915 Sekunden
- Blocksort: 0.0891 Sekunden
- Lineare Suche: 0.0257 Sekunden
- Binäre Suche: 1.0579 Sekunden
### Analyse:
Sortieralgorithmen: Quicksort und Blocksort sind deutlich schneller als Bubblesort, was bei großen Datenmengen zu erwarten ist. Mergesort zeigt ebenfalls eine gute Performance, ist aber langsamer als Quicksort aufgrund der zusätzlichen Speicheranforderungen. Bubblesort zeigt eine extrem lange Laufzeit, was seine Verwendung für große Listen unpraktisch macht.
Suchalgorithmen: Die lineare Suche zeigt eine geringere Laufzeit im Vergleich zur binären Suche, weil die Binärsuche zunächst die Liste sortiert, bevor sie die Suche durchführt. Bei einer bereits sortierten Liste wäre die binäre Suche effizienter.

## 6. Zusammenfassung
Dieses Projekt zeigt, wie Such- und Sortieralgorithmen auf eine große Menge an Musiktiteln angewendet werden können, um deren Effizienz und Leistung zu evaluieren. Die Anwendung bietet eine umfassende Verwaltung von Songs und Playlists und ermöglicht es dem Benutzer, die Algorithmen direkt zu testen und zu vergleichen. Die Laufzeitanalyse verdeutlicht die Unterschiede zwischen verschiedenen Algorithmen und zeigt auf, welche Methoden für große Datensätze geeignet sind.

