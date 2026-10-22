import cv2
import numpy as np


def overlay_transparent(background, foreground, x, y, width=None):
    """
    Overlay a PNG with transparency onto the webcam frame.
    """

    if foreground is None:
        return background

    if width is not None:

        ratio = width / foreground.shape[1]

        height = int(foreground.shape[0] * ratio)

        foreground = cv2.resize(
            foreground,
            (width, height),
            interpolation=cv2.INTER_AREA
        )

    h, w = foreground.shape[:2]

    x1 = max(0, x)
    y1 = max(0, y)

    x2 = min(background.shape[1], x + w)
    y2 = min(background.shape[0], y + h)

    if x1 >= x2 or y1 >= y2:
        return background

    foreground_crop = foreground[
        y1 - y:y2 - y,
        x1 - x:x2 - x
    ]

    if foreground_crop.shape[2] < 4:
        background[y1:y2, x1:x2] = foreground_crop
        return background

    alpha = foreground_crop[:, :, 3] / 255.0

    alpha = alpha[:, :, np.newaxis]

    background_region = background[y1:y2, x1:x2]

    foreground_rgb = foreground_crop[:, :, :3]

    background[y1:y2, x1:x2] = (
        foreground_rgb * alpha +
        background_region * (1 - alpha)
    ).astype(np.uint8)

    return background
import cv2
import numpy as np


def overlay_transparent(
    background,
    foreground,
    center_x,
    center_y,
    width=250
):
    """
    Places a transparent PNG on the webcam frame.
    """

    if foreground is None:
        return background

    # Resize
    original_height, original_width = foreground.shape[:2]

    ratio = width / original_width
    new_height = int(original_height * ratio)

    foreground = cv2.resize(
        foreground,
        (width, new_height),
        interpolation=cv2.INTER_AREA
    )

    h, w = foreground.shape[:2]

    # Convert center position to top-left
    x = int(center_x - w / 2)
    y = int(center_y - h / 2)

    # Keep image inside frame
    x1 = max(0, x)
    y1 = max(0, y)

    x2 = min(background.shape[1], x + w)
    y2 = min(background.shape[0], y + h)

    if x1 >= x2 or y1 >= y2:
        return background

    foreground_crop = foreground[
        y1 - y:y2 - y,
        x1 - x:x2 - x
    ]

    # If no alpha channel
    if foreground_crop.shape[2] < 4:
        background[y1:y2, x1:x2] = foreground_crop
        return background

    # Alpha channel
    alpha = foreground_crop[:, :, 3] / 255.0
    alpha = alpha[:, :, np.newaxis]

    foreground_rgb = foreground_crop[:, :, :3]

    background_region = background[
        y1:y2,
        x1:x2
    ]

    background[y1:y2, x1:x2] = (
        foreground_rgb * alpha +
        background_region * (1 - alpha)
    ).astype(np.uint8)

    return background