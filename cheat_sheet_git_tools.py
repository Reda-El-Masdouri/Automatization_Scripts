import requests

from PIL import Image

image_1 = requests.get("https://raw.githubusercontent.com/JustFS/cours-github/team_work/travailler_en_equipe.png")
if image_1.status_code == 200:
    f = open("cour_2.jpg", "wb")
    f.write(image_1.content)
    f.close()
else:
    print("ERREUR:", image_1.status_code)


image_2 = requests.get("https://raw.githubusercontent.com/JustFS/cours-github/master/versionner.png")
if image_2.status_code == 200:
    f = open("cour_1.jpg", "wb")
    f.write(image_2.content)
    f.close()
else:
    print("ERREUR:", image_2.status_code)

pic_1 = Image.open(r"C:\Users\REDA\PycharmProjects\Les_Scripts_d'Automatisation\Automatization_Scripts\cour_1.jpg")
im_1_convert = pic_1.convert('RGB')
pic_2 = Image.open(r"C:\Users\REDA\PycharmProjects\Les_Scripts_d'Automatisation\Automatization_Scripts\cour_2.jpg")
im_2_convert = pic_2.convert('RGB')

list_images = [im_2_convert]

im_1_convert.save(r"C:\Users\REDA\PycharmProjects\Les_Scripts_d'Automatisation\Automatization_Scripts\cheat_sheet.pdf", save_all=True, append_images=list_images)

