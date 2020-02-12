from inspect import getmembers, isclass, isabstract
import Processors

class ProcessorFactory:
    processes = {}

    def __init__(self):
        self.load_processors()

    def load_processors(self):
        classes = getmembers(Processors, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Processors.ProcessorABC):
                self.processes.update([[name, _type]])
                print(name, _type)


    def create_instance(self, processname):
        if processname in self.processes:
            return self.processes[processname]()
        else:
            return Processors.NullProcessor(processname)