# Elteridium Contract Platform PoC

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r backend/requirements.txt`
4. Run backend: `python backend/main.py`
5. Open frontend/index.html in a browser

## Usage Examples

### Create a Contract
```json
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

### Deployment Notes
- This is a PoC and requires additional security, error handling, and production configurations
- CORS and proper API authentication should be implemented
- Consider using environment variables for configuration

### Next Steps
1. Add authentication
2. Implement more robust condition checking
3. Create more complex action handlers
4. Add logging and monitoring

## Running the PoC
1. Start the backend: 
   ```bash
   cd backend
   uvicorn main:app --reload

Elteridium Contract Platform - Proof of Concept (PoC)
Table of Contents

Project Overview
System Architecture
Setup and Installation
Usage Guide
API Endpoints
Frontend Interactions
Backend Entry Management
Example Use Cases
Troubleshooting
Future Improvements

Project Overview
Purpose
The Elteridium Contract Platform is a lightweight, flexible system for creating and managing contracts with condition-based execution.
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

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Run the backend
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
Frontend JavaScript to List Contracts
Add to frontend/script.js:
javascriptCopyasync function listContracts() {
    try {
        const response = await fetch('http://localhost:8000/list_contracts');
        const contracts = await response.json();
        const contractList = document.getElementById('contractList');
        contractList.innerHTML = '<h3>Contracts:</h3>';
        
        contracts.forEach(contract => {
            const contractElement = document.createElement('div');
            contractElement.classList.add('contract-item');
            contractElement.innerHTML = `
                <strong>ID:</strong> ${contract.id}<br>
                <strong>Name:</strong> ${contract.name}<br>
                <strong>Status:</strong> ${contract.status}<br>
                <strong>Conditions:</strong> ${JSON.stringify(contract.conditions)}<br>
                <strong>Created At:</strong> ${contract.created_at}
            `;
            contractList.appendChild(contractElement);
        });
    } catch (error) {
        console.error('Error listing contracts:', error);
        alert('Failed to list contracts');
    }
}
Update HTML
Add to frontend/index.html:
htmlCopy<div class="section" id="listContracts">
    <h2>List Contracts</h2>
    <button onclick="listContracts()">Refresh Contract List</button>
    <div id="contractList"></div>
</div>
Add CSS to frontend/styles.css:
cssCopy.contract-item {
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
}
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


