# Sketchy Skies Application

Welcome aboard **Sketchy Skies**, where every journey is an adventure! We're thrilled you've chosen us—whether intentionally or accidentally—to take you to your next destination. Our enthusiastic crew is _probably_ trained, our planes have _mostly_ passed inspection, and we're confident that at least some of your luggage will arrive with you. Sit back, relax (if you can), and enjoy our in-flight entertainment, which occasionally works! We know you have plenty of choices when it comes to air travel, and we’re genuinely surprised—and slightly concerned—that you picked us. Here’s to hoping for smooth skies and functional landing gear—fingers crossed! 


# Setup

There is some setup to be done with this application with the database connection. You will need to add your own MongoDB connection string to the configure file. You will also need to update the **[db_name]** and **[db_collection]** variables in app.py to match your database name and preferred 

## configure.py

Create a configure.py file inside your directory.
Inside this file, add your MongoDB connection string to a variable called **MONGO_URI**.  It should look something like:

    MONGO_URI=mongodb+srv://<db_username>:<db_password>@cluster0.h38ne.mongodb.net/

## app.py
Inside app.py, find the MongoConnection section to modify the database name and cluster name.

    cluster = MongoClient(MONGO_URI)
    db = cluster["yourDataBaseNameHere"]
    collection = db["yourCollectionNameHere"]
Change "yourDataBaseName" to match the name of the database that you will be using, and "yourCollectionHere" to either the name of the collection you will be using if it exists. If the collection does not exist, a new collection will be created in the database with whatever you enter as a string.

## Running The Application
Assuming you have made the necessary changes, the application should start immediately. The data from the JSON file should be added to the collection and you should be able to use the GUI to interact with the data. 