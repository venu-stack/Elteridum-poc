async function createContract() {
    const contractJson = document.getElementById('contractJson').value;
    try {
        const response = await fetch('http://localhost:8000/create_contract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: contractJson
        });
        const result = await response.json();
        alert(`Contract created with ID: ${result.contract_id}`);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function updateCondition() {
    const contractId = document.getElementById('contractId').value;
    const conditionJson = document.getElementById('conditionJson').value;
    try {
        const response = await fetch(`http://localhost:8000/update_condition/${contractId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: conditionJson
        });
        const result = await response.json();
        alert(`Condition updated: ${JSON.stringify(result)}`);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function checkStatus() {
    const contractId = document.getElementById('statusContractId').value;
    try {
        const response = await fetch(`http://localhost:8000/check_status/${contractId}`);
        const result = await response.json();
        document.getElementById('statusResult').innerText = JSON.stringify(result, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}                   