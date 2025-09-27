from .base import LEDMatrixBase

class FillColor(LEDMatrixBase):
    def __init__(self, r, g, b, *args, **kwargs):
        super(FillColor, self).__init__(*args, **kwargs)
        self.r, self.g, self.b = r, g, b

    def run(self):
        matrix = self.matrix
        width, height = matrix.width, matrix.height
        while True:
            for x in range(width):
                for y in range(height):
                    matrix.SetPixel(x, y, self.r, self.g, self.b)

