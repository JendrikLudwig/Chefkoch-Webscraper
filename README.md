
# Chefkoch Webscraper

Dieser Webscraper wurde für ein Projekt im Modul "Fortgeschrittene Programmierung" des Studiengangs "Digital Reality" der HAW Hamburg entwickelt.

Als Codebasis diente das folgende [Repository]("https://github.com/VinzSpring/Chefkoch-API") von [VincSpring]("https://github.com/VinzSpring"). 


## Anpassungen
Der Webscraper wurde auf die spezifischen Anforderungen des Projektes angepasst. Hierzu gehörten unter anderem:

- Aktualisierung der API auf den neusten Stand der Chefkoch Webseite
- Entfernung von unbenutzten Klassen und Funktionen
- Anpassung des Hauptprogrammes auf die benötigten Daten
## Ordnerstruktur

```
Chefkoch-API
|
├── Datenaufbereitung
|   ├── raw/                    # Rohdaten aus dem Webscrapingprozess
|   ├── process_data.ipynb      # Notebook zur aufbereitung der Datein
|   └── export.pkl              # Aufbereiteter Datensatz als Pandas Dataframe
|
└── recipe_aquire 
    ├── chefkoch.py             # Klassendeklarationen zur Datenbeschaffung
    └── main.py                 # Hauptprogramm
```