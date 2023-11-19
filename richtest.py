import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen
from rich.progress import track
from time import sleep


from rich.progress import (
            BarColumn,
            DownloadColumn,
            Progress,
            TaskID,
            TextColumn,
            TimeRemainingColumn,
            TransferSpeedColumn,
)

progress = Progress(
            TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
            BarColumn(bar_width=None),
                    "[progress.percentage]{task.percentage:>3.1f}%",
                    "•",
            DownloadColumn(),"•",
            TransferSpeedColumn(),"•",
            TimeRemainingColumn())

task_id = progress.add_task("A", along=0)

progress.update(task_id, along=1)
progress.update(task_id, along=3)
progress.update(task_id, along=90)

progress.console.log("blah " + str(progress))
progress.console.log(f"[green] Downloaded")

def process_data():
    sleep(0.02)


for _ in track(range(100), description='[green]Processing data'):
    process_data()



with ThreadPoolExecutor(max_workers=4) as pool:
 task_id = progress.add_task("download", filename='filename', start=False)                                                                                    
 pool.submit('copy_url', task_id, 'url', 'dest_path')

