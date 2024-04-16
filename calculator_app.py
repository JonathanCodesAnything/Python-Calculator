import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text=f"Result: {result}")
    except Exception as e:
        output.config(text="Error")

# Create the main application window
app = tk.Tk()
app.title("Python Calculator")

# Create widgets
label = tk.Label(app, text="Enter an equation:")
entry = tk.Entry(app)
button = tk.Button(app, text="Calculate", command=calculate)
output = tk.Label(app, text="Result:")

# Arrange widgets using grid layout
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, columnspan=2)
output.grid(row=2, columnspan=2)

# Run the application
app.mainloop()
 