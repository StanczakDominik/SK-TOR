# SK-TOR
Projekt na Sieci Komputerowe: prosta implementacja komunikatora opartego o koncept  sieci TOR bez enkrypcji w Pythonie 3.

Wykorzystuje protokół UDP poprzez niskopoziomową bibliotekę `socket` z biblioteki standardowej.

### Wymagania
* `Python 3` (polecamy: [dystrybucja Anaconda](https://www.continuum.io/downloads)).
* `bash`

### Instrukcja obsługi, z konsoli:
1. W `data.py` wpisz numery i adres IP + porty *node'ów*, które mają pośredniczyć w
przesyłaniu wiadomości.
2. Uruchom na każdym *node* `node.py` poprzez `python node.py 0`, gdzie `0` to numer *node*.
3. Uruchom klienta poprzez `python client.py`
4. Podaj nazwę użytkownika, nazwę odbiorcy, wiadomość

Mikołaj Synowiec, Dominik Stańczak
