#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String

def callback(data):
# Muestra la información en el terminal que esta recibiendo
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listalker():
# rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    pub = rospy.Publisher('shido', String, queue_size=10) 
# INICIADOR DEL NODO: rospy.init_node('nombre_del_nodo', anonymous) 
# Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('listalker', anonymous=False)
# Definir la velocidad en 5 Hz por ciclo
    rate = rospy.Rate(5) # 5 Hz
# Recibe la información del nodo que esta enviando 
    rospy.Subscriber('chatter', String, callback)
    while not rospy.is_shutdown():
# Mensaje que el nodo va a enviar
    	hello_str = "Hola mundo 2.0 %s" % rospy.get_time()
# Muestra en el terminal lo que esta enviando
    	rospy.loginfo(hello_str)
# Envia la información por el nodo
    	pub.publish(hello_str)
# Hace cumplir el ciclo de 5 Hz
    	rate.sleep()

if __name__ == '__main__':
    try:
        listalker()
    except rospy.ROSInterruptException:
        pass
