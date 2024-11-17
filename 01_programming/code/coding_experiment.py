import subprocess
import os
import shutil
import random
import json
import datetime

# Define the model name
model_name = "GPT4o-mini"  # Replace with actual model name

# Define the selection mode: "random" or "sequential"
selection_mode = "random"  # Change to "sequential" / "random" 

# Define the number of iterations
n = 5  # Change this to how many times you want to run it

# Store the argument in a separate variable
task_prompt = """
You are tasked to solve a programming related exercise. I provided you with the task in your directory. It consists of one "instruction.md" file containing the task instruction and one ".py" file that has to be modified in the way it is described in the instruction.md file.
Don't change the file-name or function signature (name, arguments) in the template file as it will break the evaluation with automated tests.
Complete the task.
"""
# Max iterations for the agent per task
max_iterations = 15

# Define the base command, excluding the task argument
base_command = ["poetry", "run", "python", "-m", "openhands.core.main", "-t"]

# Define directories
task_items_dir = "./task_items"
workspace_dir = "./workspace"
exercise_dir = "./task_results/Exercise"  # New directory for storing task results

# Check if the "Exercise" directory already exists and is not empty
if os.path.exists(exercise_dir) and os.listdir(exercise_dir):
    print(f"The directory '{exercise_dir}' already exists and is not empty. Exiting the script.")
    exit(1)  # Exit with a non-zero status to indicate an abnormal exit

# Ensure the workspace and Exercise directories exist
os.makedirs(workspace_dir, exist_ok=True)
os.makedirs(exercise_dir, exist_ok=True)

# Initialize the generation log
generation_log = []
log_entry = {
    "unique_id": f"OpenHands Agent with {model_name}",
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "seed": "agent",
    "exercise_count": 0,
    "exercises": []
}
generation_log.append(log_entry)

# Get the list of task items
items = [item for item in os.listdir(task_items_dir) if os.path.isdir(os.path.join(task_items_dir, item))]
if not items:
    raise FileNotFoundError("No folders found in './task_items'. Make sure it contains folders.")

# Sort items if using sequential mode to ensure consistent order
if selection_mode == "sequential":
    items.sort()

# Function to handle file naming with both underscores and hyphens
def get_task_file(task_folder):
    task_name = os.path.basename(task_folder)
    task_name_with_underscores = task_name.replace('-', '_')
    
    # Check for the Python file with underscores (as that seems to be the common format)
    possible_files = [f"{task_name_with_underscores}.py", f"{task_name}.py"]
    
    # List all available files in the task folder for debugging
    available_files = os.listdir(task_folder)    
    for file in possible_files:
        file_path = os.path.join(task_folder, file)
        if os.path.exists(file_path):
            return file_path, os.path.basename(file)  # Return file path and the file name
    
    # If no file is found, raise an error and print available files for debugging
    raise FileNotFoundError(f"No valid Python file found for task '{task_name}'. "
                            f"Checked: {possible_files}. "
                            f"Available files: {available_files}")

# Loop to perform the operation n times
for i in range(n):
    print(f"Running iteration {i + 1}")
    
    # Clear the workspace directory before each iteration
    if os.listdir(workspace_dir):
        shutil.rmtree(workspace_dir)
        os.makedirs(workspace_dir)
    
    # Select a folder from task_items based on selection_mode
    if selection_mode == "random":
        selected_folder = random.choice(items)
    elif selection_mode == "sequential":
        selected_folder = items[i % len(items)]  # Wrap around if n > number of items
    else:
        raise ValueError("Invalid selection_mode. Choose 'random' or 'sequential'.")
    
    selected_folder_path = os.path.join(task_items_dir, selected_folder)
    
    # Copy the <task_name>.py file to the workspace directory
    try:
        task_file_path, task_file_name = get_task_file(selected_folder_path)
        shutil.copy(task_file_path, workspace_dir)
    except FileNotFoundError as e:
        print(e)  # Print the error for debugging
        continue  # Skip this iteration and move to the next if no valid file is found
    
    # Copy the instructions.md file from the .docs directory
    instructions_path = os.path.join(selected_folder_path, ".docs", "instructions.md")
    if not os.path.exists(instructions_path):
        raise FileNotFoundError(f"Instructions file not found for task '{selected_folder}'.")
    shutil.copy(instructions_path, workspace_dir)
    
    # Combine the base command with the task argument
    command = base_command + [task_prompt] + [f" --max_iterations {max_iterations}"]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Output the result if you want to see it
    print(result.stdout)  # To see the output of the command
    print(result.stderr)  # To see if there are any errors
    
    # Update the generation log
    log_entry["exercise_count"] += 1
    log_entry["exercises"].append(selected_folder)
    
    # Determine the next folder name based on the number of existing folders in "Exercise"
    existing_folders = [f for f in os.listdir(exercise_dir) if os.path.isdir(os.path.join(exercise_dir, f))]
    running_number = len(existing_folders) + 1
    selected_folder_sanitized = selected_folder.replace("-", "_")
    task_folder_name = f"Task_{running_number:02}_{selected_folder_sanitized}"
    task_folder_path = os.path.join(exercise_dir, task_folder_name)
    
    # Create the new folder for this task iteration
    os.makedirs(task_folder_path)
    
    # Move only the <task_name>.py file to the task-specific folder
    source_file = os.path.join(workspace_dir, task_file_name)
    destination_file = os.path.join(task_folder_path, task_file_name)
    
    shutil.move(source_file, destination_file)
    
    console_output_file = os.path.join(task_folder_path, "console_output.txt")
    with open(console_output_file, "w") as output_file:
        output_file.write("STDOUT:\n")
        output_file.write(result.stdout)
        output_file.write("\nSTDERR:\n")
        output_file.write(result.stderr)



    # Clear the workspace directory at the end of each iteration
    shutil.rmtree(workspace_dir)
    os.makedirs(workspace_dir)  # Recreate workspace directory for the next iteration

# Save the generation log to a JSON file
with open("./task_results/Exercise/generation_log.json", "w") as json_file:
    json.dump(generation_log, json_file, indent=4)

print("All iterations completed.")
