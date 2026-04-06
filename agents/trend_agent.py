from agents.base_agent import BaseAgent

SYSTEM = """You are a price trend and momentum analyst.
Analyze recent price action and volume to detect trends and patterns.
Always respond ONLY in this exact JSON with no extra text:
{
  "signal": "BUY or SELL or HOLD",
  "confidence": <0-100>,
  "trend": "UPTREND or DOWNTREND or SIDEWAYS",
  "reasoning": "<2-3 sentence explanation>",
  "pattern": "<detected chart pattern if any, or None>"
}"""

class TrendAgent(BaseAgent):
    def __init__(self):
        super().__init__("Trend Agent", SYSTEM)

    def analyze(self, hist_data: dict, price: float) -> dict:
        return self.run(
            f"Current price: {price}. Recent price/volume data: {hist_data}"
        )