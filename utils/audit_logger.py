import json
import os
from datetime import datetime

LOG_DIR = "data/logs"
LOG_FILE = os.path.join(LOG_DIR, "audit_log.json")

def log_action(action: str, metadata: dict = None):
    """
    Logs user actions for audit purposes without storing sensitive data.
    """

    if metadata is None:
        metadata = {}

    os.makedirs(LOG_DIR, exist_ok=True)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "metadata": metadata
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)
