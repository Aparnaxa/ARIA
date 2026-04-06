class DebateEngine:
    WEIGHTS = {
        "Quant Agent":     0.35,
        "Sentiment Agent": 0.25,
        "Trend Agent":     0.40,
    }

    def run_debate(self, quant, sentiment, trend, risk) -> dict:
        signals = {
            "Quant Agent":     quant,
            "Sentiment Agent": sentiment,
            "Trend Agent":     trend,
        }

        # Weighted vote
        scores = {"BUY": 0.0, "SELL": 0.0, "HOLD": 0.0}
        for agent, result in signals.items():
            sig  = result.get("signal", "HOLD")
            conf = result.get("confidence", 50) / 100
            if sig in scores:
                scores[sig] += self.WEIGHTS[agent] * conf

        majority   = max(scores, key=scores.get)
        total      = sum(scores.values()) or 1
        confidence = round((scores[majority] / total) * 100)

        # Risk Guardian veto
        vetoed = risk.get("veto", False)
        if vetoed:
            final_signal = "HOLD"
            final_reason = f"VETOED by Risk Guardian: {risk.get('reasoning','')}"
        else:
            final_signal = majority
            final_reason = f"Consensus: {majority} with {confidence}% confidence"

        return {
            "final_signal":    final_signal,
            "confidence":      confidence,
            "scores":          scores,
            "vetoed":          vetoed,
            "risk_level":      risk.get("risk_level", "MEDIUM"),
            "final_reasoning": final_reason,
            "agent_signals":   signals,
            "risk_analysis":   risk,
        }