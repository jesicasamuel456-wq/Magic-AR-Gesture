# ✨ Magic-AR-Gesture

### 🖐️ Turn Hand Gestures into 3D Magic!

Magic-AR-Gesture is an interactive, webcam-based project that uses real-time hand tracking to control and display 3D models. It combines computer vision and 3D graphics to create an engaging, gesture-controlled experience directly in the browser.

## 🚀 Features

- 🖐️ **Real-Time Hand Tracking** — Detects hand landmarks using MediaPipe.
- ☝️ **Gesture-Based Controls** — Uses finger counts to select different 3D models.
- 🐉 **Interactive 3D Models** — Display models such as a dragon, butterfly, flower, rose, and eagle.
- 🔍 **Zoom Interaction** — Use two hands to control the model's scale.
- 🔄 **Rotation** — Move your hands to interact with the 3D scene.
- ✨ **Visual Effects** — Sparkles, glowing particles, and motion trails.
- 🎥 **Webcam Integration** — Uses your camera for live gesture detection.

*Note: Features depend on the current implementation and available 3D assets.*

## 🛠️ Tech Stack

- **JavaScript** — Application logic
- **Three.js** — 3D rendering
- **MediaPipe Tasks Vision** — Hand landmark detection
- **Vite** — Development server and build tool
- **HTML5 & CSS3** — Web interface
- **GLB / glTF** — 3D model assets

## 📁 Project Structure

```text
Magic-AR-Gesture/
├── index.html
├── package.json
├── package-lock.json
├── public/
│   └── hand_landmarker.task
├── models/
│   ├── dragon.glb
│   ├── butterfly.glb
│   ├── flower.glb
│   ├── rose.glb
│   └── eagle.glb
├── src/
│   └── main.js
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jesicasamuel456-wq/Magic-AR-Gesture.git
```

### 2. Open the project folder

```bash
cd Magic-AR-Gesture
```

### 3. Install dependencies

```bash
npm install
```

### 4. Start the development server

```bash
npx vite
```

### 5. Open the application

Visit the local URL shown in your terminal, usually:

`http://localhost:5173/`

Allow camera access when your browser asks for permission.

## 🎮 Gesture Controls

| Gesture | Intended action |
|---|---|
| ☝️ 1 finger | Display dragon |
| ✌️ 2 fingers | Display butterfly |
| 🤟 3 fingers | Display flower |
| 🖖 4 fingers | Display rose |
| 🖐️ 5 fingers | Display eagle |
| ✊ Closed fist | Hide the model |
| 🤲 Two hands | Zoom and rotate interaction |

## 📋 Requirements

- Node.js and npm
- A modern browser such as Chrome
- A working webcam
- Internet access during initial dependency installation
- Required 3D model files and the MediaPipe hand landmark model

## 🎯 Project Goal

The goal of Magic-AR-Gesture is to explore natural human-computer interaction by combining hand tracking with real-time 3D graphics. It demonstrates how computer vision can make web experiences more interactive and intuitive.

## 🔮 Future Improvements

- Improve gesture recognition accuracy.
- Add more 3D models and customizable effects.
- Optimize rendering and tracking performance.
- Improve compatibility across devices.
- Deploy a live web demo.

## 👩‍💻 Author

**Jesica Samuel**

GitHub: [@jesicasamuel456-wq](https://github.com/jesicasamuel456-wq)

Project Repository: [Magic-AR-Gesture](https://github.com/jesicasamuel456-wq/Magic-AR-Gesture)

---

⭐ If you find this project interesting, consider giving the repository a star!

*Built with curiosity, creativity, and a passion for AI and interactive technology.* ✨
