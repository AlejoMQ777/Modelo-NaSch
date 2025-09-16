import random, time


W, H = 40, 20    
N = 10            
V = 8             

boids = [[random.randint(0, W-1),
          random.randint(0, H-1),
          random.choice([-1, 0, 1]),
          random.choice([-1, 0, 1])]
         for _ in range(N)]

def mostrar():
    tablero = [["." for _ in range(W)] for _ in range(H)]
    for x, y, vx, vy in boids:
        tablero[y % H][x % W] = "O"
    for fila in tablero: print("".join(fila))
    print("-"*W)

def mover():
    for b in boids:
        x, y, vx, vy = b
        cerca = [o for o in boids if o != b and abs(o[0]-x)<V and abs(o[1]-y)<V]
        if cerca:
          
            cx = sum(o[0] for o in cerca)//len(cerca)
            cy = sum(o[1] for o in cerca)//len(cerca)
            vx += (cx-x)//max(1,len(cerca))
            vy += (cy-y)//max(1,len(cerca))
            # Alineación: seguir dirección
            vx += sum(o[2] for o in cerca)//len(cerca)
            vy += sum(o[3] for o in cerca)//len(cerca)
        
        vx = max(-1, min(1, vx))
        vy = max(-1, min(1, vy))
       
        b[0] = (x+vx)%W
        b[1] = (y+vy)%H
        b[2], b[3] = vx, vy


for _ in range(50):
    mostrar()
    mover()
    time.sleep(0.2)

