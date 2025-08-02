from flask import Flask, request, jsonify
import requests
import os # Ortam değişkenlerini kullanmak için

# Eğer ortam değişkenlerini kullanıyorsanız
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)

@app.route("/send-code", methods=["POST"])
def send_code():
    data = request.json
    email = data.get("email")
    code = data.get("code")

    if not email or not code:
        return jsonify({"error": "Email and code required"}), 400

    # ✅ Düzeltme burada yapılıyor:
    # `user_id` alanını `public_key` ile doldurun,
    # `private_key` alanını da kendi Private Key'inizle doldurun.
    response = requests.post(
        "https://api.emailjs.com/api/v1.0/email/send",
        headers={"Content-Type": "application/json"},
   json={
    "service_id": "service_29j3o7t",
    "template_id": "template_rrrzuzg",
    "user_id": "iQ8i0nyrhHe48SfaK",  # Public Key'iniz burada
    "private_key": "URkgM7ufJ9m7560kgPVF", # Private Key'iniz burada
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
