from model.ui_models.membership import MembershipPlan

def get_membership_plans_list():
    membership_plans_list = [
        ("FULL TIME","Work full time out of a Beagles Loft","20","Preferred access to learning tracks by experts","Experts, community members help improving daily work","Access to all events at a Beagles Loft"),
        ("FLEX","Flexible access to a Beagles Loft","80","Access to open learning tracks by experts","Flexible access to experts and community members","Flexible access to open  events at a Loft")
    ]
    return membership_plans_list

class Memberships():
    @classmethod
    def get_memberships(self):
        ret_val = []
        membership_plans = get_membership_plans_list()
        for membership_plan in membership_plans:
            m = MembershipPlan(membership_plan[0], membership_plan[1], membership_plan[2], membership_plan[3], membership_plan[4], membership_plan[5])
            ret_val.append(m)
        return ret_val