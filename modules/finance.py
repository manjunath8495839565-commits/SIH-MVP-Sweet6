# finance.py
"""Finance module.
Provides functions to calculate financial metrics for a business plan.
"""

def calculate_roi(investment: float, returns: float) -> float:
    """Return on Investment = (returns - investment) / investment.
    Returns 0 if investment is zero.
    """
    if investment == 0:
        return 0.0
    return (returns - investment) / investment

def break_even_point(fixed_costs: float, variable_cost_per_unit: float, price_per_unit: float) -> float:
    """Calculate break-even quantity.
    Returns None if price_per_unit <= variable_cost_per_unit.
    """
    margin = price_per_unit - variable_cost_per_unit
    if margin <= 0:
        return None
    return fixed_costs / margin
