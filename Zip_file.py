import os
import zipfile
import datetime

# lista katalogów
source_dirs = ["Zabawa1", "Zabawa2", "Zabawa3"]

# nazwa archiwum
today = datetime.datetime.today().strftime('%Y-%m-%d')

# stwórz folder dla kopii
backup_dir = "Backup"
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# skopiuj każdy wybrany katalog do archiwum
for source_dir in source_dirs:
    # utwórz nazwę pliku archiwum zip z aktualną datą
    zip_filename = f"{today}_{source_dir}.zip"

    # ścieżka do katalogu, który ma zostać skopiowany
    source_path = os.path.abspath(source_dir)

    # ścieżka do pliku archiwum
    zip_path = os.path.join(backup_dir, zip_filename)

    # skopiuj katalog do archiwum
    with zipfile.ZipFile(zip_path, "w") as zip_file:
        for folder_name, subfolders, filenames in os.walk(source_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                zip_file.write(file_path, os.path.relpath(file_path, source_path), compress_type=zipfile.ZIP_DEFLATED)

    print(f"Kopia bezpieczeństwa {source_dir} została utworzona.")
