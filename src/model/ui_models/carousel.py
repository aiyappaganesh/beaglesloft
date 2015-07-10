class Carousel():
    def __init__(self, id, classes, slides, slide_classes="", indicator_classes="", indicators=True, controls=True, data_interval=4000, data_pause=False):
        self.id = id
        self.classes = classes
        self.slides = slides
        self.slide_classes = slide_classes
        self.indicator_classes = indicator_classes
        self.indicators = indicators
        self.controls = controls
        self.data_interval = data_interval
        self.data_pause = data_pause