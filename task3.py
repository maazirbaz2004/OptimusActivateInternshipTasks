import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="YOLO Object Detection")

st.title("Object Detection using YOLOv8")

model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image)

    img_array = np.array(image)

    results = model(img_array)

    result = results[0]

    annotated_image = result.plot()

    st.subheader("Detected Objects")
    st.image(
        annotated_image,
        channels="BGR"
    )

    st.subheader("Detection Results")

    for box in result.boxes:

        cls_id = int(box.cls[0])

        confidence = float(box.conf[0])

        class_name = model.names[cls_id]

        st.write(
            f"{class_name}: {confidence:.2f}"
        )