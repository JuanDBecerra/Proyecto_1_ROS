#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir uno de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String
from std_msgs.msg import UInt16 # Usar el mensaje UInt16

x=None
# Función para enviar datos, segun la información que reciba.
def var_global(a):
    global x
    if a>=0 and a<85:
        alto=0
        medio=0
        bajo=100
    if a>=85 and a<127:
        alto = 6350/21 - (50*a)/21
        medio = (50*a)/21 - 4250/21
        bajo=0
    if a>=127 and a<170:
        alto =0
        medio=17000/43 - (100*a)/43
        bajo= (100*a)/43 - 12700/43
    if a>=170 and a<=255:
        alto=100
        medio=0
        bajo=0
    alto = f"{alto:.2f}"	# El float solo presenta dos decimales.
    medio = f"{medio:.2f}"
    bajo = f"{bajo:.2f}"
    alto=alto.zfill(6)
    medio=medio.zfill(6)	# String.zfill(n), n = número de caracteres que va a tener el string, forma de asegurarse que el número se envia de la forma xxx.xx 
    bajo=bajo.zfill(6)
    x=f"Alto/{alto}/Medio/{medio}/Bajo/{bajo}"
    
# Función que recibe la informacion de otro nodo.        
def callback(data):
    y=data.data
    rospy.loginfo(y)
    var_global(y)

def nodoC():
    global x
    # rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    str_F = rospy.Publisher('CF', String, queue_size=100) 
    # INICIADOR DEL NODO: rospy.category:themes init_node('nombre_del_nodo', anonymous) 
    # Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('NodoC', anonymous=False)
    # Definir la velocidad en 1 Hz por ciclo
    rate = rospy.Rate(1) 
    # Recibe la información del nodo que esta enviando 
    rospy.Subscriber('AC', UInt16, callback)
    # While hasta que se interrumpa el nodo
    while not rospy.is_shutdown():
        rospy.loginfo(x)    # Muestra en el terminal #a40000lo que esta enviando
        str_F.publish(x)      # Envia la información por el nodo
        rate.sleep()                # Hace cumplir el ciclo de 1 Hz
if __name__ == '__main__':
    try:
        nodoC()
    except rospy.ROSInterruptException:
        pass
