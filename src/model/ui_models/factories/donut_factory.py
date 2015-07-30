from model.ui_models.donut import Donut
class DonutFactory():
	@classmethod
	def get_donuts(cls, size, cutout, donuts, container_color, empty_color):
		ret_val = []
		for donut in donuts:
			d = Donut(size, cutout, donut[0], donut[1], container_color, empty_color, donut[2] if len(donut)>2 else None)
			ret_val.append(d)
		return ret_val