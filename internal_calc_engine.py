# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(scheduled_value, completed_stored_value, retainage_withholding_rate=0.10):
    total_completed_stored = float(completed_stored_value)
    cash_retainage_held = total_completed_stored * float(retainage_withholding_rate)
    net_billable_balance = total_completed_stored - cash_retainage_held
    return [float(scheduled_value), total_completed_stored, net_billable_balance]
