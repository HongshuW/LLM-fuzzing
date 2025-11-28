import os

folder_path = "processed_results_paper2"

samples = {"repair": 0, "trans": 0, "synth": 0}

for subfolder in os.listdir(folder_path):
    file_path = os.path.join(folder_path, subfolder)
    if "_c" in subfolder and not "_nc" in subfolder:
        if "repair-all" in file_path:
            samples["repair"] += len(os.listdir(file_path))
        elif "translate" in file_path:
            samples["trans"] += len(os.listdir(file_path))
        elif "synth" in file_path:
            samples["synth"] += len(os.listdir(file_path))

print(samples)