# Your imports
import task


# Make changes to the Widget class as needed
class WidgetTask:
    def run(self, parameters):
        return [f'{parameters["first_name"]} {parameters["last_name"]}'.encode()]


# Make changes to the Gadget class as needed
class GadgetTask:
    def run(self, parameters):
        return [f'{int(parameters["end_time"]) - int(parameters["start_time"])}'.encode()]
