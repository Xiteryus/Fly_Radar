from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class LEDMatrixBase(SampleBase):
    def __init__(self, *args, **kwargs):
        super(LEDMatrixBase, self).__init__(*args, **kwargs)

    def init_matrix(self, rows=32, cols=64, gpio_mapping="regular"):
        options = RGBMatrixOptions()
        options.rows = rows
        options.cols = cols
        options.gpio_mapping = gpio_mapping
        self.matrix = RGBMatrix(options=options)
        return self.matrix
