from flask import Flask , request
from PIL import Image
from FaceRecService import FaceModelService

# python -m flask --app .\app.py run

app = Flask(__name__)
face_service = FaceModelService()
# hello lolllyyyy <3<3<3
@app.route("/upload", methods=["POST"])
def upload_image():
    image_bytes = request.data  # Read raw bytes from request
    embedding = face_service.ConvertImageToEmbedding(image_bytes)
    return embedding
