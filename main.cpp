#include <iostream>
#include <fstream>
#include <sys/stat.h>
#include <vector>
#include "SerialPort.h"
#include <bitset>

#include <conio.h>

#define DATA_LENGTH 64 //send 512 byte blobs of data to the arduino at a time
using namespace std;

char* portName = "\\\\.\\COM9";

SerialPort *arduino;

int main(int argc, char *argv[])
{
    //cout << "Hello world!" << endl;
    ofstream tapeData (argv[1], ios::out | ios::binary);
    cout << "File: " << argv[1] << endl;
    char * readData = new char [1];
    int hasData = 0;
    cout << "TEST" << endl;
    arduino = new SerialPort(portName);
    cout << "ASDFASDF" << endl;
    if (!arduino->isConnected()){
        delete arduino;
        delete readData;
        return -1;
    }
    std::cout << "is connected: " << arduino->isConnected() << std::endl;

    cout << "Beggining Serial communication:" << endl;
    char ch = 'z';
    while(!kbhit()){
        hasData = arduino->readSerialPort(readData,1);
        if(hasData != 0){
            //cout << "ASDFASDF" << endl;
            tapeData << readData[0];
            cout << std::bitset<8>(readData[0]) << endl;
            readData[0] = 0;
            hasData = 0;
        }
    }
    tapeData.close();
    return 0;
}
