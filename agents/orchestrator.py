from agents.quant_agent import QuantAgent
from agents.sentiment_agent import SentimentAgent
from agents.trend_agent import TrendAgent
from agents.risk_guardian import RiskGuardian
from core.debate_engine import DebateEngine
from data.indicators import get_indicators

class Orchestrator:
    def __init__(self):
        self.quant     = QuantAgent()
        self.sentiment = SentimentAgent()
        self.trend     = TrendAgent()
        self.risk      = RiskGuardian()
        self.debate    = DebateEngine()
        self.portfolio = {"cash": 100000, "holdings": {}}

    def run(self, ticker: str) -> dict:
        # Step 1: Get market data
        data = get_indicators(ticker)

        # Step 2: All agents analyze
        q = self.quant.analyze(data)
        s = self.sentiment.analyze(ticker)
        t = self.trend.analyze(data["hist_data"], data["price"])

        # Step 3: Risk Guardian evaluates
        proposed = {"ticker": ticker, "signal": q.get("signal", "HOLD")}
        r = self.risk.evaluate([q, s, t], self.portfolio, proposed)

        # Step 4: Debate engine decides
        result = self.debate.run_debate(q, s, t, r)
        result["ticker"]     = ticker
        result["price"]      = data["price"]
        result["indicators"] = {
            k: v for k, v in data.items() if k != "hist_data"
        }

        return result