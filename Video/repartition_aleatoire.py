import os
from random import sample
from math import floor
from PIL import Image
import shutil

# répartition des fichiers dans train et test
liste = []
n = 0
for fname in os.listdir("label/"):
    liste.append(fname)
    n += 1
train = sample(liste, floor(0.7*n))
test = []
for fname in liste:
    if fname not in train:
        test.append(fname)
# copie des fichiers
for fname in train:
    # textes
    filePath = shutil.copy('label/'+fname, 'obj/'+fname)
    # images
    print(fname)
    fname = fname[:-4]
    fname1 = "image/" + fname + '.png'
    im = Image.open(fname1)
    name = "obj/"+fname+'.png'
    im.save(name, "PNG")
for fname in test:
    filePath = shutil.copy('label/'+fname, 'test/'+fname)
    print(fname)
    fname = fname[:-4]
    fname1 = "image/" + fname+'.png'
    im = Image.open(fname1)
    name = "test/"+fname+'.png'
    im.save(name, "PNG")
