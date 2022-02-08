from Canvas import Canvas
from Grammar import Grammar
from Alphabet import Alphabet
from datetime import datetime
from PIL import Image
from PIL import EpsImagePlugin


def draw():
    while True:
        alphabet = Alphabet(7)
        grammar = Grammar(alphabet, 8, 5, 10)

        axiom = grammar.generate_axiom(8)
        print(axiom)
        s = grammar.apply(axiom, 7)
        print(s)

        canvas = Canvas()

        for ch in s:
            symbol = alphabet.dict[ch]
            symbol.execute(canvas)

        canvas.turtle.update()

        ts = canvas.turtle.getscreen()
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        ts.getcanvas().postscript(file=rf'imgs\ps\{date}.ps', width=6000, height=2000, x=-3000, y=-1000)
        img = Image.open(rf'imgs\ps\{date}.ps')
        img = img.convert("RGB")

        datas = img.getdata()

        new_image_data = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                new_image_data.append((0, 0, 0))
            else:
                new_image_data.append(item)

        img.putdata(new_image_data)
        img.save(rf'imgs\jpg\{date}.jpg')


if __name__ == '__main__':
    EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'
    draw()
