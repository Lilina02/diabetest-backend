# DiabeTest Backend

Selamat datang di repositori frontend untuk aplikasi DiabeTest! Aplikasi ini adalah platform web interaktif untuk memprediksi risiko diabetes.

## Tentang Proyek

DiabeTest adalah aplikasi web yang dirancang untuk deteksi risiko diabetes secara mandiri. Frontend ini menyediakan antarmuka pengguna yang responsif, memungkinkan pengguna memasukkan data kesehatan dan melihat hasil prediksi dari backend.

## Fitur Utama

* Antarmuka pengguna interaktif dan responsif.
* Formulir input data kesehatan untuk prediksi risiko.
* Tampilan hasil prediksi yang jelas.
* Mudah diakses melalui web browser di berbagai perangkat.

## Demo Aplikasi

Anda bisa mencoba aplikasi DiabeTest secara langsung di:
[DiabeTest Live Demo](https://diabetest-frontend-8ugr-git-master-lilina02s-projects.vercel.app/)

## Teknologi yang Digunakan

* **Framework UI:** React.js
* **Build Tool:** Vite
* **Styling:** [Sertakan nama library CSS/UI yang Anda gunakan, misal: Bootstrap]
* **Deployment:** Vercel

## Instalasi dan Menjalankan Proyek

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah di bawah:

### Prasyarat

* [Node.js](https://nodejs.org/) (direkomendasikan versi LTS terbaru)
* [npm](https://www.npmjs.com/) atau [yarn](https://yarnpkg.com/)

### Langkah-langkah

1.  **Clone repositori:**
    ```bash
    git clone [https://github.com/Lilina02/diabetest-frontend.git](https://github.com/Lilina02/diabetest-frontend.git)
    cd diabetest-frontend
DiabeTest Backend

Selamat datang di repositori backend untuk aplikasi DiabeTest! Backend ini mengelola logika inti prediksi risiko diabetes menggunakan Machine Learning.

## Daftar Isi
- [Tentang Proyek](#tentang-proyek)
- [Status Deployment](#status-deployment)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi dan Menjalankan Proyek](#instalasi-dan-menjalankan-proyek)
- [API Endpoints](#api-endpoints)
- [Struktur Proyek](#struktur-proyek)
- [Kontak](#kontak)

## Tentang Proyek

Backend DiabeTest adalah API yang dibangun dengan Flask. Tugas utamanya adalah menerima data kesehatan dari frontend, memprosesnya menggunakan model Machine Learning (TensorFlow) yang sudah dilatih, dan mengembalikan prediksi risiko diabetes.

## Status Deployment

Backend ini sudah berhasil di-deploy dan dapat diakses publik melalui Railway.

* **URL API:** [https://diabetest-backend-production.up.railway.app](https://diabetest-backend-production.up.railway.app)
* **Informasi API:**
    ```json
    {
      "api_name": "DiabeTest API",
      "description": "API untuk prediksi diabetes menggunakan model Deep learning dengan validasi dan rekomendasi.",
      "version": "2.0.0"
    }
    ```

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python [Sertakan versi Python Anda, misal: 3.9+]
* **Framework API:** Flask
* **Machine Learning:** TensorFlow
* **Preprocessing:** Pandas, NumPy, Scikit-learn
* **Package Manager:** pip
* **Deployment:** Railway
* **Tools:** VSCode, Jupyter Notebook, Postman

## Instalasi dan Menjalankan Proyek

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan backend ini secara lokal.

### Prasyarat

Pastikan Anda memiliki [Python](https://www.python.org/downloads/) terinstal. Direkomendasikan untuk menggunakan virtual environment.

### Langkah-langkah

1.  **Clone repositori:**
    ```bash
    git clone [https://github.com/Lilina02/diabetest-backend.git](https://github.com/Lilina02/diabetest-backend.git)
    cd diabetest-backend
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    # Di Windows:
    .\venv\Scripts\activate
    # Di macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *Pastikan file `requirements.txt` Anda sudah diperbarui dan mencakup semua dependensi.*

4.  **Jalankan aplikasi Flask:**
    ```bash
    flask run
    # atau, jika Anda menjalankan langsung app.py
    # python app.py
    ```
    API akan berjalan di `http://localhost:5000`.

## API Endpoints

Berikut adalah endpoint utama yang disediakan oleh API ini:

### `POST /predict`

* **Deskripsi:** Menerima data kesehatan pengguna dan mengembalikan prediksi risiko diabetes.
* **Metode:** `POST`
* **URL Contoh:** `http://localhost:5000/predict` (atau URL deployment Railway Anda)
* **Body Request (JSON):**
    ```json
    {
        "Pregnancies": [Jumlah Kehamilan (int)],
        "Glucose": [Kadar Glukosa (int)],
        "BloodPressure": [Tekanan Darah (int)],
        "SkinThickness": [Ketebalan Kulit (int)],
        "Insulin": [Kadar Insulin (int)],
        "BMI": [BMI (float)],
        "DiabetesPedigreeFunction": [Riwayat Keluarga (float)],
        "Age": [Usia (int)]
    }
    ```
    *Ganti dengan parameter input yang sesuai dengan model Anda, sesuai dengan yang diterima di `app.py`.*
* **Contoh Response (JSON):**
    ```json
    {
        "prediction": "Risiko Diabetes Rendah"
    }
    ```
    Atau
    ```json
    {
        "prediction": "Risiko Diabetes Tinggi"
    }
    ```
    *Sesuaikan dengan output prediksi model Anda.*

## Struktur Proyek

diabetest-backend/
├── model/                  # Direktori untuk model ML yang sudah dilatih dan scaler
│   ├── model_diabetes.h5   # Model TensorFlow/Keras
│   └── scaler_diabetes.pkl # Objek scaler (misal: StandardScaler)
├── Procfile                # Konfigurasi untuk deployment (Railway)
├── app.py                  # File utama aplikasi Flask API
└── requirements.txt        # Daftar dependensi Python

## Kontak

Untuk pertanyaan, silakan hubungi:
* TEAM CAPSTONE DICODING CC25 - CF024
