#include <math.h>

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  for (int pin = 5; pin <= 13; pin++){ // initializes the pins needed (5 - 13)
      pinMode(pin, OUTPUT);
  }
  Serial.write('1');
}

void loop() {
  int input_data[9]; // 3x3 array
  
  if(Serial.available() > 0){
    for (int i = 0; i < 9; i++){
      input_data[i] = Serial.parseInt(); // Receive serial signal and put in array
    }
    
    for (int pin = 0; pin < 9; pin++){
      //analogWrite(pin+5, input_data[pin]);
      analogWrite(pin+5, 150);
    }
  }
  
  Serial.write('0');
}
