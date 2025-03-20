
from deepface import DeepFace
import numpy as np
from PIL import Image
import io

class FaceModelService:
    def ConvertImageToEmbedding(self, image_bytes: bytes):
        try:
            # Convert bytes to image using PIL
            image = Image.open(io.BytesIO(image_bytes))
            image_np = np.array(image)
            # Extract facial embedding using DeepFace
            embedding = DeepFace.represent(
                img_path=image_np,  # Pass the image object
                model_name="Facenet",
                enforce_detection=False
            )[0]["embedding"]
            return embedding
        except Exception as e:
            print(f"Error generating embedding: {str(e)}")
            return []
