import os
import json

results_dir = "experiments/main/results_paper"

for filename in os.listdir(results_dir):
    if "_nc" in filename:
        prefix = filename.split("_nc")[0]
        print(prefix)

        nc_file = filename
        nc_filepath = os.path.join(results_dir, nc_file)
        
        c_file = prefix + "_c.jsonl"
        c_filepath = os.path.join(results_dir, c_file)

        with open(nc_filepath, 'r') as f_nc, open(c_filepath, 'r') as f_c:
            nc_entries = [json.loads(line) for line in f_nc]
            c_entries = [json.loads(line) for line in f_c]
            
            total_count = len(nc_entries)
            nc_passed_count = sum(1 for entry in nc_entries if entry["tests_passed"])
            c_passed_count = sum(1 for entry in c_entries if entry["tests_passed"])

            print(nc_passed_count / len(nc_entries), c_passed_count / len(c_entries))

            # for nc_data in nc_entries:
            #     # if test not passed, check whether it passes in constrained setting
            #     if not nc_data["tests_passed"]:
            #         instance_id = nc_data["instance_id"]
            #         for c_data in c_entries:
            #             if c_data["instance_id"] == instance_id:
            #                 if c_data["tests_passed"]:
            #                     print(f"Instance {instance_id} passes in constrained setting but not in non-constrained setting.")
            #                 else:
            #                     print(f"Instance {instance_id} fails in both settings.")
            #                 break
            # break