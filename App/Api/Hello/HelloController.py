from fastapi import HTTPException

from app import app

@app.get('/')
def hello_get():

    try:
    
        response = {
            'response' : 'Hello World'
        }

        return response

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))