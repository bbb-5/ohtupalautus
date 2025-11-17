class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = ["New user registered","User with username kalle already exists","Username is too short","Password is too short","Username not valid, can't include ' '", "Password needs to include numbers"]

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value):
        self.inputs.append(value)
