

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

    POSITION_BOUTON_REFRESH = (-1393, 73)
    TEMPS_AVANT_REFRESH = 170

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
            print("\nAvertissement")

            print("Lancement du refresh")
            position_actuelle_souris_x, position_souris_actuelle_y = pyautogui.position()

            print("Déplacement + click...")
            pyautogui.click(x = self.POSITION_BOUTON_REFRESH[0], y = self.POSITION_BOUTON_REFRESH[1])
            print("Fait.")

            print("Retour à la position initiale...")
            pyautogui.moveTo(x = position_actuelle_souris_x, y = position_souris_actuelle_y)
            print("Fait.")

            temps_avant_refresh = self.TEMPS_AVANT_REFRESH 
            temps_avant_refresh += random.randint(-10, 10)
            
            time.sleep(temps_avant_refresh)
        

if __name__ == "__main__":
    prog = Programme()
    prog.main()
