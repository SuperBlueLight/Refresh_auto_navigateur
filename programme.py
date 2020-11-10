

# .................................................................
# NOTES : 
# 

# .................................................................
# Imports librairie standard
import pyautogui
import time
import random

# Imports tiers

# Imports locaux


# .................................................................
# Classes
class Programme():
    """TODO"""

    # .................................................................
    # Constantes

    POSITION_BOUTON_REFRESH = (-1393, 79)
    TEMPS_AVANT_REFRESH = 30 # Temps d'attente entre deux clicks, en secondes

    # .................................................................
    # Constructeur & méthodes spéciales

    def __init__(self):
        pass

    # .................................................................
    # Propriétés

    # .................................................................
    # Méthodes

    def main(self):
        print("Lancement du programme.")
        time.sleep(3)

        while True:
            print("\nConfigurer la position du bouton refresh du navigateur? (oui/non)")
            saisie = input()

            if saisie in ["yes", "y", "oui", "o"]:
                print("\nClick de test dans 5 secondes...")
                time.sleep(1.0)
                print("4 secondes...")
                time.sleep(1.0)
                print("3 secondes...")
                time.sleep(1.0)
                print("2 secondes...")
                time.sleep(1.0)
                print("1 seconde...")
                time.sleep(1.0)
                print("Click...")
                position_souris_x, position_souris_y = pyautogui.position()
                pyautogui.click(x = self.POSITION_BOUTON_REFRESH[0], y = self.POSITION_BOUTON_REFRESH[1])
                print(f"Fait. Position de la souris lors du click: ({position_souris_x}, {position_souris_y})")

                print("\nConserver cette position? (oui/non)")
                saisie = input()

                if saisie in ["yes", "y", "oui", "o"]:
                    self.POSITION_BOUTON_REFRESH = (position_souris_x, position_souris_y)
                    print("Nouvelle position enregistrée.")

            elif saisie in ["no", "n", "non", "q", "quitter"]:
                break

        while True:
            print("\nLancement du refresh")
            position_souris_x, position_souris_y = pyautogui.position()

            print("Déplacement + click...")
            pyautogui.click(x = self.POSITION_BOUTON_REFRESH[0], y = self.POSITION_BOUTON_REFRESH[1])
            print("Fait.")

            print("Retour à la position initiale...")
            pyautogui.moveTo(x = position_souris_x, y = position_souris_y)
            print("Fait.")

            time.sleep(self.TEMPS_AVANT_REFRESH)
        

if __name__ == "__main__":
    prog = Programme()
    prog.main()
