import time
import playsound

morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": " / ",  # space
}

def string_to_morse(metin):
    string_parameters = ""
    for harf in metin.upper():
        if harf in morse_alphabet:
            string_parameters += morse_alphabet[harf] + " "
    return string_parameters.strip()

def play_morse(morse_string):
    for harf in morse_string.split(" "):
        for symbol in harf:
            print(symbol, end='', flush=True)
            if symbol == ".":
                playsound.playsound('nokta.mp3', block=False)
                time.sleep(0.15)  
            elif symbol == "-":
                playsound.playsound('çizgi.mp3', block=False)
                time.sleep(0.2)  
        time.sleep(0.35) 


inverted_dict = {v: k for k, v in morse_alphabet.items()}

def morse_to_string(morse):
    morse_parameters = ""
    split_by_space = morse.split(" ")
    for alphabet in split_by_space:
        if alphabet in inverted_dict:
            morse_parameters += inverted_dict[alphabet]
        if alphabet == "/":
            morse_parameters += " "
    return morse_parameters

sec = input("Metni mors alfabesine çevirmek için '1' tersi için '2' tuşlayınız: ")
if sec == "1":
    metin_girdi = input("Metin giriniz: ")
    mors_cikti = string_to_morse(metin_girdi)
    print(f"Mors çevirisi: {mors_cikti}")
    play_morse(mors_cikti)

elif sec == "2":
    gir = input("Morse kodunu giriniz: ")
    translate = morse_to_string(gir).capitalize()
    print(f"Morsun çevirisi: {translate}")
