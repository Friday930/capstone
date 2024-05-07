import sys
import time
import socket

text = 0


if __name__ == "__main__":

    text = 0
    try:
            with open("example.txt", "r") as file:
                text1 = file.read().strip()
                text = int(text1)
                
            if text == 0:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'0')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'0')
                
            elif text == 1:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'1')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'1')
            
            elif(text == 2):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'2')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'2')
            
            elif(text == 3):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'3')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'3')
            
            elif(text == 4):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'4')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'4')
            
            elif(text == 5):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'5')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'5')
            
            elif(text == 6):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'6')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'6')
            
            elif(text == 7):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'7')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'7')
            
            elif(text == 8):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'8')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'8')
            
            elif(text == 9):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'9')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'9')
            
            elif(text == 10):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'10')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'10')
            
            elif(text == 11):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'11')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'11')
            
            elif(text == 12):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'12')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'12')
            
            elif(text == 13):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'13')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'13')
            
            elif(text == 14):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'14')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'14')
                
            elif(text == 15):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.189.45', 12345))
                    s.sendall(b'15')
                    s.connect(('192.168.189.174', 12345))
                    s.sendall(b'15')
        
            
        
    except KeyboardInterrupt:
        pass
    
    finally:
        print("Finally block executed")