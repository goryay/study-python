def build_profile(first, last, **profile):
    profile['first_name'] = first
    profile['last_name'] = last
    return profile


user_profile = build_profile('ilya', 'goryaynov', location='moscow', field='programming')

print(user_profile)
