#define DATA0 3
#define DATA1 4
#define DATA2 5
#define DATA3 6
#define DATA4 7
#define DATA5 8
#define DATA6 9
#define DATA7 10
#define READ 2
#define ACK 11

uint8_t readVal = 0b0;
uint8_t temp = 0b0;
void read(){
//  readVal = PORTD;
//  readVal = readVal >> 2;
//  temp = (PORTB && B00000011);
//  temp = temp << 6;
//  readVal = readVal || temp;
  for(int i = 3; i < 11; i++){
    temp = digitalRead(i);
    readVal = ((readVal) | (temp << (i-3)));
    //Serial.write(readVal);
  }
  Serial.write(readVal);
  //Serial.print(readVal, BIN);
  //Serial.write('\r');
  readVal = 0b0;
  digitalWrite(ACK, HIGH);
  delayMicroseconds(10);
  digitalWrite(ACK, LOW);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(DATA0, INPUT);
  pinMode(DATA1, INPUT);
  pinMode(DATA2, INPUT);
  pinMode(DATA3, INPUT);
  pinMode(DATA4, INPUT);
  pinMode(DATA5, INPUT);
  pinMode(DATA6, INPUT);
  pinMode(DATA7, INPUT);
  pinMode(READ, INPUT);
  pinMode(ACK, OUTPUT);
  digitalWrite(ACK, LOW);
  Serial.begin(115200);
  attachInterrupt(
    digitalPinToInterrupt(READ),
    read,
    RISING);
  digitalWrite(ACK, HIGH);
  delayMicroseconds(5);
  digitalWrite(ACK, LOW);
  Serial.write("Begin\r\n");
}

void loop() {
  // put your main code here, to run repeatedly:
}
