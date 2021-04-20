#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

import rospy 	# Se importa para escribir un nodo de ROS
from std_msgs.msg import String # Para poder utilizar el tipo mensaje String

# Variables globales
x=""
c=""
d=0

# Función toma la decisión del porcentaje de velocidad que va el motor y se la envia a Arduino.
def var_global(a):
    global x,c,d
    d=d+1
    c=c+a
    if d==3:
        flag = False  # Bandera para saber si se ejecutó algún if
        # Según la combinación de los Char recibidos ejecuta una acción diferemte
        if c=="Aah" or c=="Aha" or  c=="aAh" or c=="ahA" or c=="hAa" or  c=="haA":
            x="Motor al 100 %"
            flag = True
        if c=="Aai" or c=="Aia" or  c=="aAi" or c=="aiA" or c=="iAa" or  c=="iaA":
            x="Motor al 90 %"
            flag = True
        if c=="Aal" or c=="Ala" or  c=="aAl" or c=="alA" or c=="lAa" or  c=="laA":
            x="Motor al 75 %"
            flag = True
        if c=="Amh" or c=="Ahm" or  c=="mAh" or c=="mhA" or c=="mAa" or  c=="maA":
            x="Motor al 90 %"
            flag = True
        if c=="Ami" or c=="Aim" or  c=="mAi" or c=="miA" or c=="iAm" or  c=="imA":
            x="Motor al 65 %"
            flag = True
        if c=="Aml" or c=="Alm" or  c=="mAl" or c=="mlA" or c=="lAm" or  c=="lmA":
            x="Motor al 55 %"
            flag = True
        if c=="Abh" or c=="Ahb" or  c=="bAh" or c=="bhA" or c=="hAb" or  c=="hbA":
            x="Motor al 75 %"
            flag = True
        if c=="Abi" or c=="Aib" or  c=="bAi" or c=="biA" or c=="iAb" or  c=="ibA":
            x="Motor al 55 %"
            flag = True
        if c=="Abl" or c=="Alb" or  c=="bAl" or c=="blA" or c=="lAb" or  c=="lbA":
            x="Motor al 50 %"
            flag = True
        if c=="Bah" or c=="Bha" or  c=="aBh" or c=="ahB" or c=="hBa" or  c=="haB":
            x="Motor al 50 %"
            flag = True
        if c=="Bai" or c=="Bia" or  c=="aBi" or c=="aiB" or c=="iBa" or  c=="iaB":
            x="Motor al 25 %"
            flag = True
        if c=="Bal" or c=="Bla" or  c=="aBl" or c=="alB" or c=="lBa" or  c=="laB":
            x="Motor al 35 %"
            flag = True
        if c=="Bmh" or c=="Bhm" or  c=="mBh" or c=="mhB" or c=="hBm" or  c=="hmB":
            x="Motor al 30 %"
            flag = True
        if c=="Bmi" or c=="Bim" or  c=="mBi" or c=="miB" or c=="iBm" or  c=="imB":
            x="Motor al 40 %"
            flag = True
        if c=="Bml" or c=="Blm" or  c=="mBl" or c=="mlB" or c=="lBm" or  c=="lmB":
            x="Motor al 20 %"
            flag = True
        if c=="Bbh" or c=="Bhb" or  c=="bBh" or c=="bhB" or c=="hBb" or  c=="hbB":
            x="Motor al 35 %"
            flag = True
        if c=="Bbi" or c=="Bib" or  c=="bBi" or c=="biB" or c=="iBb" or  c=="ibB":
            x="Motor al 20 %"
            flag = True
        if c=="Bbl" or c=="Blb" or  c=="bBl" or c=="blB" or c=="lBb" or  c=="lbB":
            x="Motor al 10 %"
            flag = True
        if flag == False:
            x="Motor al 0 %"
        c=""
        d=0
        
def callback(data):
    y=data.data
    rospy.loginfo(y)
    var_global(y)

def nodoH():
    global x
    # rospy.Publisher('chatter', tipo de mensaje, mensajes en cola si el subscritor no los ha recibido)
    str_I = rospy.Publisher('HI', String, queue_size=10) 
    # INICIADOR DEL NODO: rospy.category:themes init_node('nombre_del_nodo', anonymous) 
    # Si anonymous = true => hace que cada nodo sea único y asigna un número aleatorio al final del nombre del nodo; si anonymous = false => el nodo va a tener nombre único 
    rospy.init_node('NodoH', anonymous=False)
    # Definir la velocidad en 0.2 Hz por ciclo
    rate = rospy.Rate(0.2) 
    # Recibe la información del nodo que esta enviando 
    rospy.Subscriber('EH', String, callback)
    rospy.Subscriber('FH', String, callback)
    rospy.Subscriber('GH', String, callback)

    while not rospy.is_shutdown():
        rospy.loginfo(x)    # Muestra en el terminal #a40000lo que esta enviando
        str_I.publish(x)      # Envia la información por el nodo
        rate.sleep()                # Hace cumplir el ciclo de 1 Hz
if __name__ == '__main__':
    try:
        nodoH()
    except rospy.ROSInterruptException:
        pass
