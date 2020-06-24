from flask import Flask, request
import os

app = Flask(__name__)
filesLocation = "/tmp"
runCurrentLoc = os.getcwd()


@app.route('/', methods=["POST"])
def homepage():
    if request.method == "POST":
        if request.files["image-file"]:
            imageFile = request.files["image-file"]
            fileLoc = os.path.join(
                filesLocation, imageFile.filename)
            imageFile.save(fileLoc)
            gcodeCommand = "python3 " + runCurrentLoc + \
                "/gcodeGenerator/imageToGcode.py " + fileLoc
            print(gcodeCommand)
            gcodeLocation = os.popen(gcodeCommand)
            output = gcodeLocation.read()
            print(output)
            return "Done"
    else:
        return "Send POST request"


def main():
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()
