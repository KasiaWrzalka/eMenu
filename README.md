# eMenu - restauracyjna karta menu online.

Projekt opiera się na dwóch modelach: Cards (Karta - Menu) i CardsItem (Danie - Pozycja menu). Każda karta może zawierać dowolną liczbę dań. Każde z dań może być przypisane do wielu kart. Relacja ManyToMany - wiele do wielu. <br />
Projekt zawiera panel do zarządzania treścią serwisu Django Admin. Wykorzystany został relacyjny silnik bazodanowy PostgreSQL. <br />
Projekt składa się z 3 widoków: 
1. Hello world. 
2. Lista kart - paginacja, sortowanie wykonane asynchronicznie za pomocją Django Rest Framework oraz JavaScript.
3. Szczegóły karty - lista dań.
##Użyte technologie:
* Python 3.6
* Django 2.1
* PostgreSQL 9.5.14
* JavaScript
* Django Rest Framework 3.8.2
## Instalacja projektu
Zalecam posiadać na komputerze takie same wersje użytych technologi. <br />
Stwórz virtualenva wirtualne środowisko. <br />
Wpisz w cmd/terminalu:
```bash
git clone git@github.com:KasiaWrzalka/eMenu.git
```
Wpisz w cmd/terminalu aby zainstalować potrzebne . 
```bash
pip install -r requirements.txt 
```
Stwórz pustą bazę PostgreSQL. <br />
Zaimportuj bazę:
```bash
psql empty_database < backup.bak
```
Zaktualizuj settings.by DATABASES. By wykonać migrację wpisz:
```bash
python manage.py migrate
```
Wpisz polecenie aby uruchomić serwer
```bash
python manage.py runserver
```
Projekt powinien być dostępny pod **127.0.0.1:8000**.


