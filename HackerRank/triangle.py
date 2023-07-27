import math 
import decimal as d
ab, bc = int(input()), int(input())
ac = math.hypot(ab, bc)
mc = ac / 2
 
# formula para el triangulo recto, conociendo todos sus lados. 
#  seno(ang) = cateto opuestos sobre hypo, sen(ang) = mc/bc , ang = arcseno(mc/bc)
print(ac)
print(mc)
ang = math.degrees(math.atan(ab/bc))

dec_part = math.modf(ang)[0]

if (dec_part * 10) >= 5:
    ang = math.ceil(ang)
else:
    ang = math.floor(ang)
      
print(ang, chr(176), sep='')