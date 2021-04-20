#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy  # Se importa para escribir uno de ROS

from std_msgs.msg import String   #Para poder utilizar el tipo mensaje String
def callback(data):
# Muestra la información en el terminal que este nodo esta recibiendo
    rospy.loginfo(data.data)
    #data.data

def listener():

# INICIADOR DEL NODO: rospy.init_node('nombre_del_nodo', anonymous) 
# Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('listener', anonymous=False)
# Recibe la información del nodo que esta enviando 
    rospy.Subscriber('HI', String, callback)
# spin() Evita que python se salga hasta que se detenga
    rospy.spin()

if __name__ == '__main__':
    listener()
