import tempfile
from django.test import TestCase
from django.conf import settings
from django.test.utils import override_settings
from django.utils.translation import ugettext_lazy as _
from jssor.models import Slideshow, Slide


SLIDESHOW_TYPES = (
                   ('jssor/full_width_slider.html',_(u'Full width slider')),
                   ('jssor/banner_slider.html',_(u'Banner slider')),
                   ('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
                   )
# models test
class SlideshowTest(TestCase):

    def create_slideshow(self, template_name="full_width_slider.html", title="Slideshow", width=780, height=300):        
        return Slideshow.objects.create(template_name=template_name, title=title, width=width, height=height)

    @override_settings(SLIDESHOW_TYPES=SLIDESHOW_TYPES)
    def test_slideshow_creation(self):
        slideshow = self.create_slideshow()
        self.assertEqual(settings.SLIDESHOW_TYPES, SLIDESHOW_TYPES)
        self.assertTrue(isinstance(slideshow, Slideshow))
        self.assertEqual(slideshow.template_name, "full_width_slider.html")
        self.assertEqual(slideshow.title, "Slideshow")
        self.assertEqual(slideshow.autoplay, False)
        self.assertEqual(slideshow.width, 780)
        self.assertEqual(slideshow.height, 300)
        self.assertEqual(slideshow.__unicode__(), slideshow.title)
        

class SlideTest(TestCase):
    
    def create_slideshow(self, template_name="full_width_slider.html", title="Slideshow", width=780, height=300):
        return Slideshow.objects.create(template_name=template_name, title=title, width=width, height=height)

    def create_slide(self, title='Test slide', slideshow=None, order=10, link='/'):
        self.image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.slideshow = slideshow
        slide = Slide.objects.create(title=title, slideshow=slideshow, order=order, link=link, image=self.image)
        return slide
    
    def test_slide_creation(self):
        slideshow=self.create_slideshow()
        slide=self.create_slide(slideshow=slideshow)
        self.assertTrue(isinstance(slide, Slide))
        self.assertEqual(slide.title, "Test slide")
        self.assertEqual(slide.__unicode__(), "Test slide")
        self.assertEqual(slide.image, self.image)
        self.assertEqual(slide.slideshow, self.slideshow)
        self.assertEqual(slide.order, 10)
        self.assertEqual(slide.link, '/')
        self.assertEqual(str(slide),unicode(slide.title))
        self.assertFalse(slide.link_is_blank)

        
        
    
    
