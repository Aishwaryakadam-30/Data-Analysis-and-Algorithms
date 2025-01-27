import platform
import psutil

def display_system_details():
    print("System Details:")
    print(f"CPU Model: {platform.processor()}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Operating System: {platform.system()} {platform.release()}")

display_system_details()
