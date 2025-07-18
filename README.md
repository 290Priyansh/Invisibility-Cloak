# 🧙‍♂️ Invisibility Cloak using OpenCV

Bring the magic of Harry Potter into the real world using Python and OpenCV! This project captures the background and replaces the cloak-colored area with it in real-time video, creating an invisibility effect.

---
## 🛠 Tech Stack

- **Python 3** 🐍  
- **OpenCV** 🎥  
- **NumPy** 🔢

---

## 🧠 How It Works

1. **Capture background**: A few frames of the background (without the subject) are captured.
2. **Detect cloak color**: HSV color range is defined for the cloak (usually red).
3. **Create mask**: Mask is created for pixels that fall within this cloak color range.
4. **Apply invisibility**: Detected cloak region is replaced by the background pixels, making it "invisible".
