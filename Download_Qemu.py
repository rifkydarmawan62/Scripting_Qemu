from subprocess import run, CalledProcessError
from colorama import Fore, Back
from tkinter.filedialog import askdirectory as pilih_direktori
from platform import system

def bersihkan_layar(teks : str | None = None):
    if system() == "Windows":
        run("cls", shell = True)
    else:
        run("clear", shell = True)
    if teks:
        print(teks)
if system() == "Windows":
    bersihkan_layar(f"{Fore.LIGHTBLUE_EX}Tekan Alt + Tab untuk membuka jendela baru{Fore.RESET}")
    DIREKTORI_FOLDER = pilih_direktori(title = "Pilih lokasi unduhan file instalasi Qemu disimpan").replace("/", "\\")
    if DIREKTORI_FOLDER:
        URL = "https://qemu.weilnetz.de/w64/2023/qemu-w64-setup-20231224.exe"
        LOKASI_UNDUHAN = f"{DIREKTORI_FOLDER}\\{URL.split("/")[-1]}"
        PERINTAH = f"bitsadmin /transfer \"Mengunduh_Instalasi_Qemu\" /download /priority FOREGROUND \"{URL}\" \"{LOKASI_UNDUHAN}\" && \"{LOKASI_UNDUHAN}\""
        print(f"{Fore.YELLOW}Menjalankan perintah Windows Command Prompt {Fore.LIGHTYELLOW_EX}{Back.BLUE}{PERINTAH}{Fore.YELLOW}{Back.RESET} ...{Fore.RESET}")
        try:
            run(PERINTAH, shell = True, check = True)
        except CalledProcessError:
            print(f"{Fore.LIGHTRED_EX}Gagal mengunduh atau menjalankan instalasi Qemu!{Fore.RESET}")
        except KeyboardInterrupt:
            print(f"{Fore.LIGHTRED_EX}Unduhan atau instalasi Qemu dihentikan!{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}Berhasil menjalankan instalasi Qemu{Fore.RESET}")