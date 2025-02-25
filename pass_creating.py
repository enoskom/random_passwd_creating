import random
import string
import tkinter as tk
from tkinter import messagebox
import pyfiglet  # ASCII art için pyfiglet kütüphanesini ekliyoruz

# Şifre üretim fonksiyonu
def password_generator(length, use_upper, use_lower, use_digits, use_special):
    # Sabit karakter setleri (Bunları koda dahil ettik)
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Büyük harfler
    lower_chars = "abcdefghijklmnopqrstuvwxyz"  # Küçük harfler
    digits = "0123456789"  # Rakamlar
    special_chars = "!@#$%^&*()-_=+[{]}|;:'\",<.>/?~"  # Özel karakterler
    
    # Boş bir karakter seti oluştur
    char_pool = ''
    
    # Kullanıcı hangi karakter türlerini isterse o setleri ekle
    if use_upper:
        char_pool += upper_chars
    if use_lower:
        char_pool += lower_chars
    if use_digits:
        char_pool += digits
    if use_special:
        char_pool += special_chars
    
    # Eğer hiçbir karakter türü seçilmediyse, kullanıcıya bilgi ver ve çık
    if not char_pool:
        return "Hiçbir karakter türü seçmediniz."
    
    # Şifreyi oluştur
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    # Şifreyi karıştır
    password = ''.join(random.sample(password, len(password)))
    
    return password


# Terminal için şifre üretme fonksiyonu
def terminal_password_generator():
    # Kullanıcıdan şifre uzunluğunu alma
    length = int(input("Şifreniz kaç karakterli olsun? "))
    
    # Kullanıcıdan hangi karakter tiplerini kullanmak istediğini alma
    use_upper = input("Büyük harf ? (e/h): ").lower() == 'e'
    use_lower = input("Küçük harf ? (e/h): ").lower() == 'e'
    use_digits = input("Rakam ? (e/h): ").lower() == 'e'
    use_special = input("Özel karakter ? (e/h): ").lower() == 'e'
    
    # Şifreyi oluştur
    password = password_generator(length, use_upper, use_lower, use_digits, use_special)
    
    # Son olarak, şifreyi yazdır
    print(f"şifre: {password}")


