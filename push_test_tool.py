import json

# --- Core Functions ---

def greet(name):
    return f"Hello, {name}!"

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return f"Saved to {filename}"

def add_numbers(a, b):
    return a + b

# --- Action Router ---
def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("action")
    parser.add_argument("--params")
    args = parser.parse_args()
    params = json.loads(args.params) if args.params else {}
    if args.action == "greet":
        result = greet(**params)
    elif args.action == "save_json":
        result = save_json(**params)
    elif args.action == "add_numbers":
        result = add_numbers(**params)
    else:
        result = {"status": "error", "message": f"Unknown action {args.action}"}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()