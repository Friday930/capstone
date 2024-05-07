// 풍향센서 master (main.c)
#include "RS485_Wind_Direction_Transmitter.h"
#include <Python.h>
#include <signal.h>

volatile int keepRunning = 1; // Flag to control the main loop

void intHandler(int dummy) {
    keepRunning = 0; // Set the flag to stop the main loop
}

int main() {
    char Address = 2;
    int WindDirection = 0;
    char *Direction[16] = {"North", "Northeast by north", "Northeast", "Northeast by east", "East", "Southeast by east", "Southeast", "Southeast by south", "South", "Southwest by south", "Southwest", "Southwest by west", "West", "Northwest by west", "Northwest", "Northwest by north"};

    signal(SIGINT, intHandler);

    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Unable to initialize wiringPi: %s\n", strerror(errno));
        return 1;
    }

    if (Init("/dev/ttyUSB0")) {
        fprintf(stderr, "Unable to initialize communication\n");
        return 1;
    }

    const char *filename = "/home/pi/final/wind_master.py";
    FILE *pyfile1 = fopen(filename, "r");


    const char* txt = "/home/pi/final/example.txt";
    FILE *file = fopen(txt, "w");
    Py_Initialize();
    if (!Py_IsInitialized()) {
        fprintf(stderr, "Python 초기화 실패\n");
        return 1;
    }

    PyObject *main_module = PyImport_AddModule("__main__");
    PyObject *main_dict = PyModule_GetDict(main_module);

    while (keepRunning) {
        
        delay(500);
        WindDirection = readWindDirection(Address);
        fprintf(file, "%d\n", WindDirection);
        fflush(file);
        fseek(file, 0, SEEK_SET);
        clearerr(file);
        fgetc(file);

        if (WindDirection >= 0) {
            delay(500);
            // printf("WindDirection:%d\n", WindDirection);
            printf("WindDirection:%s\n\n", Direction[WindDirection]);

            // 파일을 다시 열어서 코드를 반복 실행
            FILE *pyFile = fopen(filename, "r");
            PyRun_File(pyFile, filename, Py_file_input, main_dict, main_dict);
            fclose(pyFile);
        }
    }

    Py_Finalize();
    fclose(pyfile1);
    fclose(file);
    serialClose(fd);
    return 0;
}
