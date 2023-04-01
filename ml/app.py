from flask import Flask, jsonify, request
from flask_cors import CORS
from torch import hub
import argparse
import io
from PIL import Image
from flask import Flask, request
import generateUniqueId
import os

app = Flask(__name__)
CORS(app)


@app.route("/api/defect", methods=["POST"])
def predict():
    # jsonData = request.get_json()
    # url = jsonData['url']
    # filepath = retrieveImage.getImagePath(url)
    if "file" not in request.files:
        return jsonify(error='no input file')
    file = request.files["file"]
    if not file:
        return
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img)  # inference
    results.render()  # updates results.ims with boxes and labels
    filename = generateUniqueId.getUniqueId()
    filepath = str(filename) + '.png'
    Image.fromarray(results.ims[0]).save(filepath)
    s = str(results)
    l = s.split(" ")
    temp = "detections"
    if l[4][0] == 'D':
        temp = "Deformations"
    elif l[4][0] == 'S':
        temp = 'Scratchs'
    os.remove(filepath)
    # if str(l[3]) == "(no":
    #     return jsonify(factor=0.9)
    s = str(l[3]) + " " + temp
    # if str(l[4]) == "Scratch" or str(l[4]) == "Scratchs":
    #     f = 0.1 * int(l[3])
    #     if f > 0.6:
    #         f = 0.6
    #     f = 1 - f
    #     return jsonify(factor=f)
    # if str(l[4]) == "Deformation" or str(l[4]) == "Deformations":
    #     f = 0.3 * int(l[3])
    #     if f > 0.6:
    #         f = 0.6
    #     f = 1 - f
    #     return jsonify(factor=f)
    s = s.strip()
    return jsonify(defects=s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=8000, type=int, help="port number")
    args = parser.parse_args()

    # force_reload = recache latest code
    model = hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.eval()
    app.run(port=8000, debug=True)
