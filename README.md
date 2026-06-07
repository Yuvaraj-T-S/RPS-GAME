# 🎮 Rock Paper Scissors Web App (Best of 5)

An elegant web-based implementation of the classic **Rock-Paper-Scissors** game built using **Python Flask** for the backend and **HTML5, CSS3, and JavaScript** for a smooth, interactive user experience.

---

## ✨ Features

* **Modern UI Design** – Clean minimalist layout with a stylish sidebar and soft lavender-themed aesthetics.
* **Asynchronous Gameplay** – Uses JavaScript Fetch API to communicate with the Flask backend without page reloads.
* **Interactive Battle Arena** – Animated status indicators update dynamically as players make their choices.
* **Best of 5 Tournament Mode** – First player to reach 3 wins becomes the champion.
* **Responsive Experience** – Smooth gameplay across modern desktop and mobile browsers.
* **Pure CSS Visual Effects** – Ambient decorative elements and subtle animations for a polished feel.

---

## 🛠️ Project Structure

```text
RPS-GAME/
├── app.py                  # Core Flask application and game logic
├── .gitignore              # Ignored files and folders
├── README.md               # Project documentation
├── static/
│   ├── style.css           # Custom styling and animations
│   ├── rock.png            # Rock icon
│   ├── paper.png           # Paper icon
│   └── scissors.png        # Scissors icon
└── templates/
    └── index.html          # Frontend layout and JavaScript logic
```

---

## 📋 Prerequisites

### Software Requirements

* Python 3.x
* Flask
* Modern Web Browser:

  * Google Chrome
  * Mozilla Firefox
  * Microsoft Edge
  * Safari

### Hardware Requirements

* Minimum 4 GB RAM
* At least 100 MB free storage

---

## 🚀 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Yuvaraj-T-S/RPS-GAME.git
cd RPS-GAME
```

### 2. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

---

## ⚙️ How It Works

1. The player selects **Rock**, **Paper**, or **Scissors**.
2. JavaScript sends the selected choice to the Flask backend using a POST request.
3. The server generates a random choice for the computer.
4. The winner of the round is determined.
5. Scores are updated dynamically without refreshing the page.
6. The first player to reach **3 wins** wins the match.

---

## 🧰 Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript (Fetch API)

---

