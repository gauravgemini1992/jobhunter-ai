class Pipeline:

    def __init__(self):
        self.steps = []

    def register(self, step):
        self.steps.append(step)

    def run(self, data):

        result = data

        for step in self.steps:
            result = step.parse(result)

        return result