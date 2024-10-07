import os
import json
import csv
import glob
import tempfile
import shutil
import subprocess
import re

def main():
    submissions_dir = 'submissions'
    data_dir = 'data'
    output_csv = 'test_results.csv'

    # Open CSV file for writing
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'student_submission',
            'task_number',
            'task_name',
            'unique_id',
            'timestamp',
            'seed',
            'exercise_count',
            'test_passed',
            'tests_passed_percent',  # Added new field
            'pylint_score',
            'cyclomatic_complexity'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over submissions
        submission_paths = glob.glob(os.path.join(submissions_dir, 'submission_*'))
        print(f"Found submissions: {submission_paths}")
        for submission_path in submission_paths:
            print(f"Processing submission: {submission_path}")
            process_submission(submission_path, data_dir, writer)
        print(f"Results written to {output_csv}")

def process_submission(submission_path, data_dir, writer):
    # Paths and metadata
    exercise_dir = os.path.join(submission_path, 'Exercise')
    generation_log_path = os.path.join(exercise_dir, 'generation_log.json')

    # Read generation_log.json
    if not os.path.exists(generation_log_path):
        print(f'No generation_log.json found in {submission_path}')
        return

    with open(generation_log_path, 'r', encoding='utf-8') as f:
        generation_log = json.load(f)[0]
    print(f"Read generation_log.json from {generation_log_path}")

    unique_id = generation_log.get('unique_id', '')
    timestamp = generation_log.get('timestamp', '')
    seed = generation_log.get('seed', '')
    exercise_count = generation_log.get('exercise_count', '')
    exercises = generation_log.get('exercises', [])

    print(f"Submission metadata: unique_id={unique_id}, timestamp={timestamp}, seed={seed}, exercise_count={exercise_count}, exercises={exercises}")

    # Iterate over tasks in the Exercise directory
    task_dirs = glob.glob(os.path.join(exercise_dir, 'Task_*'))
    print(f"Found task directories: {task_dirs}")
    for task_dir in task_dirs:
        print(f"Processing task directory: {task_dir}")
        process_task(
            task_dir,
            data_dir,
            writer,
            os.path.basename(submission_path),
            unique_id,
            timestamp,
            seed,
            exercise_count
        )

def process_task(task_dir, data_dir, writer, submission_name, unique_id, timestamp, seed, exercise_count):
    # Extract task number and task name
    task_folder_name = os.path.basename(task_dir)
    print(f"Processing task folder: {task_folder_name}")

    if not task_folder_name.startswith('Task_'):
        print(f'Unexpected task folder name format: {task_folder_name}')
        return

    task_info = task_folder_name[5:]
    underscore_index = task_info.find('_')
    if underscore_index == -1:
        print(f'Unexpected task folder name format: {task_folder_name}')
        return

    task_number = task_info[:underscore_index]
    task_name = task_info[underscore_index+1:]
    print(f"Extracted task number: {task_number}, task name: {task_name}")

    # Adjust task name for data folder (replace underscores with hyphens)
    data_task_name_folder = task_name.replace('_', '-')
    data_task_name = task_name
    print(f"Adjusted task name for data folder: {data_task_name_folder}")

    # Paths to student's implementation and test script
    student_code_path = os.path.join(task_dir, f'{task_name}.py')
    print(f"Looking for student code at: {student_code_path}")
    if not os.path.exists(student_code_path):
        print(f'Student code not found: {student_code_path}')
        return

    test_script_path = os.path.join(data_dir, data_task_name_folder, f'{data_task_name}_test.py')
    print(f"Looking for test script at: {test_script_path}")
    if not os.path.exists(test_script_path):
        print(f'Test script not found: {test_script_path}')
        return

    # Create temporary directory and run the test
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Created temporary directory: {temp_dir}")
        shutil.copy(student_code_path, temp_dir)
        shutil.copy(test_script_path, temp_dir)
        print(f"Copied student code and test script to temporary directory")

        result = run_test(temp_dir, f'{data_task_name}_test.py', task_name)

        # Paths to the student's code in the temp directory
        student_code_filename = f'{task_name}.py'
        student_code_path_in_temp = os.path.join(temp_dir, student_code_filename)

        # Run code analysis
        pylint_result = run_pylint(student_code_path_in_temp)
        radon_result = run_radon(student_code_path_in_temp)

        # Log the results
        print(f"Test result for {task_name}: Passed={result['test_passed']}")
        print(f"Tests passed percent for {task_name}: {result['tests_passed_percent']}")
        print(f"Pylint score for {task_name}: {pylint_result['pylint_score']}")
        print(f"Cyclomatic complexity for {task_name}: {radon_result['cyclomatic_complexity']}")
        writer.writerow({
            'student_submission': submission_name,
            'task_number': task_number,
            'task_name': task_name,
            'unique_id': unique_id,
            'timestamp': timestamp,
            'seed': seed,
            'exercise_count': exercise_count,
            'test_passed': result['test_passed'],
            'tests_passed_percent': result['tests_passed_percent'],  # Added this line
            'pylint_score': pylint_result['pylint_score'],
            'cyclomatic_complexity': radon_result['cyclomatic_complexity']
        })
        print(f"Wrote results to CSV for task {task_name}")

