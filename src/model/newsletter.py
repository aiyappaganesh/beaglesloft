from google.appengine.ext import db

date_format = '%b. %d %Y'
time_format = "%I:%M%p"

class Newsletter(db.Model):
    date_time = db.DateTimeProperty()
    link = db.StringProperty(indexed=False)
    snapshot = db.StringProperty(indexed=False)

    def update(self, link, snapshot):
        if link:
            self.link = link
        if snapshot:
            self.snapshot = snapshot
        self.put()

    def json(self):
        newsletter_json = dict()
        newsletter_json['date'] = (self.date_time).strftime(date_format)
        newsletter_json['time'] = "%s"%((self.date_time).strftime(time_format))
        newsletter_json['link'] = self.link
        newsletter_json['snapshot'] = self.snapshot
        return newsletter_json

    @staticmethod
    def get_newsletters(type=None):
        newsletters = []
        for newsletter in Newsletter.all().order('-date_time'):
            newsletters.append(newsletter.json())
        return newsletters

    @staticmethod
    def get_paged_newsletters(type=None):
        newsletters = {}
        newsletters_temp = []
        for newsletter in Newsletter.all().order('-date_time'):
            newsletters_temp.append(newsletter.json())
        if newsletters_temp:
            counter = 0
            for newsletter in newsletters_temp:
                if not counter/3 in newsletters:
                    newsletters[counter/3] = []
                newsletters[counter/3].append(newsletter)
                counter+=1
        return newsletters