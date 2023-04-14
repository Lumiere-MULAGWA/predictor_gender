import tkinter as tk
from tkinter import ttk

def predict_gender(name):
    name = name.lower()
    if (name[-1] == 'a') or (name[-1] == 'e') or (name[-1] == 'h') or (name[-1] == 'i') or (name[-1] == 'n'):
        return "female"
    elif (name[-1] == 'o')or (name[-1] == 'l') or (name[-1] == 'm') or (name[-1] == 'y') or (name[-1] == 't') or (name[-1] == 's'):
        return "male"
    else:
        return "unknown"

def main():
    root = tk.Tk()
    root.title("Gender Predictor")
    root.geometry("400x200")

    
    name_label = ttk.Label(root, text="Enter name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ttk.Label(root, text="Predicted gender:")
    result_label.grid(row=1, column=0, padx=5, pady=5)
    result_entry = ttk.Entry(root, state="readonly")
    result_entry.grid(row=1, column=1, padx=5, pady=5)

    
    
    def predict():
        name = name_entry.get()
        gender = predict_gender(name)
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, gender)
        result_entry.config(state="readonly")

    
    predict_button = ttk.Button(root, text="Predict", command=predict)
    predict_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
