from PIL import Image
import os

for fname in os.listdir("sample_data/frames/"):
    fname1 = "sample_data/frames/" + fname
    im = Image.open(fname1)
    largeur, hauteur = im.size
    # Define box inside image
    for i in range(0, 8):
        for j in range(0, 8):
            left = largeur/8 * i
            top = hauteur/8 * j
            width = largeur/8
            height = hauteur/8
            # Create Box
            box = (left, top, left+width, top+height)
            # Crop Image
            area = im.crop(box)
            # Save Image
            name = "sample_data/frames2/"+str(i)+"_"+str(j)+"_"+fname
            print(name)
            area.save(name, "PNG")
