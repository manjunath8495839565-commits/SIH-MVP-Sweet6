# schemes.py
"""Schemes module.
Provides utilities to select appropriate loan or subsidy schemes based on business criteria.
"""

def select_scheme(business_profile: dict, schemes_list: list) -> dict:
    """Select a suitable scheme.
    Placeholder returns the first scheme that matches the business's category.
    """
    category = business_profile.get("category")
    for scheme in schemes_list:
        if scheme.get("category") == category:
            return scheme
    return schemes_list[0] if schemes_list else {}
