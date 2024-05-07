#master
import cv2
from PIL import Image
from rpi_ws281x import PixelStrip, Color
import time
import socket


LED_COUNT = 140
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 60
LED_INVERT = False

def send_sync_signal():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'SYNC', ('192.168.65.45', 12345))

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
            for row in range(rows):
                new_matrix.append(matrix[row][col])
        else:
            for row in range(rows - 1, -1, -1):
                new_matrix.append(matrix[row][col])
            
    return new_matrix

def color_all(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def run_led_display(frame, strip, image_width=10, image_height=14):
    #left_frame = frame[:, :frame.shape[1]//2, :]
    #hex_values = get_image_hex_values(left_frame, image_width, image_height)

    right_frame = frame[:, frame.shape[1]//2:, :]
    hex_values = get_image_hex_values(right_frame, image_width, image_height)
    hex_matrix = convert_to_matrix(hex_values, image_height, image_width)
    rearranged_hex_values = rearrange_matrix_alternating(hex_matrix)

    try:
        for i, hex_code in enumerate(rearranged_hex_values):
            r = int(hex_code[0:2], 16)
            g = int(hex_code[2:4], 16)
            b = int(hex_code[4:6], 16)
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
        time.sleep(0.05)
    except KeyboardInterrupt:
        color_all(strip, Color(0, 0, 0), 10)
    finally:
        strip.show()

if __name__ == "__main__":
    cap = cv2.VideoCapture("shin.mp4")
    send_sync_signal()
    #time.sleep(0.43) #zzanggu x bounce o
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 20)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 14)

    frame_skip = 2
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