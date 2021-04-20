PROYECTO ROS
==============
*En este proyecto se realiza la creación de diferentes nodos con el proposito de intercambiar información entre ellos, leer informacación de Arduino y realizar una toma de decisiones en los nodos variar la velocidad de un motor*

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
``` 
