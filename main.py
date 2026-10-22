import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from config import MODEL_PATH, OBJECTS
from gesture import count_fingers, is_fist
from renderer import overlay_transparent


# ============================================================
# MEDIAPIPE SETUP
# ============================================================

base_options = python.BaseOptions(
    model_asset_path=str(MODEL_PATH)
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,

    # IMPORTANT:
    # We are using detect_for_video()
    running_mode=vision.RunningMode.VIDEO,

    num_hands=2,

    min_hand_detection_confidence=0.6,
    min_hand_presence_confidence=0.6,
    min_tracking_confidence=0.6
)

detector = vision.HandLandmarker.create_from_options(
    options
)


# ============================================================
# LOAD AR OBJECTS
# ============================================================

objects = {}

for finger_count, information in OBJECTS.items():

    image_path = information["file"]

    image = cv2.imread(
        str(image_path),
        cv2.IMREAD_UNCHANGED
    )

    if image is None:

        print(
            f"WARNING: Could not load {image_path}"
        )

    else:

        print(
            f"Loaded: {information['name']}"
        )

        objects[finger_count] = image


# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("ERROR: Could not open webcam.")

    detector.close()

    exit()


cap.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    1280
)

cap.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    720
)


# ============================================================
# TIMESTAMP
# ============================================================

timestamp_ms = 0


# ============================================================
# SMOOTHING
# ============================================================

previous_x = None
previous_y = None

SMOOTHING = 0.25


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    success, frame = cap.read()

    if not success:

        print(
            "Could not read camera frame."
        )

        break


    # Mirror camera
    frame = cv2.flip(
        frame,
        1
    )

    height, width = frame.shape[:2]


    # ========================================================
    # MEDIAPIPE IMAGE
    # ========================================================

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )


    # ========================================================
    # VIDEO TIMESTAMP
    # ========================================================

    timestamp_ms += 33


    result = detector.detect_for_video(
        mp_image,
        timestamp_ms
    )


    hands = result.hand_landmarks


    # ========================================================
    # DEFAULT STATE
    # ========================================================

    selected_object = None

    object_x = None
    object_y = None


    # ========================================================
    # HAND DETECTION
    # ========================================================

    if hands:

        # ----------------------------------------------------
        # CHECK IF ANY HAND IS A FIST
        # ----------------------------------------------------

        fist_detected = False

        for hand in hands:

            if is_fist(hand):

                fist_detected = True
                break


        # ----------------------------------------------------
        # IF FIST → HIDE OBJECT
        # ----------------------------------------------------

        if not fist_detected:

            # Use first detected hand
            hand = hands[0]

            fingers = count_fingers(hand)


            # ------------------------------------------------
            # SELECT OBJECT
            # ------------------------------------------------

            if fingers in objects:

                selected_object = objects[fingers]


                # ------------------------------------------------
                # INDEX FINGERTIP POSITION
                # MediaPipe landmark 8 = index fingertip
                # ------------------------------------------------

                index_tip = hand[8]

                target_x = int(
                    index_tip.x * width
                )

                target_y = int(
                    index_tip.y * height
                )


                # ------------------------------------------------
                # SMOOTH POSITION
                # ------------------------------------------------

                if previous_x is None:

                    previous_x = target_x
                    previous_y = target_y

                else:

                    previous_x = (
                        previous_x * (1 - SMOOTHING)
                        +
                        target_x * SMOOTHING
                    )

                    previous_y = (
                        previous_y * (1 - SMOOTHING)
                        +
                        target_y * SMOOTHING
                    )


                object_x = int(previous_x)
                object_y = int(previous_y)


            # ------------------------------------------------
            # SHOW FINGER COUNT
            # ------------------------------------------------

            cv2.putText(
                frame,
                f"Fingers: {fingers}",
                (40, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )


        else:

            # Fist
            cv2.putText(
                frame,
                "FIST - OBJECT HIDDEN",
                (40, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )


    else:

        cv2.putText(
            frame,
            "SHOW YOUR HAND",
            (40, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )


    # ========================================================
    # DRAW AR OBJECT
    # ========================================================

    if (
        selected_object is not None
        and object_x is not None
        and object_y is not None
    ):

        frame = overlay_transparent(
            frame,
            selected_object,
            object_x,
            object_y,
            width=260
        )


    # ========================================================
    # PROJECT TITLE
    # ========================================================

    cv2.putText(
        frame,
        "MAGIC AR",
        (40, height - 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2
    )


    cv2.putText(
        frame,
        "1 Dragon | 2 Butterfly | 3 Flower | 4 Rose | 5 Eagle",
        (40, height - 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )


    # ========================================================
    # DISPLAY
    # ========================================================

    cv2.imshow(
        "Magic AR - Gesture Controlled Objects",
        frame
    )


    # ESC TO EXIT
    key = cv2.waitKey(1) & 0xFF

    if key == 27:

        break


# ============================================================
# CLEANUP
# ============================================================

cap.release()

cv2.destroyAllWindows()

detector.close()