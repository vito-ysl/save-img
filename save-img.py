import tkinter as tk
from tkinter import Entry, Button, Label, filedialog, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def show_image():
    # Limpa o label da imagem anterior
    image_label.config(image='')
    
    # Obtém o URL da entrada
    url = entry.get()
    
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira um link da imagem.")
        return

    try:
        # Faz o download da imagem
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx
        image_data = Image.open(BytesIO(response.content))

        # Redimensiona a imagem para 300x300 (ajuste conforme necessário)
        image_data.thumbnail((300, 300))

        # Converte a imagem para um formato que o Tkinter pode usar
        global current_image  # Armazena a imagem atual para salvar
        current_image = image_data
        photo = ImageTk.PhotoImage(image_data)

        # Exibe a imagem no label
        image_label.config(image=photo)
        image_label.image = photo  # Armazena a referência da imagem
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Download", f"Erro ao baixar a imagem: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")

def save_image():
    if current_image:
        # Abre a caixa de diálogo para salvar a imagem
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg;*.jpeg"),
                                                              ("All files", "*.*")])
        if file_path:
            current_image.save(file_path)
            messagebox.showinfo("Sucesso", f"Imagem salva em: {file_path}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma imagem carregada para salvar.")

# Criar a janela principal
root = tk.Tk()
root.title("Exibidor de Imagem")
root.geometry("400x400")  # Largura x Altura

# Campo de entrada
entry = Entry(root, width=40)
entry.pack(pady=20)

# Botão para carregar a imagem
button = Button(root, text="Mostrar Imagem", command=show_image)
button.pack()

# Botão para salvar a imagem
save_button = Button(root, text="Salvar Imagem", command=save_image)
save_button.pack()

# Label para exibir a imagem
image_label = Label(root)
image_label.pack(pady=20)

# Variável global para armazenar a imagem atual
current_image = None

# Iniciar o loop principal
root.mainloop()
