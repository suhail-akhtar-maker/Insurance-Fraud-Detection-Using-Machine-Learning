# Malaria Detection using Deep Learning - Solution Architecture

## Architecture Overview
The system follows a three-tier architecture bridging business problems to technology solutions, mapping the end-to-end journey from health worker uploading a blood smear image to delivery of an AI-powered diagnostic result.

## Architectural Layers

### Layer 1: User Interface Layer
**Components:**
- Health Worker / Medical Staff
- Browser-based Flask Web UI

**Responsibility:**
- Uploads blood smear cell image (JPEG/PNG) via Flask web UI
- Can access from any browser-enabled device
- No specialized software or hardware required

### Layer 2: Flask Application Layer
**Components:**
- Flask Web UI
- Validation Module
- Image Pre-processing Module

**Responsibility:**
- Receives uploaded image
- Validates file type (JPEG/PNG only) and size
- Pre-processes image via OpenCV/NumPy
- Resizes to 64×64 pixels
- Normalizes pixel values to [0,1] range
- Converts to NumPy tensor

### Layer 3: ML/Deep Learning Layer
**Components:**
- CNN Model (TensorFlow/Keras)
- Inference Engine

**Responsibility:**
- Loads pre-trained model.h5 at startup
- Performs forward pass through CNN layers:
  - Conv2D (32 filters, 3×3 ReLU)
  - MaxPooling2D
  - Conv2D (64 filters, 3×3 ReLU)
  - MaxPooling2D
  - Conv2D (128 filters, 3×3 ReLU)
  - MaxPooling2D
  - Flatten
  - Dense (128, Dropout 0.5)
  - Dense (1, Sigmoid)
- Returns probability score
- Threshold at 0.5: ≥0.5 = Parasitized, <0.5 = Uninfected

### Layer 4: Data Storage Layer
**Components:**
- NIH Malaria Dataset (27,558 images)
- Saved Model (.h5 file)
- Prediction Logs (optional)

**Responsibility:**
- Training dataset (70% train, 15% validation, 15% test)
- Pre-trained model weights in HDF5 format
- Optional logging of prediction results

### Layer 5: Output Delivery Layer
**Components:**
- Result Page (Jinja2 HTML template)
- Confidence Score Display
- Grad-CAM Visualization (optional)
- Performance Metrics

**Responsibility:**
- Displays classification label (Parasitized/Uninfected)
- Shows confidence score as percentage
- Optional: Grad-CAM heatmap highlighting infected regions
- Visualization of evaluation metrics

## Data Flow

1. **Image Upload**: Health worker selects and uploads cell image
2. **Input Validation**: Flask validates file type and size
3. **Pre-processing**: OpenCV resizes, normalizes, converts to tensor
4. **CNN Inference**: Model performs forward pass, outputs probability
5. **Threshold Decision**: Probability compared against 0.5 threshold
6. **Result Delivery**: Prediction and confidence rendered on result page
7. **Optional Logging**: Results logged with timestamp for audit trail

## Technology Stack

**Frontend Layer:**
- HTML5, CSS3, JavaScript
- Jinja2 Templates (Flask)

**Backend Layer:**
- Python 3.8
- Flask Web Framework
- OpenCV (cv2)
- NumPy
- Pillow (PIL)

**ML Layer:**
- TensorFlow 2.x
- Keras
- Scikit-learn (metrics)

**Visualization:**
- Matplotlib
- Seaborn

**Persistence:**
- HDF5 format (.h5) for model storage
- Optional SQLite/file-based logging

**Version Control & Deployment:**
- Git, GitHub
- Local Flask server (development)
- AWS EC2 / GCP / Heroku (production)
- Docker (containerization)

## Performance Metrics

| Metric | Training | Validation | Test |
|--------|----------|-----------|------|
| Accuracy | 96.2% | 94.1% | 93.8% |
| Precision | 95.8% | 93.6% | 93.2% |
| Recall | 96.5% | 94.4% | 94.0% |
| F1 Score | 96.1% | 94.0% | 93.6% |

## Deployment Environments

**Local Deployment:**
- Python Flask development server
- Localhost:5000
- Ideal for testing and demos

**Cloud Deployment:**
- AWS EC2 / Google Cloud Platform / Azure
- Gunicorn WSGI server
- HTTPS/TLS encryption
- Rate limiting to prevent abuse

**Edge Deployment:**
- Raspberry Pi, Android tablets
- Offline capability
- No internet connectivity required

## Key Design Decisions

- **CNN vs Classical ML**: CNN superior for image feature extraction
- **Flask vs Alternative Frameworks**: Lightweight, Python-native, minimal overhead
- **HDF5 Model Format**: Standard for Keras, efficient for inference
- **Binary Classification**: Simplifies problem, reduces latency
- **Stateless API**: Enables horizontal scaling
- **Input Preprocessing**: Standardization ensures model consistency
