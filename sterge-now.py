import os
import time
import shutil
import stat

# Specifică calea relativă a directorului curent
folder_path = "."  # Sau calea absolută

# Specifică perioada în secunde pentru a considera folderele ca fiind noi (de exemplu, 1 zi = 86400 secunde)
time_period = 300  # 3600 = 1 zi

# Funcție pentru a elimina atributul "Read-Only"
def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# Funcție principală de ștergere
def delete_folders():
    current_time = time.time()
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folder_creation_time = os.path.getctime(item_path)
            if (current_time - folder_creation_time) < time_period:
                try:
                    shutil.rmtree(item_path, onerror=remove_readonly)
                    print(f"S-a șters folderul: {item_path}")
                except Exception as e:
                    print(f"Nu s-a putut șterge folderul {item_path}. Eroare: {e}")

# Rulare infinită la interval de 1 oră
while True:
    delete_folders()
    print("Aștept 300 s pentru a rula din nou.")
    time.sleep(300)  # Așteaptă 1 oră (3600 secunde)
