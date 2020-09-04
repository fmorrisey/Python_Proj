#Imports System Depend
from os import system, name
from subprocess import call, os
from time import sleep

#Imports Astronomical Charts
from skyfield.api import load
from skyfield.api import Topos
from astropy import units as u

# define clear function 
def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls') 


def _break_():

    print("#############", " ", sep='\n')

    pass

def copernicus():
    #loads timescale
    ts = load.timescale(builtin=True)
    t = ts.now()

    #Computes Position of Mars in the Sky
    planets = load('de421.bsp')
    eph = load('de421.bsp')
    earth, mars = planets['earth'], planets['mars']
        
    astronomic = earth.at(t).observe(mars)
    ra , dec, distance = astronomic.radec()

    #load planets
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

    #Geocentric Coords @ Urban Ecology Center Tower uecTwr
    uecTwr= earth + Topos('43.067754 N', '-87.891068 W')
    astronomic = uecTwr.at(t).observe(mars)
    alt, az, d = astronomic.apparent().altaz()

    #Astropy API returns
    """Fix
    xyz = ?astrometric.postition.to(u.au)?
    altitude = alt.to(u.deg)
    """

    #moonphase
    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().ecliptic_latlon()
    _, mlon, _ = e.observe(moon).apparent().ecliptic_latlon()
    phase = phasePass = (mlon.degrees - slon.degrees) % 360.0
    #Convert Variable
    
    
    if int(phasePass) in range(0, 22):
        phaseViz = str("New Moon Phase")
    elif int(phasePass) in range(23, 68):
        phaseViz = str("Waxing Cresent Moon")
    elif int(phasePass) in range(69, 112):
        phaseViz = str("1st Quarter Moon")
    elif int(phasePass)  in range(113, 157):
        phaseViz = str("Waxing Gibbous Moon")
    elif int(phasePass) in range(158, 175):
        phaseViz = str("Almost Full Moon")
    
    elif int(phasePass) in range(176, 185):
        phaseViz = str("Full Moon")

    elif int(phasePass) in range(186, 270):
        phaseViz = str("Wanning Gibbous Moon")
    elif int(phasePass) in range(292, 314):
        phaseViz = str("3rd Quarter Moon")
    elif int(phasePass)  in range(315, 336):
        phaseViz = str("Wanning Cresent Moon")
    elif int(phasePass) in range(337, 360):
        phaseViz = str("New Moon Phase")

    else: 
        phaseViz = str("Error Check Code")
    

    #print results_printed
    print("Position and Distance of Mars", ra, dec, distance, " ", sep='\n')
    _break_()
    print("Geocenteric coordinates", alt, az, "", sep='\n')
    _break_()
    #FIX print(xyz, '{0:0.03f}'.format(altitude))
    #FIX _break_()
    print("Moon Phase", '{0:.5f}'.format(phase), phaseViz, "", sep='\n')

#Ask for observation length and time in sec
observationCount = int(input("How long would like to observe the cosmos?:  "))
observationTime = float(input("How often are these observations?(sec):  "))


#Start at 1
observationCount += 1
observationTime += 1

for count in range(0,observationCount):
    clear()
    copernicus()
    sleep(observationTime)
    count + 1
    print(count)
