import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'development'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])
#subprocess.call(['conda', 'activate', '{{ cookiecutter.project_slug }}'])
#subprocess.call(['pip', 'install', 'jupyter_contrib_nbextensions'])
#subprocess.call(['jupyter', 'contrib', 'nbextension', 'install', '--user'])



condition = "{{ cookiecutter.repository_remote }}"

if condition == "Enlazar":
    subprocess.call(['git', 'remote', 'add', 'origin', "{{ cookiecutter.git_url }}"])
    





print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")