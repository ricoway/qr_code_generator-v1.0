from flask import Flask, render_template, request, send_from_directory, jsonify, url_for
import qrcode
import os
import uuid
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx', 'xls', 'xlsx'}
METADATA_FILE = 'metadata.json'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f)

NGROK_URL = 'https://1caa-103-189-206-122.ngrok-free.app'  # Ganti URL ngrok setiap kali program di jalankan, sesuai url pada terminal command prompt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    token = request.args.get('token')
    metadata = load_metadata()
    filename = metadata.get(token)
    if filename and allowed_file(filename):
        return render_template('upload.html', filename=filename, token=token)
    else:
        return render_template('upload.html', filename=None, token=token)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    metadata = load_metadata()
    data = request.form.get('data')
    token = uuid.uuid4().hex
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            data = f"{NGROK_URL}/upload?token={token}"
            metadata[token] = filename

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_path = os.path.join(UPLOAD_FOLDER, 'qrcode.png')
    img.save(img_path)

    save_metadata(metadata)

    return jsonify({'url': url_for('uploaded_file', filename='qrcode.png')})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
