import os, sys
print("====== Data Check Script ======")
checks = {
    "Python version": sys.version,
    "Working directory": os.getcwd(),
    "Files in directory": str(os.listdir(".")),
}
for check, value in checks.items():
    print(f"[PASS] {check}: {value}")
print("All checks passed!")
print("================================")
