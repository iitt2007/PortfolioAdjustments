import data
import riskcalculation
import portfolio

def main():
    # Prompt the user for inputs
    file_name = input("Enter the file name: ")

    # Read the data from the CSV file
    data_df = data.read_csv(file_name)

    # Extract equity prices
    equity_prices = data.extract_equities(data_df)

    # Extract bond details
    bond_names = data.extract_bonds(data_df)

    # Adjust equity prices
    adjusted_prices = data.adjust_equity_prices(equity_prices)

    # Calculate risk metrics
    risk_calculator = riskcalculation.RiskCalculator(data_df)
    risk_metrics = risk_calculator.calculate_portfolio_risk()

    # Set up optimization problem and solve for optimal weights
    portfolio_data = {
        'returns': data_df['Returns'],
        'cov_matrix': data_df['Covariance Matrix'],
        'weights': [0.2, 0.3, 0.5],  # Placeholder weights, replace with actual weights
        'constraints': []  # Placeholder constraints, add any additional constraints
    }
    portfolio_optimizer = portfolio.PortfolioOptimizer(portfolio_data)
    optimal_weights = portfolio_optimizer.solve_optimization_problem()

    # Suggest weight adjustments
    suggested_weights = portfolio_optimizer.suggest_weight_adjustments(optimal_weights, risk_metrics)

    # Display the output
    print("Adjusted Portfolio Weights:")
    for symbol, weight in suggested_weights.items():
        print(f"{symbol}: {weight}")

    # Provide options for further actions or adjustments
    # ...

if __name__ == "__main__":
    main()
