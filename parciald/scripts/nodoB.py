#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String
from std_msgs.msg import Bool	# Usark ek tipo de mensaje Bool

x=None

## Función para enviar información, según la información recibida. 
def var_global(a):
    global x
    if a==1:
        x="Alto/100/Medio/000/Bajo/000" 
    if a==0:
        x="Alto/000/Medio/000/Bajo/100"
        
##Función para recibir la información de otro nodo.
def callback(data):
    y=data.data
    rospy.loginfo(y)
    if y==True:
        var_global(1)
    if y==False:
        var_global(0)
        
def nodoB():
    global x
    # rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    str_E = rospy.Publisher('BE', String, queue_size=100) 
    # INICIADOR DEL NODO: rospy.category:themes init_node('nombre_del_nodo', anonymous) 
    # Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('NodoB', anonymous=False)
    # Definir la velocidad en 1 Hz por ciclo
    rate = rospy.Rate(1) 
    # Recibe la información del nodo que esta enviando 
    rospy.Subscriber('AB', Bool, callback)
    # El while se mantiene hasta que se interrumpe el nodo.
    while not rospy.is_shutdown():
        rospy.loginfo(x)    # Muestra en el terminal #a40000lo que esta enviando
        str_E.publish(x)      # Envia la información por el nodo
        rate.sleep()                # Hace cumplir el ciclo de 1 Hz
if __name__ == '__main__':
    try:
        nodoB()
    except rospy.ROSInterruptException:
        pass
