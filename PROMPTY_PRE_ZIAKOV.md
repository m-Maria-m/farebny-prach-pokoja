# Promptovací postup pre žiakov

## Ako používať AI pri tvorbe projektu

Pri tejto aktivite môžete použiť AI ako pomocníka pri programovaní.
AI však nemá iba napísať celý projekt naraz.
Lepšie je pýtať si projekt po menších krokoch, skúšať ho spustiť, kontrolovať chyby a postupne ho vylepšovať.

Úlohou žiaka je:

- premyslieť nápad,
- napísať dobrý prompt,
- spustiť a otestovať kód,
- všimnúť si, čo nefunguje alebo čo sa mu nepáči,
- požiadať AI o konkrétnu úpravu,
- rozumieť hlavným častiam programu.

## Pravidlá dobrého promptu

Dobrý prompt by mal obsahovať:

- čo chceme vytvoriť,
- v akom jazyku to má byť,
- pre koho je projekt určený,
- aké funkcie má mať,
- ako má vyzerať,
- čo má byť jednoduché a zrozumiteľné,
- čo sa má v kóde okomentovať.

Príklad slabého promptu:

```text
Urob mi antistresový program.
```

Lepší prompt:

```text
Vytvor jednoduchý antistresový program v Pythone pomocou tkinter.
Program má zobraziť tmavé pokojné okno, v ktorom sa pri pohybe myši tvoria farebné častice.
Kód má byť jednoduchý a okomentovaný po slovensky, aby mu rozumeli žiaci strednej školy.
```

## Postup skladania projektu pomocou promptov

## 1. prompt: Nápad a cieľ projektu

```text
Navrhni jednoduchú antistresovú aktivitu v Pythone pre žiakov strednej školy.
Aktivita nemá byť súťažná, nemá mať skóre ani časový tlak.
Má slúžiť na oddych, pokojné sústredenie a tvorivé programovanie.
Navrhni názov, cieľ aktivity, ovládanie a hlavné funkcie.
```

Po tomto prompte si žiak vyberie, čo sa mu páči.
Nemusí prijať prvý návrh AI.

## 2. prompt: Základné okno

```text
Vytvor základný Python program pomocou tkinter.
Program má otvoriť okno s názvom "Farebný prach pokoja".
Okno má mať veľkosť približne 980 x 640 pixelov.
V okne má byť Canvas s tmavým pokojným pozadím.
Kód okomentuj po slovensky.
```

Žiak program spustí a skontroluje:

- otvorilo sa okno?
- má správny názov?
- je pozadie príjemné?

## 3. prompt: Farebné častice

```text
Doplň do programu triedu Castica.
Každá častica má mať polohu, smer pohybu, rýchlosť, farbu, veľkosť a životnosť.
Častica sa má pri každom obnovení obrazovky trochu posunúť a postupne zmiznúť.
Použi jednoduchý kód vhodný pre začiatočníkov a pridaj slovenské komentáre.
```

Žiak sa môže AI opýtať:

```text
Vysvetli mi jednoducho, čo robí trieda Castica.
```

## 4. prompt: Pohyb myši

```text
Doplň do programu sledovanie pohybu myši.
Keď používateľ pohybuje myšou po plátne, za kurzorom sa majú vytvárať farebné častice.
Pri pomalom pohybe má vzniknúť jemná stopa, pri rýchlejšom pohybe viac častíc.
Kód nech zostane jednoduchý a okomentovaný po slovensky.
```

Žiak testuje:

- tvoria sa častice?
- miznú postupne?
- nie je ich príliš veľa?

## 5. prompt: Kliknutie myšou

```text
Doplň reakciu na kliknutie myšou.
Po kliknutí sa má na danom mieste vytvoriť pokojný farebný výbuch častíc.
Nemá to pôsobiť ako akčná hra, ale ako jemné rozprášenie farieb.
```

Možný doplňujúci prompt:

```text
Uprav počet častíc po kliknutí tak, aby efekt nebol príliš silný a nepôsobil rušivo.
```

## 6. prompt: Farebné nálady

```text
Pridaj do programu viac farebných nálad.
Napríklad: dúhový prúd, lesný pokoj, večerná obloha, teplé svetlo, mäta a voda.
Kláves R má prepínať medzi náladami.
Na obrazovke zobraz názov aktuálnej nálady.
```

Žiak si môže vytvoriť vlastné režimy:

```text
Navrhni ďalšie pokojné farebné nálady vhodné pre antistresovú aktivitu.
```

