import requests

image_1 = requests.get("http://git-scm.com/images/logos/downloads/Git-Logo-1788C.png")
if image_1.status_code == 200:
    f = open("image.jpg", "wb")
    f.write(image_1.content)
    f.close()
else:
    print("ERREUR:", image_1.status_code)

