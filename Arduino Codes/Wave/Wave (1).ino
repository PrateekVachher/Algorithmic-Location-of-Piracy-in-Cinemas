#define LED5 5
#define LED4 4
#define LED3 3
#define LED2 2
#define LED1 1 

void setup()
{
 pinMode(LED5, OUTPUT);
 pinMode(LED4, OUTPUT);
 pinMode(LED3, OUTPUT);
 pinMode(LED2, OUTPUT);
 pinMode(LED1, OUTPUT);
}

void loop(){
 // slow line top to bottom
 digitalWrite(LED5, HIGH);
 digitalWrite(LED4, HIGH);
 delay(160);
 digitalWrite(LED3, HIGH);
 delay(160);
 digitalWrite(LED2, HIGH);
 delay(160);
 digitalWrite(LED1, HIGH);
 digitalWrite(LED4, LOW);
 digitalWrite(LED3, LOW);
 delay(160);
 digitalWrite(LED2, LOW);
 delay(160);
 digitalWrite(LED1, LOW);
 delay(160);

}
