import hashlib
import json
import os
from datetime import datetime
from typing import List, Optional

class LogBlock:
    """
    A class representing a single log block in the blockchain.
    """
    def __init__(self, index: int, timestamp: str, message: str, prev_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.message = message
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Compute the hash of the block using SHA-256.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class LogBlockchain:
    """
    A class representing the blockchain for secure logging.
    """
    def __init__(self):
        self.chain: List[LogBlock] = []
        self._initialize_chain()

    def _initialize_chain(self):
        """
        Initialize the blockchain with a genesis block.
        """
        genesis_block = LogBlock(0, str(datetime.utcnow()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_log(self, message: str):
        """
        Add a new log to the blockchain.
        """
        last_block = self.chain[-1]
        new_block = LogBlock(
            index=len(self.chain),
            timestamp=str(datetime.utcnow()),
            message=message,
            prev_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            # Validate hash
            if current_block.hash != current_block.compute_hash():
                return False

            # Validate chain linkage
            if current_block.prev_hash != prev_block.hash:
                return False

        return True

    def get_logs(self) -> List[dict]:
        """
        Retrieve the logs as a list of dictionaries.
        """
        return [block.__dict__ for block in self.chain]

class Logger:
    """
    A modular logging system built on blockchain technology.
    """
    def __init__(self, log_file: Optional[str] = None):
        self.blockchain = LogBlockchain()
        self.log_file = log_file

    def log(self, message: str):
        """
        Log a message to the blockchain and optionally to a file.
        """
        self.blockchain.add_log(message)
        if self.log_file:
            self._write_to_file(message)

    def _write_to_file(self, message: str):
        """
        Write the log to a file.
        """
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.utcnow()} - {message}\n")

    def get_logs(self) -> List[dict]:
        """
        Retrieve the logs from the blockchain.
        """
        return self.blockchain.get_logs()

    def validate_logs(self) -> bool:
        """
        Validate the blockchain logs for integrity.
        """
        return self.blockchain.is_chain_valid()

# API Interface
logger_instance = None

def init(log_file: Optional[str] = None):
    """
    Initialize the logger instance.
    """
    global logger_instance
    logger_instance = Logger(log_file=log_file)

def log(message: str):
    """
    Log a message using the logger instance.
    """
    if logger_instance is None:
        raise ValueError("Logger is not initialized. Call `init()` first.")
    logger_instance.log(message)

def get_logs() -> List[dict]:
    """
    Retrieve all logs using the logger instance.
    """
    if logger_instance is None:
        raise ValueError("Logger is not initialized. Call `init()` first.")
    return logger_instance.get_logs()

def validate_logs() -> bool:
    """
    Validate the blockchain logs using the logger instance.
    """
    if logger_instance is None:
        raise ValueError("Logger is not initialized. Call `init()` first.")
    return logger_instance.validate_logs()

# Example Usage
if __name__ == "__main__":
    init(log_file="logs/blockchain_logs.txt")
    log("User A logged in.")
    log("Transaction: User A transferred $500 to User B.")
    log("User B logged out.")

    logs = get_logs()
    print("Logs:", json.dumps(logs, indent=4))

    is_valid = validate_logs()
    print("Blockchain valid:", is_valid)
