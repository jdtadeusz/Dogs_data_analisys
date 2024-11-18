import subprocess

data_filter = "./ProcessingScripts/filtering_data.py"
analyze_data = "./AnalisysScripts/analyze_data.py"

subprocess.run(["python", data_filter], check=True)

subprocess.run(["python", analyze_data], check=True)