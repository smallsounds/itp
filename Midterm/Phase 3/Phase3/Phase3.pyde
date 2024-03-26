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
    drawObject(0, 0, 1)
    drawObject(200, 200, 1)
