import os
import numpy as np
import cv2
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Fungsi untuk memuat gambar dari folder
def load_images_from_folder(folder, label, img_size=(128, 128)):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, img_size)
            images.append(img)
            labels.append(label)
    return images, labels

# Fungsi untuk memproses gambar
def preprocess_images(images):
    images = np.array(images) / 255.0
    images = images.reshape(images.shape[0], -1)
    return images

# Fungsi untuk mendeteksi gambar
def detect_image(file_path, model):
    img = cv2.imread(file_path)
    img_resized = cv2.resize(img, (128, 128))
    img_flattened = img_resized.reshape(1, -1) / 255.0
    prediction = model.predict(img_flattened)
    return "Cat" if prediction[0] == 0 else "Dog"

# Fungsi untuk memuat gambar dan menampilkan hasil prediksi
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Menampilkan gambar di GUI
        img = Image.open(file_path)
        img_resized = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img_resized)
        panel.config(image=img_tk)
        panel.image = img_tk

        # Prediksi gambar
        result = detect_image(file_path, model)
        result_label.config(text=f"Prediction: {result}")

# Load dataset
cat_folder = r"C:\Machine Learning\Cat"
dog_folder = r"C:\Machine Learning\Dog"

cat_images, cat_labels = load_images_from_folder(cat_folder, label=0)
dog_images, dog_labels = load_images_from_folder(dog_folder, label=1)

images = cat_images + dog_images
labels = cat_labels + dog_labels

images_flat = preprocess_images(images)
X_train, X_test, y_train, y_test = train_test_split(images_flat, labels, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Membuat GUI dengan Tkinter
root = Tk()
root.title("Cat or Dog Classifier")

# Tombol untuk mengunggah gambar
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Panel untuk menampilkan gambar
panel = Label(root)
panel.pack()

# Label untuk menampilkan hasil prediksi
result_label = Label(root, text="Prediction: ", font=("Arial", 16))
result_label.pack()

# Menjalankan GUI
root.mainloop()