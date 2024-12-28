# Blockchain Logger

Blockchain Logger is a secure logging system that leverages blockchain technology to ensure the integrity, immutability, and verifiability of log entries. This Python-based implementation is suitable for applications requiring robust and tamper-proof logging mechanisms, such as ERP systems, eGov platforms, and other critical systems.

## Features
- **Immutable Logs:** Each log entry is cryptographically linked to the previous one, forming a tamper-proof chain.
- **Validation:** Verify the integrity of the blockchain to ensure logs have not been altered.
- **File Logging:** Optionally write logs to a file for external storage.
- **Easy Integration:** A modular design allows seamless integration into existing systems.

## Use Cases
The system has been validated in:
1. **ERP Systems:** Deployed in a real-world company, demonstrating enhanced auditability and trust in logging.
2. **eGov Platforms:** Utilized in a government project for secure logging (details are confidential).

## Getting Started

### Prerequisites
- Python 3.7+
- `hashlib` and `json` (included in Python's standard library)

### Installation
1. Clone the repository:
```bash
   git clone https://github.com/mehdiaitsaid/blockchain-logger.git
   cd blockchain-logger
```   


### Ensure Python is installed:
```bash
python --version
```
## Usage
### Initialize the Logger:
```python
from blockchain_logger import init, log, get_logs, validate_logs

init(log_file="logs/blockchain_logs.txt")
```


### Add Logs:
```python
log("User A logged in.")
log("Transaction: User A transferred $500 to User B.")

```

### Retrieve Logs:
```python
logs = get_logs()
print(logs)
```



### Validate Blockchain:
```python
is_valid = validate_logs()
print("Blockchain valid:", is_valid)
```


### Run Example: To see a working example, run the script directly:
```bash
python blockchain_logger.py
```


