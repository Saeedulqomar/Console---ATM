#drawing landmarks >>> face, hands, pose
import os

import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic


cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = holistic.process(img)


        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        #face
        mp_drawing.draw_landmarks(img, result.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                                  mp_drawing.DrawingSpec(color= (88, 78, 69), thickness=1, circle_radius=1),
                                  mp_drawing.DrawingSpec(color= (49, 65, 23), thickness=1, circle_radius=1))

        #right hand
        mp_drawing.draw_landmarks(img, result.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color= (240, 0, 0), thickness= 2, circle_radius= 2),
                                  mp_drawing.DrawingSpec(color= (0, 0, 250), thickness= 4, circle_radius= 2))

        #left hand
        mp_drawing.draw_landmarks(img, result.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color= (0, 0, 250), thickness= 2, circle_radius= 2),
                                  mp_drawing.DrawingSpec(color= (0, 255, 70), thickness= 6, circle_radius= 9))

        #pose detection
        mp_drawing.draw_landmarks(img, result.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow('Holistic', img)






        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


