class Ziel:
    def __init__(self, name, gewichtung, startwert, zielwert):
        self.name = name
        self.gewichtung = gewichtung
        self.startwert = startwert
        self.zielwert = zielwert
        self.fortschritt = 0

    def update_fortschritt(self, aktueller_wert):
        # Beispiel für Gewicht verlieren
        if self.startwert > self.zielwert:
            self.fortschritt = (self.startwert - aktueller_wert) / (self.startwert - self.zielwert) * 100

        # Beispiel für Sprachen lernen
        # hier bleibt die Logik einfach, da es von der Selbsteinschätzung abhängt
        self.fortschritt = aktueller_wert

def main():
    ziele = []
    print("Gib deine Ziele ein:")
    # Eingabe der Ziele ...
    # Beispiel: Gewicht verlieren
    ziele.append(Ziel("Gewicht verlieren", 3, 80, 70))
    # Beispiel: Französisch lernen
    ziele.append(Ziel("Französisch lernen", 1, 0, 100))

    # Update des Fortschritts
    for z in ziele:
        aktueller_wert = float(input(f"Gib deinen aktuellen Wert für {z.name} ein: "))
        z.update_fortschritt(aktueller_wert)
        print(f"Fortschritt für {z.name}: {z.fortschritt}%")

if __name__ == "__main__":
    main()