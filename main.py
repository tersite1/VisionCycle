import argparse
import subprocess

def run_script(script_name, data_path, output_path):
    command = ["python", script_name, "--data", data_path, "--output_dir", output_path]
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="Run AutoBounding, AutoCapture, and MeshCalc scripts")
    parser.add_argument("--data", type=str, required=True, help="Path to the data file")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the output")

    args = parser.parse_args()

    scripts = ["AutoBounding.py", "AutoCapture.py", "MeshCalc.py"]

    for script in scripts:
        run_script(script, args.data, args.output_dir)

if __name__ == "__main__":
    main()
