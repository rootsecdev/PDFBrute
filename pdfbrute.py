import pikepdf
import time
import colorama
from colorama import Fore
print("[+] Starting PDFBrute")
print()
time.sleep(1)
print("[+] PDFBrute Started...")
print()
time.sleep(1)
print("[+] Wait for the PDF PWNAGE....")
print()
time.sleep(1)
with open("/usr/share/wordlists/rockyou.txt",'r',encoding='ISO-8859-1') as file_1:
    for word in [word.strip('\n\r') for word in file_1]:
        try:
            with pikepdf.open("file.pdf", password=word) as pdf:
                print(Fore.RED + "------------------------------------")
                print(Fore.RED+"| "+Fore.WHITE+"[+] Password found: "+word+Fore.RED+" |")
                print(Fore.RED + "------------------------------------")
                print()
                break
        except pikepdf._qpdf.PasswordError as e:
            continue
print(Fore.WHITE+"[+] Hack the Planet!")
