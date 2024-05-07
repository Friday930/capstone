import cv2
from PIL import Image
from rpi_ws281x import PixelStrip, Color
import time

LED_COUNT = 1200
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 120
LED_INVERT = False

def get_image_hex_values(frame, width, height):
    # Convert OpenCV frame to RGB PIL Image
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img = img.resize((width, height))
    pixels = list(img.getdata())
    hex_values = [f"{r:02X}{g:02X}{b:02X}" for r, g, b in pixels]
    return hex_values

def convert_to_matrix(line, rows, cols):
    return [line[i * cols:(i + 1) * cols] for i in range(rows)]

def rearrange_matrix_alternating(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []
    for col in range(cols):
        if col % 2 == 0:
            for row in range(rows - 1, -1, -1):
                new_matrix.append(matrix[row][col])
        else:
            for row in range(rows):
                new_matrix.append(matrix[row][col])
    return new_matrix

def color_all(strip, color, wait_ms=50): #50
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0) #1000.0

def run_led_display(frame, strip, image_width=40, image_height=30):
    hex_values = get_image_hex_values(frame, image_width, image_height)

    hex_matrix = convert_to_matrix(hex_values, image_height, image_width)
    rearranged_hex_values = rearrange_matrix_alternating(hex_matrix)

    try:
        for i, hex_code in enumerate(rearranged_hex_values):
            r = int(hex_code[0:2], 16)
            g = int(hex_code[2:4], 16)
            b = int(hex_code[4:6], 16)
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
        time.sleep(0.03) #0.03
    except KeyboardInterrupt:
        color_all(strip, Color(0, 0, 0), 10)
    finally:
        strip.show()

if __name__ == "__main__":
    cap = cv2.VideoCapture("shin.mp4")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 40)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 30)

    frame_skip = 3 #2
    frame_count = 0

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_skip == 0:
                run_led_display(frame, strip)

            frame_count += 1

    except KeyboardInterrupt:
        color_all(strip, Color(0, 0, 0), 10)

    finally:
        cap.release()
        cv2.destroyAllWindows()
        strip.show()

    cap.release()
    cv2.destroyAllWindows()
