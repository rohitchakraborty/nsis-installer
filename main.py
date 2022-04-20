import os
import subprocess
from tkinter import messagebox


def main():
    task_name = "ACTA-Surveyor-Edition"
    command = "schtasks.exe /END /TN " + task_name
    subprocess.run(command)
    py_ids = [int(line.split()[1]) for line in os.popen('tasklist').readlines()[3:] if line.split()[0] == "pythonw.exe"]
    py_ids_to_kill = [id for id in py_ids if id != os.getpid()]
    for pid in py_ids_to_kill:
        os.system("taskkill /pid {} /T /F".format(pid))
    command = "schtasks.exe /RUN /TN " + task_name
    subprocess.run(command)
    messagebox.showinfo(title=task_name, message="Started successfully")
