import cv2
import clip
import torch
from ultralytics import YOLO
from PIL import Image


def analyze_video(video_path, config):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    clip_model, preprocess = clip.load(config["models"]["clip"], device=device)
    yolo_model = YOLO(config["models"]["yolo"])

    cap = cv2.VideoCapture(video_path)
    results = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to PIL Image
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)

        # CLIP processing
        image_input = preprocess(pil_image).unsqueeze(0).to(device)
        with torch.no_grad():
            image_features = clip_model.encode_image(image_input)

        # YOLO processing
        detections = yolo_model(frame)
        results.append(process_frame(detections))

    return aggregate_results(results)


def aggregate_results(frame_results):
    object_counts = {}
    violence_frames = 0

    for frame in frame_results:
        for obj in frame["objects"]:
            class_name = obj["class"]
            object_counts[class_name] = object_counts.get(class_name, 0) + 1
        if frame["violence_flag"]:
            violence_frames += 1

    return {
        "object_counts": object_counts,
        "violence_percent": (violence_frames / len(frame_results)) * 100
        if frame_results
        else 0,
    }


def process_frame(detections):
    violence_flag = False
    objects = []

    for box in detections[0].boxes:
        class_id = int(box.cls)
        class_name = detections[0].names[class_id]
        objects.append({"class": class_name, "confidence": float(box.conf)})

        if class_name in ["knife", "gun", "fire"]:
            violence_flag = True

    return {"objects": objects, "violence_flag": violence_flag}
