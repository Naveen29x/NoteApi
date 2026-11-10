from fastapi import FastAPI,HTTPException
from pydantic import BaseModel



class Note(BaseModel):
    
    tittle:str
    content:str
    category:str
    is_complited:str

notes=[]

app=FastAPI()

@app.post("/Note")
def create_post(note:Note):
    new_note={
        "id":len(notes)+1,
        "tittle":note.tittle,
        "content":note.category,
        "is_complcated":note.is_complited
    }
    notes.append(new_note)
    return new_note
@app.get("/Note")
def view_post():
    return notes

@app.get("/Note/{user_id}")
def view_by_id(user_id:int):
    for single_note in notes:
        if single_note["id"]==user_id:
            return single_note
       
    return {
                "messgae":"error erorr"
            }
class Update_note(BaseModel):
        tittle:str
        content:str
        category:str
        is_complited:str
    
    
@app.put("/Note/{user_id}") 
def update_user(user_id:int,update_note:Update_note):
    for single_note in notes:
        if single_note["id"]==user_id:
            single_note["tittle"]=update_note.tittle
            single_note["content"]=update_note.content
            single_note["category"]=update_note.category
            single_note["is_complited"]=update_note.is_complited
            return single_note

    raise HTTPException(status_code=404)        
     
        
    





