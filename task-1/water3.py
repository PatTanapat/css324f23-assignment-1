def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return (s[0]==4 and s[1]==4)

def successors(s):
    x, y, z = s
    if x>0:
        vy=5-y
        vz=3-z
        if y<5:
            if x>vy:
               yield ((x-vy,5,z),vy)
            else:
               yield ((0,y+x,z),x)
        if z<3:
             if x>vz:
               yield ((x-vz,5,z),vz)  
             else:
               yield ((0,y,x+z),x)
    if y>0:
        vz=3-z
        yield ((x+y,0,z),y)
        if z<3:
            if y>vz:
              yield ((x,y-vz,3),vz)  
            else:
              yield ((x,0,y+z),x)
    if z>0:
       vy=5-y
       yield((x+z,y,0),z)
       if z<3:
          if z<vy:
             yield((x,5,z-vy),vy)
          else:
             yield((x,y+z,0),z)
             
       
            
        
    
