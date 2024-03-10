import tkinter as tk

class State:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.id = canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue')
        self.text_id = canvas.create_text(x, y, text=text)
        self.transitions = []

    def delete(self):
        for transition in self.transitions:
            transition.delete()
        self.canvas.delete(self.id)
        self.canvas.delete(self.text_id)

class Transition:
    def __init__(self, canvas, from_state, to_state):
        self.canvas = canvas
        self.from_state = from_state
        self.to_state = to_state
        self.id = canvas.create_line(
            canvas.coords(from_state.id)[:2],
            canvas.coords(to_state.id)[:2],
            arrow=tk.LAST
        )
        from_state.transitions.append(self)
        to_state.transitions.append(self)

    def delete(self):
        self.canvas.delete(self.id)
        self.from_state.transitions.remove(self)
        self.to_state.transitions.remove(self)

class StateChart(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.states = {}  # Dictionary to store states
        self.transitions = {}  # Dictionary to store transitions
        self.bind("<Button-1>", self.create_state)
        self.selected_state = None

    def create_state(self, event):
        state_id = len(self.states) + 1
        state = State(self, event.x, event.y, str(state_id))
        self.states[state_id] = state

    def add_transition(self, from_state_id, to_state_id):
        if from_state_id in self.states and to_state_id in self.states:
            transition = Transition(self, self.states[from_state_id], self.states[to_state_id])
            self.transitions[(from_state_id, to_state_id)] = transition

    def delete_state(self, state_id):
        if state_id in self.states:
            self.states[state_id].delete()
            del self.states[state_id]

    def delete_transition(self, from_state_id, to_state_id):
        key = (from_state_id, to_state_id)
        if key in self.transitions:
            self.transitions[key].delete()
            del self.transitions[key]

# Example usage
root = tk.Tk()
chart = StateChart(root, width=600, height=400)
chart.pack()

# Add buttons for adding transitions and deleting elements
def add_transition():
    from_state_id = int(from_state_entry.get())
    to_state_id = int(to_state_entry.get())
    chart.add_transition(from_state_id, to_state_id)

def delete_state():
    state_id = int(delete_state_entry.get())
    chart.delete_state(state_id)

from_state_entry = tk.Entry(root)
to_state_entry = tk.Entry(root)
add_transition_button = tk.Button(root, text="Add Transition", command=add_transition)

delete_state_entry = tk.Entry(root)
delete_state_button = tk.Button(root, text="Delete State", command=delete_state)

from_state_entry.pack()
to_state_entry.pack()
add_transition_button.pack()
delete_state_entry.pack()
delete_state_button.pack()

root.mainloop()
