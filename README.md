LÓGICA FUZZY ROS
==============
En este proyecto se realizó la creación de diferentes nodos con el propósito de intercambiar información entre ellos, leer información de Arduino y realizar una toma de decisiones por medio de lógica fuzzy para variar la velocidad de un motor.

FUNCIONAMIENTO
----------
Se realizaron ocho nodos interconectados entre ellos, la función de cada nodo se puede ver a continuación:

1. **NODO A:** Para este nodo hay dos opciones:
* *NodoA.py*, este genera tres randomicos de tipo de mensaje bool, int y float que son enviados a los nodos B, C y D respectivamente.
* *NodoA.ino*, el nodo se carga a arduino, el cual se encarga de leer 3 variables físicas que se entenderán como bool, int y float, tambien son enviados a los nodos B, C y D respectivamente. También este nodo recibe la decisión tomada en el nodo H y se encarga de variar la velocidad del motor conectado.
2. **NODOS B, C y D:** La función de estos 3 nodos es similar reciben información del nodo A, mediante conjuntos difusos y funciones de pertenencia se envía del nodo B al nodo E, del nodo C al nodo F y del nodo D al nodo G un mensaje tipo string *Alto/xxx.xx/Medio/xxx.xx/Bajo/xxx.xx*, donde las x representan el porcentaje que le corresponde a cada conjunto.
3. **NODOS E, F y G:** Al igual que los anteriores nodos estos también son similares. En el funcionamiento interno de los nodos E, F y G reciben el mensaje string de los nodos B, C y D respectivamente, cada nodo elige el mayor valor de los porcentaje. Por ejemplo, al nodo E llegó *"Alto/0.00/Medio/35.25/Bajo/64.75"*, el nodo elige Bajo porque es el porcentaje mayor y envía al nodo H un mensaje tipo char indicando la decisión elegida, para los nodos F y G es similar.
4. **Nodo H:** Recibe mensaje tipo char de los nodos E, F y G que le indican de cada uno si es Alto, Medio o Bajo, pero cada nodo envía un char diferente para que el nodo H sepa de donde proviene, dependiendo de la combinación de char que llega toma la decisión en porcentaje de la velocidad del motor y se la transmite al nodo A (arduino)

PRE-REQUISITOS
--------------
- Se hizo la instalación de rosserial y rosserial arduino
``` 
$ sudo apt-get install ros-<distro>-rosserial
$ sudo apt-get install ros-<distro>-rosserial-arduino
```
- Despues de la instalación de rosserial y rosserial arduino para usarlo como nodo se usa el siguiente comando
``` 
$ rosrun rosserial_python serial_node.py _port:=<puerto_arduino_conectado> _baud:=57600
