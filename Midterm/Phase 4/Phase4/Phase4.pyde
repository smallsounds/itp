def setup():
    size(400, 400)
    noStroke()
    
def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    fill(255, 255, 255);
    ellipse(100, 145, 160, 50);
    fill(255, 213, 44);
    square(60, 70, 80);
    fill(255, 255, 255);
    quad(70, 90, 75, 100, 70, 110, 65, 100);
    quad(130, 80, 135, 90, 130, 100, 125, 90);
    quad(110, 120, 115, 130, 110, 140, 105, 130);
    pop()

def draw():
    i=5
    h=height / i
    s=h / 200.0
    for p in range(i):
        for k in range(i):
            drawObject(h*p,h*k,s);
