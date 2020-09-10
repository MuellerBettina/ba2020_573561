# BlockIt

BlockIt ist ein benutzerfreundliches Zeitmanagementsystem, welches die besten Funktionen eines klassischen Kalenders mit denen einer To-Do-Liste vereint.

> BlockIt - Das Beste von beidem 

### Inhaltsverzeichnis

- [Beschreibung](#Beschreibung)
- [Technologien](#Technologien)
- [Installation](#Installation)

### Beschreibung

Benutzer haben die Möglichkeit ein eigenes Profil zu erstellen. Danach besitzen Sie Ihre persönliche Timeblock-Liste und einen persönlichen Kalender. Die sogenannten Timeblocks besitzen immer eine feste Länge. Sie können direkt im Kalender geplant werden, oder auf der Timeblock-Liste gespeichert werden. 

#### Technologien

Zu den verwendeten Technologien gehören unter anderem:

* Django 2.2.13
* Python
* Javascript
* HTML & CSS
* Bootstrap
* Fontawesome

### Installation

Klonen dieses Projektes

https://github.com/MuellerBettina/ba2020_573561.git

Installation der Voraussetzungen
```
pip install -r requirements.txt
```
Datenbank aktualisieren

```
python manage.py makemigrations
python manage.py migrate
```
Erstellen eines SuperUser

```
python manage.py createsuperuser
```

