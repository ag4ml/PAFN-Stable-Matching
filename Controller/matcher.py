from Model.context import Context

def main():
    data_context = Context()
    stable_match(data_context)
    data_context.print_pairings()

def stable_match(data_context):
    while(data_context.has_unmatched_advisees()):
        unmatched = data_context.get_unmatched_advisees()
        for advisee in unmatched:
            adv_pref = advisee.get_next_favorite()
            adv_pref.pairings.append((advisee, None))
        data_context.unmatch_adv_pairings()

if __name__ == '__main__':
    main()