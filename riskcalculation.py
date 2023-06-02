import riskfolio as rp

class RiskCalculator:
    def __init__(self, portfolio_data):
        self.portfolio_data = portfolio_data

    def calculate_standard_deviation(self):
        returns = self.portfolio_data['returns']
        return rp.annualized_volatility(returns, scale=252)

    def calculate_beta(self, market_returns):
        returns = self.portfolio_data['returns']
        return rp.beta(returns, market_returns)

    def calculate_var(self, confidence_level):
        returns = self.portfolio_data['returns']
        return rp.var(returns, alpha=1 - confidence_level, scale=252)

    def calculate_cvar(self, confidence_level):
        returns = self.portfolio_data['returns']
        return rp.cvar(returns, alpha=1 - confidence_level, scale=252)

    def calculate_sharpe_ratio(self, risk_free_rate):
        returns = self.portfolio_data['returns']
        return rp.sharpe_ratio(returns, risk_free_rate, scale=252)

    def calculate_max_drawdown(self):
        returns = self.portfolio_data['returns']
        return rp.max_drawdown(returns)
