"""
Chess-Inspired Explainable AI for Supply Chain Forecasting
Main entry point for running the complete pipeline
"""

import os
import numpy as np

from src.scenarios import get_all_scenarios
from src.forecasting import compute_stats, fit_arima, recommend_adjustment
from src.classification import classify_motif, generate_explanations
from src.analysis import simulate_user_study, run_full_analysis, print_results_table
from src.visualization import (
    plot_motif_distribution,
    plot_scenario_mapping,
    plot_user_study_results,
    plot_effect_sizes,
    plot_taxonomy_card,
    plot_forecast_example,
    plot_chess_motifs_board
)


def process_scenario(scenario: dict) -> dict:
    """
    Process a single scenario through the complete pipeline.
    
    Args:
        scenario: Scenario dictionary with id, product, context, data
        
    Returns:
        Complete result dictionary
    """
    # Statistical analysis
    stats = compute_stats(scenario['data'])
    
    # ARIMA forecasting
    arima_result = fit_arima(scenario['data'])
    
    # Generate recommendation
    recommendation = recommend_adjustment(stats, arima_result['forecast'])
    
    # Classify motif
    motif_result = classify_motif(stats, recommendation['adjustment'], scenario['context'])
    
    # Generate explanations
    explanations = generate_explanations(
        motif_result, stats, recommendation['adjustment'], scenario['product']
    )
    
    # Apply adjustment to forecast
    adjusted_forecast = arima_result['forecast'] * (1 + recommendation['adjustment'])
    
    return {
        'id': scenario['id'],
        'product': scenario['product'],
        'context': scenario['context'],
        'stats': stats,
        'forecast': adjusted_forecast,
        'adjustment': recommendation['adjustment'],
        'confidence': recommendation['confidence'],
        'motif': motif_result['motif'],
        'motif_name': motif_result['name'],
        'standard': explanations['standard'],
        'chess': explanations['chess']
    }


def run_all_scenarios():
    """Process all scenarios and return results."""
    scenarios = get_all_scenarios()
    results = []
    
    for scenario in scenarios:
        result = process_scenario(scenario)
        results.append(result)
    
    return results


def print_results(results: list):
    """Print formatted results for all scenarios."""
    print("=" * 80)
    print("CHESS-INSPIRED XAI FOR SUPPLY CHAIN FORECASTING")
    print("=" * 80)
    print()
    
    for r in results:
        print(f"[{r['id']}] {r['product']}")
        print(f"    Context: {r['context'][:60]}...")
        print(f"    Motif: {r['motif_name']}")
        print(f"    Adjustment: {r['adjustment']*100:+.1f}%")
        print(f"    Standard: {r['standard'][:70]}...")
        print(f"    Chess: {r['chess'][:70]}...")
        print()
    
    # Motif distribution
    motif_counts = {}
    for r in results:
        m = r['motif']
        motif_counts[m] = motif_counts.get(m, 0) + 1
    
    print("-" * 80)
    print("MOTIF DISTRIBUTION")
    print("-" * 80)
    for motif, count in sorted(motif_counts.items()):
        print(f"    {motif.upper():<15} {count} scenario(s)")
    print(f"    {'TOTAL':<15} {len(results)} scenarios, {len(motif_counts)} unique motifs")
    print()


def generate_all_figures(results: list, analysis_results: dict, output_dir: str = 'figures'):
    """Generate all publication-ready figures."""
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating figures...")
    
    # Figure 1: Motif Distribution
    plot_motif_distribution(results, f'{output_dir}/figure1_motif_distribution.png')
    print("  ✓ Figure 1: Motif Distribution")
    
    # Figure 2: Scenario Mapping
    plot_scenario_mapping(results, f'{output_dir}/figure2_scenario_mapping.png')
    print("  ✓ Figure 2: Scenario Mapping")
    
    # Figure 3: User Study Results
    plot_user_study_results(analysis_results, f'{output_dir}/figure3_user_study_results.png')
    print("  ✓ Figure 3: User Study Results")
    
    # Figure 4: Effect Sizes
    plot_effect_sizes(analysis_results, f'{output_dir}/figure4_effect_sizes.png')
    print("  ✓ Figure 4: Effect Sizes")
    
    # Figure 5: Taxonomy Card
    plot_taxonomy_card(f'{output_dir}/figure5_taxonomy.png')
    print("  ✓ Figure 5: Taxonomy Card")
    
    # Figure 6: Forecast Example
    scenarios = get_all_scenarios()
    plot_forecast_example(
        scenarios[0]['data'],
        results[0]['forecast'],
        results[0]['motif'],
        results[0]['chess'],
        results[0]['product'],
        f'{output_dir}/figure6_forecast_example.png'
    )
    print("  ✓ Figure 6: Forecast Example")
    
    # Chess boards
    plot_chess_motifs_board(f'{output_dir}/chess_motifs_boards.png')
    print("  ✓ Chess Motifs Board")
    
    print(f"\nAll figures saved to '{output_dir}/'")


def main():
    """Main entry point."""
    print()
    
    # 1. Process all scenarios
    results = run_all_scenarios()
    print_results(results)
    
    # 2. Run user study analysis (simulated)
    print("=" * 80)
    print("USER STUDY ANALYSIS (Simulated Data)")
    print("=" * 80)
    
    study_data = simulate_user_study(n_per_group=15)
    analysis_results = run_full_analysis(study_data)
    print(print_results_table(analysis_results))
    print()
    
    # 3. Generate figures
    generate_all_figures(results, analysis_results)
    
    print()
    print("=" * 80)
    print("COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
