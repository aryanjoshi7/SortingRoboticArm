import math
#import matplotlib.pyplot as plt
#import numpy as np
import sys
import serial
import time

#from serialsend import *
def coslaw(a,b,c):
    return math.acos((pow(a,2)+pow(b,2)-pow(c,2))/(2*a*b))
def coslawangle(a,b,ang):
    return pow(((pow(a,2)+pow(b,2))-(2*a*b*math.cos(math.radians(ang)))),.5)

def mover(first, second, third):
    start = (0,4)
    target = [first, second, third]
    print(target)


    link1 = 4.125
    link2 = 3.5
    link3 = 7
    angle2_3 = 115
    z = abs(math.atan((target[1]-start[1])/(target[0]-start[0])))
    if target[1]>start[1]:
        z=z*-1
    #z = abs(math.atan((target[1]-start[1])/(target[0]-start[0])))
    intermediate = coslawangle(link2,link3,angle2_3)

    interangle = coslaw(link2,intermediate,link3)

    hypot = pow(pow(target[0]-start[0],2)+pow(target[1]-start[1],2),.5)

    angle1 = coslaw(hypot,link1, intermediate)-z

    angle2 = coslaw(intermediate, link1, hypot)
    angle2+=interangle


    explinks = [link1,link2,link3]
    angles = [angle1,angle2, math.radians(angle2_3)]
    print("Right here",angles)
    X = [start[0]]
    Y = [start[1]]
    actualang = []
    for i in range(3):
        if i>0:
            temp = angles[i]+actualang[i-1]-math.radians(180)
        else:
            temp = angles[i]
        X.append(X[i]+explinks[i]*math.cos(temp))
        Y.append(Y[i]+explinks[i]*math.sin(temp))
        actualang.append(temp)
        print(math.degrees(temp))
    print("Another thing")
    print(X,Y)

    angles[1] = math.radians(math.degrees(angles[1])-90)
    angles[2] = math.radians(math.degrees(angles[2])-90)

    stringsend = str(len(angles)+1)+" "

    rotang = math.degrees(math.asin(target[2]/target[0]))
    print("this",rotang)

    print(rotang)
    #helf = int(((2000/180)*rotang)+500)

    helf = int(((1312/118.08)*rotang)-1844)*-1
    print(helf)
    #exit()
    if helf<500 or helf>2500:
            print(helf)
            exit()

    stringsend = stringsend+str(6)+"_"+str(helf)+" "
    print("This is what I am looking at")
    print(angles, math.degrees(angles[0]))
    for i in range(len(angles)):
    #    math.degrees(print(angles[i]))
            if i == 0:
                helf = int(((2000/180)*math.degrees(angles[i]))+500)
                    helf = ((1500-helf)*2)+helf
                    helf-=90
                    if helf<500 or helf>2500:
                        print(helf,i)
                        exit()
                    stringsend = stringsend+str(6-i-1)+"_"+str(helf)+" "
                    #stringsend = stringsend+str(6-i-1)+"_"+str(int(((2000/180)*math.degrees(angles[i]))+500))+" "
            elif i == 1:
                    helf = int(((2000/180)*math.degrees(angles[i]))+500)
                    #helf = int(((1848/180)*math.degrees(angles[i]))+552)
                    helf+=70

                    if helf<500 or helf>2500:
                        print(helf,i)
                        exit()
                    stringsend = stringsend+str(6-i-1)+"_"+str(helf)+" "
            else:
                    helf = int(((2000/180)*math.degrees(angles[i]))+500)
                    #helf = int(((1848/180)*math.degrees(angles[i]))+552)
                    if helf<500 or helf>2500:
                            exit()
                    helf+=50
                    stringsend = stringsend+str(6-i-1)+"_"+str(helf)+" "
    print(stringsend)
    tosend = stringsend
    sendmssg(tosend)