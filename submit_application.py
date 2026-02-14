import hashlib
import hmac
import json
import os
import sys
from datetime import datetime, timezone

import requests


def create_signature(payload_string, secret):
    signature = hmac.new(
        secret.encode("utf-8"), payload_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    return f"sha256={signature}"


def submit_application():
    payload = {
        "action_run_link": os.environ.get("ACTION_RUN_LINK", ""),
        "email": os.environ.get("EMAIL", ""),
        "name": os.environ.get("NAME", ""),
        "repository_link": os.environ.get("REPOSITORY_LINK", ""),
        "resume_link": os.environ.get("RESUME_LINK", ""),
        "timestamp": datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z"),
    }

    payload_string = json.dumps(
        payload, separators=(",", ":"), sort_keys=True, ensure_ascii=False
    )

    secret = "hello-there-from-b12"
    signature = create_signature(payload_string, secret)

    print("Sending request to https://b12.io/apply/submission")
    print(f"Payload: {payload_string}")
    print(f"Signature: {signature}")

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-Signature-256": signature,
    }

    print("Sending request to https://b12.io/apply/submission")
    print(f"Payload: {payload_string}")
    print(f"Signature: {signature}")

    response = requests.post(
        "https://b12.io/apply/submission",
        data=payload_string.encode("utf-8"),
        headers=headers,
    )

    if response.status_code == 200:
        result = response.json()
        print(f"Success: {result.get('success')}")
        print(f"Receipt: {result.get('receipt')}")
        return result.get("receipt")
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        sys.exit(1)


if __name__ == "__main__":
    submit_application()
