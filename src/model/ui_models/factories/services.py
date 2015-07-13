from model.ui_models.service import Service
from model.ui_models.carousel import Carousel
from model.ui_models.image_carousel_slide import Image_Carousel_Slide

lofts = 'lofts'
programs = 'programs'
startups = 'startups'
community = 'community'
events = 'events'

services_list = [lofts, programs, startups, community, events]

def get_images(service):
    images = {
        lofts: ['/assets/img/landing/service_imgs/easychair.jpg','/assets/img/landing/service_imgs/terrace.jpg','/assets/img/landing/service_imgs/sunlight.jpg'],
        programs: ['/assets/img/landing/service_imgs/tb1.jpg','/assets/img/landing/service_imgs/tb2.jpg'],
        startups: ['/assets/img/landing/service_imgs/st1.jpg','/assets/img/landing/service_imgs/st2.jpg', '/assets/img/landing/service_imgs/st3.jpg'],
        community: ['/assets/img/landing/service_imgs/cm1.jpg','/assets/img/landing/service_imgs/cm2.jpg'],
        events: ['/assets/img/landing/service_imgs/ev2.jpg','/assets/img/landing/service_imgs/ev3.jpg', '/assets/img/landing/service_imgs/ev1.jpg']
    }
    return images[service]

def get_images_carousel(id, images, classes=None, slide_classes=None, indicator_classes=None):
    if not classes:
        classes = "service-carousel"
    if not slide_classes:
        slide_classes= "landing-carousel-item"
    if not indicator_classes:
        indicator_classes= "landing-carousel-indicators"
    slides = [Image_Carousel_Slide(img) for img in images]
    carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return carousel

def get_services_list():
    services = [('/assets/img/landing/'+service+'.png','/assets/img/landing/'+service+'_dark.png',service,get_images_carousel('services-'+service,get_images(service))) for service in services_list]
    return services

class Services():
    @classmethod
    def get_services(self):
        ret_val = []
        services = get_services_list()
        for service in services:
            s = Service(service[0], service[1], service[2], service[3])
            ret_val.append(s)
        return ret_val