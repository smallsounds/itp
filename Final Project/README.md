# Sprint 1
### Day 1
I started my final project by watching a little under a half of [this video](https://youtu.be/GMHK-0TKRVk?si=kSbIBFjFNWH1sWbu). I followed along with the YouTuber. I learned how to open sqlite in the command prompt, create tables, insert data, and some shell commands (.tables, .save, .header). Here are some other notes I took:

    TIPS AND TROUBLESHOOTING
    Type SQL in ALL CAPS
    
    ...> means the command hasn't finished, so you should type ; to end
    
    Shell commands = all lowercase and don't need a semicolon at the end
    
    Up arrow retrieves the last line you typed. You can fix errors in single lines faster lol

### Day 2
I met with Gaby, the school nutritionist. I gave her a spreadsheet that had the majority of my safe foods (thirteen food items) and some categories I use to determine what makes them safe (texture, taste, when I eat them, etc...). We brainstormed foods that were similar and could substitute these foods as well as foods that are completely new but have similar texture to safe foods. Using this data, I created two new tables in the spreadsheet; one for similar foods and one for new foods. There were seven similar foods added and fourteen new foods added. To end off, we set up another appointment two weeks from this one. 

# Sprint 2
### Day 3
I started creating the two databases. I created new database called "fooddatabase.db" and then created a table called "SAFE" which had the follow categories: FOODID INT, FOODNAME TEXT, FOODTEXTURE TEXT, FOODTASTE TEXT, FOODFUNCTION TEXT

I then created my first safe food by typing:

    INSERT INTO SAFE(FOODID, FOODNAME, FOODTEXTURE, FOODTASTE, FOODFUNCTION) VALUES (1,'CHIPS','CRUNCHY','SALTY','SNACK');

I checked my work using SELECT * FROM and then made a new database called "NEW" with the same categories. For this one, I made an entry for salted almonds. All categories but "FOODNAME" are the same as the chips entry.

I then began to work on the Python part of the project because I knew it would be the most difficult part. I want to query a safe food and have new foods with similar textures and functions pop up. I chose these two categories because they weigh the heaviest in my food decision making. The taste category is to give more information about a new food that I might be unsure of (it helps me make an informed decision). 

First I opened [the Python/SQLite documentation](https://docs.python.org/3/library/sqlite3.html#), filled out lines 1,3, and 4 of the example below and downloaded the Python interpreter. I don't know why Windows machines have so much bloatware pre-installed rather than common third party drivers and interpreters like Apple... (rare Apple win). After that, I created a definition that controls the safe food query. 

    import sqlite3
    def query_new_foods_for_safe_food(safe_food_name):
    conn = sqlite3.connect('fooddatabase.db')
    cursor = conn.cursor()

I figured out that cursor.execute(''' ''') is a string that queries a database, so I used that as the basis for the next statement. However, I didn't know how to get one table to reference another. I contacted my friend Willow who is a part of the EAE program at the University of Utah (and coincidentally also has ARFID) for help. 

    cursor.execute('''
        SELECT n.FOODNAME, n.FOODTEXTURE, n.FOODTASTE, n.FOODFUNCTION
        FROM SAFE s
        JOIN NEW n ON s.FOODTEXTURE = n.FOODTEXTURE AND s.FOODFUNCTION = n.FOODFUNCTION
        WHERE s.FOODNAME = ?
    ''', (safe_food_name,))
    
    results = cursor.fetchall()

    conn.close()

    return results

We went over each line together for me to understand what was going on. The "SELECT" is referencing the NEW (n) table based on FROM. The FROM is a claue that tells the computer where to retrieve data which is the SAFE (s) table. The JOIN condition is telling the program to only match the SAFE and NEW table results based on FOODTEXTURE and FOODFUNCTION. The WHERE clause has a ? which is where the user input  will go. Because we ended the execute with (safe_food_name,), it will only accept the SAFE table's names as inputs. Willow told me this was a safeguard just to make sure inputs are formatted right and vaguely mentioned something about cybersecurity. Fetchall will retieve all the rows matching the query as tuples (ordered sequence of values aka rows). The "close" is to close the connection to SQLite. The "return results" is storing the rows quered for later use.  

From here, I took the reins. I wanted the user (me lol) to be able to type the safe food into the terminal as an input sooooo:

    safe_food_name = input("Enter the safe food name: ")
    new_foods = query_new_foods_for_safe_food(safe_food_name)

The other line is referring to this next part:

    if new_foods:
        print("New foods with similar characteristics:")
        for food in new_foods:
            print(food)
    else:
        print("No new foods found with similar characteristics to", safe_food_name)

This prints the result of the query.

I ran the program, and it didn't work. An error message popped up: "sqlite3.OperationalError: no such table: SAFE". In the terminal, I opened the folder which held both the database and Python files. I ran the program again, and it worked. I figured I had to have the program open the location of both files in order for it to find the database. For this, I looked up "os path" in the [Python/SQLite documentation](https://docs.python.org/3/library/os.path.html#module-os.path). I found "os.path.dirname(path)" which was what I needed, but I didn't know how to format the path. I asked Willow who created:

    current_directory = os.path.dirname(os.path.abspath(__file__))

abspath formats the path or something like that. \_\_file__ is a way for Python to reference its own Python file. Willow also helped me make this:

    database_path = os.path.join(current_directory, 'fooddatabase.db')

This just says "Hey, the current_directory path is what you should follow. Now, you just need to find this file called 'fooddatabase.db'"

I had to use this new information in these lines:

    def query_new_foods_for_safe_food(safe_food_name, database_path):
        conn = sqlite3.connect(database_path)
and 

    new_foods = query_new_foods_for_safe_food(safe_food_name, database_path)

Everything worked correctly when I queried "CHIPS"!

# Sprint 3
### Day 4
I met with Professor Rome for a check-in. Everything was good! I just need to put in some more entries, and the project will be done. I took some time after our check-in to insert one new food (whole grain bread) and two safe foods (mac and cheese, bread--referring to sourdough bc that's the only bread that's cheap and yummy right now). I also created INSERT text to copy and paste so that I didn't have to type everything out and to avoid syntax errors.

### Day 5
I added some more safe and new foods into the database during my shift at Guitar Center. I added seven more safe foods and twelve more new foods. This brings my safe food table to ten items, and my new food table to thirteen items.

    4|CHEESE|SOFT|SAVORY|INGREDIENT
    5|PIZZA|CRUNCHY|SAVORY|MAIN DISH
    6|BAGEL|CHEWY|BLAND|MAIN DISH
    7|PUDDING|CREAMY|SWEET|SNACK
    8|ICE CREAM|CREAMY|SWEET|SNACK
    9|CHICKEN|FIRM|SAVORY|MAIN DISH
    10|NUTELLA|THICK|SWEET|SNACK

    
    2|WHOLE GRAIN BREAD|CHEWY|BLAND|INGREDIENT
    3|BAGEL PIZZA|CHEWY|SAVORY|MAIN DISH
    4|PITA POCKET PIZZA|CHEWY|SAVORY|MAIN DISH
    5|PITA CHIPS|CRUNCHY|SALTY|SNACK
    6|TORTILLA CHIPS|CRUNCHY|SALTY|SNACK
    7|SWEET POTATO CHIPS|CRUNCHY|SALTY|SNACK
    8|GREEK YOGURT|CREAMY|TANGY|SNACK
    8|CANNED TUNA|FIRM|MILD FISH|MAIN DISH
    9|BABY CARROTS|CRUNCHY|BLAND|SNACK
    10|NUTELLA WITH NUTS|THICK|SWEET|SNACK
    11|MASHED POTATO|MUSHY|BLAND|MAIN DISH
    12|WATERMELON|MUSHY|SWEET|MAIN DISH
    13|DRIED FRUIT|CHEWY|SWEET|SNACK

# Sprint 4 (Final Sprint)

### Day 6
My goal was to enter all of the new and safe foods and then finish the presentation in one session. In my proposal, I mentioned having 20+ safe food rows. I realized that I don't have that many safe foods that could be query-able. I have fourteen though! I also ended with twenty two new food items with some texture variations as some items have more than one texture. The health providers I'm working with wanted me to log all of my meals along with my thoughts, feelings, and physical sensations through a form that wouldn't have been easily integrated into my program, so I will not be pursuing my stretch goal. While some new foods may not be able to be queried based on their texture/function, I hope that as I expand my safe foods with my health provider's help, I will be able to in the future. 