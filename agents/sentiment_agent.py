from agents.base_agent import BaseAgent

SYSTEM = """You are a market sentiment analyst. Given a stock ticker,
assess the likely market mood and its price impact based on your knowledge.
Always respond ONLY in this exact JSON with no extra text:
{
  "signal": "BUY or SELL or HOLD",
  "confidence": <0-100>,
  "sentiment": "BULLISH or BEARISH or NEUTRAL",
  "reasoning": "<2-3 sentence explanation>",
  "key_headline": "<a plausible recent theme for this stock>"
}"""

class SentimentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Sentiment Agent", SYSTEM)

    def analyze(self, ticker: str) -> dict:
        return self.run(
            f"Analyze market sentiment for stock ticker: {ticker}"
        )