class Advisor:
    def __init__(self, props, advisor_name, email, id):
        self.properties = props
        self.name = advisor_name
        self.id = id
        self.email = email
        self.pairings = []
        self.quota = 5

    def rate_against(self, advisee):
        total_score = 0
        for property_name, property in self.properties:
            advisor_val = property[0]
            advisee_val = advisee.properties[property_name][0]
            total_score += property[1](advisor_val, advisee_val)
        return total_score

    def unmatch_unqualified(self):
        #rate everyone assigned
        for i in range(0, len(self.pairings)):
            advisee_obj = self.pairings[i][0]
            advisee_rating = self.rate_against(advisee_obj)
            advisee_obj.matched = (True, self.name)
            self.pairings[i] = (advisee_obj, advisee_rating)
        #reverse sort
        self.pairings = sorted(self.pairings, key=lambda x: x[1], reverse=True)
        #keep the best
        if len(self.pairings) > self.quota:
            for i in range(self.quota, len(self.pairings)):
                advisee_obj = self.pairings[i][0]
                advisee_obj.matched = (False, None)
            self.pairings = self.pairings[0:self.quota]

    def __repr__(self):
        return "Name: {}\n\tPairings: {}".format(self.name, ",".join([pairing[0].name for pairing in self.pairings]))
