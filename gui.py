import tkinter as tk
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_uptime

def update_stats():
    cpu_label.config(text=f"CPU Usage: {get_cpu_usage()}%")
    mem_label.config(text=f"Memory Usage: {get_memory_usage()}%")
    disk_label.config(text=f"Disk Usage: {get_disk_usage()}%")
    uptime_label.config(text=f"Uptime: {get_uptime()}")
    root.after(1000, update_stats)

root = tk.Tk()
root.title("Linux Monitor Dashboard")
root.geometry("300x200")

cpu_label = tk.Label(root, text="CPU Usage:", font=("Helvetica", 12))
cpu_label.pack(pady=5)

mem_label = tk.Label(root, text="Memory Usage:", font=("Helvetica", 12))
mem_label.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage:", font=("Helvetica", 12))
disk_label.pack(pady=5)

uptime_label = tk.Label(root, text="Uptime:", font=("Helvetica", 12))
uptime_label.pack(pady=5)

update_stats()
root.mainloop()
