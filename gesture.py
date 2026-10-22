import math


def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2 +
        (p1.z - p2.z) ** 2
    )


def count_fingers(hand):
    """
    Returns number of extended fingers.
    """

    wrist = hand[0]

    # Index, middle, ring, pinky
    finger_pairs = [
        (8, 6),
        (12, 10),
        (16, 14),
        (20, 18)
    ]

    count = 0

    for tip, pip in finger_pairs:

        tip_distance = distance(hand[tip], wrist)
        pip_distance = distance(hand[pip], wrist)

        if tip_distance > pip_distance * 1.12:
            count += 1

    # Thumb
    thumb_tip = distance(hand[4], wrist)
    thumb_ip = distance(hand[3], wrist)

    if thumb_tip > thumb_ip * 1.12:
        count += 1

    return count


def is_fist(hand):
    """
    A fist means zero fingers extended.
    """

    return count_fingers(hand) == 0