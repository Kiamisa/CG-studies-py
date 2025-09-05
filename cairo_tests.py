import cairo
import os
import math
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

    def cross_lines(self, file):
        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        #line1
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.move_to(15, 128)
        ctx.line_to(240,128)
        ctx.stroke()
        #line2
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.move_to(128, 15)
        ctx.line_to(128,240)
        ctx.stroke()

        surface.write_to_png(file)

    def circle(self, file):
        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.arc(128,128,100,0,2*math.pi)

        ctx.stroke()

        surface.write_to_png(file)

    def square(self, file):
        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.set_line_width(10)
        ctx.rectangle(15,15,227,227)

        ctx.stroke()

        surface.write_to_png(file)
  
    def smiling_face(self, file):

        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill()

        # Face
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(6)
        ctx.arc(128, 128, 100, 0, 2*math.pi)
        ctx.stroke()

        # Olho esquerdo
        ctx.arc(90, 100, 10, 0, 2*math.pi)
        ctx.fill()

        # Olho direito
        ctx.arc(165, 100, 10, 0, 2*math.pi)
        ctx.fill()

        # Boca
        ctx.set_line_width(6)
        ctx.arc(128, 140, 50, math.pi/6, 5*math.pi/6)
        ctx.stroke()

        surface.write_to_png(file)


def main():
    saida = Saidas()
    saida.vertical_line(os.path.join(OUTPUT_DIR, "vert_line.png"))
    saida.horizontal_line(os.path.join(OUTPUT_DIR, "hori_line.png"))
    saida.cross_lines(os.path.join(OUTPUT_DIR, "cross_lines.png"))
    saida.circle(os.path.join(OUTPUT_DIR, "circle.png"))
    saida.square(os.path.join(OUTPUT_DIR, "square.png"))
    saida.smiling_face(os.path.join(OUTPUT_DIR, "emoji.png"))

if __name__ == "__main__":
    main()
