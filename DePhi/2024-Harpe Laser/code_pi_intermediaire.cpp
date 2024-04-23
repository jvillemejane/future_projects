/* DePhi Project / Harpe Laser 	*/
/* LEnsE - 2024					*/

#include "mbed.h"

#define     SEUIL       2.5/3.3
#define     NB_NOTES    3

// Analog Input : one per note (all = 12)
AnalogIn analog_in[NB_NOTES] = {A0, A1, A2};  
// Array to store the analog values
double meas[NB_NOTES];

DigitalOut led(D13);

// UART communication with Raspberry Pi 
UnbufferedSerial pi_serial(USBTX, USBRX); // Adjust pins as necessary
// Ticker to pace the sampling of the analog inputs
Ticker ticker;

// String to collect data to play
char str_c[25];
int ind_c = 0;

// Send a string on a serial link 
void sendMessageToPi(char *message) {
    pi_serial.write(message, strlen(message));
}


/////////////////////////////////////////////////
// SAMPLING FUNCTION
/////////////////////////////////////////////////
void checkAnalogInput() {
    if(pi_serial.readable()){
        pi_serial.read(str_c, 1);

        ind_c = 0;
        for(int k = 0; k < NB_NOTES; k++){
            meas[k] = analog_in[k].read();
        }

        for(int k2 = 0; k2 < NB_NOTES; k2++){
            if(meas[k2] > SEUIL){
                if(k2 < 9){
                    str_c[ind_c] = '1'+k2;
                }
                else{
                    str_c[ind_c] = 'A'+(k2 - 9);
                }
                str_c[ind_c+1] = ',';
                ind_c += 2;            
            }
        }
        if(ind_c == 0){
            str_c[ind_c] = '0';
            str_c[ind_c+1] = ',';
            ind_c += 2;         
        }
        str_c[ind_c] = '\0';
        sendMessageToPi(str_c);
    }
}

/////////////////////////////////////////////////
// MAIN FUNCTION
/////////////////////////////////////////////////
int main() {
    pi_serial.baud(115200);
    sendMessageToPi("Test");

    pi_serial.attach(&checkAnalogInput, SerialBase::RxIrq);
    // ticker.attach(&checkAnalogInput, 50ms);

    while (1) {
        wait_us(1000);
    }
}