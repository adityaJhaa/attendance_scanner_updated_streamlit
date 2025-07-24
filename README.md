# Face Attendance System using Face Recognition

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-orange)

## Overview
This project is a Face Recognition-based Attendance Management System built with Python, OpenCV, and Tkinter for the desktop UI, and Streamlit for a modern web UI. It allows you to register students, train a face recognition model, mark attendance automatically using a webcam or camera input, and view attendance records.

## Features
- **Register New Students**: Capture face images and store student details.
- **Train Model**: Train a face recognition model using the registered images.
- **Automatic Attendance**: Mark attendance by recognizing faces in real-time (Tkinter) or from camera input (Streamlit demo).
- **View Attendance**: Display attendance records in tabular format.
- **Modern Web UI**: Use Streamlit for a browser-based experience.

## Project Structure
```
Attendance-Management-system-using-face-recognition/
├── attendance.py                # Main Tkinter GUI
├── app_streamlit.py             # Streamlit web app
├── automaticAttedance.py        # Attendance logic
├── takeImage.py                 # Image capture logic
├── trainImage.py                # Model training logic
├── show_attendance.py           # Attendance viewing logic
├── requirements.txt             # Python dependencies
├── StudentDetails/
│   └── studentdetails.csv       # Student info
├── TrainingImage/               # Registered face images
├── TrainingImageLabel/
│   └── Trainner.yml             # Trained model
├── Attendance/                  # Attendance CSVs
├── UI_Image/                    # UI images
└── ...
```

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Attendance-Management-system-using-face-recognition
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **(Optional) For Streamlit Web UI**
   ```bash
   pip install streamlit
   ```

## Usage
### Desktop (Tkinter) App
1. Run the main app:
   ```bash
   python attendance.py
   ```
2. Use the GUI to register students, train the model, mark attendance, and view records.

### Web (Streamlit) App
1. Run the Streamlit app:
   ```bash
   python -m streamlit run app_streamlit.py
   ```
2. Open your browser at [http://localhost:8501](http://localhost:8501)
3. Use the sidebar to:
   - Register new students (with camera input)
   - Train the model
   - (Demo) Mark attendance from a photo
   - View attendance records

## Notes
- The Streamlit app currently demonstrates registration, training, and attendance viewing. Attendance from a static image is a placeholder and requires further adaptation for real face recognition.
- All data (images, models, CSVs) are stored locally in the project folders.
- For best results, provide clear, well-lit face images during registration.

## Requirements
- Python 3.9+
- OpenCV
- Pillow
- Pandas
- Streamlit (for web UI)
- pyttsx3 (for text-to-speech)

Install all requirements with:
```bash
pip install -r requirements.txt
pip install streamlit
```

## Screenshots
> Add screenshots of the desktop and web UI here for better documentation.

## License
This project is for educational purposes. Feel free to use and modify it.

## Author
Made by Aditya ([GitHub](https://github.com/adityaJhaa))


