import matplotlib.pyplot as plt                         #importing_modules_and_libraries
import numpy as np
import math as mh
import statistics as stc
import time 
from random import randrange as rand
import sys
print("[*         ] 10% Loaded!!!")                     #loading screen
time.sleep(1)
print("[**        ] 20% Loaded!!!")
time.sleep(1)
print("[***       ] 30% Loaded!!!")
time.sleep(1)
print("[****      ] 40% Loaded!!!")
time.sleep(1)
print("[*****     ] 50% Loaded!!!")
time.sleep(1)
print("[******    ] 60% Loaded!!!")
time.sleep(1)
print("[*******   ] 70% Loaded!!!")
time.sleep(1)
print("[********  ] 80% Loaded!!!")
time.sleep(1)
print("[********* ] 90% Loaded!!!")
time.sleep(1)
print("[**********] 100% Loaded!!!")


time.sleep(1)
print("                              HELLO SIR/MAM                                      ")
time.sleep(1.6)
na=str(input("Enter your name please:"))                #taking_name_as_an_input
nam=na.capitalize()
print("                           Thank  You ",nam)    
print("                   THIS IS A CALCULATOR ASSISTANT MADE BY W                     ")
time.sleep(4)
print("                          !!!Are You A Robot!!!                                  ")
time.sleep(2)
print("              A SECURITY CHECK WILL BE REQUIRED TO MOVE FORWARD                  ")
time.sleep(3.5)
print("                        THE PASSWORD IS:********                                 ")

#add_function
def add(a,b): 
    x=a+b
    return x
#substact_function
def subs(a,b):
    x=a-b
    return x
#multiplication_fumction
def mult(a,b):
    x=a*b
    return x
#division_function
def divd(a,b):
    x=a/b
    return x
#remainder_function
def rem(a,b):
    x=a%b
    return x

#standard_graph_function_using_input_coordinates
def grph():
    print("This will create a graph using your input coordinates")
    lst=[]
    xlst=[]
    ylst=[]
    p=0
    n=int(input("Enter the number of coordinates to be entered:"))
    for k in range(0,n):
        ele=[int(input("Enter X-Coordinates:")),int(input("Enter Y-Coordinates:"))]
        print(ele)
        lst.append(ele)
        abb=ele
        x=abb[0]
        y=abb[1]
        xlst.append(x)
        ylst.append(y)
    plt.plot(xlst,ylst)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Your Required Graph')
    plt.show()

#sine_curve
def sn1():
    x1=np.arange(0,4*np.pi,0.01)
    y1=np.sin(x1)
    plt.plot(x1,y1)
    plt.show()
    plt.xlabel('Values from 0 to 4pi')
    plt.ylabel('Value of sine function at respective point')
    plt.title('Sine curve')

#cosine_function
def cs1():
    x1=np.arange(0,4*np.pi,0.01)
    y1=np.cos(x1)
    plt.plot(x1,y1)
    plt.show()
    plt.xlabel('Values from 0 to 4pi')
    plt.ylabel('Value of cosine function at respective point')
    plt.title('Cosine curve')

#sine_and_cosine_function_merged
def sincosfn():
    x1=np.arange(0,4*np.pi,0.01)
    y1=np.sin(x1)
    z1=np.cos(x1)
    plt.plot(x1,y1,x1,z1)
    plt.show()
    plt.xlabel('Values from 0 to 4pi')
    plt.ylabel('Value of sine and cosine function at respective point')
    plt.title('Sine and Cosine curve')
                                                                        #2D Section
#circle_area_function
def cirar(r):
    ar=mh.pi*r*r
    print(ar)
#parallelogram_area_function
def prllar(bs,hg):
    ar=bs*hg
    print(ar)
#circumference_circle
def cir(r):
    permtr=2*mh.pi*r
    print(permtr)
#quadrilateral_perimeter
def perquad(l1,l2,l3,l4):
    dat=raw_input("Specify the quadrilateral in small letters:")
    if dat=="square"or"rhombos":
        perq=4*l1
        print(perq)
    elif dat=="parallelogram"or"rectangle":
        perq=2*l1+2*l2
        print(perq)
    else:
        perq=l1+l2+l3+l4
        print(perq)
#no_of_diagonals
def diag(sd):
    sdm=sd-3
    dg=sd*sdm*0.5
    print(dg)
#triangle_area_perimeter
def tri(s1,s2,s3):
    s4=s1+s2+s3
    s=s4*0.5
    ss1=s-s1
    ss2=s-s2
    ss3=s-s3
    ss4=s*ss1*ss2*ss3
    artr=ss4**0.5
    print("FOR AREA ENTER AR")
    print("FOR PERIMETER ENTER PE")
    datri=raw_input("Enter your Choice:")
    if datri=="AR":
        print(artr)
    elif datri=="PE":
        print(s4)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)

