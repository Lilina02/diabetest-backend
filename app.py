# 1. IMPORT LIBRARY
# -----------------------------------------------------------------------------
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import joblib # Library untuk memuat file scaler .pkl
import os

# Mencegah pesan log TensorFlow yang tidak perlu
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 2. INISIALISASI APLIKASI FLASK
# -----------------------------------------------------------------------------
app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk seluruh API

# 3. MEMUAT MODEL DAN SCALER
# -----------------------------------------------------------------------------
# Definisikan path ke model dan scaler untuk kerapian
MODEL_PATH = 'model/model_diabetes.h5'
SCALER_PATH = 'model/scaler_diabetes.pkl'

try:
    # Memuat model Keras dan scaler Scikit-learn
    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print(">>> Model dan Scaler berhasil dimuat dari path 'model/'.")
except Exception as e:
    print(f">>> Terjadi kesalahan saat memuat model atau scaler: {e}")
    print(">>> Pastikan folder 'model' dengan file 'model_diabetes.h5' dan 'scaler_diabetes.pkl' ada.")
    model = None
    scaler = None

# 4. FUNGSI-FUNGSI PEMBANTU (HELPER FUNCTIONS)
# -----------------------------------------------------------------------------

# Definisikan rentang valid untuk validasi input
VALID_RANGES = {
    'Pregnancies': (0, 20),
    'Glucose': (70, 200),
    'BloodPressure': (40, 120),
    'SkinThickness': (10, 50),
    'Insulin': (0, 846),
    'BMI': (18, 50),
    'DiabetesPedigreeFunction': (0.078, 2.42),
    'Age': (0, 100)
}
# Daftar fitur yang diharapkan oleh model
EXPECTED_FEATURES = list(VALID_RANGES.keys())

def validate_input(data):
    """Memvalidasi data input dari pengguna (tipe data, kelengkapan, dan rentang)."""
    errors = []
    
    # Cek kelengkapan field
    for field in EXPECTED_FEATURES:
        if field not in data:
            errors.append(f"Field yang wajib diisi '{field}' tidak ditemukan.")
    if errors: return False, errors

    # Cek tipe data dan rentang nilai
    for field, value in data.items():
        if field not in VALID_RANGES: continue
        try:
            value = float(value)
            data[field] = value
        except (ValueError, TypeError):
            errors.append(f"Nilai untuk '{field}' harus berupa angka.")
            continue
        
        min_val, max_val = VALID_RANGES[field]
        if not (min_val <= value <= max_val):
            errors.append(f"Nilai untuk '{field}' harus di antara {min_val} dan {max_val}.")
    
    return not errors, errors

def get_risk_level_and_recommendations(probability, input_data):
    """Menentukan level risiko dan memberikan rekomendasi yang dipersonalisasi."""
    recommendations = []
    
    # Tentukan level risiko
    if probability < 0.3:
        risk_level = 'Rendah'
        recommendations.append("Bagus! Pertahankan gaya hidup sehat Anda dengan olahraga teratur dan pola makan seimbang.")
        recommendations.append("Lakukan pemeriksaan gula darah secara rutin setidaknya setahun sekali sebagai langkah pencegahan.")
    elif probability < 0.7:
        risk_level = 'Sedang'
        recommendations.append("Segera konsultasikan dengan dokter untuk pemeriksaan dan saran lebih lanjut.")
        recommendations.append("Tingkatkan aktivitas fisik Anda, targetkan minimal 150 menit per minggu (contoh: jalan cepat, bersepeda).")
        recommendations.append("Kurangi konsumsi makanan dan minuman dengan indeks glikemik tinggi seperti nasi putih, roti tawar, dan minuman manis.")
    else:
        risk_level = 'Tinggi'
        recommendations.append("Sangat disarankan untuk segera menemui dokter untuk diagnosis medis yang akurat dan penanganan lebih lanjut.")
        recommendations.append("Penting untuk memantau kadar gula darah Anda secara teratur sesuai anjuran dokter.")
        recommendations.append("Ikuti program diet dan olahraga yang dirancang khusus oleh ahli kesehatan atau ahli gizi.")
    
    # Rekomendasi spesifik berdasarkan input
    if input_data.get('Glucose', 0) > 140:
        recommendations.append("Perhatian khusus pada kadar glukosa Anda yang tinggi. Batasi asupan gula dan karbohidrat sederhana secara signifikan.")
    if input_data.get('BMI', 0) > 30:
        recommendations.append("BMI Anda berada dalam kategori obesitas, yang merupakan faktor risiko utama. Pertimbangkan untuk mengikuti program penurunan berat badan yang sehat dan terstruktur.")
    if input_data.get('Age', 0) > 45:
        recommendations.append("Mengingat usia Anda, risiko diabetes secara alami meningkat. Pastikan untuk melakukan pemeriksaan kesehatan (medical check-up) secara rutin.")
        
    return risk_level, recommendations

# 5. ENDPOINTS API
# -----------------------------------------------------------------------------

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint utama untuk melakukan prediksi diabetes."""
    if not model or not scaler:
        return jsonify({'status': 'error', 'message': 'Model atau scaler tidak berhasil dimuat. Periksa log server.'}), 500

    try:
        data = request.json
        is_valid, errors = validate_input(data)
        if not is_valid:
            return jsonify({'status': 'error', 'message': 'Input tidak valid.', 'errors': errors}), 400
        
        # Susun data dalam urutan yang benar sesuai dengan pelatihan model
        input_features = np.array([data[feature] for feature in EXPECTED_FEATURES]).reshape(1, -1)
        
        # Standarisasi input menggunakan scaler yang telah dimuat
        input_scaled = scaler.transform(input_features)
        
        # Lakukan prediksi
        prediction_prob = float(model.predict(input_scaled)[0][0])
        
        # Dapatkan level risiko dan rekomendasi
        risk_level, recommendations = get_risk_level_and_recommendations(prediction_prob, data)
        
        # Siapkan respons JSON yang lengkap
        result = {
            'status': 'success',
            'prediction_result': {
                'probability': round(prediction_prob, 4),
                'is_diabetic': bool(prediction_prob >= 0.5),
                'risk_level': risk_level,
                'recommendations': recommendations
            }
        }
        return jsonify(result)
    
    except Exception as e:
        print(f"Error pada /predict: {e}")
        return jsonify({'status': 'error', 'message': 'Terjadi kesalahan internal pada server.'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint untuk health check API."""
    return jsonify({'status': 'ok', 'message': 'DiabeTest API is running'})

@app.route('/', methods=['GET'])
def index():
    """Endpoint root untuk informasi API."""
    return jsonify({
        'api_name': 'DiabeTest API',
        'version': '2.0.0',
        'description': 'API untuk prediksi diabetes menggunakan model Deep Learning dengan validasi dan rekomendasi.',
    })

# 6. MENJALANKAN SERVER
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
