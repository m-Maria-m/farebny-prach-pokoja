# Postup pre žiakov: Farebný prach pokoja

## Názov aktivity

**Farebný prach pokoja**

## Cieľ aktivity

Cieľom je vytvoriť jednoduchú antistresovú pomôcku v Pythone.
Používateľ pohybuje myšou po obrazovke a za kurzorom vzniká jemná farebná stopa.
Tá sa postupne rozplýva, takže program pôsobí pokojne a relaxačne.

Aktivita nie je súťažná. Nemá skóre ani časový limit.
Zmyslom je tvorivé programovanie, oddych a uvedomenie si, že programovanie môže slúžiť aj na vytváranie pomôcok pre pohodu.

## Čo budeme vytvárať

Vytvoríme aplikáciu, ktorá bude obsahovať:

- tmavé pokojné pozadie,
- farebné častice, ktoré sa tvoria pri pohybe myši,
- jemnú stopu za pohybom myši,
- výbuch farebných častíc po kliknutí,
- možnosť meniť farebnú náladu,
- tlačidlo na vyčistenie obrazovky,
- výber relaxačnej hudby.

## Pomôcky a nástroje

Budeme potrebovať:

- Python,
- vývojové prostredie PyCharm alebo iný editor,
- knižnicu `tkinter`, ktorá je súčasťou Pythonu,
- priečinok s relaxačnou hudbou vo formáte MP3.

## 1. krok: Premyslenie nápadu

Najprv si so žiakmi položme otázky:

- Čo môže človeku pomôcť upokojiť sa?
- Musí mať každá hra víťaza a porazeného?
- Ako môže pohyb myši pôsobiť relaxačne?
- Aké farby pôsobia pokojne?
- Aký zvuk alebo hudba môže podporiť relaxáciu?

Žiaci by mali pochopiť, že cieľom nie je rýchlosť ani výkon, ale pokojné tvorenie.

## 2. krok: Vytvorenie okna programu

V Pythone vytvoríme hlavné okno pomocou knižnice `tkinter`.
Do okna vložíme plátno `Canvas`, na ktoré budeme kresliť častice.

V tejto fáze ešte nič nelieta ani sa nehýbe.
Cieľom je len vytvoriť prázdne okno programu.

Žiaci si môžu vyskúšať:

- zmeniť názov okna,
- zmeniť veľkosť okna,
- nastaviť tmavú farbu pozadia.

## 3. krok: Kreslenie pozadia

Na plátno pridáme pokojné tmavé pozadie.
Môžeme použiť viac vrstiev farieb, napríklad tmavé pásy alebo jemné kruhy.

Cieľom je, aby obrazovka nepôsobila prázdne, ale zároveň nebola rušivá.

Otázky pre žiakov:

- Aké farby by ste použili na pokojné pozadie?
- Čo pôsobí rušivo?
- Má byť pozadie výrazné alebo jemné?

## 4. krok: Vytvorenie jednej častice

Vytvoríme objekt častice.
Každá častica bude mať:

- polohu `x` a `y`,
- smer pohybu,
- rýchlosť,
- farbu,
- veľkosť,
- životnosť.

Častica sa po čase stratí.
Vďaka tomu sa obrazovka nebude donekonečna zapĺňať.

Toto je dobrý moment na vysvetlenie, čo je objekt a prečo je výhodné mať časticu ako samostatnú triedu.

## 5. krok: Pohyb myši vytvára farebný prach

Program bude sledovať pohyb myši.
Keď sa myš pohne, vytvorí sa niekoľko farebných častíc.

Čím rýchlejšie sa myš pohne, tým viac častíc môže vzniknúť.
Pri pomalom pohybe vzniká jemná stopa.

Žiaci môžu skúšať:

- zmeniť počet častíc,
- zmeniť veľkosť častíc,
- zmeniť rýchlosť miznutia,
- zmeniť farby.

## 6. krok: Kliknutie vytvorí pokojný výbuch

