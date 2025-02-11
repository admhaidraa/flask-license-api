from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Konfigurasi logging untuk melihat aktivitas API
logging.basicConfig(level=logging.INFO)

# Database sementara (gunakan database sungguhan di produksi)
LICENSE_DB = {
    "LISENSI-12345": "HWID-ABC123",
    "LISENSI-67890": "HWID-XYZ789"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "License API is running"}), 200

@app.route("/validate", methods=["POST"])
def validate():
    if not request.is_json:
        logging.warning("Request tidak dalam format JSON")
        return jsonify({"error": "Request harus berupa JSON"}), 400

    data = request.get_json()
    license_key = data.get("license")
    hwid = data.get("hwid")

    if not license_key or not hwid:
        logging.warning("License atau HWID tidak diisi")
        return jsonify({"error": "License dan HWID wajib diisi"}), 400

    if license_key in LICENSE_DB and LICENSE_DB[license_key] == hwid:
        logging.info(f"License valid: {license_key} untuk HWID: {hwid}")
        return jsonify({"status": "valid"}), 200

    logging.warning(f"License invalid: {license_key} untuk HWID: {hwid}")
    return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
