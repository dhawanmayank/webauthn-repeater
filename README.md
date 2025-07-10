# 🧩 WebAuthn Repeater Burp Extension

A lightweight Burp Suite extension for manually editing and decoding WebAuthn request payloads such as `clientDataJSON`, `attestationObject`, and `authenticatorData`.

---

## 📦 Features

- Adds a new **WebAuthn** tab in Burp's Repeater
- Automatically detects and decodes WebAuthn JSON blobs
- Pretty-prints base64url-decoded content
- Helps in analyzing passkey registration and login flows

---

## 🛠 Installation

1. Download and install **Jython**:
   - Download: https://www.jython.org/download
   - Recommended: `jython-standalone-2.7.2.jar`

2. Configure Jython in Burp:
   - `Extender → Options → Python Environment`
   - Set path to Jython standalone JAR

3. Load this extension:
   - `Extender → Extensions → Add`
   - Extension Type: `Python`
   - File: `WebAuthnRepeater.py`

---

## 🔍 Usage

- Open any intercepted request/response with WebAuthn data.
- Switch to the **WebAuthn** tab to view decoded content.
- Great for use with the [`passkeys-vuln-lab`](https://github.com/dhawanmayank/passkeys-vuln-lab).

---

## 🧪 Tested On

- Burp Suite Community/Pro 2023+
- Python (via Jython)
- Chrome + WebAuthn test requests

---

## 📜 License

MIT License
