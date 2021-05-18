/**rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600**/
/** La instrucción anterior se corre en el terminal para usar arduino como nodo de ROS**/

/**Librerías**/
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

/**Variables usadas de la librería std_msgs**/
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
  String Recibe=data.data;   // Recibe la información enviada del nodo H
  /**El valor de la señal anológica se le envía al motor esta dada por la función "separa" que recibe un a variable tipo
  string y devuelve una variable tipo int**/
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
/**La función separa recibe un string, el for recorre todo el string buscando un valor numérico el cual es almacenado en la variable valor1, después
con la función map los valores de 0 a 100 se escalan de 0 a 255**/
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
