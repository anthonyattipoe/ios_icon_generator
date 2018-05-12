import os
from PIL import Image
from resizeimage import resizeimage


def resize(pixel_size, icon_extension, magnitude):
	dir_path = os.path.dirname(os.path.realpath(__file__)) + "/icon_bundle"
	if not os.path.exists(dir_path): os.makedirs(dir_path)
	fd_img = open('image.png', 'r')
	img = Image.open(fd_img)
	img = resizeimage.resize_width(img, pixel_size)
	img.save(dir_path+'/Icon-%d%s.png' %(icon_extension,magnitude), img.format)
	fd_img.close()


def generate_iphone_icons():
	iphone_sizes = [20, 29, 40, 60]
	for pixel_size in iphone_sizes:
		resize(pixel_size, pixel_size, "")
	for pixel_size in iphone_sizes:
		resize(pixel_size*2, pixel_size, "@2x")
	for pixel_size in iphone_sizes:
		resize(pixel_size*3, pixel_size, "@3x")


def generate_ipad_icons():
	ipad_sizes = [76, 83.5]
	for pixel_size in ipad_sizes:
		resize(pixel_size, pixel_size, "")
	for pixel_size in ipad_sizes:
		resize(pixel_size*2, pixel_size, "@2x")
	for pixel_size in ipad_sizes:
		resize(pixel_size*3, pixel_size, "@3x")


def generate_watch_icons():
	watch_sizes = [24, 27.5, 86, 98]
	for pixel_size in watch_sizes:
		resize(pixel_size, pixel_size, "")
	for pixel_size in watch_sizes:
		resize(pixel_size*2, pixel_size, "@2x")
	for pixel_size in watch_sizes:
		resize(pixel_size*3, pixel_size, "@3x")


def generate_mac_icons():
	mac_sizes = [16, 32, 128, 256, 512]
	for pixel_size in  mac_sizes:
		resize(pixel_size, pixel_size, "")
	for pixel_size in mac_sizes:
		resize(pixel_size*2, pixel_size, "@2x")
	for pixel_size in mac_sizes:
		resize(pixel_size*3, pixel_size, "@3x")


def main():
	generate_iphone_icons()
	generate_ipad_icons()
	generate_watch_icons()
	generate_mac_icons()


if __name__ == "__main__":
	main()