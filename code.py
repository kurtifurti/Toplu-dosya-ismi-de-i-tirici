import os
import sys
import time

def toplu_degistirici(directory, old_char, new_char):
    
    for item_name in os.listdir(directory):
        item_path = os.path.join(directory, item_name)
        
        new_item_name = item_name.replace(old_char, new_char)
        new_item_path = os.path.join(directory, new_item_name)
        
        os.rename(item_path, new_item_path)
        print(f"'{item_name}' ismi '{new_item_name}' olarak degistirildi.")


directory_path = input("Klasor yolunu girin: ")
if "system32" in directory_path.lower() and "windows" in directory_path.lower():
    print("System32 yolunu girdiniz. Program sonlandiriliyor.")
    time.sleep(3)
    sys.exit()
old_character = input("Degistirilecek karakteri girin: ")
new_character = input("Yeni karakteri girin: ")

toplu_degistirici(directory_path, old_character, new_character)
time.sleep(3)
