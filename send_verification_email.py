from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Eğer ortam değişkenlerini kullanıyorsanız, bu satırı etkinleştirin.
# from dotenv import load_dotenv
# load_dotenv()

@app.route("/send-code", methods=["POST"])
def send_code():
    data = request.json
    email = data.get("email")
    code = data.get("code")

    if not email or not code:
        return jsonify({"error": "Email and code required"}), 400

    # `private_key` anahtarı, dokümantasyona göre `accessToken` olarak değiştirildi.
    # Diğer anahtarlar (`service_id`, `template_id`, `user_id`) aynı kaldı.
    response = requests.post(
        "https://api.emailjs.com/api/v1.0/email/send",
        headers={"Content-Type": "application/json"},
        json={
            "service_id": "service_29j3o7t",
            "template_id": "template_rrrzuzg",
            "user_id": "iQ8i0nyrhHe48SfaK",  # Public Key'iniz burada
            "accessToken": "URKgM7uFJI9m7S60kgFVF",  # Private Key'iniz accessToken anahtarıyla gönderiliyor
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
        # Hata mesajını daha anlaşılır hale getirelim
        print(f"EmailJS API Error: {response.text}")
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
