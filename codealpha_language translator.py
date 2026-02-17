import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# -------------------- TRANSLATE FUNCTION --------------------
def translate_text():
    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    source_lang = source_var.get()
    target_lang = target_var.get()

    try:
        translated = GoogleTranslator(
            source=lang_codes[source_lang],
            target=lang_codes[target_lang]
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", "Internet connection required")


# -------------------- LANGUAGE LIST --------------------
lang_codes = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

# -------------------- WINDOW --------------------
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x420")
root.resizable(False, False)

# -------------------- INPUT LABEL --------------------
tk.Label(root, text="Enter Text", font=("Arial", 12, "bold")).pack(pady=5)

# -------------------- INPUT BOX --------------------
input_box = tk.Text(root, height=6, width=70, font=("Arial", 11))
input_box.pack(pady=5)

# -------------------- LANGUAGE SELECTION --------------------
frame = tk.Frame(root)
frame.pack(pady=10)

source_var = tk.StringVar()
target_var = tk.StringVar()

source_var.set("Auto Detect")
target_var.set("Hindi")

tk.Label(frame, text="From: ").grid(row=0, column=0, padx=5)
source_menu = ttk.Combobox(frame, textvariable=source_var, values=list(lang_codes.keys()), state="readonly")
source_menu.grid(row=0, column=1, padx=5)

tk.Label(frame, text="To: ").grid(row=0, column=2, padx=5)
target_menu = ttk.Combobox(frame, textvariable=target_var, values=list(lang_codes.keys()), state="readonly")
target_menu.grid(row=0, column=3, padx=5)

# -------------------- TRANSLATE BUTTON --------------------
tk.Button(root, text="Translate", font=("Arial", 12, "bold"), bg="green", fg="white", command=translate_text).pack(pady=10)

# -------------------- OUTPUT LABEL --------------------
tk.Label(root, text="Translated Text", font=("Arial", 12, "bold")).pack(pady=5)

# -------------------- OUTPUT BOX --------------------
output_box = tk.Text(root, height=6, width=70, font=("Arial", 11))
output_box.pack(pady=5)

# -------------------- RUN APP --------------------
root.mainloop()
