import tkinter as tk
from tkinter import Entry, Button, Label, filedialog, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def show_image():
    image_label.config(image='')
    url = entry.get()

    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira um link da imagem.")
        return

    try:
        # Faz o download da imagem
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para códigos de status HTTP 
        image_data = Image.open(BytesIO(response.content))


        image_data.thumbnail((300, 300))

        
        global current_image  
        current_image = image_data
        photo = ImageTk.PhotoImage(image_data)

        
        image_label.config(image=photo)
        image_label.image = photo  
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Download", f"Erro ao baixar a imagem: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")

def save_image():
    if current_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg;*.jpeg"),
                                                              ("All files", "*.*")])
        if file_path:
            current_image.save(file_path)
            messagebox.showinfo("Sucesso", f"Imagem salva em: {file_path}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma imagem carregada para salvar.")

# janela principal
root = tk.Tk()
root.title("Exibidor de Imagem")
root.geometry("400x400")  # Largura x Altura


entry = Entry(root, width=40)
entry.pack(pady=20)


button = Button(root, text="Mostrar Imagem", command=show_image)
button.pack()

save_button = Button(root, text="Salvar Imagem", command=save_image)
save_button.pack()
image_label = Label(root)
image_label.pack(pady=20)
current_image = None
root.mainloop()
