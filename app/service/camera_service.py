from ultralytics import YOLO
import cv2
from app.utils.utils import draw_bounding_boxes,draw_bounding_boxes_per_leaf

def CameraService():
    model = YOLO("app/models/best.pt")

    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame, conf=0.5, imgsz=640, verbose=False)
        
        results = results[0]
        annoted_frame = draw_bounding_boxes(results, frame)
        
        cv2.imshow("Melon Leaf Disease Detection", annoted_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Keluar dari program")
            break
        
    cap.release()
    cv2.destroyAllWindows()
        
        
def detect_image(image_path):
    model = YOLO("app/models/best.pt")
    
    # Deteksi langsung dari path
    results = model(image_path, conf=0.5, imgsz=640, verbose=False)
    results = results[0]
    
    # Baca gambar untuk ditampilkan
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (640, 640))
    annoted_frame = draw_bounding_boxes_per_leaf(results, frame)
    
    cv2.imshow("Melon Leaf Detection", annoted_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    CameraService()
        