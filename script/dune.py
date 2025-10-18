import cv2
import dlib
import numpy as np
import tkinter as tk
from tkinter import ttk, scrolledtext
import time
import math

# Constants
CAM_INDEX = 0
HOVER_TIME = 0.8
KEY_LAYOUT = [
    list("1234567890-="),
    list("qwertyuiop[]"),
    list("asdfghjkl;'"),
    list("zxcvbnm,./"),
    ["Space", "Backspace", "Enter"]
]
WINDOW_W, WINDOW_H = 1200, 800
KEY_H, KEY_SPACING = 70, 8
KB_TOP = 20

# Load Dlib's face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Eye Aspect Ratio (EAR) calculation
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# Initialize the camera
cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Initialize the Tkinter window
root = tk.Tk()
root.title("Facial Gesture Controlled Keyboard")
root.geometry(f"{WINDOW_W}x{WINDOW_H}")
root.resizable(True, True)

# Input & Answer areas
input_var = tk.StringVar()
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=12, pady=8)
entry = ttk.Entry(top_frame, textvariable=input_var, font=("Helvetica", 18))
entry.pack(side="left", fill="x", expand=True, padx=(0,8), ipady=6)

bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="both", expand=True, padx=12, pady=(0,12))
ttk.Label(bottom_frame, text="Answer Papers:").pack(anchor="w")
answer_txt = scrolledtext.ScrolledText(bottom_frame, height=8, font=("Consolas", 12))
answer_txt.pack(fill="both", expand=True)

# Canvas for keyboard
canvas_width = WINDOW_W - 40
num_rows = len(KEY_LAYOUT)
canvas_height = num_rows * (KEY_H + KEY_SPACING) + KB_TOP + 40
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#222")
canvas.pack(padx=12, pady=6)

# Create keys
keys = []
def create_keyboard():
    y = KB_TOP
    for row in KEY_LAYOUT:
        num_keys = len(row)
        key_w_dynamic = (canvas_width - (num_keys + 1) * KEY_SPACING) // num_keys
        x = KEY_SPACING
        for key in row:
            w = key_w_dynamic * 3 if key == "Space" else key_w_dynamic
            rect = (x, y, x + w, y + KEY_H)
            rect_id = canvas.create_rectangle(rect, fill="#444", outline="#999", width=2)
            text_id = canvas.create_text((x + w / 2, y + KEY_H / 2), text=key, font=("Helvetica", 14), fill="white")
            keys.append({"rect": rect, "label": key, "rect_id": rect_id, "text_id": text_id})
            x += w + KEY_SPACING
        y += KEY_H + KEY_SPACING
create_keyboard()

# Hover & press
hovered_key = None
hover_start = None
selected_key = None
hovered_key_last_pressed = None

def update_ui():
    for k in keys:
        canvas.itemconfig(k['rect_id'], fill="#444")
    if hovered_key:
        canvas.itemconfig(hovered_key['rect_id'], fill="#666")
    if selected_key:
        canvas.itemconfig(selected_key['rect_id'], fill="#2a9d8f")
    root.after(50, update_ui)

# Process facial landmarks
def process_landmarks(shape):
    global hovered_key, hover_start, hovered_key_last_pressed
    left_eye = shape[36:42]
    right_eye = shape[42:48]
    nose = shape[27:36]
    mouth = shape[48:68]

    # Eye Aspect Ratio (EAR) thresholds
    EAR_THRESHOLD = 0.25
    blinked = False

    # Calculate EAR for both eyes
    left_EAR = eye_aspect_ratio(left_eye)
    right_EAR = eye_aspect_ratio(right_eye)

    # Detect blink
    if left_EAR < EAR_THRESHOLD and right_EAR < EAR_THRESHOLD:
        blinked = True

    # Detect nod (head tilt)
    nose_tip = shape[30]
    if nose_tip[1] < 200:
        # Head nod up
        pass
    elif nose_tip[1] > 300:
        # Head nod down
        pass

    return blinked

# Main loop
def main_loop():
    global hovered_key, hover_start, hovered_key_last_pressed
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        shape = predictor(gray, face)
        blinked = process_landmarks(shape)
        if blinked:
            # Handle blink action
            pass

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return

# Start the main loop
while True:
    main_loop()

cap.release()
cv2.destroyAllWindows()
