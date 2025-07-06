# AI-Driven-Gesture-Control-for-Games
## Project Overview
AI-Driven Gesture Control for Games is a capstone project that introduces a novel way to interact with digital games using real-time hand gestures. Instead of traditional keyboards or mouse, this project uses AI and computer vision to provide a touchless, immersive gaming experience.\
Built and tested using the popular game Hill Climb Racing, the system allows players to control game actions through natural hand gestures captured via webcam.
________________________________________
## Problem Statement
“In an age of AI and automation, why are we still clicking and tapping?”\
Traditional gaming relies heavily on physical devices . This project explores how gesture recognition powered by machine learning can revolutionize the gaming experience and enhance inclusivity.
________________________________________
## Proposed Solution
The system uses MediaPipe’s machine learning-based hand tracking model to detect 21 key hand landmarks and interpret gestures in real time.\
These gestures are then mapped to in-game controls, allowing the user to play Hill Climb Racing without physical input devices.
________________________________________
## Video Demonstration
[Click Here To See Video Demo Of Project](https://drive.google.com/file/d/1KGHzO89oW9HlPLdZhbj7wnniE5LByPZk/view?usp=drive_link)

________________________________________
## Tech Stack
•	Libraries/Frameworks:
- MediaPipe – ML-based hand tracking
- OpenCV – Real-time video processing
- NumPy – Array and matrix operations
- AutoPy – Keyboard and mouse control
- PyDirectInput – Input simulation for games
- Protobuff – Data serialization
________________________________________
## Algorithm & Gesture Mapping
### Hand Gesture Actions:
Gesture	Action
- ✋ Open Palm	Accelerate (Fuel in Hill Climb Racing)
- ✊ Fist	Apply Brakes
- ☝️ Index Finger	Move cursor in pointing direction
- 👍 Thumbs Up	Perform Left Click
### Workflow: 
1.	Webcam captures real-time video feed.
2.	MediaPipe processes and identifies hand landmarks.
3.	Custom logic interprets gesture and maps it to game control.
4.	Input is simulated using PyAutoGUI or PyDirectInput.
________________________________________
# Results
- Performance: ~30–40ms delay in gesture detection.
- Accuracy: Consistent gesture recognition under varied lighting and backgrounds.
- Adaptability: Works with different hand sizes, angles, and motion variations.
________________________________________
# Conclusion
This project successfully demonstrates how machine learning and AI can enhance user interaction in gaming.\
It promotes accessibility and offers a glimpse into the future of gesture-based interfaces across industries.
________________________________________
# Future Scope
- Global Accessibility: Assist users with physical disabilities.
- Software & AR/VR: Apply to desktops, presentations, and immersive environments.
- Healthcare: Use in operating rooms for touchless navigation.
- Consumer Electronics: Smart TVs, home automation, infotainment.
- Automotive Sector: Touch-free control of in-car systems.
________________________________________
# References
- [OpenCV GitHub](https://github.com/opencv/opencv)
- [MediaPipe Documentation](https://ai.google.dev/edge/mediapipe/solutions/guide)
________________________________________
# About the Author
Ishita Saxena\
B.Tech CSE, KIET Group Of Institutions\
Email: ishita.2428cse1823@kiet.edu\
AICTE Student ID: STU67796f57012c41736011607
________________________________________
