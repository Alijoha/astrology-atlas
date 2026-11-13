# Swiss Ephemeris is an optional validation dependency, never shipped with the app.
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '.validation'))
import swisseph as swe
cases=[('2000-01-01T12:00:00Z',2000,1,1,12.,51.4779,0.),('1995-11-07T14:30:00Z',1995,11,7,14.5,51.5074,-.1278),('1990-06-15T12:30:00Z',1990,6,15,12.5,40.7128,-74.006),('2024-04-08T18:00:00Z',2024,4,8,18.,-33.8688,151.2093)]
refs=[]
for iso,y,m,d,h,lat,lon in cases:
 jd=swe.julday(y,m,d,h)
 pos={name:swe.calc_ut(jd,body,swe.FLG_MOSEPH|swe.FLG_SPEED)[0][0] for name,body in [('Sun',swe.SUN),('Moon',swe.MOON),('Mercury',swe.MERCURY),('Venus',swe.VENUS),('Mars',swe.MARS),('Jupiter',swe.JUPITER),('Saturn',swe.SATURN),('Uranus',swe.URANUS),('Neptune',swe.NEPTUNE),('Pluto',swe.PLUTO)]}
 cusps,angles=swe.houses(jd,lat,lon,b'W')
 refs.append(dict(utc=iso,lat=lat,lon=lon,positions=pos,asc=angles[0],mc=angles[1]))
print(json.dumps(dict(reference='Swiss Ephemeris '+swe.version,mode='Moshier, geocentric apparent tropical of date, whole-sign houses',cases=refs),indent=2))
