from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# NOT: Hassas anahtarları .env dosyasında saklamanız önerilir.
# Eğer kullanıyorsanız, aşağıdaki satırları etkinleştirin.
# from dotenv import load_dotenv
# load_dotenv()

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
            # Bu anahtarlar, EmailJS dokümantasyonuna göre zorunludur.
            "service_id": "service_29j3o7t", 
            "template_id": "template_rrrzuzg",
            "user_id": "iQ8i0nyrhHe48SfaK",
            
            # Sunucu tarafı doğrulama için Private Key'inizi `accessToken` olarak gönderin.
            "accessToken": "URKgM7uFJI9m7S60kgFVF",  
            
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
        print(f"EmailJS API Hata Mesajı: {response.text}")
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
