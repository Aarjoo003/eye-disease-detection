👁️ Eye Disease Detection System (AI-Powered)
🚀 Project Overview
This project is an AI-driven diagnostic tool designed to assist in the early detection of various eye conditions using Retinal Fundus images. Developed as a 3rd-year project at SGSITS, Indore, it leverages Deep Learning (Transfer Learning) to provide real-time screening.

🌐 Live Demo
You can access the live working version of this project here:
 👉 https://huggingface.co/spaces/aarzoodahiya81/eye-disease-detection

🔍 Key Features:
Instant Analysis: Upload a retinal scan and get results in seconds.
Multi-Class Classification: Detects Cataract, Glaucoma, Diabetic Retinopathy, and Normal eye conditions.
High Precision: Built using the ResNet50V2 architecture for superior feature extraction.
User-Friendly Dashboard: A modern, glassmorphism-inspired UI built with Streamlit.

🛠️ Technical Stack
Deep Learning Framework: TensorFlow / Keras
Model Architecture: ResNet50V2 (Pre-trained on ImageNet)
Frontend: Streamlit (Python-based Web Framework)
Image Processing: PIL (Pillow), NumPy
Deployment: Hugging Face Spaces

📂 Project Structure
Plaintext
├── .gitattributes       # Git LFS configuration (if used)
├── streamlit_app.py     # Main Streamlit Application UI
├── utils.py             # Image preprocessing & model inference logic
├── requirements.txt     # Python dependencies
├── README.md            # Project Documentation
└── model/               # (Note: Large model weights are hosted on Hugging Face)