# GUI için şifre üretme fonksiyonu
def gui_password_generator():
    def show_password_generator():
        # Başla butonunu gizle
        button_start.pack_forget()

        # Çıkış butonunu gizle
        button_exit.pack_forget()

        # Dikkat uyarılarını gizle
        label_attention.pack_forget()
        label_attention_message.pack_forget()

        # Şifre üretme formunu göster
        label_length.pack(pady=10)
        entry_length.pack(pady=10)
        check_upper.pack()
        check_lower.pack()
        check_digits.pack()
        check_special.pack()
        entry_result.pack(pady=10)
        button_generate.pack()
        button_copy.pack(pady=10)

    def on_generate():
        try:
            length = int(entry_length.get())
            use_upper = var_upper.get()
            use_lower = var_lower.get()
            use_digits = var_digits.get()
            use_special = var_special.get()

            password = password_generator(length, use_upper, use_lower, use_digits, use_special)
            
            # Şifreyi entry widget'ında göster
            entry_result.config(state=tk.NORMAL)
            entry_result.delete(0, tk.END)  # Önceki şifreyi sil
            entry_result.insert(0, password)  # Yeni şifreyi ekle
            entry_result.config(state='readonly')
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir sayı girin.")

    def on_copy():
        # Şifreyi panoya kopyala
        window.clipboard_clear()
        window.clipboard_append(entry_result.get())
        messagebox.showinfo("Başarılı", "Şifre panoya kopyalandı.")

    def on_exit():
        window.quit()

    def toggle_color(checkbutton):
        if checkbutton.cget("bg") == "green":
            checkbutton.config(bg="red")
        else:
            checkbutton.config(bg="green")

    # GUI penceresini oluştur
    window = tk.Tk()
    window.title("Şifre Üretici")
    
    # Pencereyi tam ortada açmak ve boyutları ayarlamak
    screen_width = window.winfo_screenwidth()  # Ekran genişliği
    screen_height = window.winfo_screenheight()  # Ekran yüksekliği
    window_width = 800  # Pencere genişliği
    window_height = 720  # Pencere yüksekliği
    
    # Pencereyi ekrana ortalayacak şekilde konumlandırma
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    
    window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    
    # GUI penceresinin arka planını siyah yap
    window.config(bg="black")
    
    # ASCII art ile ENOSKOM yazısını oluşturma
    ascii_art = pyfiglet.figlet_format("ENOSKOM")
    
    # ASCII art'ı Label widget'ı ile ekleme
    label_ascii = tk.Label(window, text=ascii_art, font=("Courier", 18, "bold"), bg="black", fg="green", justify=tk.LEFT)
    label_ascii.pack(pady=1)

    # Dikkat başlığı ve mesajları
    label_attention = tk.Label(window, text="Dikkat!", font=("Courier", 14, "bold"), bg="black", fg="yellow")
    label_attention_message = tk.Label(window, text="Lütfen şifre uzunluğu ve en az bir karakter tipi seçin.\n"
                                                     "Şifreler, seçtiğiniz kriterlere göre oluşturulacaktır.\n"
                                                     "En güvenli şifreyi oluşturmak için hepsini seçmeniz önerilir.",
                                        font=("Courier", 12), bg="black", fg="yellow")

    label_attention.pack(pady=10)
    label_attention_message.pack(pady=10)

    # Başla butonu (arxa planı siyah yapma ve yazıyı beyaz yapma)
    button_start = tk.Button(window, text="Başla", command=show_password_generator, bg="green", fg="white", font=("Courier", 16))
    button_start.pack(pady=20)

    # Çıkış butonu
    button_exit = tk.Button(window, text="Çıkış", command=on_exit, bg="red", fg="white", font=("Courier", 16))
    button_exit.pack(pady=10)

    # Şifre uzunluğu
    label_length = tk.Label(window, text="Şifre uzunluğunu girin", bg="black", fg="yellow")
    entry_length = tk.Entry(window)

    # Seçenekler
    var_upper = tk.BooleanVar()
    var_lower = tk.BooleanVar()
    var_digits = tk.BooleanVar()
    var_special = tk.BooleanVar()

    # Hepsinin boyutlarını eşitle
    button_width = 15
    button_height = 2

    check_special = tk.Checkbutton(window, text="Özel karakter", variable=var_special, bg="green", fg="white", width=button_width, height=button_height, command=lambda: toggle_color(check_special))
    check_upper = tk.Checkbutton(window, text="Büyük harf", variable=var_upper, bg="green", fg="white", width=button_width, height=button_height, command=lambda: toggle_color(check_upper))
    check_lower = tk.Checkbutton(window, text="Küçük harf", variable=var_lower, bg="green", fg="white", width=button_width, height=button_height, command=lambda: toggle_color(check_lower))
    check_digits = tk.Checkbutton(window, text="Rakam", variable=var_digits, bg="green", fg="white", width=button_width, height=button_height, command=lambda: toggle_color(check_digits))

    # Şifreyi göstermek için entry widget'ı kullanıyoruz
    entry_result = tk.Entry(window, width=50, state='readonly')  # Şifreyi burada göstereceğiz

    # Şifreyi oluştur butonu
    button_generate = tk.Button(window, text="Şifre oluştur", command=on_generate, bg="red", fg="white", width=button_width, height=button_height)

    # Şifreyi kopyala butonu
    button_copy = tk.Button(window, text="Şifreyi kopyala", command=on_copy, bg="blue", fg="white", width=button_width, height=button_height)

    # "Version 1.0.0" etiketini sağ alt köşeye sabitleme
    label_version = tk.Label(window, text="Version 1.0.0", font=("Courier", 10), bg="black", fg="white")
    label_version.place(x=window_width - 10, y=window_height - 5, anchor="se")

    # Pencereyi çalıştır
    window.mainloop()


# Ana fonksiyon, hangi modun seçileceğini sorar
def main():
    choice = input("Terminal mi GUI mi? (T/G): ").lower()

    if choice == 't':
        terminal_password_generator()
    elif choice == 'g':
        gui_password_generator()
    else:
        print("Geçersiz seçim. Program sonlanıyor.")


# Programı başlat
if __name__ == "__main__":
    main()
