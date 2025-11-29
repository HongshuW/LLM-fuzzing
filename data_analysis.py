import json

file_path = "experiments/main/results2/humaneval_google_gemma-2-9b-it_s=0_t=1_translate_c.jsonl"

def read_jsonl(file_path):
    """Read a JSONL file and return a list of dictionaries."""
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data

# Usage
if __name__ == "__main__":
    records = read_jsonl(file_path)
    initial_passes = 0
    fuzzing_found_bugs = 0
    for record in records:
        trials = record["trials"]
        if trials == 2:
            initial_passes += 1
            tests_passed = record["tests_passed"]
            if not tests_passed == True:
                fuzzing_found_bugs += 1
    print(f"Initial passes: {initial_passes}")
    print(f"Fuzzing found bugs: {fuzzing_found_bugs}")
    print(fuzzing_found_bugs / initial_passes)