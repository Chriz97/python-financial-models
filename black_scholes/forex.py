import math
import scipy

# Currency pair quotation
# EUR/USD means:
# - EUR = Foreign currency
# - USD = Home (domestic) currency
quotation = "EUR/USD"  # Right side is the Home currency

# Market inputs
spot_rate = 1.1743          # Current spot exchange rate (EUR/USD)
strike_price = 1.1770       # Strike price of the option
us_1mth = 0.0025            # Domestic (USD) risk-free interest rate (annualized)
eur_1mth = -0.00195         # Foreign (EUR) risk-free interest rate (annualized)
volatility = 0.12           # Annualized volatility of the exchange rate
expiration = 30             # Time to maturity in days
option = "call"             # Option type (currently only call is implemented)


def Black_Scholes_Foreign_Exchange(
    spot_rate,
    strike_price,
    us_1mth,
    eur_1mth,
    volatility,
    expiration
):
    """
    Prices a European FX Call option using the Black-Scholes model.

    Parameters:
    spot_rate (float): Current spot exchange rate
    strike_price (float): Strike price of the option
    us_1mth (float): Domestic risk-free interest rate
    eur_1mth (float): Foreign risk-free interest rate
    volatility (float): Annualized volatility
    expiration (int): Time to maturity in days

    Returns:
    float: Call option price
    """

    # Convert time to maturity from days to years
    t = expiration / 365

    # Black-Scholes d1 term for FX options
    # Includes interest rate differential (domestic - foreign)
    d1 = (
        math.log(spot_rate / strike_price)
        + (us_1mth - eur_1mth + (volatility ** 2) / 2) * t
    )

    # Black-Scholes d2 term
    d2 = d1 - volatility * math.sqrt(t)

    # FX Black-Scholes call option pricing formula
    call = (
        math.e ** (-us_1mth * t)
        * spot_rate
        * scipy.stats.norm.cdf(d1)
        - math.e ** (-eur_1mth * t)
        * strike_price
        * scipy.stats.norm.cdf(d2)
    )

    # Return rounded option price
    return call.round(3)


# Calculate the FX call option price
call_price = Black_Scholes_Foreign_Exchange(
    spot_rate,
    strike_price,
    us_1mth,
    eur_1mth,
    volatility,
    expiration
)

# Output result
print("Call:", call_price)
