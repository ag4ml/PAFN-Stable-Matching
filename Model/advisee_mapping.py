from Model.comparators import string_cmp_fn
from Model.comparators import num_cmp_fn
import collections

excel_mapping = {
    'Email': ('C', None),
    'Name': ('B', None),
    'Pre Profession': ('T', string_cmp_fn(20)),
    'Major(s)':('F',string_cmp_fn(16)),
    'Minor(s)':('U', string_cmp_fn(1)),
    'Region':('H', string_cmp_fn(1)),
    'Hometown':('I', string_cmp_fn(1)),
    'Preference: Same Major': ('P', num_cmp_fn(4)),
    'Preference: Advising Style':('Q', num_cmp_fn(3)),
    'Preference: Watching Movies':('J', num_cmp_fn(1)),
    'Preference: Eating Together':('K', num_cmp_fn(1)),
    'Preference: Study Sessions': ('L', num_cmp_fn(1)),
    'Preference: Sports':('M', num_cmp_fn(1)),
    'Preference: Staying In':('N', num_cmp_fn(1)),
    'Preference: Going Downtown':('O', num_cmp_fn(1)),
    'Preference: Contact': ('R', string_cmp_fn(1)),
    'Preference: Weekend':('AD', string_cmp_fn(1)),
    'Preference: Sudden Event':('AE', string_cmp_fn(1)),
    'Preference: Personality1':('V', num_cmp_fn(1)),
    'Preference: Personality2':('W', num_cmp_fn(1)),
    'Preference: Personality3':('X', num_cmp_fn(1)),
    'Preference: Personality4':('Y', num_cmp_fn(1)),
    'Preference: Personality5':('Z', num_cmp_fn(1)),
    'Preference: Personality6':('AA', num_cmp_fn(1)),
    'Preference: Personality7':('AB', num_cmp_fn(1)),
    'Preference: Personality8':('AC', num_cmp_fn(1)),
    'Rank1':('AF', None),
    'Rank2':('AG', None),
    'Rank3':('AH', None),
    'Rank4':('AI', None),
    'Rank5':('AJ', None)
}

excel_display_mapping = [
    ('Name', ('B', None)),
    ('Nickname', ('C', None)),
    ('Email', ('D', None)),
    ('School',('G', None)),
    ('Ethnicity', ('I', None)),
    ('Region', ('J', None)),
    ('Hometown', ('K', None)),
    ('Anticipated Major(s)', ('H', None)),
    ('Pre-X', ('AA', None)),
    ('Funnest fact', ('L', None)),
    ('Favorite TV Shows/Movies', ('M', None)),
    ('Most Nervous About', ('N', None)),
    ('My Advisor Should Know', ('O', None)),
    ('Want To Be Involved In', ('P', None)),
    ('Hobbies And Interests', ('Z', None))
]
excel_display_ordered = collections.OrderedDict(excel_display_mapping)