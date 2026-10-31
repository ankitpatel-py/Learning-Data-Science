
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title= "The Placement Filter API")
cgpa=input("Enter CGPA")

class Data(BaseModel):
    cgpa:int
    

@app.post('/check_eligibility')
def FiterAPI(cgpa):
    if cgpa > 8.0:
        return {
            'status' : 'Tier 1 Companies (Dream)',
            'advice' : 'Start Grinding Leetcode'
        }
    elif cgpa >= 6.0:
        return {
            'status':'Tier 2 Companies  (Standard)',
            'advice':'learn skill'
        }
    else:
        return {
            'status':'Mass Recruiter',
            'advice':'start learning today'
        }
    
