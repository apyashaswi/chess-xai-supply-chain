# ♟️ Chess-Inspired Explainable AI for Supply Chain Forecasting

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Translating AI recommendations into strategic mental models using chess concepts

## 🎯 Overview

This project introduces a novel framework that maps **8 chess strategic concepts** to supply chain decision patterns, making AI demand forecasting explanations more intuitive and trustworthy.

### The Problem

Traditional AI explanations like *"Increase forecast 12% due to positive trend coefficient"* don't match how practitioners think about inventory decisions.

### The Solution

Chess-framed explanations like *"[TEMPO] Build inventory ahead of demand curve — like advancing pawns before an attack"* leverage universal strategic concepts that people already understand.

## 📊 Pilot Study Results

| Measure | Standard | Chess-Framed | Effect Size |
|---------|----------|--------------|-------------|
| Comprehension | 62.1% | 70.1% | d = 0.80* |
| Trust | 4.05 | 5.12 | d = 1.33* |
| Satisfaction | 4.54 | 5.38 | d = 0.86* |

*All effects statistically significant (p < .05) with large effect sizes (d ≥ 0.8)*

## ♟️ The Chess Motif Taxonomy

| Motif | Chess Meaning | Supply Chain Application |
|-------|---------------|--------------------------|
| **TEMPO** | Gaining move advantage | Order early to gain lead time |
| **FORK** | Attack two pieces at once | One action achieves multiple benefits |
| **PROPHYLAXIS** | Prevent future threats | Preemptive risk mitigation |
| **ZUGZWANG** | Any move worsens position | Forced action when all options are bad |
| **DEVELOPMENT** | Activate pieces for future | Build capabilities for flexibility |
| **EXCHANGE** | Trade pieces for advantage | Accept cost for benefit elsewhere |
| **MATERIAL** | Have more valuable pieces | Optimize cost/inventory position |
| **POSITION** | Control key squares | Maintain strategic flexibility |

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/chess-xai-supply-chain.git
cd chess-xai-supply-chain
pip install -r requirements.txt
```

### Run Demo

```bash
python main.py
```

### Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/chess-xai-supply-chain/blob/main/notebooks/chess_xai_demo.ipynb)

## 📁 Repository Structure

```
chess-xai-supply-chain/
├── src/
│   ├── forecasting.py      # ARIMA forecasting pipeline
│   ├── classification.py   # Motif classification logic
│   ├── scenarios.py        # 10 supply chain scenarios
│   ├── analysis.py         # Statistical analysis
│   └── visualization.py    # Publication-ready figures
├── figures/
│   ├── figure1_motif_distribution.png
│   ├── figure2_scenario_mapping.png
│   ├── figure3_user_study_results.png
│   ├── figure4_effect_sizes.png
│   ├── figure5_taxonomy.png
│   ├── figure6_forecast_example.png
│   └── chess_motifs_explained.png
├── notebooks/
│   └── chess_xai_demo.ipynb
├── docs/
│   └── PROJECT_DESCRIPTION.md
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🔧 Technical Architecture

```
Historical Data → Statistical Analysis → ARIMA Forecast → Rule-Based Adjustment → Motif Classification → Dual Explanations
```

### Key Components

1. **Statistical Analysis**: Computes CV, trend, momentum from time series
2. **ARIMA Forecasting**: Auto-selects (p,d,q) parameters for 6-period forecast
3. **Adjustment Logic**: Rule-based recommendations (±20%) based on patterns
4. **Motif Classification**: Context-aware mapping to chess concepts
5. **Explanation Generation**: Produces both standard and chess-framed outputs

## 📈 Example Output

**Scenario**: Premium Organic Pasta with 5% monthly growth

**Standard Explanation**:
> "Forecast suggests 4.8% increase based on positive demand trend and stable variability."

**Chess-Framed Explanation**:
> "[TEMPO] Build inventory ahead of the demand curve. Like advancing pawns before an attack, ordering now gains lead time advantage over the coming growth trend."

## 🧪 Experimental Design

- **Design**: Between-subjects randomized controlled trial
- **Conditions**: Standard vs Chess-framed explanations
- **Sample**: n = 30 (pilot)
- **Measures**: Comprehension (% correct), Trust (1-7), Satisfaction (1-7)
- **Analysis**: Independent t-tests, Cohen's d effect sizes

## 📊 Visualizations

### Motif Distribution
![Motif Distribution](figures/figure1_motif_distribution.png)

### Effect Sizes
![Effect Sizes](figures/figure4_effect_sizes.png)

### Chess Motifs Explained
![Chess Motifs](figures/chess_motifs_explained.png)

## 🛠️ Dependencies

- Python 3.8+
- pandas >= 2.0.0
- numpy >= 1.24.0
- scipy >= 1.10.0
- statsmodels >= 0.14.0
- pmdarima >= 2.0.0
- matplotlib >= 3.7.0

## 📚 References

1. McGrath, T., et al. (2022). Acquisition of chess knowledge in AlphaZero. *PNAS*, 119(47).
2. Kim, B., et al. (2025). Bridging the human-AI knowledge gap. *PNAS*, 122(13).
3. Hoffman, R.R., et al. (2023). Measures for explainable AI. *Frontiers in Computer Science*, 4.

## 📝 Citation

```bibtex
@misc{prasannakumar2024chessxai,
  author = {Prasannakumar, Yashaswi Alur},
  title = {Chess-Inspired Explainable AI for Supply Chain Demand Forecasting},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/yourusername/chess-xai-supply-chain}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Yashaswi Alur Prasannakumar**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

⭐ If you find this project useful, please consider giving it a star!
