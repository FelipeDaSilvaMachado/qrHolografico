import qrcode
from PIL import Image, ImageOps

# Criando o objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
)

# Adicionando o link do vídeo, página
# ou imagem que deseja incluir no QR Code
# qr.add_data("https://www.instagram.com/destinoidealtur/")
qr.add_data("https://felipedasilvamachado.github.io/qrHolografico/")
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(fill="black", back_color="white").convert("RGBA")

# Carregar o logo da Destino Ideal Tour
logoDIT = Image.open("Logo Destino Ideal Tour.jpg")

# Garantir que o logo seja convertido para RGBA (caso tenha canal alfa)
if logoDIT.mode != "RGBA":
    logoDIT = logoDIT.convert("RGBA")

# Adicionar fundo branco ao logo para remover qualquer transparência
background = Image.new("RGBA", logoDIT.size, "white")  # Criar um fundo branco
logoDIT = Image.alpha_composite(background, logoDIT)  # Mesclar o logo com o fundo branco

# Redimensionar o logo
logoDIT_size = (img.size[0] // 3, img.size[1] // 3)
logoDIT = logoDIT.resize(logoDIT_size, Image.Resampling.LANCZOS)

# Calculando a posição do logo no QR Code
position = ((img.size[0] - logoDIT_size[0]) // 2,
            (img.size[1] - logoDIT_size[1]) // 2)

# Colocar o logo no QR Code (agora sem transparência)
img.paste(logoDIT, position)

# Converter a imagem para RGB antes de salvar como JPEG (já que JPEG não suporta transparência)
img = img.convert("RGB")

# Salvando o QR Code
img.save("video holografico.jpg")