#2D_Structure_Conditionals
def geo():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("AREA OF CIRCLE               ENTER 1")
    print("AREA OF PARALLELOGRAM        ENTER 2")
    print("CIRCLE CIRCUMFERENCE         ENTER 3")
    print("QUADRILATERAL PERIMETER      ENTER 4")
    print("NO OF DIAGONAL               ENTER 5")
    print("TRIANGLE AREA PERIMETER      ENTER 6")
    cho=int(input("Enter Choice:"))
    if cho==1:
        r=int(input("Enter the radius of circle:"))
        cirar(r)
    elif cho==2:
        bs=int(input("Enter the length of the base:"))
        hg=int(input("Enter the length of the height:"))
        prllar(bs,hg)
    elif cho==3:
        r=int(input("Enter the radius of circle:"))
        cir(r)
    elif cho==4:
        print("ENTER THE LENGTH IN ORDER") 
        l1=int(input("Enter the first length:"))
        l2=int(input("Enter the second length:"))
        l3=int(input("Enter the third length:"))
        l4=int(input("Enter the fourth length:"))
        perquad(l1,l2,l3,l4)
    elif cho==5:
        sd=int(input("Enter the number the side:"))
        diag(sd)
    elif cho==6:
        print("ENTER THE LENGTH IN ORDER")
        s1=int(input("Enter the first side:"))
        s2=int(input("Enter the second side:"))
        s3=int(input("Enter the third side:"))
        tri(s1,s2,s3)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
                                                    #lateral_surface_area_functions
#cylinder_lateral_surface_area
def cyllsa():
    radcyl=int(input("Enter the radius:"))
    heicyl=int(input("Enter the height:"))
    clsa=2*mh.pi*radcyl*heicyl
    print(clsa)
#cone_lateral_surface_area    
def cnelsa():
    radcne=int(input("Enter the radius:"))
    heicne=int(input("Enter the height:"))
    rcn=radcne**2
    hcn=heicne**2
    slancne=rcn+hcn
    scn=slancne**0.5
    cnlsa=mh.pi*radcne*scn
    print(cnlsa)
#lateral_surface_area
def lsa():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Cylinder            ENTER 1")
    print("To Access Cone                ENTER 2")
    choilsa=int(input("Enter Choice:"))
    if choilsa==1:
        cyllsa()
    elif choilsa==2:
        cnelsa()
    else:
        print("ERROR",nam)
        sys.exit(0)
                                                        #total_surface_area_functions
#cylinder_total_surface_area
def cyltsa():
    radcyl=int(input("Enter the radius:"))
    heicyl=int(input("Enter the height:"))
    ctsa=2*mh.pi*radcyl*heicyl+2*mh.pi*radcyl*radcyl
    print(ctsa)
#cone_total_surface_area
def cnetsa():
    radcne=int(input("Enter the radius:"))
    heicne=int(input("Enter the height:"))
    rcn=radcne**2
    hcn=heicne**2
    slancne=rcn+hcn
    scn=slancne**0.5
    cntsa=mh.pi*radcne*scn+mh.py*radcne*radcne
    print(cntsa)
#sphere_total_surface_area
def sphtsa():
    rads=int(input("Enter the radius:"))
    stsa=4*mh.pi*rads*rads
    print(stsa)
#cuboid_total_surface_area
def cubtsa():
    clen=int(input("Enter the length:"))
    cbre=int(input("Enter the breadth:"))
    chei=int(input("Enter the height:"))
    cutsa=clen*cbre+cbre*chei+clen*chei
    ctsa=cutsa*2
    print(ctsa)
#total_surface_area
def tsa():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Cylinder            ENTER 1")
    print("To Access Cone                ENTER 2")
    print("To Access Sphere              ENTER 3")
    print("To Access Cuboid              ENTER 4")
    choitsa=int(input("Enter Choice:"))
    if choitsa==1:
        cyltsa()
    elif choitsa==2:
        cnetsa()
    elif choitsa==3:
        sphtsa()
    elif choitsa==4:
        cubtsa()
    else:
        print("ERROR",nam)
        sys.exit(0)
                                                                            #Volume
#cylinder_volume
def cylvol():
    radcyl=int(input("Enter the radius:"))
    heicyl=int(input("Enter the height:"))
    cyvol=mh.pi*radcyl*radcyl*heicyl
    print(cyvol)
