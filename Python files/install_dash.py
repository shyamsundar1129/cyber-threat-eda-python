import subprocess
import sys

def install_packages():
    packages = ["dash", "plotly", "pandas"]
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("All required packages installed successfully!")

if __name__ == "__main__":
    install_packages()
