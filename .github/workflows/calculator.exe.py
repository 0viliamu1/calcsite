import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Створення головного вікна
root = tk.Tk()
root.title('Calculator')
root.geometry('300x350')

# Завантаження іконки
try:
    image = Image.open('da70511b-9425-419f-9e18-dfaa4833d9ef.PNG')  # Перевір шлях до файлу
    icon = ImageTk.PhotoImage(image)
    root.iconphoto(False, icon)  # Встановлення іконки
except Exception as e:
    print(f"Помилка завантаження іконки: {e}")

# Функція для обробки натискань кнопок
def click(button):
    if button == '÷':
        button = '/'
    elif button == '×':
        button = '*'
    
    if button == '=':
        try:
            result = str(eval(display.get()))
            display.delete(0, ctk.END)
            display.insert(0, result)
        except:
            display.delete(0, ctk.END)
            display.insert(0, 'ERROR')
    elif button == 'C':
        display.delete(0, ctk.END)
    else:
        display.insert(ctk.END, button)

# Налаштування теми
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

# Поле для введення
display = ctk.CTkEntry(root, font=("Arial", 24))
display.pack(fill='x', padx=10, pady=10)

# Кнопки калькулятора
buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

frame = ctk.CTkFrame(root)
frame.pack()

for i, button in enumerate(buttons):
    btn = ctk.CTkButton(frame, text=button, width=60, height=60, font=("Arial", 18),
                        command=lambda b=button: click(b))
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

root.mainloop()

# Додано input(), щоб термінал не закривався
input("Натисніть Enter, щоб вийти...")