import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    text = entry_text.get()
    target_language = entry_language.get()

    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        label_translation.config(text="Çevirilen Metin: " + translated_text.text)
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Hatalı dil kodu! Lütfen geçerli bir dil kodu girin.", fg="#DB4840")

def show_languages():
    languages = {
        "İngilizce": "en",
        "Türkçe": "tr",
        "Fransızca": "fr",
        "Almanca": "de",
        "İspanyolca": "es",
        "Kürtçe": "ku",
        "Rusça": "ru",
        "Japonca": "ja",
        "Çince": "zh-cn",
        "Arapça": "ar",
        "Portekizce": "pt",
        "Farsça": "fa"
    }

    popup = tk.Toplevel(window)
    popup.title("Desteklenen Dil Kodları")
    popup.geometry("300x330")  # Yüksekliği 330 olarak değiştirildi
    popup.configure(bg="#DB4840")

    # Ana pencerenin konumunu al
    window_x = window.winfo_x()
    window_y = window.winfo_y()

    # Popup pencerenin konumunu ayarla
    popup_x = window_x + window.winfo_width()
    popup_y = window_y
    popup.geometry("+{}+{}".format(popup_x, popup_y))

    for language, code in languages.items():
        ttk.Label(popup, text=f"{language}: {code}", background="#DB4840", foreground="white", font=("Arial", 10)).pack()

# Pencere oluştur
window = tk.Tk()
window.title("Language Translator")
window.geometry("450x330")
window.configure(bg="#313131")

# Icon eklemek
#window.iconbitmap("C:\\Users\\ferha\\Downloads\\icon.png")

# Metin girişi ve dil seçimi için etiketler
label_text = tk.Label(window, text="Çevrilecek Metin:", bg="#313131", fg="white", font=("Arial", 10))
label_text.grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(window, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_language = tk.Label(window, text="Hedef Dil Kodu:", bg="#313131", fg="white", font=("Arial", 10))
label_language.grid(row=1, column=0, padx=10, pady=10)
entry_language = tk.Entry(window, width=10)
entry_language.grid(row=1, column=1, padx=10, pady=10)

# Dil kodu girme hata mesajı
error_label = tk.Label(window, text="", bg="#313131", fg="#DB4840", font=("Arial", 10))
error_label.grid(row=2, columnspan=2, padx=10, pady=0)

# Çeviri sonucunu göstermek için etiket
label_translation = tk.Label(window, text="", bg="#313131", fg="white", font=("Arial", 10), wraplength=400)
label_translation.grid(row=3, columnspan=2, padx=10, pady=10)

# Çeviri butonu
button_translate = tk.Button(window, text="Çevir", bg="#DB4840", fg="white", font=("Arial", 10), command=translate_text)
button_translate.grid(row=4, columnspan=2, padx=10, pady=10)

# Örnek dil kodlarını göstermek için açılır pencere
button_languages = tk.Button(window, text="Desteklenen Dil Kodları", bg="#DB4840", fg="white", font=("Arial", 10), command=show_languages)
button_languages.grid(row=5, columnspan=2, padx=10, pady=10)

# Uygulamayı çalıştır
window.mainloop()
