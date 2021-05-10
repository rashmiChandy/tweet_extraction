Algorithm for Tweet Extraction process: 
1.	Authentication and establishing connection with Twitter API
a)	Invoke OAuth Authentication handler:
      i.	Pass consumer key and consumer secret to get Authorization token
      ii.	Set Access Token key to our access key and access secret present in Twitter developer account
b)	Establish connection with twitter API:
      i.	Through OAuth Authentication successful connection returns an API instance
   
   
2.	Establish connection with MongoDB:
a)	Create two databases in MongoDb Compass
      i.	RawDb
      ii.	ProcessedDb
b)	Establish connection with MongoClient through the connection URL with username and password
c)	Using dictionary style lookup fetch the database 
      i.	RawDb – To insert and fetch unprocessed data 
      ii.	ProcessedDb – To cleaned and store processed data
    
    
3.	Tweet extraction of Search API tweets:
a)	Initialize search keywords as a list
b)	Import tweepy library which is a Twitter API library to connect with Twitter API
c)	Fetch records from Twitter search API for each keyword:
      i.	Using Cursor fetch 300 records for each keyword
d)	Using CursorIterator, iterate through each tweet and store tweets in a list
      i.	Store tweet by fetching value from tweet._json property of result returned from Tweet API. 
      ii.	Tweet text and metadata such as created_at, id, user info, retweeted status etc. are stored in database for future processing 
e)	Insert list of unprocessed tweets into Search Collection of RawDb as key value pairs using insertMany operation


4.	Tweet extraction of Stream API tweets:
a)	Initialize search keywords as a list
b)	Initialize tweet count to fetch as 2000 tweets
c)	Create a Stream object which open the stream for live tweets. 
d)	Filter Stream using filter function to retrieve tweets of for the given keywords
e)	A Listener class is created which extends the StreamListener class and has the count of tweets fetched each time the method is invoked.
f)	Overridden on_data() method will append each tweet fetched into a list. 
g)	The stream is invoked multiple time until we get the required tweet count as 2000 records.
h)	Once the required count is fetched onData method returns false and the Stream is closed.
i)	Finally, the list of streamed tweets is inserted into the Stream Collection of RawDb as key value pairs using insertMany operation
************************************************************************************************************************************************************
Algorithm for Tweet Cleaning process: 
Before the data is inserted into ProcessedDb the data is cleaned to remove:
-	Special characters
- URLs
-	Emoticons
1.	Fetch Collections from RawDb
a.	 Using the list_collection_names operation provided by MongoDB, retrieve collections present in RawDB 

2.	For each collection (Search and Stream collection) fetch all the tweets 
a.	 Using the fetch operation provided by MongoDB, retrieve tweets from each collection 

3.	For each record (dictionary) fetched clean each key’s value present

4.	Cleaning Process using regex:
a.	Using find method in regex find the parts of the tweet text which has only alphabets, numbers and space.
b.	Join the list of matched words 
c.	Use substitute function to replace the newlines with empty string so that the entire sentence will be in a single line
d.	Remove the URLs by using sub functions to replace with empty string 
e.	If Space is more than 2 spaces between the words, then it is placed with a single space

5.	Once it is cleaned store the cleaned records in a list

6.	Insert the list of cleaned processed tweets into ProcessedDb so that every value in document stored as key value pair is free for any special characters, URLs and emoticons.

