import os
import shutil
from helpers import split_val

class MoleculeContainer:
    def __init__(self, temp, conditions, console) -> None:
        self.temp = temp
        self.conditions = conditions
        self.tracker = ActivityTracker(console)
        self.tracker.start(f"simulation {temp}K")

    def __repr__(self) -> str:
        return f"<MoleculeContainer: temp<{self.temp}>, coditions<{self.conditions}>>"
    
    def make_workspace(self):
        self.dir = f"simulation_{self.temp}"
        self.tracker.process(f"making workspace {self.dir}")
        os.mkdir(dir)
        os.mkdir(f"{dir}/logs")
        for f in filter(os.path.isfile, os.listdir()):
            shutil.copy(f, self.dir)
        return
    
    def setup(self):
        schema = open("layout", "rt")
        data = schema.read()
        data.replace("TEMP", split_val(self.temp)[0])
        data.replace("TEMP_U", split_val(self.temp)[1])
        data.replace("TIME1", split_val(elf.conditions["time"][0])[0])
        data.replace("TIME2", split_val(self.conditions["time"][1])[0])
        data.replace("DT1", split_val(self.conditions["time"][0])[0])
        data.replace("DT2", split_val(self.conditions["time"][1])[0])
        data.replace("STEPS1", self.conditions["time"][0])
        data.replace("STEPS2", self.conditions["time"][1])
        data.replace("TIME1_U", split_val(self.conditions["time"][0])[1])
        data.replace("TIME2_U", split_val(self.conditions["time"][1])[1])
        data.replace("DT1_U", split_val(self.conditions["time"][0])[1])
        data.replace("DT2_U", split_val(self.conditions["time"][1])[1])
        schema.close()
        specifications = open("layout", "wt")
        specifications.write(data)
        specifications.close()
        for 

    def start(self):


class ActivityTracker:
    def __init__(self, console) -> None:
        self.console = console

    def start(self, simu):
        self.console.rule(f"[bold green]{simu}")
    
    def process(self, label):
        self.console.print(f"--> {label}")

    def finish(self):
        self.console.rule()
