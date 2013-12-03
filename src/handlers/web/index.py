import webapp2
import logging
from handlers.web import WebRequestHandler
import re
from model import Member
from google.appengine.api import mail

reg_b = re.compile(r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino", re.I|re.M)
reg_v = re.compile(r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|le(no|xi)|lg( g|\\/(k|l|u)|50|54|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\\-|your|zeto|zte\\-", re.I|re.M)

class IndexPage(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        template_values['member_keys'] = Member.get_member_keys()
        self.write(self.get_rendered_html(path, template_values), 200)

class TestSpyPage(WebRequestHandler):
    def get(self):
        path = 'testspy.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'	
        self.write(self.get_rendered_html(path, template_values), 200)

class CalendarPage(WebRequestHandler):
    def get(self):
        path = 'calendar.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        self.write(self.get_rendered_html(path, template_values), 200)

class MemberRegistrationPage(WebRequestHandler):
    def get(self):
        path = 'member_registration.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        self.write(self.get_rendered_html(path, template_values), 200)

class MemberAccessPage(WebRequestHandler):
    def get(self):
        path = 'member_access.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        self.write(self.get_rendered_html(path, template_values), 200)

class MemberAccessQuestionPage(WebRequestHandler):
    def get(self):
        path = 'member_access_question.html'
        category = self['category']
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        if category == 'Mathematics':
            template_values['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            template_values['question_id'] = 'M1'
        elif category == 'Science':
            template_values['question'] = 'The Large Hadron Collider (LHC) was built to confirm the existence of which particle?'
            template_values['question_id'] = 'S1'
        elif category == 'Business':
            template_values['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            template_values['question_id'] = 'B1'
        elif category == 'Art':
            template_values['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            template_values['question_id'] = 'A1'
        else:
            template_values['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            template_values['question_id'] = 'O1'
        self.write(self.get_rendered_html(path, template_values), 200)

class AcceptContact(WebRequestHandler):
    def post(self):
        name = self['contact_name']
        from_email = self['contact_email']
        message = self['contact_message']

        to_email = "BeaglesLoft Contact <aiyappa@b-eagles.com>"
        subject = "BeaglesLoft Contact"
        body = """ Name: %s , Email: %s , Message: %s """ % (name, from_email, message)
        mail.send_mail(from_email, to_email, subject, body)
        self.redirect("/")

app = webapp2.WSGIApplication(
    [
        ('/', IndexPage),
        ('/testspy', TestSpyPage),
        ('/calendar', CalendarPage),
        ('/member_registration', MemberRegistrationPage),
        ('/member_access', MemberAccessPage),
        ('/member_access_question', MemberAccessQuestionPage),
        ('/accept_contact', AcceptContact)
    ]
)