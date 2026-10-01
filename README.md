# Farebný prach pokoja

**Farebný prach pokoja** je jednoduchá antistresová pomôcka vytvorená v Pythone.
Používateľ pohybom myši kreslí jemnú farebnú stopu, ktorá sa pomaly rozplýva.
Projekt je určený na pokojné sústredenie, oddych a tvorivú relaxáciu.

## Na čo pomôcka slúži

Cieľom aktivity nie je získavať skóre ani súťažiť.
Používateľ si môže vytvárať vlastný pokojný obraz z farebných častíc,
meniť farebnú náladu a popritom počúvať relaxačnú hudbu.

Pomôcka môže slúžiť ako krátka prestávka pri učení, práci s počítačom
alebo ako ukážka tvorivého programovania v rámci CodeWeek aktivity.

## Ovládanie

- **pohyb myši** - vytvára farebnú stopu
- **kliknutie myšou** - vytvorí pokojný výbuch farieb
- **rozbaľovací zoznam Hudba** - výber relaxačnej hudby
- **Stop** - zastaví prehrávanie hudby
- **medzerník** - vyčistí obrazovku
- **R** - zmení farebnú náladu
- **Esc** - ukončí program

## Ako spustiť projekt

1. Stiahni alebo otvor priečinok projektu.
2. Skontroluj, či je v priečinku aj podpriečinok `mp3_hudba`.
3. Spusti súbor:

```bash
python Farebny_prach_pokoja.py
```

Projekt používa knižnicu `tkinter`, ktorá je súčasťou bežnej inštalácie Pythonu.
Na prehrávanie hudby v systéme macOS sa používa príkaz `afplay`.

## Hudba

Hudobné súbory sú uložené v priečinku `mp3_hudba`.
V aplikácii sa zobrazujú jednoducho ako **Hudba 1**, **Hudba 2**, **Hudba 3** atď.

Použitá relaxačná hudba pochádza zo stránky [Pixabay](https://pixabay.com/sk/).
Pri ďalšom zdieľaní projektu je potrebné rešpektovať licenčné podmienky použitých hudobných súborov.

## Autor

Ing. Mária Mrazová

## Poznámka

Projekt je vytvorený ako školská antistresová aktivita.
Kód je písaný jednoducho, aby ho mohli žiaci ďalej upravovať a rozširovať.

## Materiály pre žiakov

- `POSTUP_PRE_ZIAKOV.md` - metodický postup, ako projekt vznikal krok za krokom
- `PROMPTY_PRE_ZIAKOV.md` - návrhy promptov, pomocou ktorých môžu žiaci skladať projekt s podporou AI
