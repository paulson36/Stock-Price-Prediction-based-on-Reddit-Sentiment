# -*- coding: utf-8 -*-
"""models_evals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kw3uKjekPoCnbdSSqo0QCQd2DngDbG7o
"""

# Dictionary to store model results
results = {}

# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Lasso (L1)': Lasso(alpha=0.1),
    'Ridge (L2)': Ridge(alpha=0.1),
    'SVR': SVR(),
    'Random Forest': RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.1,
        random_state=42
    )
}

# Helper function to plot and encode line plot as base64
def plot_actual_vs_predicted(val_y_inv, y_pred_inv, model_name):
    plt.figure(figsize=(8, 5))
    plt.plot(val_y_inv, label='Actual', color='blue', alpha=0.7)
    plt.plot(y_pred_inv, label='Predicted', color='orange', alpha=0.7)
    plt.title(f'{model_name}: Actual vs Predicted')
    plt.xlabel('Sample Index')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode plot as base64 string
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

# Train and evaluate ML models
plots = {}
for model_name, model in models.items():
    model.fit(train_X, train_y)  # Train the model
    y_pred = model.predict(val_X)  # Predict

    # Inverse transform predictions and validation targets
    y_pred_inv = scaler_y.inverse_transform(y_pred.reshape(-1, 1)).flatten()
    val_y_inv = scaler_y.inverse_transform(val_y.reshape(-1, 1)).flatten()

    # Calculate metrics
    mae = mean_absolute_error(val_y_inv, y_pred_inv)
    mape = mean_absolute_percentage_error(val_y_inv, y_pred_inv)
    r2 = r2_score(val_y_inv, y_pred_inv)

    # Generate line plot
    plot_base64 = plot_actual_vs_predicted(val_y_inv, y_pred_inv, model_name)
    plots[model_name] = plot_base64

    # Store results
    results[model_name] = {'MAE': mae, 'MAPE': mape, 'R2': r2}

# Convert results to DataFrame
results_df = pd.DataFrame(results).T

# Add plots as a column in the DataFrame
results_df['Actual vs Predicted Plot'] = pd.Series(plots)

# Display DataFrame
for model_name, row in results_df.iterrows():
    print(f"\nModel: {model_name}")
    print(row.drop('Actual vs Predicted Plot'))  # Print metrics
    # Display the line plot in text-based interface
    display_html = f'<img src="data:image/png;base64,{row["Actual vs Predicted Plot"]}" />'
    display(HTML(display_html))