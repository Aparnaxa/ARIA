from agents.base_agent import BaseAgent

SYSTEM = """You are a quantitative trading analyst specializing in
technical indicators. Analyze RSI, MACD, and Bollinger Bands data.
RSI > 70 = overbought (bearish), RSI < 30 = oversold (bullish).
MACD > signal line = bullish momentum.
Price near BB lower = potential bounce, near BB upper = potential drop.
Always respond ONLY in this exact JSON with no extra text:
{
  "signal": "BUY or SELL or HOLD",
  "confidence": <0-100>,
  "reasoning": "<2-3 sentence explanation>",
  "key_indicator": "<which indicator drove your decision>"
}"""

class QuantAgent(BaseAgent):
    def __init__(self):
        super().__init__("Quant Agent", SYSTEM)

    def analyze(self, indicators: dict) -> dict:
        return self.run(f"Analyze these indicators: {indicators}")