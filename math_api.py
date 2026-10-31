def get_math_inputs(a:int=0,b:int=0):
    return {"a":a,"b":b}

@app.get("api/add")
def sum(inputs:dict= Depends(get_math_input)):
    return {"sum" : input['a'] + input['b']}
