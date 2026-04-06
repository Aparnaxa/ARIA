import yfinance as yf

def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    return round(hist['Close'].iloc[-1], 2)

def get_summary(ticker):
    stock = yf.Ticker(ticker)
    hist  = stock.history(period="1d")
    info  = stock.info
    return {
        "ticker":   ticker,
        "price":    round(hist['Close'].iloc[-1], 2),
        "pe_ratio": info.get("trailingPE", "N/A"),
        "52w_high": info.get("fiftyTwoWeekHigh", "N/A"),
        "52w_low":  info.get("fiftyTwoWeekLow", "N/A"),
        "volume":   info.get("volume", "N/A")
    }