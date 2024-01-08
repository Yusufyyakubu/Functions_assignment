def build_profile(first_name, last_name, **additional_info):
    """Build a user profile with the provided information."""
    profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    profile.update(additional_info)
    return profile
my_profile = build_profile(
    first_name='Yusuf',
    last_name='Yakubu',
    age=50,
    occupation='Data scientist',
    interests=['Research', 'Sleeping', 'Cooking']
)
print("My Profile:")
print(my_profile)