## 7. prompt: Ovládanie klávesmi

```text
Doplň ovládanie klávesmi.
Medzerník má vyčistiť obrazovku.
Kláves R má zmeniť farebnú náladu.
Kláves Esc má ukončiť program.
Na obrazovke zobraz krátky návod na ovládanie.
```

## 8. prompt: Relaxačná hudba

```text
Doplň do programu výber relaxačnej hudby.
Hudobné súbory budú uložené v priečinku mp3_hudba.
V programe sa majú zobrazovať ako Hudba 1, Hudba 2, Hudba 3.
Používateľ si má vedieť vybrať hudbu z rozbaľovacieho zoznamu.
Pridaj aj tlačidlo Stop na zastavenie hudby.
Kód nech je jednoduchý a okomentovaný po slovensky.
```

Ak program nehrá hudbu, žiak môže použiť prompt:

```text
Hudba sa mi nespustí. Skontroluj tento kód a navrhni opravu.
Používam macOS a hudba je v priečinku mp3_hudba.
```

## 9. prompt: Úprava vzhľadu

```text
Uprav rozhranie tak, aby pôsobilo pokojne a moderne.
Výber hudby nemá prekrývať hlavný obraz.
Tlačidlo Stop má byť dobre čitateľné.
Nepoužívaj zbytočné veľké rámy ani rušivé prvky.
```

Toto je dôležitý typ promptu.
Žiak už neopisuje novú funkciu, ale hodnotí vzhľad a žiada úpravu.

## 10. prompt: Vysvetlenie kódu

```text
Vysvetli mi tento program po častiach tak, aby tomu rozumel žiak strednej školy.
Zameraj sa na:
- hlavné okno,
- Canvas,
- triedu Castica,
- pohyb myši,
- častice,
- hudbu,
- klávesové ovládanie.
```

Žiak by nemal odovzdať kód, ktorému vôbec nerozumie.
Mal by vedieť povedať, čo robia hlavné časti programu.

## 11. prompt: Hľadanie chýb

Ak program spadne, treba AI poslať presnú chybu.

Príklad:

```text
Po spustení programu sa zobrazí táto chyba:

SEM VLOŽ CHYBOVÚ HLÁŠKU

Vysvetli, čo chyba znamená, a ukáž opravenú časť kódu.
```

Ak sa niečo zobrazuje škaredo:

```text
Rozbaľovací zoznam sa prekrýva s textom.
Navrhni úpravu rozmiestnenia prvkov tak, aby bol výber hudby menší a neprekážal animácii.
```

## 12. prompt: README

```text
Napíš README.md pre môj Python projekt s názvom Farebný prach pokoja.
README má obsahovať:
- krátky popis projektu,
- na čo antistresová pomôcka slúži,
- ovládanie,
- postup spustenia,
- informáciu o priečinku mp3_hudba,
- kredity k hudbe z Pixabay,
- meno autora.
Text napíš po slovensky.
```

## 13. prompt: Metodický popis aktivity

```text
Napíš metodický postup pre žiakov, ako si môžu postupne vytvoriť projekt Farebný prach pokoja.
Nech to nie je len hotový kód, ale návod, ako projekt skladať po krokoch.
Zahrň premýšľanie nad nápadom, tvorbu okna, častíc, hudby, testovanie a zverejnenie.
```

## 14. prompt: Kontrola pred odovzdaním

```text
Skontroluj, či je môj projekt pripravený na odovzdanie.
Projekt obsahuje Python súbor, priečinok mp3_hudba, README a metodický postup.
Napíš mi kontrolný zoznam, čo mám ešte overiť pred zverejnením.
```

## Čo by žiak mal vedieť na konci vysvetliť

Žiak by mal vedieť povedať:

- aký problém alebo potrebu projekt rieši,
- prečo je aktivita antistresová,
- ako sa projekt ovláda,
- ako vznikajú častice,
- ako sa menia farby,
- ako sa vyberá hudba,
- čo by vedel v projekte ďalej zlepšiť.

## Dôležité upozornenie

AI môže pomôcť s kódom, ale žiak je autorom rozhodnutí.
Mal by vedieť obhájiť:

- prečo si vybral takýto nápad,
- čo v programe upravil,
- čo testoval,
- čo mu nefungovalo,
- ako chybu vyriešil.

Najlepšie projekty nevznikajú jedným promptom.
Vznikajú postupným skúšaním, opravovaním a vylepšovaním.
