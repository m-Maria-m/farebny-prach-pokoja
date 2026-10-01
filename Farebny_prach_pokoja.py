"""
Farebný prach pokoja

Antistresová aktivita v Pythone.
Pohybom myši vzniká jemný farebný prach, ktorý sa pomaly rozplýva.

Ovládanie:
- pohyb myši: kreslí farebnú stopu
- kliknutie: pokojný výbuch farieb
- medzerník: vyčistí obrazovku
- R: zmení farebnú náladu
- Esc: ukončí program
"""

import colorsys
import math
import random
import subprocess
import tkinter as tk
from tkinter import ttk
from pathlib import Path


SIRKA = 980
VYSKA = 640
FPS = 30
MAX_CASTIC = 2400


NALADY = [
    ("dúhový prúd", 0.00, 1.0),
    ("lesný pokoj", 0.28, 0.28),
    ("večerná obloha", 0.62, 0.24),
    ("teplé svetlo", 0.08, 0.18),
    ("mäta a voda", 0.46, 0.20),
]


def nahodne(minimum, maximum):
    return random.uniform(minimum, maximum)


def farba_z_hsv(h, s=0.75, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


class Castica:
    def __init__(self, x, y, hue, sila=1.0):
        self.x = x + nahodne(-5, 5)
        self.y = y + nahodne(-5, 5)

        uhol = nahodne(0, math.tau)
        rychlost = nahodne(0.4, 3.0) * sila

        self.vx = math.cos(uhol) * rychlost
        self.vy = math.sin(uhol) * rychlost
        self.trenie = nahodne(0.955, 0.985)

        self.zivot = random.randint(42, 95)
        self.max_zivot = self.zivot
        self.velkost = nahodne(2.0, 5.5) * sila
        self.hue = hue + nahodne(-0.035, 0.035)

    def aktualizuj(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= self.trenie
        self.vy *= self.trenie
        self.vy += 0.01
        self.zivot -= 1

    def vykresli(self, canvas):
        if self.zivot <= 0:
            return

        pomer = self.zivot / self.max_zivot
        r = self.velkost * (0.35 + pomer)
        farba = farba_z_hsv(self.hue, 0.72, 0.55 + 0.45 * pomer)

        canvas.create_oval(
            self.x - r,
            self.y - r,
            self.x + r,
            self.y + r,
            fill=farba,
            outline="",
        )


class FarebnyPrachPokoja:
    def __init__(self, root):
        self.root = root
        self.root.title("Farebný prach pokoja")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, highlightthickness=0)
        self.canvas.pack()

        self.castice = []
        self.stopa = []

        self.mys_x = SIRKA / 2
        self.mys_y = VYSKA / 2
        self.pred_x = self.mys_x
        self.pred_y = self.mys_y

        self.cas = 0
        self.nalada = 0
        self.ukaz_uvod = True

        self.hudba = None
        self.hudba_nazov = "hudba nie je zapnutá"
        self.hudobny_zoznam = []
        self.hudobny_scroll = 0
        self.hudobny_dropdown_otvoreny = False
        self.combo_hudba = None
        self.hudba_label = None

        self.tlacidla = []

        self.canvas.bind("<Motion>", self.pohyb)
        self.canvas.bind("<Button-1>", self.klik)
        self.root.bind("<space>", self.vycisti)
        self.root.bind("<r>", self.zmen_naladu)
        self.root.bind("<R>", self.zmen_naladu)
        self.root.bind("<Escape>", lambda _event: self.zavri())
        self.root.protocol("WM_DELETE_WINDOW", self.zavri)

        self.vytvor_panel_hudby()
        self.slucka()

    def pohyb(self, event):
        self.pred_x = self.mys_x
        self.pred_y = self.mys_y
        self.mys_x = event.x
        self.mys_y = event.y
        self.ukaz_uvod = False

        vzdialenost = math.hypot(self.mys_x - self.pred_x, self.mys_y - self.pred_y)
        pocet = max(2, min(18, int(vzdialenost / 3)))

        for i in range(pocet):
            t = i / max(1, pocet - 1)
            x = self.pred_x + (self.mys_x - self.pred_x) * t
            y = self.pred_y + (self.mys_y - self.pred_y) * t
            self.pridaj_prach(x, y, 1.0)

    def klik(self, event):
        self.ukaz_uvod = False

        for _ in range(80):
            self.pridaj_prach(event.x, event.y, 1.7)

    def pridaj_prach(self, x, y, sila):
        nazov, zaklad, rozsah = NALADY[self.nalada]

        if nazov == "dúhový prúd":
            hue = (self.cas * 0.003 + x / SIRKA * 0.4 + y / VYSKA * 0.2) % 1.0
        else:
            hue = zaklad + nahodne(-rozsah, rozsah)

        self.castice.append(Castica(x, y, hue, sila))

        if len(self.castice) > MAX_CASTIC:
            self.castice = self.castice[-MAX_CASTIC:]

        self.stopa.append((x, y, hue))

        if len(self.stopa) > 180:
            self.stopa.pop(0)

    def vycisti(self, _event=None):
        self.castice.clear()
        self.stopa.clear()

    def zmen_naladu(self, _event=None):
        self.nalada = (self.nalada + 1) % len(NALADY)

    def najdi_hudbu(self):
        zakladny_priecinok = Path(__file__).resolve().parent
        priecinok = zakladny_priecinok / "mp3_hudba"

        if not priecinok.exists():
            return []

        subory = []
        for pripona in ["*.mp3", "*.wav", "*.m4a", "*.aiff", "*.aac"]:
            subory.extend(sorted(priecinok.glob(pripona)))

        return subory

    def obnov_hudobny_zoznam(self):
        self.hudobny_zoznam = self.najdi_hudbu()

    def vytvor_panel_hudby(self):
        # Skutočný rozbaľovací zoznam hudby je mimo plátna, preto sa neprekrýva s animáciou.
        self.obnov_hudobny_zoznam()
        hodnoty = [f"Hudba {i + 1}" for i in range(len(self.hudobny_zoznam))]

        style = ttk.Style()
        style.configure("Hudba.TCombobox", font=("Arial", 11))

        self.combo_hudba = ttk.Combobox(
            self.root,
            values=hodnoty,
            state="readonly",
            width=12,
            style="Hudba.TCombobox",
        )
        self.combo_hudba.set("Vyber hudbu")
        self.combo_hudba.place(x=36, y=VYSKA - 69, width=118, height=27)
        self.combo_hudba.bind("<<ComboboxSelected>>", self.vyber_hudbu_z_combo)

        self.stop_tlacidlo = tk.Label(
            self.root,
            text="Stop",
            bg="#263249",
            fg="#d8f8f0",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        )
        self.stop_tlacidlo.place(x=164, y=VYSKA - 69, width=70, height=27)
        self.stop_tlacidlo.bind("<Button-1>", lambda _event: self.zastav_hudbu())

        self.hudba_label = tk.Label(
            self.root,
            text="Hudba: vypnutá",
            bg="#132622",
            fg="#a9c9c4",
            font=("Arial", 9),
            anchor="w",
        )
        self.hudba_label.place(x=36, y=VYSKA - 38, width=198, height=18)

    def vyber_hudbu_z_combo(self, _event=None):
        index = self.combo_hudba.current()
        if 0 <= index < len(self.hudobny_zoznam):
            self.spusti_hudbu(self.hudobny_zoznam[index])

    def aktualizuj_label_hudby(self):
        if self.hudba_label is not None:
            self.hudba_label.config(text=f"Hudba: {self.hudba_nazov}")

    def prepni_hudobny_dropdown(self):
        self.hudobny_dropdown_otvoreny = not self.hudobny_dropdown_otvoreny

    def hudba_hore(self, _event=None):
        self.hudobny_scroll = max(0, self.hudobny_scroll - 1)

    def hudba_dole(self, _event=None):
        self.obnov_hudobny_zoznam()
        maximum = max(0, len(self.hudobny_zoznam) - 5)
        self.hudobny_scroll = min(maximum, self.hudobny_scroll + 1)

    def spusti_hudbu(self, subor):
        self.zastav_hudbu()

        try:
            self.hudba = subprocess.Popen(["afplay", str(subor)])

            if subor in self.hudobny_zoznam:
                cislo = self.hudobny_zoznam.index(subor) + 1
                self.hudba_nazov = f"Hudba {cislo}"
            else:
                self.hudba_nazov = "vybraná hudba"

            self.hudobny_dropdown_otvoreny = False
            self.aktualizuj_label_hudby()

        except Exception:
            self.hudba = None
            self.hudba_nazov = "hudbu sa nepodarilo spustiť"
            self.aktualizuj_label_hudby()

    def zastav_hudbu(self):
        if self.hudba and self.hudba.poll() is None:
            self.hudba.terminate()

        self.hudba = None
        self.hudba_nazov = "hudba vypnutá"
        self.aktualizuj_label_hudby()

    def zavri(self):
        self.zastav_hudbu()
        self.root.destroy()

    def spracuj_tlacidlo(self, x, y):
        for x1, y1, x2, y2, akcia in self.tlacidla:
            if x1 <= x <= x2 and y1 <= y <= y2:
                akcia()
                return True
        return False

    def pozadie(self):
        self.canvas.create_rectangle(0, 0, SIRKA, VYSKA, fill="#11131d", outline="")

        for i in range(10):
            y = i * 75
            farba = "#141827" if i % 2 == 0 else "#10141f"
            self.canvas.create_rectangle(0, y, SIRKA, y + 75, fill=farba, outline="")

        self.canvas.create_oval(-160, 420, 430, 760, fill="#132622", outline="")
        self.canvas.create_oval(560, 390, 1160, 750, fill="#20172a", outline="")

    def vykresli_stopu(self):
        if len(self.stopa) < 2:
            return

        for i in range(1, len(self.stopa)):
            x1, y1, h1 = self.stopa[i - 1]
            x2, y2, _h2 = self.stopa[i]

            farba = farba_z_hsv(h1, 0.6, 0.65)
            sirka = max(1, int(i / 45))

            self.canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill=farba,
                width=sirka,
                smooth=True,
            )

    def tlacidlo(self, x, y, w, h, text, akcia):
        self.canvas.create_rectangle(
            x,
            y,
            x + w,
            y + h,
            fill="#1e2636",
            outline="#82d6c8",
            width=2,
        )

        self.canvas.create_text(
            x + w / 2,
            y + h / 2,
            text=text,
            font=("Arial", 11, "bold"),
            fill="#d8f8f0",
        )

        self.tlacidla.append((x, y, x + w, y + h, akcia))

    def vykresli_hudbu(self):
        self.tlacidla = []

        x = 28
        y = VYSKA - 82

        sipka = "▴" if self.hudobny_dropdown_otvoreny else "▾"

        if self.hudba_nazov.startswith("Hudba "):
            text_vyberu = self.hudba_nazov
        else:
            text_vyberu = "Relax hudba"

        self.tlacidlo(
            x,
            y,
            175,
            34,
            f"{text_vyberu} {sipka}",
            self.prepni_hudobny_dropdown,
        )

        self.tlacidlo(
            x + 185,
            y,
            70,
            34,
            "Stop",
            self.zastav_hudbu,
        )

        if self.hudobny_dropdown_otvoreny:
            self.vykresli_zoznam_hudby(x, y - 142)

        if self.hudba_nazov.startswith("Hudba "):
            self.canvas.create_text(
                x,
                y - 10,
                text=f"Prehráva sa: {self.hudba_nazov}",
                anchor="w",
                font=("Arial", 11),
                fill="#a9c9c4",
            )

    def vykresli_zoznam_hudby(self, x, y):
        self.obnov_hudobny_zoznam()

        sirka = 255
        vyska_riadku = 24
        pocet_riadkov = 4

        self.canvas.create_rectangle(
            x + 4,
            y + 4,
            x + sirka + 4,
            y + pocet_riadkov * vyska_riadku + 42,
            fill="#090d16",
            outline="",
        )

        self.canvas.create_rectangle(
            x,
            y,
            x + sirka,
            y + pocet_riadkov * vyska_riadku + 42,
            fill="#151d2b",
            outline="#82d6c8",
            width=2,
        )

        if not self.hudobny_zoznam:
            self.canvas.create_text(
                x + 12,
                y + 28,
                text="V priečinku mp3_hudba nie je hudba.",
                anchor="w",
                font=("Arial", 12),
                fill="#d8f8f0",
            )
            return

        maximum = max(0, len(self.hudobny_zoznam) - pocet_riadkov)
        self.hudobny_scroll = min(max(self.hudobny_scroll, 0), maximum)

        viditelne = self.hudobny_zoznam[
            self.hudobny_scroll : self.hudobny_scroll + pocet_riadkov
        ]

        for i, subor in enumerate(viditelne):
            poradove_cislo = self.hudobny_scroll + i + 1
            nazov = f"Hudba {poradove_cislo}"

            ry = y + 8 + i * vyska_riadku

            if nazov == self.hudba_nazov:
                farba_pozadia = "#223047"
            else:
                farba_pozadia = "#151d2b"

            self.canvas.create_rectangle(
                x + 6,
                ry,
                x + sirka - 6,
                ry + 21,
                fill=farba_pozadia,
                outline="",
            )

            self.canvas.create_text(
                x + 14,
                ry + 10,
                text=nazov,
                anchor="w",
                font=("Arial", 11),
                fill="#d8f8f0",
            )

            self.tlacidla.append(
                (x + 6, ry, x + sirka - 6, ry + 21, lambda s=subor: self.spusti_hudbu(s))
            )

        if len(self.hudobny_zoznam) > pocet_riadkov:
            self.tlacidlo(
                x + 8,
                y + pocet_riadkov * vyska_riadku + 16,
                58,
                22,
                "↑",
                self.hudba_hore,
            )

            self.tlacidlo(
                x + 74,
                y + pocet_riadkov * vyska_riadku + 16,
                58,
                22,
                "↓",
                self.hudba_dole,
            )

            self.canvas.create_text(
                x + sirka - 12,
                y + pocet_riadkov * vyska_riadku + 28,
                text=f"{self.hudobny_scroll + 1}-{self.hudobny_scroll + len(viditelne)} / {len(self.hudobny_zoznam)}",
                anchor="e",
                font=("Arial", 10),
                fill="#a9c9c4",
            )

    def vykresli_text(self):
        nazov, _zaklad, _rozsah = NALADY[self.nalada]

        self.canvas.create_text(
            28,
            28,
            text=f"Nálada: {nazov}",
            anchor="w",
            font=("Arial", 16, "bold"),
            fill="#d8f8f0",
        )

        self.canvas.create_text(
            SIRKA - 28,
            28,
            text="Medzerník vyčistí  |  R zmení farby  |  Esc ukončí",
            anchor="e",
            font=("Arial", 13),
            fill="#a9c9c4",
        )

        if self.ukaz_uvod:
            self.canvas.create_text(
                SIRKA / 2,
                250,
                text="Farebný prach pokoja",
                font=("Arial", 38, "bold"),
                fill="#f0fffb",
            )

            self.canvas.create_text(
                SIRKA / 2,
                310,
                text="Pohybuj myšou pomaly a sleduj, ako sa stopa rozplýva.",
                font=("Arial", 18),
                fill="#ccebe5",
            )

            self.canvas.create_text(
                SIRKA / 2,
                350,
                text="Nie je tu skóre. Cieľom je vytvoriť vlastný pokojný obraz.",
                font=("Arial", 15),
                fill="#a9c9c4",
            )

    def slucka(self):
        self.cas += 1

        self.canvas.delete("all")
        self.pozadie()
        self.vykresli_stopu()

        for castica in self.castice:
            castica.aktualizuj()
            castica.vykresli(self.canvas)

        self.castice = [c for c in self.castice if c.zivot > 0]

        self.vykresli_text()

        self.root.after(int(1000 / FPS), self.slucka)


if __name__ == "__main__":
    okno = tk.Tk()
    aplikacia = FarebnyPrachPokoja(okno)
    okno.mainloop()
