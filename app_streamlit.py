import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import os
import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINING_IMAGE_DIR = os.path.join(BASE_DIR, "TrainingImage")
TRAINING_LABEL_PATH = os.path.join(BASE_DIR, "TrainingImageLabel", "Trainner.yml")
STUDENT_CSV = os.path.join(BASE_DIR, "StudentDetails", "studentdetails.csv")
ATTENDANCE_DIR = os.path.join(BASE_DIR, "Attendance")
CASCADE_PATH = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")



st.set_page_config(page_title="Face Attendance System", layout="centered")
st.title("Face Based Attendance System")

menu = ["Register New Student", "Train Images", "Take Attendance", "View Attendance"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register New Student":
    st.header("Register New Student")
    name = st.text_input("Enter Name")
    enroll = st.text_input("Enter Enrollment No")
    img_file = st.camera_input("Take a picture")
    if st.button("Save Image"):
        if name and enroll and img_file:
            img = Image.open(img_file)
            save_dir = os.path.join(TRAINING_IMAGE_DIR, f"{enroll}_{name}")
            os.makedirs(save_dir, exist_ok=True)
            img.save(os.path.join(save_dir, f"{name}_{enroll}_1.jpg"))
            st.success(f"Image saved for {name}")
            # Optionally, append to studentdetails.csv
            if not os.path.exists(STUDENT_CSV):
                pd.DataFrame([[enroll, name]], columns=["Enrollment", "Name"]).to_csv(STUDENT_CSV, index=False)
            else:
                df = pd.read_csv(STUDENT_CSV)
                if not ((df["Enrollment"] == enroll) & (df["Name"] == name)).any():
                    df = df.append({"Enrollment": enroll, "Name": name}, ignore_index=True)
                    df.to_csv(STUDENT_CSV, index=False)

        else:
            st.warning("Please enter all details and take a picture.")

elif choice == "Train Images":
    st.header("Train Images")
    if st.button("Train Model"):
        try:
            import trainImage
            trainImage.TrainImage(CASCADE_PATH, TRAINING_IMAGE_DIR, TRAINING_LABEL_PATH, None, None)
            st.success("Model trained successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

elif choice == "Take Attendance":
    st.header("Take Attendance")
    subject = st.text_input("Enter Subject Name")
    img_file = st.camera_input("Show your face to mark attendance")
    if st.button("Mark Attendance"):
        if subject and img_file:
            try:
                import automaticAttedance
                # You would need to adapt automaticAttedance to work with a single image, not webcam
                st.info("Attendance marking from static image is not implemented in this demo.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter subject and take a picture.")

elif choice == "View Attendance":
    st.header("View Attendance")
    if os.path.exists(ATTENDANCE_DIR):
        files = [f for f in os.listdir(ATTENDANCE_DIR) if f.endswith('.csv')]
        if files:
            file = st.selectbox("Select Attendance File", files)
            if file:
                df = pd.read_csv(os.path.join(ATTENDANCE_DIR, file))
                st.dataframe(df)
        else:
            st.info("No attendance files found.")
    else:
        st.info("Attendance directory does not exist.")

# Footer with author and GitHub icon
footer = '''
---
<div style="text-align:center; padding-top: 20px;">
  <span style="font-size:18px; color:#888;">Made by Aditya Jha</span>
  <a href="https://github.com/adityaJhaa" target="_blank" style="margin-left:10px; vertical-align:middle;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="28" style="vertical-align:middle;"/>
  </a>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)