#cone_volume
def cnevol():
    radcne=int(input("Enter the radius:"))
    heicne=int(input("Enter the height:"))
    cnvol=0.333333*mh.pi*radcne*radcne*heicne
    print(cnvol)
#sphere_volume
def sphvol():
    rads=int(input("Enter the radius:"))
    svol=1.333333*mh.pi*rads*rads*rads
    print(svol)
#cuboid_volume
def cubvol():
    clen=int(input("Enter the length:"))
    cbre=int(input("Enter the breadth:"))
    chei=int(input("Enter the height:"))
    cvol=clen*cbre*chei
    print(cvol)

#volume
def volm():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Cylinder            ENTER 1")
    print("To Access Cone                ENTER 2")
    print("To Access Sphere              ENTER 3")
    print("To Access Cuboid              ENTER 4")
    choivol=int(input("Enter Choice:"))
    if choivol==1:
        cylvol()
    elif choitsa==2:
        cnevol()
    elif choitsa==3:
        sphvol()
    elif choitsa==4:
        cubvol()
    else:
        print("ERROR",nam)
        sys.exit(0)
        

#3D_Structures_Conditionals
def geod():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Lateral Surface Area            ENTER 1")
    print("To Access Total Surface Area              ENTER 2")
    print("To Access Volume                          ENTER 3")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        lsa()
    elif choi==2:
        tsa()
    elif choi==3:
        volm()
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
                                                                        #Statistics
#mean_function
def mn():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    f=stc.mean(lst)
    print(f)
#median_function
def mdn():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    f=stc.median(lst)
    print(f)
#mode_function
def md():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    f=stc.mode(lst)
    print(f)
#sorting_values_functions
def srt():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    print("To Sort in Ascending                      ENTER asc")
    print("To Sort in Descending                     ENTER dsc")
    print("To Sort in Both Ascending and Descending  ENTER adsc")
    choc=raw_input("Enter your choice:")
    if choc=="asc":
        lst.sort()
        print(lst)
    elif choc=="dsc":
        lst.sort(reverse=True)
        print(lst)
    elif choc=="adsc":
        tsl=lst
        lst.sort()
        print("Ascending Order",lst)
        tsl.sort(reverse=True)
        print("Descending Order",tsl)
    else:
        print("WRONG CHOICE",nam)
        sys.exit(0)
#counting_the_number_of_appearances
def cnt():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    f=int(input("Enter the number to be counted:"))
    cntf=0
    for ksh in lst:
        if ksh==f:
            cntf+=1
    print(cntf)
#standard_deviation_function    
def stdr():
    lst=[]
    n=int(input("Enter the number of elements to be entered:"))
    for k in range(0,n):
        ele=int(input("Enter the element:"))
        lst.append(ele)
    print(lst)
    f=stc.stdev(lst)
    print(f)

#Statistics_Conditionals
def statst():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Mean                            ENTER 1")
    print("To Access Median                          ENTER 2")
    print("To Access Mode                            ENTER 3")
    print("To Access Sorting                         ENTER 4")
    print("To Access Count                           ENTER 5")
    print("To Access Standard Deviation              ENTER 6")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        mn()
    elif choi==2:
        mdn()
    elif choi==3:
        md()
    elif choi==4:
        srt()
    elif choi==5:
        cnt()
    elif choi==6:
        stdr()
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
                                                                        #conversions
#trigonometric_conversions
def trc():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Sine                            ENTER 1")
    print("To Access Cosine                          ENTER 2")
    print("To Access Tangent                         ENTER 3")
    print("To Access Secant                          ENTER 4")
    print("To Access Cosecant                        ENTER 5")
    print("To Access Cotangent                       ENTER 6")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        ang=int(input("Enter the angle in radians:"))
        x=mh.sin(ang)
        print(x)
    elif choi==2:
        ang=int(input("Enter the angle in radians:"))
        x=mh.cos(ang)
        print(x)
    elif choi==3:
        ang=int(input("Enter the angle in radians:"))
        x=mh.tan(ang)
        print(x)
    elif choi==4:
        ang=int(input("Enter the angle in radians:"))
        x=mh.cos(ang)
        y=1/x
        print(y)
    elif choi==5:
        ang=int(input("Enter the angle in radians:"))
        x=mh.sin(ang)
        y=1/x
        print(y)
    elif choi==6:
        ang=int(input("Enter the angle in radians:"))
        x=mh.tan(ang)
        y=1/x
        print(y)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
