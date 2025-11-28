import os
import json

results_dir = "experiments/main/results_paper"
output_dir = "processed_results_paper2"
new_output_dir = "processed_results_paper2"

for filename in os.listdir(results_dir):
    file_path = os.path.join(results_dir, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            if "_nc" in filename:
                content = f.read()
                print(f"--- {filename} ---")
                prefix = filename.rsplit("_nc", 1)[0]

                for out_folder in os.listdir(output_dir):
                    if prefix in out_folder:
                        out_folder_path = os.path.join(output_dir, out_folder)
                        if os.path.isdir(out_folder_path):
                            out_files = os.listdir(out_folder_path)
                            out_files = [f[:-3] if f.endswith(".ts") else f for f in out_files]
                            
                            for line in content.strip().split('\n'):
                                data = json.loads(line)
                                new_file_name = data["instance_id"]
                                if "/" in new_file_name:
                                    new_file_name = new_file_name.split("/", 1)[0]
                                if new_file_name in out_files and data["compiler_output"] == "" \
                                    and not data["test_output"] == "Timeout" and not data["test_output"] == None \
                                        and data["tests_passed"] and not "TypeError" in data["test_output"]["stderr"]:
                                    error_with_comment = data["compiler_output"].replace("\n", "\n// ")
                                    if data["test_output"] == "Timeout":
                                        stderr_with_comment = "\n// Timeout"
                                        stdout_with_comment = "\n// Timeout"
                                    elif data["test_output"] == None:
                                        stderr_with_comment = "\n// None"
                                        stdout_with_comment = "\n// None"
                                    else:
                                        stderr_with_comment = data["test_output"]["stderr"].replace("\n", "\n// ")
                                        stdout_with_comment = data["test_output"]["stdout"].replace("\n", "\n// ")
                                    
                                    if data["compiled"] == None or data["compiled"] == "":
                                        continue
                                    
                                    file_content = data["compilable"] + "\n\n// Compilation Error\n// " + error_with_comment + "\n\n"
                                    file_content += data["compiled"] + "\n\n// stdout" + stdout_with_comment + "\n\n// stderr" + stderr_with_comment
                                    
                                    # Create the output subfolder if it doesn't exist
                                    subfolder = os.path.join(new_output_dir, os.path.splitext(filename)[0])
                                    os.makedirs(subfolder, exist_ok=True)
                                    print(subfolder)

                                    output_file = os.path.join(subfolder, new_file_name + ".ts")
                                    with open(output_file, 'w', encoding='utf-8') as out_f:
                                        out_f.write(file_content)
