import cairo
import os

# Variáveis Globais
OUTPUT_DIR = r"./outputs"


WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

class Saidas:
    def __init__(self):
        pass

    def vertical_line(self, file):
        ctx.set_source_rgb(1, 1, 1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.move_to(128, 15)
        ctx.line_to(128, 240)
        ctx.stroke()

        surface.write_to_png(file)

    def horizontal_line(self, file):
        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.move_to(15, 128)
        ctx.line_to(240, 128)
        ctx.stroke()

        surface.write_to_png(file)


def main():
    saida = Saidas()
    saida.vertical_line(os.path.join(OUTPUT_DIR, "vert_line.png"))
    saida.horizontal_line(os.path.join(OUTPUT_DIR, "hori_line.png"))

if __name__ == "__main__":
    main()