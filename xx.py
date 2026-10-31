from fastapi import FastAPI
app = FastAPI()

# 1. Get request (client will ask for data, THIS IS SERVER , so it will send data)
@app.get('/users')
def get_users():
    return {"data": ["Rahul","Priya","Aman"]}

# 2. POST (client will send new data to create an account, THIS IS SERVER, it will send - Success,new account create)
@app.post("/users")
def update_user():
    # We should update the data accroding to client's instructions, but for now it's okay
    return ("message":"Your password updated successfully")

# 3. PUT (client will send data to update, THIS IS SERVER< it will send - Data Updates Successfully)
@app.put("/users")
def update_user():
    return {"message":"Your Password updated successfully"}

#4. DELETE (client will send request to delete, THIS IS SERVER, it will send - Deletion complete)
@app.delete("/users")
def delete_user():
    return {
        "message":"Deleting successfully"
    }
