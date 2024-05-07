import sys
import cv2
from PIL import Image
from rpi_ws281x import PixelStrip, Color
import time
import socket

LED_COUNT = 140
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 30
LED_INVERT = False
text = 0

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

def color_all(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

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
        time.sleep(0.1)
    except KeyboardInterrupt:
        color_all(strip, Color(0, 0, 0), 10)
    finally:
        strip.show()

if __name__ == "__main__":
    
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    text = 0
    
    start_time = time.time()
    duration = 1
    
    try:
        # while time.time() - start_time < duration:
            with open("example.txt", "r") as file:
                text1 = file.read().strip()
                text = int(text1)
                
            if text == 0:
                color_all(strip, Color(61, 0, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'0')
                
            elif text == 1:
                color_all(strip, Color(122, 0, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'1')
            
            elif(text == 2):
                color_all(strip, Color(183, 0, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'2')
            
            elif(text == 3):
                color_all(strip, Color(255, 0, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'3')
            
            elif(text == 4):
                color_all(strip, Color(0, 61, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'4')
            
            elif(text == 5):
                color_all(strip, Color(0, 122, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'5')
            
            elif(text == 6):
                color_all(strip, Color(0, 183, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'6')
            
            elif(text == 7):
                color_all(strip, Color(0, 255, 0), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'7')
            
            elif(text == 8):
                color_all(strip, Color(0, 0, 61), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'8')
            
            elif(text == 9):
                color_all(strip, Color(0, 0, 122), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'9')
            
            elif(text == 10):
                color_all(strip, Color(0, 0, 183), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'10')
            
            elif(text == 11):
                color_all(strip, Color(0, 0, 255), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'11')
            
            elif(text == 12):
                color_all(strip, Color(61, 61, 61), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'12')
            
            elif(text == 13):
                color_all(strip, Color(122, 122, 122), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'13')
            
            elif(text == 14):
                color_all(strip, Color(183, 183, 183), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'14')
                
            elif(text == 15):
                color_all(strip, Color(255, 255, 255), 10)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'15')
        
            color_all(strip, Color(0, 0, 0), 10)
            
        
    except KeyboardInterrupt:
        pass
    
    finally:
        cv2.destroyAllWindows()
        strip.show()
        print("Finally block executed")

    cv2.destroyAllWindows()
