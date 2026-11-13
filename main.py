from fastapi import FastAPI,HTTPException
from pydantic import BaseModel



class Note(BaseModel):
    
    title:str
    content:str
    category:str
    is_completed:bool
class Noteresponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    is_completed: bool    

notes=[]

app=FastAPI()

@app.post("/Note")
def create_post(note:Note):
    new_note={
        "id":len(notes)+1,
        "title":note.title,
        "content":note.content,
        "category":note.category,
        "is_completed":note.is_completed
    }
    notes.append(new_note)
    return new_note
@app.get("/Note",response_model=list[Noteresponse])
def view_post():
    return notes

@app.get("/Note/{user_id}")
def view_by_id(note_id:int):
    for single_note in notes:
        if single_note["id"]==note_id:
            return single_note
       
    raise HTTPException(
        status_code=404,
       detail="Note not found" 
    )
class Update_note(BaseModel):
        title:str
        content:str
        category:str
        is_completed:bool
    
    
@app.put("/Note/{note_id}") 
def update_user(note_id:int,update_note:Update_note):
    for single_note in notes:
        if single_note["id"]==note_id:
            single_note["title"]=update_note.title
            single_note["content"]=update_note.content
            single_note["category"]=update_note.category
            single_note["is_complited"]=update_note.is_complited
            return single_note

    raise HTTPException(status_code=404,detail="Note not found") 

@app.delete("/Note/{Note_id}")
def delete_by_id(Note_id:int):
    for single_note in notes:
        if single_note["id"]==Note_id:
           notes.remove(single_note)
           return notes
    raise HTTPException(status_code=404,detail="Not found")
      





       
     
        
    





