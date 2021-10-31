
// Include NewPing Library for HC-SR04 sensor
#include <NewPing.h>
#include <Wire.h>
// Hook up 4 HC-SR04 sensors in 1-pin mode
// Sensor 0
#define TRIGGER_PIN_0  8
#define ECHO_PIN_0     8

// Sensor 1
#define TRIGGER_PIN_1  9
#define ECHO_PIN_1     9

// Sensor 2
#define TRIGGER_PIN_2  10
#define ECHO_PIN_2     10

// Sensor 3
#define TRIGGER_PIN_3  11
#define ECHO_PIN_3     11

#define leftLimitPin  12
#define rightLimitPin 4

// Maximum Distance is 260 cm
#define MAX_DISTANCE 260

// Create objects for ultrasonic sensors
NewPing sensor0(TRIGGER_PIN_0, ECHO_PIN_0, MAX_DISTANCE);
NewPing sensor1(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE);
NewPing sensor2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE);
NewPing sensor3(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE);

// Define return data array, one element per sensor
int distance[8];

// Define counter to count bytes in response
int bcount = 0;

// interrupt


//-----------------------------------------------------------------------------------------------------------------------
#include <math.h>                                        // necesaria para utilizar función atan()
#define PI 3.1415926535897932384626433832795             // definición del número PI

int N = 24;  // earlier it was 20                         // number of encoder slots
float diametro = 21;                                    // Wheel diameter in cm
float longitud = 22;                                   // distance between the wheels
int contadorTicks = 1;                                  // number of ticks for speed calculation(rremember the lower the value the greater the value in mesurements)
int tam = 10;                                           // vector size in average calculation (This value depends on the size of the vectorL and vectorR average vectors.)
int k = 10;                                             // sampling time

float Cdistancia = 0;                                   // distance traveled central point
float x = 0;                                            // distance traveled x axis
float y = 0;                                            // distance traveled y axis
float phi = 0;                                          // angular position

volatile unsigned muestreoActual = 0;                     // variables to define the sampling time
volatile unsigned muestreoAnterior = 0;
volatile unsigned deltaMuestreo = 0;


//------------------------------- Right motor variables---------------------------------------------

volatile unsigned muestreoActualInterrupcionR = 0;        // variables for definition of the interruption time and calculation of the right motor speed
volatile unsigned muestreoAnteriorInterrupcionR = 0;
double deltaMuestreoInterrupcionR = 0;

int encoderR = 3;   // right encoder connection pin
int llantaR = 11;      // right rim connection pin   (pin de PWM)

double frecuenciaR = 0;                                  // rim interruption frequency R
double Wr = 0;                                           // Angular velocity R
double Vr = 0;                                           // linear velocity
int CR = 0;                                             // tick counter
float vectorR[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};    // data storage vector for average interruption time
float Rdistancia = 0;                                    // distance traveled right tire
int Rtick = 0;                                           // right encoder ticks
int RtickAnt = 0;                                        // previous right encoder ticks
int deltaRtick = 0;                                      // difference of right encoder

//------------------------------ left motor variables ------------------------------------------------

volatile unsigned muestreoActualInterrupcionL = 0;        // variables for definition of interruption time and calculation of left motor speed
volatile unsigned muestreoAnteriorInterrupcionL = 0;
double deltaMuestreoInterrupcionL = 0;

int encoderL = 2;   // pin de conexiòn del encoder Izquierdo
int llantaL = 10;      // pin de conexiòn de llanta Izquierda   (pin de PWM)

double frecuenciaL = 0;                                  // frecuencia de interrupciòn llanta Izquierda
double Wl = 0;                                           // Velocidad angular L
double Vl = 0;                                           // velocidad Lineal
int CL = 0;                                              // contador Ticks
float vectorL[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};    // vector de almacenamiento de datos para promedio del tiempo de interrupciones

float Ldistancia = 0;                                    // distancia recorrida llanta izquierda
int Ltick = 0;                                           // ticks del encoder izquierdo
int LtickAnt = 0;                                        // ticks del encoder izquier anteriores
int deltaLtick = 0;                                      // diferencia del encoder izquierdo
//-----------------------------------------------------------------------------------------------------------------------------------------------------
void setup() {

  Serial.begin(9600);
  Wire.begin(8);                /* join i2c bus with address 8 */
  Wire.onReceive(receiveEvent); /* register receive event */
  Wire.onRequest(requestEvent); /* register request event */
  pinMode(leftLimitPin, INPUT_PULLUP);
  pinMode(rightLimitPin, INPUT_PULLUP);

  //----------------------------------------------------------------------------------------------------------------------------------
  attachInterrupt(digitalPinToInterrupt(encoderR), REncoder, FALLING);              // line to add an interrupt to a pin
  attachInterrupt(digitalPinToInterrupt(encoderL), LEncoder, FALLING);              // linea para añadir una interrupciòn a un PIN
}

