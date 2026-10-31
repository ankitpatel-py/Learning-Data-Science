from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentProfile(BaseModel):
    cgpa:float
    backlogs:int


@app.post('/check_eligibility')
def FiterAPI(data:StudentProfile):
    if data.backlogs >= 1:
            status = 'Not Eligible',
            advice = 'Clear your backlogs first'


    elif data.cgpa >= 8:
            status="Tier 1 Companies (Dream)"
            advice =" Start for DSA and System Design built Leetcode and Portfolio"

    elif data.cgpa >= 6:
        status = "Tier 2 Companies"
        advice = "Brush up the core and learn DSA"

    else:
        status="Mass Recruiter"
        advice="Make your skills stronger"

    return {
            "eligibility_status":status,
            "advice":advice
                }


