import platform
import subprocess
import importlib.util

print(" SYSTEM INFORMATION ")
print("Operating system:", platform.system())
print("Python version:", platform.python_version())

print("\n NVIDIA GPU ")

try:
    result = subprocess.run(
        ["nvidia-smi"],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("NVIDIA GPU not detected through nvidia-smi.")

except FileNotFoundError:
    print("nvidia-smi is not available.")
except Exception as error:
    print("Error:", error)

print("\ PYTORCH")

if importlib.util.find_spec("torch"):
    import torch

    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
else:
    print("PyTorch is not installed yet.")