# Firm capital structure and market inputs
Total_Assets = 100            # Total firm value (Debt + Equity)
Debt = 30                     # Market value of debt
Interest_on_Debt = 0.09       # Cost of debt (pre-tax)
Tax = 0.35                    # Corporate tax rate
Beta = 1.5                    # Equity beta
Market_Premium = 0.10         # Expected market return
Risk_Free_Rate = 0.03         # Risk-free rate


def WACC(
    Total_Assets,
    Debt,
    Interest_on_Debt,
    Tax,
    Beta,
    Market_Premium,
    Risk_Free_Rate
):
    """
    Calculates the Weighted Average Cost of Capital (WACC).

    Parameters:
    Total_Assets (float): Total firm value (Debt + Equity)
    Debt (float): Market value of debt
    Interest_on_Debt (float): Pre-tax cost of debt
    Tax (float): Corporate tax rate
    Beta (float): Equity beta
    Market_Premium (float): Expected market return
    Risk_Free_Rate (float): Risk-free rate

    Returns:
    str: Firm WACC expressed as a percentage
    """

    # Market value of equity
    equity = Total_Assets - Debt

    # Cost of equity using CAPM
    re = Risk_Free_Rate
    ke = re + Beta * (Market_Premium - re)

    # Capital structure weights
    Debt_ratio = Debt / Total_Assets
    Equity_ratio = equity / Total_Assets

    # Weighted Average Cost of Capital formula
    WACC = (
        Interest_on_Debt * (1 - Tax) * Debt_ratio
        + ke * Equity_ratio
    )

    # Convert WACC to percentage format
    WACC_percent = WACC * 100

    return "WACC: {:.2f}%".format(WACC_percent)


# Calculate and print WACC
print(WACC(
    Total_Assets,
    Debt,
    Interest_on_Debt,
    Tax,
    Beta,
    Market_Premium,
    Risk_Free_Rate
))
