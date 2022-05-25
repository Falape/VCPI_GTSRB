from os import remove, listdir
from os.path import splitext, join, isfile
from PIL import Image

pathTrain = 'GTSRB_TP/train_images'
pathTest = 'GTSRB_TP/test_images'
for path in [pathTrain,pathTest]:
    for classFolder in listdir(path):
        for image in listdir(join(path,classFolder)):
            if(isfile(join(path,classFolder,image))):
                f, e = splitext(image)
                if e == '.ppm': #or e == '.png' or e == '.jpeg' or e == '.jpg':
                    im = Image.open(join(path,classFolder,image))
                    f = f + '.png'
                    im.save(join(path,classFolder,f))

                    remove(join(path,classFolder,image))
                else:
                    print(image + " -> É ficheiro mas não é imagem.")
            else:
                print(image + " -> É uma pasta.")