void REncoder() {                                                                                         // right rim encoder interrupt function
  Rtick++;                                                                                           // Number of right rim ticks
  CR++;                                                                                               // tick counter increment
  if (CR == contadorTicks) {                                                                          // if the tick counter reaches the tick value determined for the time calculation
    float media = 0;                                                                                // variable created to calculate the average
    //-------------------------------------- -----------------------------    Filtro promedio    -----------------------------------------------------------------------------//
    for (int i = 0; i < tam - 1; i++) {                                                            // vector fill for later calculation of the average
      vectorR[i] = vectorR[i + 1];
    }
    vectorR[tam - 1] = deltaMuestreoInterrupcionR ;                                                 // last vector data (current measurement)

    for (int i = 0; i < tam; i++) {                                                                // Sum of vector values
      media = vectorR[i] + media;
    }
    media = media / tam;                                                                           //división by the total data of the vector
    deltaMuestreoInterrupcionR = media;                                                            // it is replaced by the value of its average.
    //-------------------------------------- ----------------------------- ---------------------------------------------------------------------------------------------------//
    frecuenciaR = (1000) / deltaMuestreoInterrupcionR;                                             // interruption frequency
    muestreoAnteriorInterrupcionR = muestreoActualInterrupcionR;                                   // the previous interruption time is updated
    CR = 0;                                                                                        //tick counter reset
  }
}

void LEncoder() {                                                                                       // funciòn de interrupciòn del enconder llanta izquierda
  Ltick++;                                                                                           // Nùmero de ticks llanta izquierda
  CL++;                                                                                             // incremento del contador de ticks
  if (CL == contadorTicks) {                                                                        // si el contador de ticks alcanza el valor de ticks determinado para el cálculo del tiempo
    float media = 0;                                                                              // variable creada para cálculo del promedio
    //-------------------------------------- -----------------------------    Filtro promedio    -----------------------------------------------------------------------------//
    for (int i = 0; i < tam - 1; i++) {                                                            // relleno del vector para calculo posterior del promedio
      vectorL[i] = vectorL[i + 1];
    }
    vectorL[tam - 1] = deltaMuestreoInterrupcionL;                                                 // último dato del vector (medida actual)

    for (int i = 0; i < tam; i++) {                                                                // Suma de los valores del vector
      media = vectorL[i] + media;
    }
    media = media / tam;                                                                           //división por el total de datos del vector
    deltaMuestreoInterrupcionL = media;                                                            // se reemplaza por el valor de su medío.
    //-------------------------------------- ----------------------------- ---------------------------------------------------------------------------------------------------//
    frecuenciaL = (1000) / deltaMuestreoInterrupcionL;                                             // frecuencia de interrupciòn
    muestreoAnteriorInterrupcionL = muestreoActualInterrupcionL;                                   // se actualiza el tiempo de interrupciòn anterior
    CL = 0;                                                                                        // Reinicio de contador de ticks
  }
}

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void loop() {

  readDistance();

  //--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  muestreoActual = millis();                                                                           //current sampling time
  muestreoActualInterrupcionR = millis();                                                              // the execution time is assigned to the current sample
  muestreoActualInterrupcionL = millis();                                                              // the execution time is assigned to the current sample

  deltaMuestreo = (double) muestreoActual - muestreoAnterior;                                          // delta sampling
  if ( deltaMuestreo >= k)                                                                             // sampling time is ensured
  {
    deltaMuestreoInterrupcionR = muestreoActualInterrupcionR -  muestreoAnteriorInterrupcionR;       // difference between interruption times of engine ticks
    deltaMuestreoInterrupcionL = muestreoActualInterrupcionL -  muestreoAnteriorInterrupcionL;       // difference between interruption times of engine ticks

    if (deltaMuestreoInterrupcionR >= 200 * contadorTicks) {                                          // This is the way to define when the engine is stationary. If deltaSampleInterruptionR is greater than 40 milliseconds by prescaling of ticks
      frecuenciaR = 0;                                                                                // 40 mS is the maximum time that a tick takes at the lowest engine speed
    }
    if (deltaMuestreoInterrupcionL >= 200 * contadorTicks) {                                          // Esta es la forma de definir cuando el motor se encuentra quieto. Si deltaMuestreoInterrupcionR es mayor a 40 milisegundos por el preescalado de ticks
      frecuenciaL = 0;                                                                                // 40 mS es el tiempo que màximo se tarda un tick a la menor velocidad del motor
    }

    Wr = contadorTicks * ((2 * PI) / N) * frecuenciaR;                                                // angular frequency Rad / s
    Vr = Wr * (diametro / 2);                                                                         // linear speed cm / s
    Wl = contadorTicks * ((2 * PI) / N) * frecuenciaL;                                                // frecuencia angular Rad/s
    Vl = Wl * (diametro / 2);                                                                         // velocidad lineal cm/s

    analogWrite(llantaR, 0);  // it should be analogWrite                                              // right rim pwm
    analogWrite(llantaL, 0);                                                                          // left rim pwm

    odometria();                                                                                      // cálculo de la odometría

    /*Serial.print(x);                                                                                  // se muestra el tiempo entre TIC y TIC
      Serial.print(" ");                                                                                 // se muestra el tiempo entre TIC y TIC
      Serial.println(y);                                                                              // se muestra el tiempo entre TIC y TIC
      Serial.print ("Left velocity......");
      Serial.print (Vl);
      Serial.print(".....");
      Serial.print(Vr);
      Serial.println ("Right velocity......");*/


  }




 

  
  }
  



