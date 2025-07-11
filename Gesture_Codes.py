import sys
import cv2
import mediapipe
import numpy
import autopy
import pydirectinput as p1

#cap = cv2.VideoCapture(0) #make this '0' if you get assertion error 
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# detector = HandDetector(detectionCon=0.8,maxHands=2)
initHand = mediapipe.solutions.hands  # Initializing mediapipe
# Object of mediapipe with "arguments for the hands module"
mainHand = initHand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
draw = mediapipe.solutions.drawing_utils  # Object to draw the connections between each finger index
wScr, hScr = autopy.screen.size()  # Outputs the high and width of the screen (1920 x 1080)
pX, pY = 0, 0  # Previous x and y location
cX, cY = 0, 0  # Current x and y location

def handLandmarks(colorImg):
    landmarkList = []  # Default values if no landmarks are tracked
    landmarkPositions = mainHand.process(colorImg)  # Object for processing the video input
    landmarkCheck = landmarkPositions.multi_hand_landmarks  # Stores the out of the processing object (returns False on empty)
    if landmarkCheck:  # Checks if landmarks are tracked
        for hand in landmarkCheck:  # Landmarks for each hand
            for index, landmark in enumerate(
                    hand.landmark):  # Loops through the 21 indexes and outputs their landmark coordinates (x, y, & z)
                draw.draw_landmarks(img, hand,
                                    initHand.HAND_CONNECTIONS)  # Draws each individual index on the hand with connections
                h, w, c = img.shape  # Height, width and channel on the image
                centerX, centerY = int(landmark.x * w), int(
                    landmark.y * h)  # Converts the decimal coordinates relative to the image for each index
                landmarkList.append([index, centerX, centerY])
            # h, w, c = colorImg.shape  # Use colorImg instead of img (since draw is removed)
            # for index, landmark in enumerate(hand.landmark):
            #     centerX, centerY = int(landmark.x * w), int(landmark.y * h)
            #     landmarkList.append([index, centerX, centerY])
              # Adding index and its coordinates to a list
    return landmarkList

def fingers(landmarks):
    fingerTips = []  # To store 4 sets of 1s or 0s
    tipIds = [4, 8, 12, 16, 20]  # Indexes for the tips of each finger
    # Check if thumb is up
    if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)
    # Check if fingers are up except the thumb
    for id in range(1, 5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:  # Checks to see if the tip of the finger is higher than the joint
            fingerTips.append(1)
        else:
            fingerTips.append(0)
    return fingerTips

frameCount = 0

while True:
    check, img = cap.read() 
    img = cv2.resize(img, (640, 480))
 # Reads frames from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
    lmList = handLandmarks(imgRGB)


    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
        x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
        finger = fingers(lmList)  # Calling the fingers function to check which fingers are up

        if finger[1] == 1 and finger[2] == 0 and finger[4] ==0:  # Checks to see if the pointing finger is up and thumb finger is down
            x3 = numpy.interp(x1, (75, 640 - 75),(0, wScr))  # Converts the width of the window relative to the screen width
            y3 = numpy.interp(y1, (75, 480 - 75),(0, hScr))  # Converts the height of the window relative to the screen height

            # cX = pX + (x3 - pX) / 7  # Stores previous x locations to update current x location
            # cY = pY + (y3 - pY) / 7  # Stores previous y locations to update current y location
            cX, cY = x3, y3
            autopy.mouse.move(wScr - cX,cY)  # Function to move the mouse to the x3 and y3 values (wSrc inverts the direction)
            pX, pY = cX, cY  # Stores the current x and y location as previous x and y location for next loop



        if finger[1] == 0 and finger[0] == 1 :  # Checks to see if the pointer finger is down and thumb finger is up
             p1.click(button = 'left')
        
        if sum(finger) == 5:
             p1.keyDown("right")
             p1.keyUp("left")
        
        elif sum(finger) == 0:
             p1.keyDown("left")
             p1.keyUp("right")
        elif finger[1] == 1 and finger[2] == 1 and finger[3] == 1:
             p1.press("space")
        elif finger[1]==1:
             p1.keyUp("right")
             p1.keyUp("left")

    cv2.imshow("Webcam", img)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
try:
    cv2.release()
except:
    sys.exit()
cv2.destroyAllWindows()
