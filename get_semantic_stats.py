import os
import json

results_dir = "experiments/main/results_paper"

stats = dict()

for filename in os.listdir(results_dir):
    if "_nc" in filename:
        prefix = filename.split("_nc")[0]
        parts = prefix.split("_")
        dataset = parts[0]
        model = parts[2]
        task = parts[-1]
        if dataset not in stats:
            stats[dataset] = dict()
        if model not in stats[dataset]:
            stats[dataset][model] = dict()
        if task not in stats[dataset][model]:
            c_dictionary = {"total": 0, "tests_passed": 0}
            nc_dictionary = {"total": 0, "tests_passed": 0}
            stats[dataset][model][task] = dict()
            stats[dataset][model][task]["c"] = c_dictionary
            stats[dataset][model][task]["nc"] = nc_dictionary

        nc_file = filename
        nc_filepath = os.path.join(results_dir, nc_file)
        
        c_file = prefix + "_c.jsonl"
        c_filepath = os.path.join(results_dir, c_file)

        with open(nc_filepath, 'r') as f_nc, open(c_filepath, 'r') as f_c:
            nc_entries = [json.loads(line) for line in f_nc]
            c_entries = [json.loads(line) for line in f_c]
            
            nc_passed_count = sum(1 for entry in nc_entries if entry["tests_passed"])
            c_passed_count = sum(1 for entry in c_entries if entry["tests_passed"])

            stats[dataset][model][task]["c"]["total"] += len(c_entries)
            stats[dataset][model][task]["c"]["tests_passed"] += c_passed_count
            stats[dataset][model][task]["nc"]["total"] += len(nc_entries)
            stats[dataset][model][task]["nc"]["tests_passed"] += nc_passed_count

            # print(nc_passed_count / len(nc_entries), c_passed_count / len(c_entries))

for dataset in stats:
    for model in stats[dataset]:
        for task in stats[dataset][model]:
            print(dataset, model, task)
            c_total = stats[dataset][model][task]["c"]["total"]
            nc_total = stats[dataset][model][task]["nc"]["total"]
            if not c_total == nc_total:
                print("total mismatch:", dataset, model, task, c_total, nc_total)
            else:
                c_passed = stats[dataset][model][task]["c"]["tests_passed"]
                nc_passed = stats[dataset][model][task]["nc"]["tests_passed"]
                if c_total > 0:
                    print("constrained:", c_passed / c_total)
                    print("not constrained:", nc_passed / nc_total)