Po kliknutí myšou sa na danom mieste vytvorí viac častíc naraz.
Nevnímame to ako výbuch v akčnej hre, ale ako jemné rozprášenie farieb.

Žiaci môžu upraviť:

- koľko častíc vznikne po kliknutí,
- ako ďaleko sa rozletia,
- aké budú mať farby.

## 7. krok: Farebné nálady

Do programu pridáme viac farebných režimov.
Napríklad:

- dúhový prúd,
- lesný pokoj,
- večerná obloha,
- teplé svetlo,
- mäta a voda.

Klávesom **R** bude možné meniť farebnú náladu.

Otázka pre žiakov:

- Aký názov by ste dali vlastnej farebnej nálade?

## 8. krok: Vyčistenie obrazovky

Klávesom **medzerník** vyčistíme obrazovku.
Program odstráni všetky častice a stopu.

Tento krok je dôležitý, aby používateľ mohol začať nový pokojný obraz.

## 9. krok: Ukončenie programu

Klávesom **Esc** sa program ukončí.
Pri ukončení treba zastaviť aj hudbu, ak práve hrá.

Žiakom môžeme vysvetliť, že program má myslieť aj na upratanie po sebe.

## 10. krok: Pridanie hudby

V projekte vytvoríme priečinok:

```text
mp3_hudba
```

Do neho vložíme MP3 súbory s relaxačnou hudbou.

V aplikácii sa hudba nezobrazuje podľa dlhých názvov súborov.
Zobrazí sa jednoducho ako:

```text
Hudba 1
Hudba 2
Hudba 3
```

Používateľ si vyberie skladbu z rozbaľovacieho zoznamu.
Tlačidlo **Stop** hudbu zastaví.

## 11. krok: Doladenie vzhľadu

Na konci upravíme rozhranie tak, aby bolo jednoduché a nerušivé.

Pri našej aktivite sme postupne upravili:

- aby výber hudby neprekrýval text,
- aby tlačidlo Stop bolo dobre viditeľné,
- aby rozhranie neobsahovalo zbytočné rámy,
- aby hudobný panel nezavadzal pri kreslení.

Toto je dôležitá časť programovania.
Program často nevznikne dokonale na prvý pokus.
Najprv funguje, potom ho postupne zlepšujeme.

## 12. krok: Testovanie

Žiaci by mali program vyskúšať:

- pohybovať myšou pomaly,
- pohybovať myšou rýchlo,
- kliknúť na rôzne miesta,
- zmeniť náladu klávesom R,
- vyčistiť obrazovku medzerníkom,
- vybrať hudbu,
- zastaviť hudbu,
- ukončiť program klávesom Esc.

Pri testovaní si zapisujú, čo by ešte zlepšili.

## 13. krok: Možné rozšírenia

Žiaci môžu doplniť napríklad:

- vlastné farebné nálady,
- nové tvary častíc,
- svetlejšie alebo prírodné pozadie,
- tlačidlo na uloženie obrázka,
- vlastné relaxačné zvuky,
- režim bez hudby,
- krátku úvodnú obrazovku s návodom.

## 14. krok: Zverejnenie projektu

Projekt môžeme nahrať na GitHub.
Do repozitára patria:

```text
Farebny_prach_pokoja.py
README.md
.gitignore
mp3_hudba/
```

Do repozitára nepatria:

```text
.venv/
.idea/
__pycache__/
.DS_Store
```

README súbor má vysvetliť:

- čo projekt robí,
- ako sa ovláda,
- ako sa spúšťa,
- odkiaľ pochádza hudba,
- kto je autor.

## Záver pre žiakov

Táto aktivita ukazuje, že programovanie nemusí byť iba o výpočtoch, hrách alebo súťažení.
Pomocou programu môžeme vytvoriť aj digitálnu pomôcku, ktorá pomáha spomaliť, sústrediť sa a oddýchnuť si.

Najdôležitejší nie je zložitý kód, ale dobrý nápad, citlivé spracovanie a ochota program postupne vylepšovať.
