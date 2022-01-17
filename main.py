import subprocess

task_name = "ACTA-Surveyor-Edition"


def main():
    command = "schtasks.exe /END /TN " + task_name
    subprocess.run(command)
    command = "schtasks.exe /RUN /TN " + task_name
    subprocess.run(command)
