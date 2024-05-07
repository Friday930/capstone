#include "RS485_Wind_Direction_Transmitter.h"


void addedCRC(unsigned char *buf, int len)
{
  unsigned int crc = 0xFFFF;
  for (int pos = 0; pos < len; pos++)
  {
    crc ^= (unsigned int)buf[pos];
    for (int i = 8; i != 0; i--)
    {
      if ((crc & 0x0001) != 0)
      {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else
      {
        crc >>= 1;
      }
    }
  }
  buf[len] = crc % 0x100;
  buf[len + 1] = crc / 0x100;
}

unsigned char ModifyAddress(unsigned char Address1, unsigned char Address2)
{
  unsigned char ModifyAddressCOM[11] = {0x00, 0x10, 0x10, 0x00, 0x00, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00};
  char ret = 0;
  long curr = millis();
  long curr1 = curr;
  char ch = 0;
  ModifyAddressCOM[0] = Address1;
  ModifyAddressCOM[8] = Address2;
  addedCRC(ModifyAddressCOM , 9);
  write(fd, ModifyAddressCOM, 11);
  while (!ret) {
    if (millis() - curr > 1000) {
      break;
    }

    if (millis() - curr1 > 100) {
      write(fd, ModifyAddressCOM, 11);
      curr1 = millis();
    }

    if (serialDataAvail(fd) > 0) {
      delay(7);
      if (read(fd, &ch, 1) == 1) {
        if (ch == Address1) {
          if (read(fd, &ch, 1) == 1) {
            if (ch == 0x10 ) {
              if (read(fd, &ch, 1) == 1) {
                if (ch == 0x10) {
                  if (read(fd, &ch, 1) == 1) {
                    if (ch == 0x00) {
                      if (read(fd, &ch, 1) == 1) {
                        if (ch == 0x00) {
                          if (read(fd, &ch, 1) == 1) {
                            if (ch == 0x01) {
                              printf("Please re-power the sensor and enter: Y.\n");
                              scanf("%s", &ch);
                              ret = 1 ;
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return ret;
}

unsigned char Init(char *device)
{
  if ((fd = serialOpen(device, 9600)) < 0) {
    fprintf(stderr, "Unable to open serial device: %s\n", strerror(errno));
    return 1;
  }
  return 0;
}

int readWindDirection(unsigned char Address)
{
  unsigned char Data[7] = {0};
  unsigned char COM[8] = {0x00, 0x03, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00};
  char ret = 0;
  int WindDirection = 0;
  int NewWindDirection;
  long curr = millis();
  long curr1 = curr;
  char ch = 0;
  COM[0] = Address;
  addedCRC(COM, 6);
  write(fd, COM, 8);
  while (!ret) {

    if (millis() - curr > 1000) {
      WindDirection = -1;
      break;
    }

    if (millis() - curr1 > 100) {
      write(fd, COM, 10);
      curr1 = millis();
    }

    if (serialDataAvail(fd) > 0) {
      delay(10);
      if (read(fd, &ch, 1) == 1) {
        if (ch == Address) {
          Data[0] = ch;
          if (read(fd, &ch, 1) == 1) {
            if (ch == 0x03) {
              Data[1] = ch;
              if (read(fd, &ch, 1) == 1) {
                if (ch == 0x02) {
                  Data[2] = ch;
                  if (read(fd, &Data[3], 4) == 4) {
                    if (CRC16_2(Data, 5) == (Data[5] * 256 + Data[6])) {
                      ret = 1;
                      // Adjust the scaling or interpretation based on the sensor's specifications
                      WindDirection = (Data[3] * 256 + Data[4]);
                                                
                        if((WindDirection >= 0) && (WindDirection < 225)) {
                          NewWindDirection = 0;
                        } 
                        else if((WindDirection >= 225) && (WindDirection < 450)) {
                          NewWindDirection = 1;
                        } 
                        else if((WindDirection >= 450) && (WindDirection < 675)) {
                          NewWindDirection = 2;
                        } 
                        else if((WindDirection >= 675) && (WindDirection < 900)) {
                          NewWindDirection = 3;
                        } 
                        else if((WindDirection >= 900) && (WindDirection < 1125)) {
                          NewWindDirection = 4;
                        } 
                        else if((WindDirection >= 1125) && (WindDirection < 1350)) {
                          NewWindDirection = 5;
                        } 
                        else if((WindDirection >= 1350) && (WindDirection < 1575)) {
                          NewWindDirection = 6;
                        } 
                        else if((WindDirection >= 1575) && (WindDirection < 1800)) {
                          NewWindDirection = 7;
                        } 
                        else if((WindDirection >= 1800) && (WindDirection < 2025)) {
                          NewWindDirection = 8;
                        } 
                        else if((WindDirection >= 2025) && (WindDirection < 2250)) {
                          NewWindDirection = 9;
                        } 
                        else if((WindDirection >= 2250) && (WindDirection < 2475)) {
                          NewWindDirection = 10;
                        } 
                        else if((WindDirection >= 2475) && (WindDirection < 2700)) {
                          NewWindDirection = 11;
                        } 
                        else if((WindDirection >= 2700) && (WindDirection < 2925)) {
                          NewWindDirection = 12;
                        } 
                        else if((WindDirection >= 2925) && (WindDirection < 3150)) {
                          NewWindDirection = 13;
                        } 
                        else if((WindDirection >= 3150) && (WindDirection < 3375)) {
                          NewWindDirection = 14;
                        } 
                        else if((WindDirection >= 3375) && (WindDirection < 3600)) {
                          NewWindDirection = 15;
                        } 
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return NewWindDirection;
}

unsigned int CRC16_2(unsigned char *buf, int len)
{
  unsigned int crc = 0xFFFF;
  for (int pos = 0; pos < len; pos++)
  {
    crc ^= (unsigned int)buf[pos];
    for (int i = 8; i != 0; i--)
    {
      if ((crc & 0x0001) != 0)
      {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else
      {
        crc >>= 1;
      }
    }
  }

  crc = ((crc & 0x00ff) << 8) | ((crc & 0xff00) >> 8);
  return crc;
}