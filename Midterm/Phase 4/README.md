# Phase 4

I had a conversation with my cs grad roommate Christina about this one. She told me that I needed to create a function that will decide how big each shape will be based on how many rows there are. She also told me that it would be easier if the shape itself started at 0,0 instead of in the middle of the canvas. I've also been looking at "The first loop goes through the x-axis of your canvas. The second loop goes through the y-axis of your canvas. You can multiply the cell width with the current x position in the nested for-loop to position your object in the x-axis. For the y-axis, this will be the cell height multiplied by the current y position" part of the instructions for a long time now and realize I need to take a break from this midterm.

A few days later, I see a vision. Using the pyramid homework as reference, I created
    
    def draw():
        for p in range(10):
            for k in range(10):
                drawObject(70*p,k*70,0.4);

to make a 10x10 grid of soaps/cheese slices/whatever people think my shape is. I also increased the canvas size to 710x710 because I didn't want to make the shape any smaller. "p" represents the rows, "k" represents the columns and each iterate 10 times. Because my drawing is centered horizontally on the original canvas, I didn't want the corners of my drawings to touch as the left side of the drawing wasn't flush against the left side of the canvas (it would look like I left random space on the left essentially). So I set my x and y coordinates to 70*row/column iteration so that each tile would be drawn each for each iteration and have enough space from the previous shape to create equal spacing horizontally. Because my sketch wasn't centered in the grid vertically, my tiles have long tops and short bottoms. I think of this draw() as my proof of concept.

I created a 10x10 grid, great. Now, I needed to figure out how to make it so that I could change all the tiles to scale based on how many rows/columns are given. 