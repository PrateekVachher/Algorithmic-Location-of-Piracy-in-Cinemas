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
 digitalWrite(LED3, HIGH);
 digitalWrite(LED2, HIGH);
 digitalWrite(LED1, HIGH);
 

}
