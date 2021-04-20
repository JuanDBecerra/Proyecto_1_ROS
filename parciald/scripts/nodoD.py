#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String
from std_msgs.msg import Float32 # Usar el mensaje tipo Float32
x=None
def var_global(a):
    global x
    if a>=0 and a<1.25:
        alto=0
        medio=0
        bajo=100
    if a>=1.25 and a<2.5:
        alto = 200 - 80*a
        medio = 80*a - 100
        bajo=0
    if a>=2.5 and a<3.75:
        alto =0
        medio=300 - 80*a
        bajo= 80*a - 200
    if a>=3.75 and a<=5:
        alto=100
        medio=0
        bajo=0
    alto = f"{alto:.2f}"	# El float solo presenta dos decimales
    medio = f"{medio:.2f}"
    bajo = f"{bajo:.2f}"
    alto=alto.zfill(6)		# String.zfill(n), n = número de caracteres que va a tener el string, forma de asegurarse que el número se envia de la forma xxx.xx 
    medio=medio.zfill(6)
    bajo=bajo.zfill(6)
    x=f"Alto/{alto}/Medio/{medio}/Bajo/{bajo}"

def callback(data):
    y=data.data
    rospy.loginfo(y)
    var_global(y)

def nodoD():
    global x
    # rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    str_G = rospy.Publisher('DG', String, queue_size=100) 
    # INICIADOR DEL NODO: rospy.category:themes init_node('nombre_del_nodo', anonymous) 
    # Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('NodoD', anonymous=False)
    # Definir la velocidad en 1 Hz por ciclo
    rate = rospy.Rate(1) 
    # Recibe la información del nodo que esta enviando 
    rospy.Subscriber('AD', Float32, callback)
    while not rospy.is_shutdown():
        rospy.loginfo(x)    # Muestra en el terminal #a40000lo que esta enviando
        str_G.publish(x)      # Envia la información por el nodo
        rate.sleep()                # Hace cumplir el ciclo de 1 Hz
if __name__ == '__main__':
    try:
        nodoD()
    except rospy.ROSInterruptException:
        pass
