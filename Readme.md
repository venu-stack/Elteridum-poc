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