import os, time

tasks = [
    "M=512 N=256 K=640",
    "M=512 N=384 K=256",
    "MNK=512",
    "MNK=896",
    "MNK=1024",
    "MNK=1152",
    "MNK=1536",
    "MNK=2048",
    "MNK=3072",
    "MNK=4096",
    "MNK=8192",
    "M=512 N=3072 K=768",
    "M=512 N=768 K=3072",
]

old_cmd = [f'python3 tune.py {t} O=65537' for t in tasks]
async_cmd = [f'python3 tune.py {t} O=65536' for t in tasks]
cmds = old_cmd + async_cmd
cmd = ' && '.join(cmds)
os.system(cmd)

time.sleep(10)

content = f'\n[FINISH | run.py] all scheduled task is finished.'
with open('finished_task.txt', 'a') as f:
    f.write(content)