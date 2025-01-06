import zipfile
import pathlib

def make_archive(filepaths, dest_directory):
    dest_path = pathlib.Path(dest_directory, "compressed.zip")
    with zipfile.ZipFile(dest_directory, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["Daily Mood Booster.py", "file_age_analyzer.py"], dest_directory="dest")