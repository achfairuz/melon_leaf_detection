import cv2

CLASS_COLORS = {
    'healthy': (0, 255, 0),      # Green
    "powdery mildew": (255, 255, 0),  # cyan
    "downy mildew": (255, 165, 0),    # oranye
    "virus gemini": (0, 0, 255)       # merah
}

def draw_bounding_boxes(result, frame):
    if len(result.boxes) == 0:
        return frame  # Tidak ada deteksi → langsung balikin frame asli
    
    for box in result.boxes:
        cls_id = int(box.cls[0])
        label = result.names[cls_id]
        conf = float(box.conf[0])
        color = CLASS_COLORS.get(label, (255, 255, 255))  
        
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        print(f"Deteksi: {label} ({conf:.2f})")  # debug di terminal
    
    return frame

def draw_bounding_boxes_per_leaf(result, frame):
    if len(result.boxes) == 0:
        return frame
    
    for i, box in enumerate(result.boxes):
        cls_id = int(box.cls[0])
        label = result.names[cls_id]
        conf = float(box.conf[0])
        color = CLASS_COLORS.get(label, (255, 255, 255))
        
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Tambahkan label unik per daun
        leaf_label = f"{label}-{i+1} {conf:.2f}"
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, leaf_label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        print(f"Daun {i+1}: {label} ({conf:.2f})")
    
    return frame

        