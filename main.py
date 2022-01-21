import subprocess
from tkinter import messagebox


def main():
    task_name = "ACTA-Surveyor-Edition"
    command = "schtasks.exe /END /TN " + task_name
    subprocess.run(command)
    command = "schtasks.exe /RUN /TN " + task_name
    subprocess.run(command)
    messagebox.showinfo(title=task_name, message="Restart successful")
