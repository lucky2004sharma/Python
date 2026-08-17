import platform
import os

def display_sys_info():
    print("=== System Information ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Current Working Directory: {os.getcwd()}")
    print("==========================")

if __name__ == "__main__":
    display_sys_info()