# Fair and Balanced Matching in Bipartite Graphs

## Overview
This project focuses on developing and evaluating fair and balanced matching algorithms for bipartite graphs. Inspired by the Gale-Shapley algorithm, the research aims to ensure fairness and mutual satisfaction between nodes in the graph while evaluating the effectiveness of these matchings through various fairness metrics.

## Contributors
- **Beloslava Malakova**
- **Janis Stepanovs**
- **Jekabs Gritans**

### Key Features
- **Synthetic Data Generation**: Generate datasets representing nodes in a bipartite graph with their preferences.
- **Matching Algorithms**: Implementation of multiple simple algorithms, including:
  - Serial Dictatorship
  - Artificial Cap Deferred Acceptance (ACDA)
  - Stable Matching
- **Fairness Evaluation**: Assessment of matchings based on:
  - Exponential Score Difference
  - Average Difference
  - Weighted Logarithmic Function

---

## Goals
- **Fairness**: Minimize discrepancies in preferences across matches.
- **Balance**: Ensure no bias toward one side of the graph.
- **Scalability**: Handle large bipartite graphs efficiently.

---

## Getting Started

### Prerequisites
- **Python**: Version 3.8+
- **Libraries**:
  - `pandas`
  - `numpy`
  - `math`
---

### Usage

#### 1. Generate Synthetic Data
Run the script to create datasets of students and universities:
```bash
python dataset_creation.py
```
This will generate:
- `synthetic_students.csv`
- `synthetic_universities.csv`

#### 2. Run Matching Algorithms
Execute the script to produce matchings:
```bash
python simple_algorithms.py
```
Results will be saved in the `matchings_results/` folder.

#### 3. Evaluate Matchings
Run the evaluation script to assess the fairness of a specific matching:
```bash
python evalate_matchings.py
```
Specify the input file for the matching (e.g., `serial_dictatorship.txt`) and view the fairness metrics.

---

## Evaluation Metrics
The project evaluates matchings using the following functions:
- **Exponential Score Difference**: Penalizes large rank discrepancies.
- **Average Difference**: Normalized rank differences.
- **Weighted Logarithmic Function**: Combines rank values and differences.

Each function provides insight into the fairness and balance of the matchings.

---

## Next Steps
- **Incorporate Constraints**: Define additional constraints to refine fairness evaluation.
- **Leverage Machine Learning**: Explore Graph Neural Networks (GNNs) and deep reinforcement learning for improving matching algorithms.
- **Collaborations**: Engage with researchers at TU/e for advanced methodologies.

