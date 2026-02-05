from utils.audit_logger import log_action

log_action(
    action="CONTRACT_ANALYZED",
    metadata={
        "contract_type": "Employment Agreement",
        "overall_risk": "High"
    }
)

print("Audit log written.")