def run_test(temp_dir, test_script_name, task_name):
    # Remove '.py' to get module name
    test_module_name = os.path.splitext(test_script_name)[0]
    # Command to run the test script as a unittest module
    cmd = ['python', '-m', 'unittest', test_module_name]
    print(f"Running test command: {cmd}")

    # Environment variables
    env = os.environ.copy()
    env['PYTHONPATH'] = temp_dir + os.pathsep + env.get('PYTHONPATH', '')
    print(f"Set PYTHONPATH to: {env['PYTHONPATH']}")

    try:
        result = subprocess.run(
            cmd,
            cwd=temp_dir,
            capture_output=True,
            text=True,
            timeout=30,
            env=env
        )
        test_passed = result.returncode == 0
        test_output = result.stdout + result.stderr
        #print(f"Test output:\n{test_output}")

        # Initialize counts
        total_tests = None
        failures = 0
        errors = 0

        # Extract total tests
        match_total = re.search(r'^Ran (\d+) tests? in', test_output, re.MULTILINE)
        if match_total:
            total_tests = int(match_total.group(1))
        else:
            print("Could not determine total number of tests run.")
            total_tests = 0

        # Extract failures and errors
        match_failed = re.search(r'^FAILED \((.+)\)', test_output, re.MULTILINE)
        if match_failed:
            failed_info = match_failed.group(1)
            # Parse failed_info, e.g., 'failures=1, errors=2'
            failure_matches = re.findall(r'(failures|errors)=(\d+)', failed_info)
            for key, value in failure_matches:
                if key == 'failures':
                    failures = int(value)
                elif key == 'errors':
                    errors = int(value)
        else:
            # No 'FAILED' line, assume failures=0, errors=0
            failures = 0
            errors = 0

        # Calculate passed tests percentage
        if total_tests > 0:
            passed_tests = total_tests - failures - errors
            tests_passed_percent = (passed_tests / total_tests) * 100
        else:
            tests_passed_percent = None

    except subprocess.TimeoutExpired:
        test_passed = False
        tests_passed_percent = None
        test_output = 'Test timed out.'
        print("Test timed out.")
    except Exception as e:
        test_passed = False
        tests_passed_percent = None
        test_output = f'Error running test: {e}'
        print(f"Error running test: {e}")

    return {
        'test_passed': test_passed,
        'test_output': test_output,
        'tests_passed_percent': tests_passed_percent  # Added this line
    }

def run_pylint(file_path):
    cmd = ['python', '-m', 'pylint', file_path, '--score', 'y', '--output-format', 'text']
    print(f"Running pylint command: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        # Capture both stdout and stderr
        output = result.stdout + result.stderr
        # Extract the score from the output
        score_line = [line for line in output.split('\n') if 'Your code has been rated at' in line]
        if score_line:
            score_str = score_line[0]
            match = re.search(r'Your code has been rated at (-?[\d\.]+)/10', score_str)
            if match:
                score = float(match.group(1))
            else:
                score = None
        else:
            score = None
        print(f"Pylint output:\n{output}")
    except subprocess.TimeoutExpired:
        score = None
        output = 'Pylint timed out.'
        print("Pylint timed out.")
    except Exception as e:
        score = None
        output = f'Error running pylint: {e}'
        print(f"Error running pylint: {e}")
    return {
        'pylint_score': score,
        'pylint_output': output
    }

def run_radon(file_path):
    cmd = ['python', '-m', 'radon', 'cc', file_path, '--total-average', '--json']
    print(f"Running radon command: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        # Capture both stdout and stderr
        output = result.stdout + result.stderr
        # The output is in JSON format
        data = json.loads(output)
        # Extract complexities
        complexities = []
        for filepath, functions in data.items():
            for func in functions:
                complexities.append(func.get('complexity', 0))
        # Compute average complexity
        if complexities:
            avg_complexity = sum(complexities) / len(complexities)
        else:
            avg_complexity = 0.0
        print(f"Radon output:\n{output}")
    except subprocess.TimeoutExpired:
        avg_complexity = None
        output = 'Radon timed out.'
        print("Radon timed out.")
    except Exception as e:
        avg_complexity = None
        output = f'Error running radon: {e}'
        print(f"Error running radon: {e}")
    return {
        'cyclomatic_complexity': avg_complexity,
        'radon_output': output
    }

if __name__ == '__main__':
    main()
