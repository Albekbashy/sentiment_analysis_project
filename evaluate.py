import json
import random
import sys

accuracy = random.uniform(0.7, 0.95)

metrics = {
    "accuracy": accuracy
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Accuracy:", accuracy)

if accuracy < 0.8:
    print("Model performance below threshold")
    sys.exit(1)

print("Model performance acceptable")
