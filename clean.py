import os
import shutil

output_dir = "processed_results_paper2"

for folder_name in os.listdir(output_dir):
    folder_path = os.path.join(output_dir, folder_name)
    if os.path.isdir(folder_path):
        if "_c" in folder_name and "_nc" not in folder_name:
            corresponding_folder = folder_name[:-2] + "_nc"
            corresponding_folder_path = os.path.join(output_dir, corresponding_folder)
            if os.path.exists(corresponding_folder_path):
                files_in_folder = set(os.listdir(folder_path))
                files_in_corresponding = set(os.listdir(corresponding_folder_path))
                extra_files = files_in_folder - files_in_corresponding

                for extra_file in extra_files:
                    extra_file_path = os.path.join(folder_path, extra_file)
                    if os.path.isfile(extra_file_path):
                        os.remove(extra_file_path)
            else:
                print(corresponding_folder_path)
                print("does not exist")
                shutil.rmtree(folder_path)