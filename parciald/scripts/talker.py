#!/usr/bin/env python  # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String

def talker():
# rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    pub = rospy.Publisher('bd', String, queue_size=10) 
# INICIADOR DEL NODO: rospy.init_node('nombre_del_nodo', anonymous) 
# si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('Talker', anonymous=False)
# Definir la velocidad en 10 Hz por ciclo
    rate = rospy.Rate(10) # 10hz
# Realiza el while hasta que no se apague ROS
    while not rospy.is_shutdown():
# Mensaje que el nodo va a enviar
        hello_str = "hola mundo" #% rospy.get_time()
# Muestra en el terminal lo que esta enviando
        rospy.loginfo(hello_str)
# Envia la información por el nodo
        pub.publish(hello_str)
# Hace cumplir el ciclo de 10 Hz
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
