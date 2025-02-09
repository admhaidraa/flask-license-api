from flask import Flask, request, jsonify

app = Flask(__name__)

# Database sementara (gunakan database sungguhan di produksi)
LICENSE_DB = {
    "LISENSI-12345": "HWID-ABC123",
    "LISENSI-67890": "HWID-XYZ789"
}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    license_key = data.get("license")
    hwid = data.get("hwid")

    if license_key in LICENSE_DB and LICENSE_DB[license_key] == hwid:
        return jsonify({"status": "valid"}), 200
    return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
