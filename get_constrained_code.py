import os
import json

results_dir = "experiments/main/results"
output_dir = "processed_results"

# List all files in the results directory
for filename in os.listdir(results_dir):
    file_path = os.path.join(results_dir, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            if "_c" in filename and "_nc" not in filename:
                content = f.read()
                print(f"--- {filename} ---")
                for line in content.strip().splitlines():
                    data = json.loads(line)
                    if data["compiler_output"] == "" and not data["tests_passed"]:
                        compiled_output = data["compiled"]

                        new_file_name = data["instance_id"]
                        if "/" in new_file_name:
                            new_file_name = new_file_name.split("/", 1)[0]
                        print(new_file_name)

                        # Write file_content to a file named after instance_id
                        if data["test_output"] == "Timeout":
                            file_content = compiled_output + "\n// Timeout"
                        else:
                            stderr_with_comment = data["test_output"]["stderr"].replace("\n", "\n// ")
                            file_content = compiled_output + "\n// " + stderr_with_comment
                        
                        # Create the output subfolder if it doesn't exist
                        subfolder = os.path.join(output_dir, os.path.splitext(filename)[0])
                        os.makedirs(subfolder, exist_ok=True)
                        
                        output_file = os.path.join(subfolder, new_file_name + ".ts")
                        with open(output_file, 'w', encoding='utf-8') as out_f:
                            out_f.write(file_content)
