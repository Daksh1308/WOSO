# Warehouse Operations Simulation

A discrete-event simulation model for warehouse operations using SimPy. Models inbound receiving, put-away, picking, packing, and outbound shipping processes to analyze throughput, bottlenecks, and resource utilization under various operational scenarios.

## Problem Statement

Warehouses face increasing pressure to optimize throughput while minimizing operational costs. Key challenges include:
- Balancing labor and equipment resources across interdependent processes
- Identifying bottlenecks that limit overall throughput
- Evaluating the impact of policy changes (e.g., batch sizing, shift scheduling) before committing resources
- Understanding how demand variability affects warehouse performance

This simulation provides a quantitative framework to model, analyze, and optimize warehouse operations before deploying changes in the real world.

## Features

- Discrete-event simulation of core warehouse processes (receiving, put-away, picking, packing, shipping)
- Configurable resource pools (dock doors, put-away crews, pickers, packers, staging lanes)
- Support for multiple operational scenarios with comparative analytics
- Real-time performance metrics (throughput, cycle time, utilization, queue depths)
- Streamlit dashboard for interactive exploration of results
- Extensible architecture for adding custom process logic or resource policies

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Simulation Engine | SimPy 4.x |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Dashboard | Streamlit |
| Language | Python 3.8+ |

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-org/warehouse-simulation.git
cd warehouse-simulation
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Usage

Run all simulation scenarios and generate comparison reports:

```bash
python src/main.py
```

Launch the interactive Streamlit dashboard:

```bash
streamlit run src/dashboard.py
```

## Project Structure

```
warehouse-simulation/
â”œâ”€â”€ requirements.txt          # Python dependencies
â”œâ”€â”€ setup.py                  # Package configuration
â”œâ”€â”€ README.md                 # This file
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ main.py               # Entry point â€” runs all scenarios
â”‚   â”œâ”€â”€ dashboard.py          # Streamlit dashboard
â”‚   â”œâ”€â”€ model.py              # Core simulation engine (SimPy processes)
â”‚   â”œâ”€â”€ config.py             # Configuration dataclasses & defaults
â”‚   â”œâ”€â”€ metrics.py            # Metrics collection and aggregation
â”‚   â”œâ”€â”€ scenarios.py          # Scenario definitions
â”‚   â””â”€â”€ utils.py              # Utility functions (random variates, etc.)
â”œâ”€â”€ data/
â”‚   â””â”€â”€ results/              # Simulation output files (CSV)
â””â”€â”€ tests/
    â”œâ”€â”€ test_model.py
    â”œâ”€â”€ test_metrics.py
    â””â”€â”€ test_scenarios.py
```

## Scenarios

The simulation includes five operational scenarios:

### 1. Baseline â€” Current Operations
Standard shift structure with average order volumes. Resources are configured at default levels. This serves as the control against which all other scenarios are measured.

### 2. High Volume â€” Peak Season
Order arrival rates and receiving volumes are increased by 50%. Evaluates whether existing resources can handle peak-season demand and identifies where bottlenecks first appear.

### 3. Reduced Resources â€” Cost Optimization
Resource counts (pickers, packers, put-away crews) are reduced by 20%. Assesses the impact of cost-cutting measures on throughput, cycle time, and service levels.

### 4. Batch Picking â€” Process Improvement
Orders are consolidated into batches of 5 before being released to picking. Analyzes how batch picking affects picker travel time, packer workload, and overall order cycle time.

### 5. Extended Shifts â€” Capacity Expansion
Two additional hours are added to each shift. Measures the incremental throughput gain from extended operating hours and evaluates whether downstream processes become new bottlenecks.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

<!-- pin -->
