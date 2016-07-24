from Model.comparators import string_cmp_fn
from Model.comparators import num_cmp_fn

excel_mapping = {
    'Email':('B', None),
    'First Name': ('C', None),
    'Last Name': ('D', None),
    'Pre Profession':('F', string_cmp_fn(20)),
    'Major(s)':('G', string_cmp_fn(16)),
    'Minor(s)':('H', string_cmp_fn(1)),
    'Region':('I', string_cmp_fn(1)),
    'Hometown':('J', string_cmp_fn(1)),
    'Preference: Same Major': ('K', num_cmp_fn(4)),
    'Preference: Advising Style':('L', num_cmp_fn(3)),
    'Preference: Watching Movies':('M', num_cmp_fn(1)),
    'Preference: Eating Together':('N', num_cmp_fn(1)),
    'Preference: Study Sessions': ('O', num_cmp_fn(1)),
    'Preference: Sports':('P', num_cmp_fn(1)),
    'Preference: Staying In':('Q', num_cmp_fn(1)),
    'Preference: Going Downtown':('R', num_cmp_fn(1)),
    'Preference: Contact': ('S', string_cmp_fn(1)),
    'Preference: Weekend':('T', string_cmp_fn(1)),
    'Preference: Sudden Event':('U', string_cmp_fn(1)),
    'Preference: Personality1':('V', num_cmp_fn(1)),
    'Preference: Personality2':('W',num_cmp_fn(1)),
    'Preference: Personality3':('X',num_cmp_fn(1)),
    'Preference: Personality4':('Y',num_cmp_fn(1)),
    'Preference: Personality5':('Z',num_cmp_fn(1)),
    'Preference: Personality6':('AA',num_cmp_fn(1)),
    'Preference: Personality7':('AB',num_cmp_fn(1)),
    'Preference: Personality8':('AC',num_cmp_fn(1))
}