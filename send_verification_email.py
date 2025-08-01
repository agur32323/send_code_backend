from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/send-code", methods=["POST"])
def send_code():
    data = request.json
    email = data.get("email")
    code = data.get("code")

    if not email or not code:
        return jsonify({"error": "Email and code required"}), 400
    response = requests.post(
        "https://api.emailjs.com/api/v1.0/email/send",
        headers={"Content-Type": "application/json"},
        json={
            "service_id": "service_29j3o7t",
            "template_id": "template_rrrzuzg",
            "public_key": "iQ8i0nyrhHe48SfaK",  # ✅ Buraya dikkat!
            "template_params": {
                "name": "Doğrulama Sistemi",
                "email": email,
                "to_email": email,
                "message": code,
            }
        },
    )

    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
