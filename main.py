from app.service.camera_service import CameraService, detect_image

IMAGE_PATH = "app/data/leafs/Downy Mildew Lower Leaf Surface-378x329.png"
if __name__ == "__main__":
    detect_image(image_path=IMAGE_PATH)