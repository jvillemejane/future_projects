# Bibliothèque utilisée
import pygame
import numpy as np
import serial
import time

def parse_signal(signal):
    return [x for x in signal.split(",")]

# Définition d'une classe
class HarpeSound:

    # Initialisation des variables
    sampleTimeSec = 1
    samplerate = 44100
    sampleMaxvalue = int(sampleTimeSec*samplerate)

    def __init__(self):
        pygame.mixer.init(frequency=44100, channels=2, size=16, buffer = 4096)

    # Ouverture des fichiers audios
    def init(self):
        self.soundC3 = self.openWaveFile('C3.wav').astype(np.int16)
        self.soundB6 = self.openWaveFile('B6.wav').astype(np.int16)
        self.soundG6 = self.openWaveFile('G6.wav').astype(np.int16)
        print(type(self.soundG6[0][0]))

    # Définition d'un dictionnaire qui associe chaque fichier audio à un numero de 1 à 8 pour la note et de -1 à 1 pour la hauteur de la gamme
        self.dictionnaire_sommation = {('1'):self.soundC3,('2'):self.soundB6,('3'):self.soundG6 }

    # fonction qui permet d'additioner le son de deux fichier afin de superposer les notes
    def sommation_note(self,list):
        l=len(list)
        if l > 0:
            son = np.zeros((HarpeSound.sampleMaxvalue, 2), dtype=np.int16)
            for i in range (l):
                if list[i] != '0':
                    son += self.dictionnaire_sommation[(list[i])] // l                
                print(type(son[0][0]))
                final_sound = pygame.sndarray.make_sound(son)
                return final_sound
        else:
            return son

    # fonction qui permet d'ouvrir les fichiers audios
    def openWaveFile(self, file):
        sound = pygame.mixer.Sound(file)
        sound_data = pygame.sndarray.array(sound)
        return sound_data[0:HarpeSound.sampleMaxvalue][:]

    # fonction qui permet de prendre le son sommet et d'émettre le son
    def sound_creatorcombinaison (self,list):
        self.sommation = self.sommation_note(list)
        self.sommation.play(0)


# Ouverture de la classe
controleur = HarpeSound()

# Initialisation de la harpe laser. Cette étape est longue mais n'est réalisé qu'une seule fois
controleur.init()
if __name__ == "__main__":

    # Nom du périphérique série
    serial_port = '/dev/ttyACM0'  # Windows

    # Bauds
    baud_rate = 115200

    # ser = serial.Serial(serial_port, baud_rate, timeout=0.1)

    # Assurez-vous que le port série est ouvert
    '''
    if not ser.is_open:
        ser.open()
    '''
    try:
        while True:
            
            '''
            ser.write("1".encode())
            # Lire les données d'un microcontrôleur
            data_received =  ser.readline().decode("utf-8").strip()
            '''
            
    
            data_received = "2,3"
            if data_received:
                print(f"Received: {data_received}")
                signal_array = parse_signal(data_received)
                # Emission du son correspondant aux donnée du microcontroleur
                controleur.sound_creatorcombinaison(signal_array)

            # Latence pour le traitement des données
            time.sleep(2)

    # expression de l'interruption du programme dans le shell
    except KeyboardInterrupt:
        print("Le programme a été interrompu")

    finally:
        # Fermez le port série
        ser.close()
