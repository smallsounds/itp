I created a project where two dogs explore their hobbies. One likes eating and the other likes painting.

I put in the easel, two dogs, and fortune cookie sprites. Then, I added the background.

Tried to get the costumes to loop when the blue dog walks, but I was having trouble getting the costumes to switch. I originally had the loop to be "repeat 10 times, 2 steps, change to costume a, 2 steps, change to costume b." I then tried "repeat 10 times, 2 steps, next costume" and that worked. 

I lengthened the steps to get the blue dog to the easel and added "switch costume to a" before the loop so that he would always start with the same costume.

Because the orange dog is a space dog, it will glide to the fortune cookie. I accidentally clicked the green flag again and ran into some placement issues. I figured out that I needed to make sure that when the green flag was clicked, all the sprites would be in their positions. I used the "go to (coordinates)" when the green flag is clicked to solve the issue. I could have also used "set x"/"set y," but then I would've had to add two blocks.

I then created a broadcast message when the blue dog reaches the easel so that the easel can receive the message and change costumes. I set the easel to change costumes twice with a "chee chee chee" sound representing the joy of painting.

After the orange space dog moves, I have it broadcast a message. This message will go to both the fortune cookie and the orange dog. The fortune cookie "hides" when the messsage is recevied. The orange dog makes a bite sound and then glides towards the stereo and barks. 

The fortune cookie remains hidden when green flag is pressed, so I needed to add "show" to its code.

I created a list that I want the orange dog to cycle through. I wanted it to say some exclamations because it's so cute. I created variable "i" and then added "set i to 1" to the bark sound on the orange dog. I then added a loop that repeated for the length of the list in which the dog would say each item of the list for 2 seconds. This is possible because I add 1 to i after each "say" command.