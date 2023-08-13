import eel
import os

# Setze das Verzeichnis für die HTML-Dateien
eel.init('web')

@eel.expose
def save_file(file_content):
    try:
        with open('filename.txt', 'w') as file:
            file.write(file_content)
        return True
    except Exception as e:
        print(str(e))
        return False

eel.init('web')
eel.start('index.html')
