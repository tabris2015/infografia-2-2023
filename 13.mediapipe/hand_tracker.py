import numpy as np
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt


INDEX_LANDMARK = 8
THUMB_LANDMARK = 4

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    # Loop through the detected hands to visualize.
    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]
        handedness = handedness_list[idx]

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
        landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
        annotated_image,
        hand_landmarks_proto,
        solutions.hands.HAND_CONNECTIONS,
        solutions.drawing_styles.get_default_hand_landmarks_style(),
        solutions.drawing_styles.get_default_hand_connections_style())
        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN

        # Draw handedness (left or right hand) on the image.
        cv2.putText(annotated_image, f"{handedness[0].category_name}",
                    (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    


    return annotated_image


cap = cv2.VideoCapture(0)

# crear detector
MODEL_PATH = "13.mediapipe/models/hand_landmarker.task"
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
# detector = vision.HandLandmarker.create_from_options(options)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")


# para usar frames de la webcam se necesita un context manager
with vision.HandLandmarker.create_from_options(options) as detector:

    while True:
        # lectura de un frame
        ret, frame = cap.read()
        # operaciones con el frame
        rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        
        # deteccion del face mesh
        detections = detector.detect(rgb_frame)

        out = frame.copy()
        # dibujar landmarks en la imagen
        out = draw_landmarks_on_image(out, detections)
        cv2.imshow("out", out)

        # detectar una tecla
        c = cv2.waitKey(1)
        # si la tecla es 'esc'
        if c == 27:
            # salir del bucle
            break

# liberar recursos
cap.release()
cv2.destroyAllWindows()
