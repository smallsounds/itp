# Phase 4

I had a conversation with my cs grad roommate Christina about this one. She told me that I needed to create a function that will decide how big each shape will be based on how many rows there are. She also told me that it would be easier if the shape itself started at 0,0 instead of in the middle of the canvas. I've also been looking at "The first loop goes through the x-axis of your canvas. The second loop goes through the y-axis of your canvas. You can multiply the cell width with the current x position in the nested for-loop to position your object in the x-axis. For the y-axis, this will be the cell height multiplied by the current y position" part of the instructions for a long time now and realize I need to take a break from this midterm.

A few days later, I see a vision. Using the pyramid homework as reference, I created
    
    def draw():
        for p in range(10):
            for k in range(10):
                drawObject(70*p,k*70,0.4);

to make a 10x10 grid of soaps/cheese slices/whatever people think my shape is. I also increased the canvas size to 710x710 because I didn't want to make the shape any smaller. "p" represents the rows, "k" represents the columns and each iterate 10 times. Because my drawing is centered horizontally on the original canvas, I didn't want the corners of my drawings to touch as the left side of the drawing wasn't flush against the left side of the canvas (it would look like I left random space on the left essentially). So I set my x and y coordinates to 70*row/column iteration so that each tile would be drawn each for each iteration and have enough space from the previous shape to create equal spacing horizontally. Because my sketch wasn't centered in the grid vertically, my tiles have long tops and short bottoms. I think of this draw() as my proof of concept.

I created a 10x10 grid, great. Now, I needed to figure out how to make it so that I could change all the tiles to scale based on how many rows/columns are given. I first changed "10" in the range to "i" and added "i=5" in the line after draw(). I then took into account the height and the width of the canvas. I resized the canvas to 400x400, which is double the original canvas' size. It's a square, so I only needed to create one equation to make sure everything is equally spaced out. I used h=height/i to represent the horizontal and vertical spacing, getting rid of the 70 in the proof of concept. The last thing I needed was the equation for the scale represented by "s" in this:


    def draw():
        i=5
        h=height / i
        s=?????
        for p in range(i):
            for k in range(i):
                drawObject(h*p,h*k,s);

To find the scale, Christina and I worked out some math.
![Picture of Neil and Christina's math work](Math.png)
I started by creating an input output table (left) in which i=input and s=output. I knew there was a relationship there, but I needed another set of eyes on it because I was burnt out. Christina drew the 4x4 output (top left of right paper) because we knew the scale for that one. I told her the coordinates at which a tile will be drawn as well as the coordinates in the drawObject order. This ended up being increments of 100. Then, she wrote out that the original image's scale is doubled (2) in the new scale as as a refresher. To further understand what I had written prior, Christina wrote out the values of i, p, k, and h. After that, we worked together and realized that h was the value I should've been paying attention to. The height divided by i was the cell size which would need to be divided by 200 in order to get the correct scale.

    def draw():
        i=5
        h=height / i
        s=h / 200
        for p in range(i):
            for k in range(i):
                drawObject(h*p,h*k,s);

This is what I wrote down in Processing. However, nothing printed. I looked up "fractions in Processing" on Google to find no helpful information. I then realized that it's probably something about ints vs floats. I added a decimal after 200 (s=h/200.0), and everything worked! I tested with i=5, i=10, and i=20!