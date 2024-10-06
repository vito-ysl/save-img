# Save-img

🌟 **Save-img** é um aplicativo desenvolvido em Python que permite visualizar e salvar imagens a partir de links diretos. Com uma interface simples e intuitiva, o Save-img facilita o processo de baixar e gerenciar imagens da web!

![save-img logo](https://i.pinimg.com/originals/0d/ea/6d/0dea6d019714ad365b3858492823f417.gif)) <!-- Substitua com o link do seu logo ou outro GIF -->

## 🚀 Funcionalidades

- Exibir imagens diretamente da URL.
- Salvar imagens no seu dispositivo em formatos PNG e JPEG.
- Interface gráfica simples, construída com Tkinter.
- Redimensionamento automático da imagem para otimizar a exibição.


## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Para a criação da interface gráfica.
- **Pillow (PIL)**: Para manipulação e exibição de imagens.
- **Requests**: Para baixar imagens da web a partir da URL.

## ⚙️ Instalação

1. **Clone este repositório**:
    ```bash
    git clone https://github.com/vito-ysl/save-img.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd save-img
    ```

3. **Instale as dependências**:
    Certifique-se de que o Python esteja instalado. Em seguida, instale as bibliotecas necessárias:
    ```bash
    pip install Pillow requests
    ```

4. **Execute o projeto**:
    ```bash
    python main.py
    ```

## 📋 Como Usar

1. Abra o aplicativo **save-img**.
2. No campo de entrada, cole um link de imagem (URL).
3. Clique no botão "Mostrar Imagem" para exibi-la.
4. Se quiser salvar a imagem, clique no botão "Salvar Imagem" e escolha o local e formato do arquivo.


## 📂 Estrutura do Projeto

```bash
save-img/
│
├── main.py         # Arquivo principal com a lógica do aplicativo
├── README.md       # Arquivo com a documentação do projeto
└── requirements.txt # Lista de dependências
