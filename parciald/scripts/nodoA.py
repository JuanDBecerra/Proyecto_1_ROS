#!/usr/bin/env python  # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
import random
from std_msgs.msg import Bool # Para poder utilizar el tipo mensaje String
from std_msgs.msg import Float32
from std_msgs.msg import UInt16

def nodoA():
# rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    pubB = rospy.Publisher('AB', Bool, queue_size=100)
    pubC = rospy.Publisher('AC', UInt16, queue_size=100)
    pubD = rospy.Publisher('AD', Float32, queue_size=100)
    # INICIADOR DEL NODO: rospy.init_node('nombre_del_nodo', anonymous)
    # si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; 
    # Si anonymous = false => el nodo va a tener nombre único
    rospy.init_node('NodoA', anonymous=False)
    # Definir la velocidad en 10 Hz por ciclo
    rate = rospy.Rate(10) # 10hz
    # Realiza el while hasta que no se apague el Nodo
    while not rospy.is_shutdown():
        b=random.randint(0, 1)          # Randomico para simular bool
        c=random.randint(0, 255)        # Randomico para simular int
        d=random.randint(0, 50)/10.0    # Randomico para simular float
        if b==0:
            send_b = False              # Mensaje que el nodo va a enviar
        if b==1:
            send_b= True               # Mensaje que el nodo va a enviar
        send_c=c
        send_d=d
        rospy.loginfo(send_b)      # Muestra en el terminal lo que esta enviando
        rospy.loginfo(send_c)
        rospy.loginfo(send_d)
        # Envia la información por el nodo
        pubB.publish(send_b)
        pubC.publish(send_c)
        pubD.publish(send_d)
        # Hace cumplir el ciclo de 10 Hz
        rate.sleep()

if __name__ == '__main__':
    try:
        nodoA()
    except rospy.ROSInterruptException:
        pass
