# Optimus Repository 📦

> A collection of **machine‑learning** and **computer‑vision** demos built with TensorFlow, Streamlit, and YOLOv8.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Setup & Installation](#setup--installation)
- [Scripts](#scripts)
  - [task1.py – CIFAR‑10 Classification](#task1py---cifar-10-classification)
  - [task2.py – University FAQ Chatbot](#task2py---university-faq-chatbot)
  - [task3.py – YOLOv8 Object Detection](#task3py---yolov8-object-detection)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The **Optimus** repo showcases three independent Python demos:

1. **`task1.py`** – Trains a CNN on the CIFAR‑10 dataset and visualises training/validation accuracy.
2. **`task2.py`** – A Streamlit‑based FAQ chatbot powered by Google Gemini (or any compatible `genai` client).
3. **`task3.py`** – Real‑time object detection using the ultralytics **YOLOv8** model inside a Streamlit UI.

Each script is self‑contained and can be run on its own after installing the required packages.

---

## Setup & Installation

1. **Clone the repository** (if you haven’t already):
   ```bash
   git clone <your‑remote‑url>
   cd optimus
   ```
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows PowerShell
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > The `requirements.txt` pins versions for TensorFlow, Streamlit, ultralytics, and the Google `genai` client.

4. **(Optional) Set your API key** for the chatbot:
   ```powershell
   $env:GENAI_API_KEY = "YOUR_API_KEY"
   ```
   Replace `YOUR_API_KEY` with a valid Gemini API key.

---

## Scripts

### `task1.py` – CIFAR‑10 Classification

```bash
python task1.py
```
- Loads the CIFAR‑10 dataset.
- Trains a simple ConvNet for 20 epochs.
- Plots training and validation accuracy using Matplotlib.

> **Tip:** Adjust the number of epochs or the model architecture in the script to experiment with performance.

---

### `task2.py` – University FAQ Chatbot

```bash
streamlit run task2.py
```
- Launches a Streamlit UI for a conversational FAQ assistant.
- Uses the `genai` client to generate responses from the **gemini‑2.5‑flash** model.
- The chat history is persisted in the Streamlit session state.

> **Tip:** Ensure the `GENAI_API_KEY` environment variable is set before running the app.

---

### `task3.py` – YOLOv8 Object Detection

```bash
streamlit run task3.py
```
- Provides a file‑uploader for images.
- Runs inference with the pretrained `yolov8n.pt` model.
- Displays the original image, the annotated detection image, and a list of detected objects with confidence scores.

> **Tip:** Install the optional **opencv‑python** package if you wish to extend functionality to video streams.

---

## Dependencies

The `requirements.txt` includes:

```
tensorflow==2.13.0
streamlit==1.38.0
ultralytics==8.2.0
Pillow==10.4.0
numpy==2.1.2
google-genai==0.5.0
matplotlib==3.9.2
seaborn==0.13.2
```

Feel free to adjust versions as needed for compatibility with your environment.

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and ensure the code runs.
4. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

**Happy hacking!** 🎉
