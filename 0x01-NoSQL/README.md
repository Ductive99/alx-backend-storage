# NoSQL

### What is NoSQL?
NoSQL (not only SQL), is a database design that enables the storage and querying of data outside the traditional structures found in relational databases.
<br>

### Difference Between SQL and NoSQL
There are mainly four areas of differences between the two:
1. Structure.
2. Properties. (mainly ACID)
3. Language.
4. Scalability.

### Tasks
| File  | Task/script Description |
| ------------- | ------------- |
| 0-list_databases       | List all db's in MongoDB |
| 1-use_or_create_database  | Create or use the db _my_db_  |
| 2-insert               | Insert a document in the collection _school_ |
| 3-all                  | List all documents in the collection _school_ |
| 4-match                | List all documents with _name="Holberton school"_ in the collection _school_ |
| 5-count                | Display the number of documents in the collection _school_ |
| 6-update               | Add a new attribute to a document in the collection _school_<br>- Updaate only documents with _name="Holberton school"_<br>- Add the attribute _address_ with the value _972 Mission street_ |
| 7-delete               | Delete all documents with _name="Holberton school"_ in the collection _school_ |
| 8-all.py               | List all documents in a collection **in Python** |
| 9-insert_school.py     | Insert a new document in a collection based on _kwargs_<br>- Prototype: *def insert_school(mongo_collection, **kwargs):*<br>- *mongo_collection* will be the _pymongo_ collection object |
| 10-update_topics.py    | Change all topics of a school document based on the name<br>- Prototype: *def update_topics(mongo_collection, name, topics):* |
| 11-schools_by_topic.py | Return the list of school having a specific topic<br>- Prototype: *def schools_by_topic(mongo_collection, topic):* |
| 12-log_stats.py        | Provide some stats about Nginx logs stored in MongoDB |

