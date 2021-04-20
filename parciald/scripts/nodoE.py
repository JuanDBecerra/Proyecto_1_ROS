#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String

x=None
def var_global(a):
    global x
    b=a.split("/")			# Divide el string en cada "/" 
    Alto=float(b[1])			# Toma la parte del string que contiene el dato requerido
    Medio=float(b[3])
    Bajo=float(b[5])
    if Alto>Medio:
        x="A"				# Envia A, para establecer alto
    if Medio>Alto and Medio>Bajo:
        x="M"				# Envia M, para establecer medio
    if Bajo>Medio:
        x="B"				# Envia B, para establecer bajo

def callback(data):
    y=data.data
    rospy.loginfo(y)
    var_global(y)

def nodoE():
    global x
# rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    str_H = rospy.Publisher('EH', String, queue_size=10) 
# INICIADOR DEL NODO: rospy.category:themes init_node('nombre_del_nodo', anonymous) 
# Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('NodoE', anonymous=False)
# Definir la velocidad en 0.5 Hz por ciclo
    rate = rospy.Rate(0.5) 
# Recibe la información del nodo que esta enviando 
    rospy.Subscriber('BE', String, callback)
    while not rospy.is_shutdown():
        rospy.loginfo(x)    # Muestra en el terminal #a40000lo que esta enviando
        str_H.publish(x)      # Envia la información por el nodo
        rate.sleep()                # Hace cumplir el ciclo de 1 Hz
if __name__ == '__main__':
    try:
        nodoE()
    except rospy.ROSInterruptException:
        pass
