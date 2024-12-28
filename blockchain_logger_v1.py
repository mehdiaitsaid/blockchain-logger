import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, message, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.message = message
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "message": self.message,
            "previous_hash": self.previous_hash
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class BlockchainLogger:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_log(self, message):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            message=message,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def export_chain(self):
        return [
            {
                "index": block.index,
                "timestamp": block.timestamp,
                "message": block.message,
                "hash": block.hash,
                "previous_hash": block.previous_hash
            }
            for block in self.chain
        ]

# Singleton logger instance
logger_instance = BlockchainLogger()

def log(message):
    logger_instance.add_log(message)

def validate_logs():
    return logger_instance.is_chain_valid()

def export_logs():
    return logger_instance.export_chain()

# Example usage
if __name__ == "__main__":
    log("User A deposited $100.")
    log("User B withdrew $50.")

    print("Is the blockchain valid?", validate_logs())

    logs = export_logs()
    for log_entry in logs:
        print(log_entry)
