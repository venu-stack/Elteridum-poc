# Elteridium Contract Platform PoC

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r backend/requirements.txt`
4. Run backend: `python backend/main.py`
5. Open frontend/index.html in a browser

## Usage Examples

### Create a Contract

json
------
{
    "name": "Sample Contract",
    "conditions": {
        "payment_received": false,
        "goods_delivered": false
    },
    "actions": [
        {
            "type": "api_call",
            "url": "https://example.com/webhook",
            "payload": {"status": "completed"}
        },
        {
            "type": "notification",
            "message": "Contract fulfilled"
        }
    ]
}

Deployment Notes
- This is a PoC and requires additional security, error handling, and production configurations
- CORS and proper API authentication should be implemented
- Consider using environment variables for configuration

 Next Steps
1. Add authentication
2. Implement more robust condition checking
3. Create more complex action handlers
4. Add logging and monitoring

Running the PoC
1. Start the backend: 
   bash
   -----
   cd backend
   uvicorn main:app --reload

Elteridium Contract Platform - Proof of Concept (PoC)
-----------------------------------------------------

Table of Contents
-----------------

1.Project Overview
2.System Architecture
3.Setup and Installation
4.Usage Guide
5.API Endpoints
6.Frontend Interactions
7.Backend Entry Management
8.Example Use Cases
9.Troubleshooting
10.Future Improvements

Project Overview
-----------------
Purpose : The Elteridium Contract Platform is a lightweight, flexible system for creating and managing contracts with condition-based execution.
Key Features

Dynamic contract creation
Condition-based contract progression
Action triggering
Status tracking
Simple web interface

System Architecture
Components

Frontend: HTML/JavaScript UI
Backend: FastAPI Python Application
Database: SQLite local database

Technology Stack
-----------------
Python 3.9+
FastAPI
SQLAlchemy
HTML/JavaScript
SQLite

Setup and Installation
Prerequisites

Python 3.9+
pip
virtualenv (recommended)

Installation Steps
bashCopy# Clone the repository
git clone <repository-url>
cd elteridium-poc

Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r backend/requirements.txt

Run the backend
uvicorn backend.main:app --reload
Usage Guide
Frontend Interaction
Open frontend/index.html in a web browser with the backend running.
Main Sections

1.Create Contract
2.Update Condition
3.Check Contract Status
4.List Contracts (New Feature)

API Endpoints
1. Create Contract

Endpoint: /create_contract
Method: POST
Payload:

jsonCopy{
    "name": "Contract Name",
    "conditions": {
        "condition1": false,
        "condition2": false
    },
    "actions": [
        {
            "type": "notification",
            "message": "Contract milestone achieved"
        }
    ]
}
2. Update Condition

Endpoint: /update_condition/{contract_id}
Method: POST
Payload:

jsonCopy{
    "conditions": {
        "condition1": true
    }
}
3. Check Status

Endpoint: /check_status/{contract_id}
Method: GET

Backend Entry Management
New Endpoint: List Contracts
I'll add a new endpoint to list all contracts in the backend.
Update backend/main.py:
pythonCopy@app.get("/list_contracts")
def list_contracts(db: Session = Depends(get_db)):
    contracts = db.query(Contract).all()
    return [
        {
            "id": contract.id,
            "name": contract.name,
            "status": contract.status,
            "conditions": contract.conditions,
            "created_at": contract.created_at.isoformat()
        } for contract in contracts
    ]
    

Example Use Cases
Freelance Contract
jsonCopy{
    "name": "Web Development Project",
    "conditions": {
        "design_approved": false,
        "backend_completed": false,
        "frontend_completed": false,
        "final_payment_received": false
    },
    "actions": [
        {
            "type": "notification",
            "message": "Project milestone achieved"
        }
    ]
}
Troubleshooting

Common Issues
-------------
CORS errors: Ensure backend is running
JSON formatting: Validate JSON structure
Database connection: Check SQLite file permissions

Debugging Tips

Use browser developer tools
Check backend console for error messages
Verify network requests in browser

Future Improvements

Add user authentication
Implement more complex condition logic
Create persistent storage solution
Add comprehensive logging
Develop more advanced action handlers 

Contribution
Feel free to fork and improve the project. Pull requests are welcome!


