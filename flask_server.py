from flask import Flask, url_for
from slides import *
app = Flask(__name__)

slideshow = 'slideshow'

@app.route('/')
def main():
	with file(slideshow) as f:
		sshow = read_slides(f)

	sshow = [make_slide(slide) for slide in sshow]
	return make_document(sshow).encode('utf-8')


if __name__ == '__main__':
	app.run()
