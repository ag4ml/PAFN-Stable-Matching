class Advisee:
    def __init__(self, props, advisee_name, email, id, ranking):
        self.properties = props
        self.name = advisee_name
        self.email = email
        self.id = id
        self.matched = (False, None)
        self.preferred_ranking = ranking
        self.secondary_ranking=[]
        self.current_favorite = 0

    def get_next_favorite(self):
        return self.preferred_ranking[self.current_favorite] if (self.current_favorite < 5) else self.secondary_ranking[self.current_favorite]

    def rate_against(self, advisor):
        total_score = 0
        for property_name, property in self.properties:
            advisor_val = advisor.properties[property_name][0]
            advisee_val = property[0]
            total_score+= property[1](advisor_val, advisee_val)
        return total_score

    def build_secondary(self, advisor_list):
        for i in range(0, len(advisor_list)):
            advisor_obj = advisor_list[i]
            advisor_rating = self.rate_against(advisor_obj)
            self.secondary_ranking.append((advisor_obj, advisor_rating))
        self.secondary_ranking = sorted(self.secondary_ranking, key= lambda x: x[1], reverse=True)

    def __repr__(self):
        return "Name: {}\n\tMatched to: {}".format(self.name, "No one" if not self.matched[0] else self.matched[1])


