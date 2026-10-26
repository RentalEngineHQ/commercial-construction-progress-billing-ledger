# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(original_basis, recovery_period, rate=0.10):
    adjusted_capital_value = float(original_basis)
    calculated_ytd_depreciation = adjusted_capital_value * float(rate)
    net_terminal_book_worth = adjusted_capital_value - calculated_ytd_depreciation
    return [adjusted_capital_value, calculated_ytd_depreciation, net_terminal_book_worth]
