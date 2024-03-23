# Phase 2

I decided that each box on the physical sketch would represent 10 pixels in Processing. That makes my setup 200x200 pixels. With the Processing reference open in my browser, I set where the top left corner of my square (soap) would be which was the coordinates (60, 70). I then put in my dimensions (80x80). After that, I made the ellipse (plate). I assumed the first two numbers in the set represented the middle of the ellipse, so I got (100, 55). The width of the ellipse was 160 and the height was 50. I ran the script and realized my y-coordinate was wrong because I forgot where the origin was. I ran it again with the y-coordinate set to 145, and it was perfect. 

Now I needed to do the sparkles. For this, I needed to fill my soap with color in order to see the sparkles. For this, I used this [guide](https://processing.org/tutorials/color). I started with this:

    def draw():
        fill(255,200,200);
        square(60, 70, 80);
        fill(255,255,255);
        ellipse(100, 145, 160, 50);

The first fill was an example for pale red, and the second is white. I just wanted to try coloring my project before putting a lot of work into finding the right colors/progressing too far. I ran the program and found that I needed to move the ellipse before the square. I figured that was the case when I started making the sketch inside of Processing, but I wanted to focus on finding the right placements before worrying about the order of shapes. I flipped the square and the ellipse to solve the issue. I used the color selector in the "tools" tab to find the values for the color I wanted for the soap. This is what I ended up with:

    def draw():
        fill(255, 255, 255);
        ellipse(100, 145, 160, 50);
        fill(255, 213, 44);
        square(60, 70, 80);

To create the sparkles, I used quadrilaterals. I tackled the sparkle on the left first. I started by making sure the sparkles would fill with white in order for me to see them. Then, I found the coordinates of all the verticies in a clockwise order, and it came out looking great when I ran the program.

    def draw():
        fill(255, 255, 255);
        ellipse(100, 145, 160, 50);
        fill(255, 213, 44);
        square(60, 70, 80);
        fill(255, 255, 255);
        quad(70, 90, 75, 100, 70, 110, 65, 100);

I tackled the top right sparkle and then the bottom right sparkle and got this for my final sketch:

    def setup():
        size(200, 200)
        noStroke()
    
    def draw():
        fill(255, 255, 255);
        ellipse(100, 145, 160, 50);
        fill(255, 213, 44);
        square(60, 70, 80);
        fill(255, 255, 255);
        quad(70, 90, 75, 100, 70, 110, 65, 100);
        quad(130, 80, 135, 90, 130, 100, 125, 90);
        quad(110, 120, 115, 130, 110, 140, 105, 130);