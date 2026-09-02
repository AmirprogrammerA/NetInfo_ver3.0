# 🔧 NetInfo v3.0 (Mobile Edition)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Android-brightgreen.svg)
![IDE](https://img.shields.io/badge/IDE-Pydroid_3-orange.svg)
![GUI](https://img.shields.io/badge/GUI-Pygame-red.svg)

**NetInfo v3.0** is a specialized networking diagnostic tool specifically designed for Android users. It provides a beautiful, interactive graphical interface to fetch real-time network details directly on your smartphone via **Pydroid 3**.

---

## ✨ Key Features

- 🖥️ **Modern GUI:** A custom-built interface using `pygame` for a smooth, touch-friendly experience.
- 🌐 **Comprehensive Network Info:**
    - **Local IP Address:** Your device's address on the current network.
    - **MAC Address:** Hardware identifier of your interface.
    - **Default Gateway:** The router address managing your connection.
    - **DNS Server:** Information about your Domain Name System.
- 🔄 **One-Tap Refresh:** Easily update information without restarting the app.
- 📱 **Mobile Optimized:** High-contrast colors and large buttons designed for mobile screens.

---

## 🛠️ Installation & Setup (Pydroid 3)

Since this tool is designed for mobile environments, please follow these exact steps to ensure it runs correctly:

### 1. Install Pydroid 3
Download and install **[Pydroid 3 - IDE for Python 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)** from the Google Play Store.

### 2. Install Required Library
This project uses `pygame` for the graphical user interface. You **must** install it via Pydroid's terminal/pip:
1. Open **Pydroid 3**.
2. Open the **Menu** (three horizontal lines) $\rightarrow$ **Pip**.
3. In the **Library name** field, type: `pygame`
4. Tap **Install**.

### 3. Running the Tool
1. Download the `netinfo.py` file to your phone.
2. In Pydroid 3, go to **Open** $\rightarrow$ **Internal Storage** $\rightarrow$ Navigate to your file.
3. Select `netinfo.py`.
4. Tap the **Play Button** (🟡) to launch the interface.

---

## 🖥️ User Interface Guide

- **Display Area:** Shows your current Network configuration (IP, MAC, etc.).
- **Refresh Button:** Tap this to re-scan the network and update the displayed data.
- **Exit Button:** Safely closes the application.

---

## 🚀 Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **ModuleNotFoundError: No module named 'pygame'** | Go to Pydroid $\rightarrow$ Pip $\rightarrow$ Install `pygame`. |
| **Blank Screen/Black Screen** | Ensure you have granted Pydroid 3 permission to access storage and network. |
| **Permission Denied** | Make sure you are running the script from a folder with read/write permissions. |

---

.

---

## 📜 License
Distributed under the MIT License.

## 👨‍💻 Author
**Amir (Amir-93)**
- GitHub: [@AmirprogrammerA](https://github.com/AmirprogrammerA)
- Specialized in Python, Custom OS, and Mobile Tooling.
 
