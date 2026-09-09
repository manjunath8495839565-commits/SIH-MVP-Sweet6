# recommender.py
"""Recommender module.
Provides functions to match users with suitable business ideas based on their profile and preferences.
"""

def match_user_to_business(user_profile: dict, business_catalog: list) -> dict:
    """Return the best matching business from the catalog.
    Placeholder implementation: returns the first business that matches the user's category.
    """
    user_category = user_profile.get("category")
    for biz in business_catalog:
        if biz.get("category") == user_category:
            return biz
    return business_catalog[0] if business_catalog else {}
