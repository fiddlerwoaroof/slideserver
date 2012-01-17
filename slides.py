import os.path
import sys
import yaml
import markdown

def get_filename(package, resource):
   """Get the absolute path to a file inside a given Python package"""
   d = os.path.dirname(sys.modules[package].__file__)
   d = os.path.abspath(d)
   return os.path.join(d, resource)

class RuleSet(object):
	def __init__(self, selector, **styles):
		self.selector = selector
		self.styles = styles

	def __str__(self):
		print self.styles
		styles = ';\n  '.join(': '.join(item) for item in self.styles.items())
		return '''\n%s {\n%s\n}''' % (self.selector, styles)

def read_slides(fil):
	slides = fil.read().split('\n------\n')
	result = []
	for slide in slides:
		slide = slide.split('\n---\n')

		result.append(dict(
			config=yaml.load(slide[0]),
			text=markdown.markdown(slide[1])
		))
	return result

import mako.template
template = mako.template.Template(
	file(
		get_filename('slideserver', 'template.mako')
	).read()
)

def make_slide(slide):
	config = slide['config']
	print config
	text = slide['text']

	attrs = config.get('attrs', {})
	attrs_out = []
	for attr, value in attrs.items():
		attrs_out.append('data-%s="%s"' % (attr, value))
	return template.get_def('slide').render(id='%s' % config['id'], attr=' '.join(attrs_out), text=text), RuleSet('#%s' % config['id'], **config.get('style', {}))

def make_document(slides):
	slides, styles = zip(*slides)
	styles = '\n'.join(
		str(ruleset) for ruleset in styles
	)
	return template.get_def('document').render(style='%s' % styles, slides=slides)

if __name__ == '__main__':
	import argparse
	import twisted.web.resource

	class SlideshowResource(twisted.web.resource.Resource):
		parser = argparse.ArgumentParser()
		parser.add_argument('slideshow', nargs=1)
		parser.add_argument('static_files', nargs=1)
		options = parser.parse_args()
		slideshow = options.slideshow[0]
		static_files = options.static_files[0]

		def render_GET(self, request):
			with file(self.slideshow) as f:
				slideshow = read_slides(f)

			slideshow = [make_slide(slide) for slide in slideshow]

			return make_document(slideshow).encode('utf-8')

	from twisted.internet import reactor
	from twisted.web import static, server
	root = static.File(SlideshowResource.static_files)
	root.putChild('', SlideshowResource())
	import os
	port = int(os.getenv('PORT', 8080))
	reactor.listenTCP(port, server.Site(root))
	reactor.run()


