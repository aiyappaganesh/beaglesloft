class Donut():
    def __init__(self, size, cutout, title, segments, container_color, empty_color, img=None):
        self.size = size
        self.cutout = cutout
        self.container_side = size * cutout
        self.container_pos = (size / 2.0) - (self.container_side / 2.0)
        self.title = title
        self.segments = segments
        self.total = sum([segment.score for segment in segments])
        self.max = max([segment.score for segment in segments])
        self.font_size = self.container_side * 0.4
        self.container_color = container_color
        self.empty_color = empty_color
        self.img = img

class DonutSegment():
    def __init__(self, score, color):
        self.score = score
        self.color = color