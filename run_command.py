import subprocess

base_command = "python cromlech.py cromlech\\jpet_servicecutter_to_cromlech.yaml 4"
start_value = 0.0
step = 0.1
iterations = 11

for i in range(iterations):
    current_value = start_value + i * step
    formatted_value = f"{current_value:.1f}"
    print(formatted_value)
    # command = f"{base_command} \"{formatted_value}\" 60"
    # subprocess.run(command, shell=True)
