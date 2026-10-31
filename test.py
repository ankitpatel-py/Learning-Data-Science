from fastapi import FastAPI, Depends

# Import FasrAPI to build the app, and depends to handle dependency injection
app = FastAPI()

# This is a fake database. It's jsut a python list containing 20 dictionaries
# Example 
fake_db = [{"id":i,"name":f"Item {i} for i in range(1,21)"}]
print(fake_db)
