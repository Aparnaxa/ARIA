import ta
import yfinance as yf

def get_indicators(ticker):
    df = yf.Ticker(ticker).history(period="3mo")

    # RSI
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()

    # MACD
    macd = ta.trend.MACD(df['Close'])
    df['macd']        = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(df['Close'])
    df['bb_upper'] = bb.bollinger_hband()
    df['bb_lower'] = bb.bollinger_lband()

    latest = df.iloc[-1]
    return {
        "price":       round(float(latest['Close']), 2),
        "rsi":         round(float(latest['rsi']), 2),
        "macd":        round(float(latest['macd']), 4),
        "macd_signal": round(float(latest['macd_signal']), 4),
        "bb_upper":    round(float(latest['bb_upper']), 2),
        "bb_lower":    round(float(latest['bb_lower']), 2),
        "volume":      int(latest['Volume']),
        "hist_data":   df[['Close', 'Volume']].tail(30).to_dict()
    }