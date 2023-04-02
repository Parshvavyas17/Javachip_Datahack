from torch import hub
from PIL import Image
# from keras.applications.imagenet_utils import preprocess_input
# from keras.models import load_model
# import numpy as np
import io
# import keras.utils as image

model = hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()

with open('img.jpg', "rb") as picture:
    f = picture.read()
    img_bytes = bytearray(f)
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img)
    # print(results)
    # print(type(results))
    results.render()
    Image.fromarray(results.ims[0]).save("firstmodel.jpg")
    s = str(results)
    l = s.split(" ")
    print(l[3])
    print(type(l[4]))
    s = str(l[3]) + " " + str(l[4])
    print(s)
    if str(l[3]) == "(no":
        print(0.95)
    # s = str(l[3]) + " " + str(l[4])
    elif l[4] == "Scratch" or l[4] == "Scratchs":
        f = 0.1 * int(l[3])
        if f > 0.6:
            f = 0.6
        f = 1 - f
        print(f)
    elif l[4] == "Deformation" or l[4] == "Deformations":
        f = 0.3 * int(l[3])
        if f > 0.6:
            f = 0.6
        f = 1 - f
        print(f)
