from pymongo import MongoClient
import preprocessor, utilities

# get db client from mongodb using hostname, post, database name
def getDB(host, port, database):
    client = MongoClient(host, port)
    db = client[database]
    return client, db

# get documents for a specific query
def getDocuments(client, db, col, query = None):
    docs = db[col].find(query)
    return docs

# get only tweet text with or without truncated.
def getTweet(client, db, col, query = None):
    tweet = []
    with client.start_session() as session:
        for doc in db[col].find(query, no_cursor_timeout=True, session=session):
            tweet.append(doc['text'])
            client.admin.command('refreshSessions', [session.session_id], session=session)
    return tweet

# get full_text if truncated.
def getFullTweet(client, db, col, query = None, version = 1):
    tweet = []
    with client.start_session() as session:
        for doc in db[col].find(query, no_cursor_timeout=True, session=session):
            if version == 1:
                if doc["truncated"] is False:
                    tweet.append(doc['text'])
                else:
                    tweet.append(doc['extended_tweet']['full_text'])
            else:
                tweet.append(doc['text'])
            client.admin.command('refreshSessions', [session.session_id], session=session)
    return tweet

# get list of tweet id for a query
def getTweetID(client, db, col, query = None):
    tweetID = []
    with client.start_session() as session:
        for doc in db[col].find(query, no_cursor_timeout=True, session=session):
            has_id = utilities.existsKeys(doc, ["id_str"])
            if has_id:
                tweetID.append(doc['id_str'])
            else:
                tweetID.append(doc['id'])
            client.admin.command('refreshSessions', [session.session_id], session=session)
    return tweetID

# get tweet count for a query.
def getTweetCount(client, db, col, query = None):
    tweet_count = db[col].find(query).count()
    return tweet_count
