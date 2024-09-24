import os
import time
import shutil
import stat

# Specifies the relative path of the current directory
folder_path = "."  # Or the absolute path

# Specifies the period in seconds to consider folders as new (eg 1 day = 86400 seconds)
time_period = 300  # 3600 = 1 hour

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
                    print(f"Folder deleted: {item_path}")
                except Exception as e:
                    print(f"Could not delete the folder {item_path}. Eroare: {e}")

# Rulare infinită la interval de 1 oră
while True:
    delete_folders()
    print("I wait 300s to run again.")
    time.sleep(300)  # 1 hour (3600 seconds)
