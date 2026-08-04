from PIL import Image, ImageDraw

WIDTH, HEIGHT = 400, 80
FRAMES = 40
BG = (13, 17, 23)       # fundo escuro (estilo GitHub)
ROAD = (48, 54, 61)
CAR = (88, 166, 255)    # azul
WHEEL = (201, 209, 217)
LIGHT = (255, 212, 59)

def draw_car(draw, x, y):
    # corpo
    draw.rectangle([x, y + 10, x + 40, y + 22], fill=CAR)
    # teto
    draw.rectangle([x + 10, y, x + 30, y + 12], fill=CAR)
    # farol
    draw.rectangle([x + 36, y + 12, x + 40, y + 16], fill=LIGHT)
    # rodas
    draw.ellipse([x + 4, y + 20, x + 14, y + 30], fill=WHEEL)
    draw.ellipse([x + 26, y + 20, x + 36, y + 30], fill=WHEEL)

def make_frame(i):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # estrada
    draw.rectangle([0, 50, WIDTH, 58], fill=ROAD)
    # faixas
    offset = (i * 8) % 30
    for sx in range(-30 + offset, WIDTH, 30):
        draw.rectangle([sx, 53, sx + 14, 55], fill=(110, 118, 129))

    # posição do carro (ida e volta)
    path = WIDTH + 50
    pos = (i * (path // FRAMES)) % path
    x = pos - 45
    draw_car(draw, x, 22)

    return img

frames = [make_frame(i) for i in range(FRAMES)]
frames[0].save(
    "car.gif",
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0,
)
print("car.gif gerado!")