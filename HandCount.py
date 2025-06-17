import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


def get_gesture(fingers):
    gestures = {
        (0, 1, 0, 0, 0): 1,
        (0, 1, 1, 0, 0): 2,
        (0, 1, 1, 1, 0): 3,
        (0, 1, 1, 1, 1): 4,
        (1, 1, 1, 1, 1): 5,
        (0, 0, 0, 0, 0): 0,
        (0, 0, 0, 0, 1): 1,
        (0, 0, 0, 1, 1): 2,
        (0, 0, 1, 1, 1): 3,
        (0, 0, 1, 0, 0): 1,
        (0, 0, 0, 1, 0): 1,
        (0, 0, 0, 0, 1): 1,
        (1, 0, 0, 0, 0): 1,
        (0, 1, 0, 1, 0): 2,
        (0, 1, 0, 0, 1): 2,
        (1, 1, 0, 0, 0): 2,
        (0, 1, 1, 0, 0): 2,
        (0, 0, 1, 1, 0): 2,
        (0, 0, 1, 0, 1): 2,
        (1, 0, 1, 0, 0): 2,
        (0, 1, 0, 1, 0): 2,
        (0, 0, 1, 1, 0): 2,
        (0, 0, 0, 1, 1): 2,
        (1, 0, 0, 1, 0): 2,
        (0, 1, 0, 0, 1): 2,
        (0, 0, 1, 0, 1): 2,
        (0, 0, 0, 1, 1): 2,
        (1, 0, 0, 0, 1): 2,
        (0, 1, 1, 0, 1): 3,
        (0, 1, 0, 1, 1): 3,
        (1, 1, 1, 0, 0): 3,
        (1, 1, 0, 1, 0): 3,
        (1, 1, 0, 0, 1): 3,
        (0, 1, 1, 0, 1): 3,
        (0, 0, 1, 1, 1): 3,
        (1, 0, 1, 1, 0): 3,
        (1, 0, 1, 0, 1): 3,
        (1, 0, 1, 1, 1): 4,
        (1, 1, 0, 1, 1): 4,
        (1, 1, 1, 0, 1): 4,
        (1, 1, 1, 1, 0): 4,
        (0, 1, 0, 0, 0): 1,
        (0, 1, 1, 0, 0): 2,
        (0, 1, 1, 1, 0): 3,
        (0, 1, 1, 1, 1): 4,
        (1, 1, 1, 1, 1): 5,
        (0, 0, 0, 0, 0): 0,
        (0, 0, 0, 0, 1): 1,
        (0, 0, 0, 1, 1): 2,
        (0, 0, 1, 1, 1): 3,
        (0, 0, 1, 0, 0): 1,
        (0, 0, 0, 1, 0): 1,
        (0, 0, 0, 0, 1): 1,
        (1, 0, 0, 0, 0): 1,
        (0, 1, 0, 1, 0): 2,
        (0, 1, 0, 0, 1): 2,
        (1, 1, 0, 0, 0): 2,
        (0, 1, 1, 0, 0): 2,
        (0, 0, 1, 1, 0): 2,
        (0, 0, 1, 0, 1): 2,
        (1, 0, 1, 0, 0): 2,
        (0, 1, 0, 1, 0): 2,
        (0, 0, 1, 1, 0): 2,
        (0, 0, 0, 1, 1): 2,
        (1, 0, 0, 1, 0): 2,
        (0, 1, 0, 0, 1): 2,
        (0, 0, 1, 0, 1): 2,
        (0, 0, 0, 1, 1): 2,
        (1, 0, 0, 0, 1): 2,
        (0, 1, 1, 0, 1): 3,
        (0, 1, 0, 1, 1): 3,
        (1, 1, 1, 0, 0): 3,
        (1, 1, 0, 1, 0): 3,
        (1, 1, 0, 0, 1): 3,
        (0, 1, 1, 0, 1): 3,
        (0, 0, 1, 1, 1): 3,
        (1, 0, 1, 1, 0): 3,
        (1, 0, 1, 0, 1): 3,
        (1, 0, 1, 1, 1): 4,
        (1, 1, 0, 1, 1): 4,
        (1, 1, 1, 0, 1): 4,
        (1, 1, 1, 1, 0): 4,
    }
    return gestures.get(tuple(fingers), -1)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    total_gesture = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            landmarks = hand_landmarks.landmark
            fingers = []

            
            wrist_x = landmarks[mp_hands.HandLandmark.WRIST].x
            thumb_cmc_x = landmarks[mp_hands.HandLandmark.THUMB_CMC].x
            is_right_hand = wrist_x < thumb_cmc_x

            
            thumb_tip_x = landmarks[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_ip_x = landmarks[mp_hands.HandLandmark.THUMB_IP].x
            thumb_mcp_x = landmarks[mp_hands.HandLandmark.THUMB_MCP].x

            if (is_right_hand and thumb_tip_x > thumb_ip_x and thumb_tip_x > thumb_mcp_x) or \
               (not is_right_hand and thumb_tip_x < thumb_ip_x and thumb_tip_x < thumb_mcp_x):
                fingers.append(1)
            else:
                fingers.append(0)

            
            for id_tip, id_pip in zip(
                [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP],
                [mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.PINKY_PIP]
            ):
                fingers.append(1 if landmarks[id_tip].y < landmarks[id_pip].y else 0)

            
            gesture = get_gesture(fingers)
            if gesture != -1:
                total_gesture += gesture

    if total_gesture != 0:
        cv2.putText(frame, f'{total_gesture}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
