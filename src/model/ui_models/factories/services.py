from model.ui_models.service import Service

class Services():
    @classmethod
    def get_services(self, services):
        ret_val = []
        for service in services:
            s = Service(service[0], service[1], service[2], service[3])
            ret_val.append(s)
        return ret_val