#logarithm_conversions
def lgc():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Natural Logarithm               ENTER 1")
    print("To Access Logarithm base 10               ENTER 2")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        x=float(input("Enter any positive number:"))
        y=mh.log(x)
        print(y)
    elif choi==2:
        x=float(input("Enter any positive number:"))
        y=mh.log10(x)
        print(y)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
#angular_conversions
def agc():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To convert degrees to radians               ENTER 1")
    print("To convert radians to degrees               ENTER 2")
    choi=int(input("Enter The Choice:"))
    if choi==2:
        x=float(input("Enter any positive number:"))
        y=mh.degrees(x)
        print(y)
    elif choi==1:
        x=float(input("Enter any positive number:"))
        y=mh.radians(x)
        print(y)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
#values_of_constant
def cntcv():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access value of pi                          ENTER 1")
    print("To Access value of tau                         ENTER 2")
    print("To Access value of eulers number               ENTER 3")
    choivol=int(input("Enter Choice:"))
    if choivol==1:
        x=mh.pi
        print(x)
    elif choitsa==2:
        x=mh.tau
        print(x)
    elif choitsa==3:
        x=mh.e
        print(x)
    else:
        print("ERROR",nam)
        sys.exit(0)
#inverse_trigonometric_conversions
def itrc():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Sine                            ENTER 1")
    print("To Access Cosine                          ENTER 2")
    print("To Access Tangent                         ENTER 3")
    print("To Access Secant                          ENTER 4")
    print("To Access Cosecant                        ENTER 5")
    print("To Access Cotangent                       ENTER 6")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        ang=int(input("Enter the value:"))
        x=mh.asin(ang)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    elif choi==2:
        ang=int(input("Enter the value:"))
        x=mh.acos(ang)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    elif choi==3:
        ang=int(input("Enter the value:"))
        x=mh.atan(ang)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    elif choi==4:
        ang=int(input("Enter the value:"))
        vl=1/ang
        x=mh.acos(ang)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    elif choi==5:
        ang=int(input("Enter the value:"))
        vl=1/ang
        x=mh.asin(ang)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    elif choi==6:
        ang=int(input("Enter the value:"))
        vl=1/ang
        x=mh.atan(vl)
        print("In Radians",x)
        y=mh.degrees(x)
        print("In Degrees",y)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)
#quadratic_root_function
def rtqdrt():
    print("A QUADRATIC EQUATION LOOKS LIKE ax2+bx+c=0; ACCORDINGLY PUT THE VALUES")
    a0=int(input("Enter the value of a:"))
    b0=int(input("Enter the value of b:"))
    c0=int(input("Enter the value of c:"))
    disc0=(b0**2-4*a0*c0)*0.5
    d0=disc0-b0
    e0=-disc0-b0
    h0=2*a0
    f0=d0/h0
    g0=e0/h0
    print("PROCESSING")
    print("The root of the equation are",f0,"and",g0)
#lcm_function
def lcm(hs,hd):
    if hs>hd:
        greater=hs
    else:
        greater=hd
    while(True):
        if ((greater%hs==0) and (greater%hd==0)):
            lcm=greater
            break
        greater+=1
    return lcm
#gcd_function
def gcd(hs,hd):
    if hs>hd:
        smaller=hd
    else:
        smaller=hs
    while(True):
        if ((hs%smaller==0) and (hd%smaller==0)):
            hcf=smaller
            break
        smaller-=1
    return hcf
#random_fun_with_maths_conditionals
def stcv():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Comparison of 3 numbers                             ENTER 1")
    print("To Access Roots of Quadratic Equation                         ENTER 2")
    print("To Access Exponentiation                                      ENTER 3")
    print("To Access Rooting                                             ENTER 4")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        va1=float(input("Enter the first number:"))
        va2=float(input("Enter the second number:"))
        va3=float(input("Enter the third number:"))
        if va1>va2 and va1>va3:
            if v2>v3:
                print("Max is",va1)
                print("Mid is",va2)
                print("Min is",va3)
            else:
                print("Max is",va1)
                print("Mid is",va3)
                print("Min is",va2)
        elif va2>va1 and va2>va3:
            if v1>v3:
                print("Max is",va2)
                print("Mid is",va1)
                print("Min is",va3)
            else:
                print("Max is",va2)
                print("Mid is",va3)
                print("Min is",va1)
        else:
            if v2>v1:
                print("Max is",va3)
                print("Mid is",va2)
                print("Min is",va1)
            else:
                print("Max is",va3)
                print("Mid is",va1)
                print("Min is",va2)
    elif choi==2:
        rtqdrt()
    elif choi==3:
        ang1=float(input("Enter the base:"))
        ang2=float(input("Enter the power:"))
        y=ang1**ang2
        print(y)
    elif choi==4:
        ang1=float(input("Enter the base:"))
        ang2=float(input("Enter the power:"))
        ang3=1/ang2
        y=ang1**ang3
        print(y)
    elif choi==5:
        print("Welcome to Random Fun Section",nam)
        print("To Access Printing Random Stuff                       ENTER 1")
        print("To Access L.C.M of two numbers                        ENTER 2")
        print("To Access H.C.F of two numbers                        ENTER 3")
        choce=int(input("Enter The Choice:"))
        if choce==1:
            a=raw_input("Enter the character to be found:")
            my_string = a
            current_str = ""
            for letter in my_string:
                prnrndm(current_str, letter)
                current_str += letter
            print("TARGET REACHED!!!")
        elif choce==2:
            num1=int(input("Enter first number:"))
            num2=int(input("Enter second number:"))
            print("The L.C.M. of",num1,"and",num2,"is",lcm(num1,num2))
        elif choce==3:
            num1=int(input("Enter first number:"))
            num2=int(input("Enter second number:"))
            print("The H.C.F. of",num1,"and",num2,"is",gcd(num1,num2))
        else:
            print("WRONG INPUT",nam)
            sys.exit(0)
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)