//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void odometria() {

  deltaRtick = Rtick - RtickAnt;                                                                         // comparison of ticks traveled since the last right wheel calculation
  Rdistancia = PI * diametro * (deltaRtick / (double) 4);                                               // distance traveled by the right tire since the last calculation

  deltaLtick = Ltick - LtickAnt;                                                                         // comparación de los ticks recorridos desde el último cálculo llanta izquierda
  Ldistancia = PI * diametro * (deltaLtick / (double) 4);                                               // distancia recorrida por la llanta izquierda desde el último cálculo

  Cdistancia = (Rdistancia + Ldistancia) / 2;                                                             // distance traveled by center point since last calculation




  x = x + Cdistancia * cos(phi);                                                                          // current point X position
  y = y + Cdistancia * sin(phi);                                                                          // posición del punto Y actual

  phi = phi + ((Rdistancia - Ldistancia) / longitud);                                                     // Angular position actually
  phi = atan2(sin(phi), cos(phi));                                                                        //transformación de la posición angular entre -PI y PI

  RtickAnt = Rtick;                                                                                       // update RtickAnt variable with Rtick values
  LtickAnt = Ltick;                                                                                       // actualización de la variable LtickAnt con los valores de Ltick
}







// function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (0 < Wire.available()) {
    byte mcu = Wire.read();      /* receive byte as a character */
    Serial.print(mcu);           /* print the character */
  }
  Serial.println();             /* to newline */
}

void requestEvent() {

  // Define a byte to hold data
  byte val;

  // Cycle through data
  // First response is always 255 to mark beginning
  switch (bcount) {
    case 0:
      val = 255;
      break;
    case 1:
      val = distance[0];
      break;
    case 2:
      val = distance[1];
      break;
    case 3:
      val = distance[2];
      break;
    case 4:
      val = distance[3];
      break;
    case 5:
      val = distance[4];
      break;
    case 6:
      val = distance[5];
      break;
    case 7:
      val = distance[6];
      break;
    case 8:
      val = distance[7];
      break;
  }

  // Send response back to Master
  Wire.write(val);

  // Increment byte counter
  bcount = bcount + 1;
  if (bcount > 8) bcount = 0;

}

void readDistance()
{
  distance[0] = sensor0.ping_cm();
  if (distance[0] > 254 ) {
    distance[0] = 254;
  }
  delay(20);

  distance[1] = sensor1.ping_cm();
  if (distance[1] > 254 ) {
    distance[1] = 254;
  }
  delay(20);

  distance[2] = sensor2.ping_cm();
  if (distance[2] > 254 ) {
    distance[2] = 254;
  }
  delay(20);

  distance[3] = sensor3.ping_cm();
  if (distance[3] > 254 ) {
    distance[3] = 254;
  }
  delay(20);

  distance[4] = digitalRead(leftLimitPin);
  delay(20);

  distance[5] = digitalRead(rightLimitPin);
  delay(20);

  distance[6] = Vl;
  distance[7] = Vr;
  delay(20);

}
