# Image_Processing_Project_ImageClassification
A powerful image processing application that provides various image classification through both a command-line interface and a user-friendly Streamlit web interface.
![Streamlit](https://cdn.discordapp.com/attachments/1371692177020813342/1371712784105996449/image.png?ex=68242294&is=6822d114&hm=aef23a6e9f8f0962fcd38a9d3d3b35558a81da4b3f5229f140dfb953eac33309&)

## Summary of Key Features

| Feature        | Description                                  |
|----------------|----------------------------------------------|
| 📥 Data Input   | Loading, resizing, and normalization         |
| 🧠 CNN Design   | Convolution + Pooling + Dense architecture   |
| ⚙️ Training     | With optimizer and loss function              |
| 📊 Evaluation   | Accuracy and loss calculation & visualization|
| 💾 Model Save  | Export model for later use                   |
| 🖼️ Inference   | Predict custom cat/dog images                |


## Trained Model
[Trained Model]([link](https://drive.google.com/drive/folders/1uxCWBJalVoGmwLO-vnbkratjdaHIMxB8?usp=drive_link))


## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Image_Processing_Project_ImageClassification.git
cd Image_Processing_Project_ImageClassification

```

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Streamlit Web Interface

The web interface provides an intuitive way to try the model:

```bash
streamlit run streamlit_app.py
```

Features of the web interface:
- Simple image upload via the upload image
- Interactive controls for image classification
- Real-time preview of processed images

## Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

