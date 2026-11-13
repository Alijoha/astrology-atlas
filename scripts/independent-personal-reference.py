# Optional validation only. Swiss Ephemeris is never a runtime dependency.
import json, sys
from pathlib import Path
import swisseph as swe
swe.set_sid_mode(swe.SIDM_LAHIRI)
planets=[('Sun',swe.SUN),('Moon',swe.MOON),('Mercury',swe.MERCURY),('Venus',swe.VENUS),('Mars',swe.MARS),('Jupiter',swe.JUPITER),('Saturn',swe.SATURN),('Uranus',swe.URANUS),('Neptune',swe.NEPTUNE),('Pluto',swe.PLUTO)]
cases=[]
for y,m,d,h in [(1900,1,1,12),(1950,6,1,12),(2000,1,1,12),(2024,4,8,18),(2099,12,31,12)]:
 jd=swe.julday(y,m,d,h);pos={name:swe.calc_ut(jd,body,swe.FLG_MOSEPH|swe.FLG_SIDEREAL)[0][0] for name,body in planets};_,an=swe.houses_ex(jd,51.4779,0,b'W',swe.FLG_SIDEREAL);shift=swe.get_ayanamsa_ut(jd)
 swe.set_sid_mode(swe.SIDM_FAGAN_BRADLEY)
 fagan={name:swe.calc_ut(jd,body,swe.FLG_MOSEPH|swe.FLG_SIDEREAL)[0][0] for name,body in planets}
 _,fagan_angles=swe.houses_ex(jd,51.4779,0,b'W',swe.FLG_SIDEREAL)
 cases.append(dict(date=f'{y:04}-{m:02}-{d:02}',time=f'{int(h):02}:00',ayanamsa=shift,positions=pos,asc=an[0],faganAyanamsa=swe.get_ayanamsa_ut(jd),faganPositions=fagan,faganAsc=fagan_angles[0]))
 swe.set_sid_mode(swe.SIDM_LAHIRI)
def wrap(x):return (x+180)%360-180
def lon(body,jd):return swe.calc_ut(jd,body,swe.FLG_MOSEPH)[0][0]
natal=swe.julday(2000,1,1,12)
transits=[]
for moving,natal_body,angle in [('Mars','Sun',90),('Venus','Moon',120),('Jupiter','Venus',60),('Saturn','Sun',60)]:
 body=dict(planets)[moving];target=lon(dict(planets)[natal_body],natal);start=swe.julday(2024,1,1,0);end=swe.julday(2025,1,1,0);found=None
 for i in range(int((end-start)*4)):
  lo=start+i/4;hi=lo+.25
  for sign in ([1] if angle in [0,180] else [1,-1]):
   point=(target+sign*angle)%360;fa=wrap(lon(body,lo)-point);fb=wrap(lon(body,hi)-point)
   if fa*fb<=0 and abs(fa-fb)<30:
    for k in range(40):
     mid=(lo+hi)/2;fm=wrap(lon(body,mid)-point)
     if fa*fm<=0:hi=mid
     else:lo=mid;fa=fm
    found=(lo+hi)/2;break
  if found:break
 if found:transits.append(dict(moving=moving,natal=natal_body,angle=angle,unixMs=(found-2440587.5)*86400000))
print(json.dumps(dict(source='Swiss Ephemeris '+swe.version+'; Moshier, apparent positions, Lahiri sidereal mode. Transit targets independently calculated from natal 2000-01-01 12:00 UTC.',cases=cases,transits=transits),indent=2))
