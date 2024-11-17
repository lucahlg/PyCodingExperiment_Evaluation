import subprocess
import os
import shutil
import random

# Define the number of iterations
n = 5  # Change this to how many times you want to run it

# Store the argument in a separate variable
task_prompt = """
You are tasked to solve a programming related exercise. I provided you with the task in your directory. It consists of one ".md" file containing the task instruction and one ".json" file that has to be modified in the way it is described in the instruction.md file.
Complete the task.
"""

# Define the base command, excluding the task argument
base_command = ["poetry", "run", "python", "-m", "openhands.core.main", "-t"]

# Define directories
bench_items_dir = "./bench_items"
workspace_dir = "./workspace"
bench_results_dir = "./bench_results"

# Ensure the workspace and results directories exist
os.makedirs(workspace_dir, exist_ok=True)
os.makedirs(bench_results_dir, exist_ok=True)

# Loop to perform the operation n times
for i in range(n):
    print(f"Running iteration {i + 1}")
    
    # Clear the workspace directory before each iteration
    if os.listdir(workspace_dir):
        shutil.rmtree(workspace_dir)
        os.makedirs(workspace_dir)
    
    # Select a random folder from bench_items
    items = [item for item in os.listdir(bench_items_dir) if os.path.isdir(os.path.join(bench_items_dir, item))]
    if not items:
        raise FileNotFoundError("No folders found in './bench_items'. Make sure it contains folders.")
    
    random_folder = random.choice(items)
    random_folder_path = os.path.join(bench_items_dir, random_folder)
    
    # Copy the random folder content to the workspace directory
    shutil.copytree(random_folder_path, workspace_dir, dirs_exist_ok=True)
    
    # Combine the base command with the task argument
    command = base_command + [task_prompt]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Output the result if you want to see it
    print(result.stdout)  # To see the output of the command
    print(result.stderr)  # To see if there are any errors
    
    # Move the content of workspace to bench_results without creating new subdirectories
    for filename in os.listdir(workspace_dir):
        source_file = os.path.join(workspace_dir, filename)
        destination_file = os.path.join(bench_results_dir, filename)
        
        # Move files to the bench_results directory
        if os.path.exists(destination_file):
            # If the file already exists in the destination, rename it to avoid overwriting
            base, extension = os.path.splitext(destination_file)
            counter = 1
            while os.path.exists(destination_file):
                destination_file = f"{base}_{counter}{extension}"
                counter += 1
        
        shutil.move(source_file, destination_file)
    
    # Recreate workspace directory for the next iteration
    #os.makedirs(workspace_dir)

print("All iterations completed.")
