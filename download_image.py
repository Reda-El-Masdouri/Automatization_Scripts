import requests

image_1 = requests.get("https://raw.githubusercontent.com/Reda-El-Masdouri/Automatization_Scripts/main/image.jpg")
if image_1.status_code == 200:
    f = open("image.jpg", "wb")
    f.write(image_1.content)
    f.close()
else:
    print("ERREUR:", image_1.status_code)

