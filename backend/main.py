from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
import requests

from database import SessionLocal, Contract

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ContractCreate(BaseModel):
    name: str
    conditions: Dict
    actions: List[Dict]

@app.post("/create_contract")
def create_contract(contract: ContractCreate, db: Session = Depends(get_db)):
    db_contract = Contract(
        name=contract.name, 
        conditions=contract.conditions, 
        actions=contract.actions
    )
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return {"contract_id": db_contract.id}

@app.post("/update_condition/{contract_id}")
def update_condition(contract_id: int, condition_status: Dict, db: Session = Depends(get_db)):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    
    # Check conditions and trigger actions
    if all(condition_status.values()):
        for action in contract.actions:
            if action['type'] == 'api_call':
                requests.post(action['url'], json=action.get('payload', {}))
            elif action['type'] == 'notification':
                print(f"Notification: {action['message']}")
        
        contract.status = 'completed'
        db.commit()
    
    return {"status": "updated"}

@app.get("/check_status/{contract_id}")
def check_status(contract_id: int, db: Session = Depends(get_db)):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    
    return {
        "id": contract.id,
        "name": contract.name,
        "status": contract.status,
        "conditions": contract.conditions
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)