#conversions_Conditionals
def conv():
    print("ENTER YOUR CHOICE ACCORDINGLY")
    print("To Access Trigonometric conversions                                   ENTER 1")
    print("To Access Logarithmic conversions                                     ENTER 2")
    print("To Access Angular conversions                                         ENTER 3")
    print("To Access Values of constants                                         ENTER 4")
    print("To Access Inverse Trigonometric conversions                           ENTER 5")
    print("To Access Random Fun With Maths                                       ENTER 6")
    choi=int(input("Enter The Choice:"))
    if choi==1:
        trc()
    elif choi==2:
        lgc()
    elif choi==3:
        agc()
    elif choi==4:
        cntcv()
    elif choi==5:
        itrc()
    elif choi==6:
        stcv()
    else:
        print("WRONG INPUT",nam)
        sys.exit(0)


#operation_and_assingning_function
def calctr():
    c=int(input("Enter the operation to be done:"))
    if c==1:
        a=int(input("Enter the first number to be processed:"))
        b=int(input("Enter the second number to be processed:"))
        d=add(a,b)
        print("The sum of the numbers",a,"and",b,"is",d)
    elif c==2:
        a=int(input("Enter the first number to be processed:"))
        b=int(input("Enter the second number to be processed:"))
        d=subs(a,b)
        print("The difference of the numbers",a,"and",b,"is",d)
    elif c==3:
        a=int(input("Enter the first number to be processed:"))
        b=int(input("Enter the second number to be processed:"))
        d=mult(a,b)
        print("The product of the numbers",a,"and",b,"is",d)
    elif c==4:
        a=int(input("Enter the first number to be processed:"))
        b=int(input("Enter the second number to be processed:"))
        d=divd(a,b)
        print("The quotiont of the numbers",a,"and",b,"is",d)
    elif c==5:
        a=int(input("Enter the first number to be processed:"))
        b=int(input("Enter the second number to be processed:"))
        d=rem(a,b)
        print("The remainder of the numbers",a,"and",b,"is",d)
    elif c==6:
        grph()
    elif c==7:
        sn1()
    elif c==8:
        cs1()
    elif c==9:
        sincosfn()
    elif c==10:
        geo()
    elif c==11:
        geod()
    elif c==12:
        statst()
    elif c==13:
        conv()
    else:
        print("WRONG INPUT",nam)
        main()


#continuation_function
def con():
    print("Do You want to continue?")
    print("TO CONTINUE press any key,OTHERWISE press Enter")
    key=input("ENTER CHOICE:")
    if key!='':
        main()
        con()
    else:
        sys.exit(0)


#List_of_operaions
def main():
    print('''    To ADD                    Enter 1
    To SUBSTRACT              Enter 2
    To MULTIPLY               Enter 3
    To DIVIDE                 Enter 4
    To REMAIN                 Enter 5
    To ACCESS graph           Enter 6
    To Get Sin graph          Enter 7
    To Get Cos graph          Enter 8
    To Get Sin & Cos graph    Enter 9
    To Access 2D Geometry     Enter 10
    To Access 3D Geometry     Enter 11
    To Access Statistics      Enter 12
    To Access Conversions     Enter 13''') 
    calctr()
                                                                #password_security
#password_function_defined
def pswd():
    p=input("Password: ") 
    if p=="********":
        main()
        con()
    else:
        print("Wrong Password")
        pswd() 
pswd()

