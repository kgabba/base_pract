from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn

api = FastAPI()

bd = {
    1:{'name':'kam', "prof":'ds', 'grade':'middle'},
    2:{'name':'art', "prof":'backend', 'grade':'junior'},
}

@api.get('/list', summary='get bd list', tags=['bd'])
def funcc():
    return FileResponse('front.html')

# Endpoint для данных в JSON
@api.get('/api/employees', summary='вспомогательная для html', tags=['Helper'])
def get_employees():
    return bd

@api.get('/list/{id}', summary='get employer photo', tags=['bd'])
def get_photo(id: int):
    if id not in bd:
        raise HTTPException(status_code=404, detail="User not found")

    path = f'./photos/{bd[id]["name"]}.avif'
    return FileResponse(path)

if __name__=='__main__':
    uvicorn.run('main:api', host='localhost', port=8000, reload=True)