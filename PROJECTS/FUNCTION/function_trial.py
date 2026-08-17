import platform
import os
import subprocess
import shutil

def get_size(bytes_val):
    """Converts bytes to a human-readable format."""
    factor = 1024
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_val < factor:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= factor
    return f"{bytes_val:.2f} PB"

def run_command(command):
    """Runs a terminal command and returns the output safely."""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
        return output.decode('utf-8', errors='ignore').strip()
    except Exception:
        return None

def extract_wmic(command, ignore_header):
    """Helper to parse Windows WMIC command outputs."""
    raw = run_command(command)
    if raw:
        lines = [line.strip() for line in raw.split('\n') if line.strip() and ignore_header.lower() not in line.lower()]
        return " | ".join(lines) if lines else "Unknown"
    return "Unknown"

def display_native_sys_info():
    os_name = platform.system()
    
    print("="*45)
    print("    NATIVE HARDWARE & SYSTEM INFORMATION")
    print("="*45)

    # 1. Basic System
    print("\n--- [ System & OS ] ---")
    print(f"System Name: {platform.node()}")
    print(f"OS: {os_name} {platform.release()} ({platform.machine()})")

    # 2. ROM / Disk Space (Built-in via shutil)
    print("\n--- [ ROM / Disk Space ] ---")
    root_drive = "C:\\" if os_name == "Windows" else "/"
    try:
        total, used, free = shutil.disk_usage(root_drive)
        print(f"Total Disk Space ({root_drive}): {get_size(total)}")
        print(f"Used Space: {get_size(used)}")
        print(f"Free Space: {get_size(free)}")
    except Exception as e:
        print(f"Disk Info Error: {e}")

    # --- WINDOWS SPECIFIC FETCHING ---
    if os_name == "Windows":
        print("\n--- [ CPU & Memory ] ---")
        print(f"Processor: {extract_wmic('wmic cpu get name', 'name')}")
        
        clock_speed = extract_wmic('wmic cpu get MaxClockSpeed', 'MaxClockSpeed')
        if clock_speed.isdigit():
            print(f"Clock Speed: {int(clock_speed) / 1000:.2f} GHz")
            
        ram_bytes = extract_wmic('wmic computersystem get TotalPhysicalMemory', 'TotalPhysicalMemory')
        if ram_bytes.isdigit():
            print(f"Total RAM: {get_size(int(ram_bytes))}")

        print("\n--- [ GPU & Display ] ---")
        print(f"GPU Name: {extract_wmic('wmic path win32_VideoController get name', 'name')}")
        
        # Use built-in ctypes to get Windows screen resolution
        try:
            import ctypes
            user32 = ctypes.windll.user32
            print(f"Primary Display: {user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}")
        except Exception:
            print("Display: Resolution unknown")

    # --- MACOS SPECIFIC FETCHING ---
    elif os_name == "Darwin":
        print("\n--- [ CPU & Memory ] ---")
        print(f"Processor: {run_command('sysctl -n machdep.cpu.brand_string') or 'Unknown'}")
        
        ram_bytes = run_command('sysctl -n hw.memsize')
        if ram_bytes and ram_bytes.isdigit():
            print(f"Total RAM: {get_size(int(ram_bytes))}")

        print("\n--- [ GPU & Display ] ---")
        gpu = run_command("system_profiler SPDisplaysDataType | grep 'Chipset Model'")
        if gpu:
            print(f"GPU Name: {gpu.replace('Chipset Model:', '').strip()}")
        
        resolution = run_command("system_profiler SPDisplaysDataType | grep 'Resolution'")
        if resolution:
            print(f"Display: {resolution.replace('Resolution:', '').strip()}")

    # --- LINUX SPECIFIC FETCHING ---
    elif os_name == "Linux":
        print("\n--- [ CPU & Memory ] ---")
        cpu_info = run_command("grep 'model name' /proc/cpuinfo | head -1")
        if cpu_info:
            print(f"Processor: {cpu_info.split(':')[1].strip()}")
            
        cpu_mhz = run_command("grep 'cpu MHz' /proc/cpuinfo | head -1")
        if cpu_mhz:
            mhz = float(cpu_mhz.split(':')[1].strip())
            print(f"Clock Speed: {mhz / 1000:.2f} GHz")
            
        ram_info = run_command("grep 'MemTotal' /proc/meminfo")
        if ram_info:
            # Output is usually "MemTotal: 16393932 kB"
            kb_str = ''.join(filter(str.isdigit, ram_info))
            if kb_str:
                print(f"Total RAM: {get_size(int(kb_str) * 1024)}")

        print("\n--- [ GPU & Display ] ---")
        gpu_info = run_command("lspci | grep -i vga")
        if gpu_info:
            print(f"GPU: {gpu_info.split(':')[2].strip()}")
            
        res_info = run_command("xrandr | grep '*'")
        if res_info:
            print(f"Display: {res_info.split()[0].strip()}")

    print("\n" + "="*45)

if __name__ == "__main__":
    display_native_sys_info()