def build_profile(first_name, last_name, **additional_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in additional_info.items():
        profile[key] = value
    return profile
