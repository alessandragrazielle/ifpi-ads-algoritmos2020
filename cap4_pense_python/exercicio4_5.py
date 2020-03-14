import turtle
pen = turtle.Turtle()

def	polyline(t,	n, length, angle):				
    for	i in range(n):
        t.fd(length)								
        t.lt(angle)

def	polygon(t, n, length):				
    angle = 360.0 / n				
    polyline(t,	n, length, angle) 

def	arc(t, r, angle):				
    arc_length = 2 * 3.14 *	r *	angle /	360				
    n =	int(arc_length / 3)				
    step_length	= arc_length / n				
    step_angle	= float(angle) / n				
    polyline(t,	n, step_length,	step_angle) 

def	circle(t, r):				
    arc(t, r, 360) 

arc(pen, 100, 180)
