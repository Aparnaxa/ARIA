from agents.base_agent import BaseAgent

SYSTEM = """You are a Risk Guardian — your sole job is to PROTECT
the portfolio from excessive risk. Be conservative.
Consider portfolio concentration, volatility, and position sizing.
You have VETO POWER over any trade.
Always respond ONLY in this exact JSON with no extra text:
{
  "veto": <true or false>,
  "risk_level": "LOW or MEDIUM or HIGH or CRITICAL",
  "confidence": <0-100>,
  "reasoning": "<2-3 sentence explanation>",
  "max_position_pct": <max % of portfolio to risk, 0-20>
}"""

class RiskGuardian(BaseAgent):
    def __init__(self):
        super().__init__("Risk Guardian", SYSTEM)

    def evaluate(self, signals: list,
                 portfolio: dict, proposed_trade: dict) -> dict:
        return self.run(
            f"Agent signals: {signals}\n"
            f"Portfolio state: {portfolio}\n"
            f"Proposed trade: {proposed_trade}"
        )