# Music-Industry-Insights

Welcome to the Music-Industry-Insights project! This repository is part of the DS5610 EDA: Final Project, where we apply exploratory data analysis (EDA) techniques to uncover insights within the music industry. Our goal is to translate complex data into actionable insights and communicate these effectively to a non-data science audience.

## Table of Contents

- [Music-Industry-Insights](#music-industry-insights)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [Key Dates](#key-dates)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Project Overview

This project involves:

- **Group Collaboration**: Working in assigned groups to select a topic and dataset relevant to the music industry.
- **Data Exploration**: Conducting thorough exploratory data analysis to understand data structure, variables, and potential insights.
- **Report Generation**: Producing a human-readable report that presents findings clearly and concisely to a non-technical audience.
- **Code Submission**: Submitting a Jupyter notebook with well-commented code that generates all tables and figures in the report.

### Key Dates

- **11/12**: Project introduction and group formation.
- **11/21**: Initial data description and visualization.
- **12/5**: Continued analysis and report drafting.
- **12/12**: Final submission of the report and code by 11:59pm CT.

## Project Structure
```
Music-Industry-Insights/
│
├── data/ # Datasets managed with DVC
│ └── data.dvc # DVC file for data
│ └── other data files
│
├── scripts/ # Python scripts and modules
│ ├── init.py # Initialize as a package
│ └── example_script.py # Example script file
│
├── experiments/ # Jupyter notebooks for experiments
│ ├── contributor1/ # Folder for Contributor 1's work
│ │ └── analysis.ipynb # Example notebook
│ └── contributor2/ # Folder for Contributor 2's work
│ └── analysis.ipynb # Example notebook
│
├── report/ # Final report files
│ └── report.pdf # Example report file
│
├── .dvc/ # DVC configuration files
│
├── .gitignore # Git ignore file
│
├── README.md # Project overview and instructions
│
├── CONTRIBUTING.md # Contribution guidelines
│
├── LICENSE # License information
│
├── requirements.txt # Python package dependencies
│
└── pyproject.toml # Project configuration for pip install
```

The repository is organized as follows:

- **data/**: Contains datasets managed with DVC (Data Version Control).
- **scripts/**: Includes Python scripts and modules for data processing and analysis.
- **experiments/**: Houses Jupyter notebooks for experiments, with each contributor having their own folder.
- **report/**: Contains the final report in HTML or PDF format.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.12
- DVC
- Jupyter Notebook

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Music-Industry-Insights.git
   cd Music-Industry-Insights
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up DVC:
   ```bash
   dvc pull
   ```

### Usage

- Run scripts from the `scripts/` directory to process data and generate insights.
- Use Jupyter notebooks in the `experiments/` directory to explore data and test hypotheses.

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the team.

Shivam Tyagi - st.shivamtyagi.01@gmail.com | FrostNT1
Beema Rajan - beema.rajan@vanderbilt.edu | BeemaRajan
Zhiqi Zhang - zhiqi.zhang@vanderbilt.edu | zhiqi-zhang233