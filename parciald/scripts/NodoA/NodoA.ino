/**rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600**/

/**Librerias**/
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Float32.h>
#include <std_msgs/UInt16.h>
#include <math.h>

/**Definición de pines**/
const int Control_Motor = 6;
const int Bool_in = 8;
const int Int_in = A0;
const int Float_in = A1;

/**Nombre nodo**/
ros::NodeHandle NodoA;
/**Variables usadas de la libreria std_msgs**/
std_msgs::Bool bool_send;
std_msgs::Float32 float_send;
std_msgs::UInt16  int_send;

/**Nodos a los que se va a publicar**/
ros::Publisher pubB("AB", &bool_send);
ros::Publisher pubC("AC", &int_send);
ros::Publisher pubD("AD", &float_send);

/**Función callback, para recibir datos del nodo que se suscribe**/

void callback(const std_msgs::String& data)
{
  String Recibe=data.data;
  analogWrite(Control_Motor, separa(Recibe));
  if (Recibe=="")
    analogWrite(Control_Motor, 0);    
}

/**Nodo al que se va a suscribir**/
ros::Subscriber<std_msgs::String> subH("HI", callback);

void setup()
{
  NodoA.initNode(); /**Inicializador del nodo**/
  NodoA.advertise(pubB); /**Instanciar el nodo publisher**/
  NodoA.advertise(pubC);
  NodoA.advertise(pubD);
  NodoA.subscribe(subH);
  /** Configuración pines entrada y salida**/
  pinMode(Control_Motor, OUTPUT);
  pinMode(Bool_in, INPUT);
  pinMode(Int_in,INPUT);
  pinMode(Float_in, INPUT);
}

void loop()
{
  /**Arduino => ROS**/
  bool_send.data = digitalRead(Bool_in);
  int_send.data = map(analogRead(Int_in), 0, 1023, 0, 255);
  float_send.data = map(analogRead(Float_in), 0, 1023, 0, 50) / 10.0;
  /*Envía información a los nodos respectivos**/
  pubB.publish( &bool_send);
  pubC.publish( &int_send);
  pubD.publish( &float_send);
  NodoA.spinOnce();
  delay(100);
}

/**Función para tratar el string recibido y devuelve un entero**/
int separa(String a)
{
  int contador = 0, valor = 0, valor1 = 0;
  for (int i = 0; i < a.length(); i++)
  {
    if (a[i] == '0' ||  a[i] == '1' ||  a[i] == '2' ||  a[i] == '3' ||  a[i] == '4'
        ||  a[i] == '5' ||  a[i] == '6' ||  a[i] == '7' ||  a[i] == '8' ||  a[i] == '9')
    {
      int dec = pow(10, contador);
      if (contador > 1)
        dec = 10;
      valor =  a[i] - '0';
      valor1 = valor1 * dec + valor;
      contador++;
    }
  }
  valor1 = map(valor1, 0, 100, 0, 255);
  return valor1;
}
