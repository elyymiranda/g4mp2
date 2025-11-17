# G4(MP2) Calculation Toolkit

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Gaussian](https://img.shields.io/badge/Gaussian-09-orange.svg)](https://gaussian.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

**A comprehensive toolkit for automated G4(MP2) calculations using Gaussian 09, including input generation, analysis, and thermochemistry calculations.**

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating Calculation Inputs](#creating-calculation-inputs)
  - [Analyzing Results](#analyzing-results)
  - [Thermochemistry Analysis](#thermochemistry-analysis)
- [Input File Format](#input-file-format)
- [Output](#output)
- [Acknowledgments](#acknowledgments)
- [Citation](#citation)
- [License](#license)

---

## Introduction

This project provides a complete workflow for G4(MP2) composite method calculations using Gaussian 09. The G4(MP2) method is a high-accuracy composite approach for computing thermochemical properties such as enthalpies of formation, bond dissociation energies, and electron affinities.

The toolkit automates:
- Generation of properly formatted Gaussian 09 input files for G4(MP2) calculations
- Extraction and analysis of energetic data from output log files
- Thermochemistry calculations including free energy corrections at various temperatures

---

## Features

- **Automated input generation**: Creates complete G4(MP2) input files with all required calculation steps
- **Results analysis**: Extracts and computes G4(MP2) energies from Gaussian log files
- **Core electron handling**: Automatic detection and counting of core electrons for various elements
- **Thermochemistry tools**: Python scripts for free energy and thermochemistry calculations
- **Temperature corrections**: Support for thermochemistry at different temperatures
- **Flexible configuration**: Easy-to-use input format for molecule specification

---

## Requirements

- **Gaussian 09** (for running calculations)
- **Bash** (for running shell scripts)
- **Python 3.x** (for thermochemistry analysis)
  - `numpy`

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/elyymiranda/g4mp2.git
cd g4mp2
```

2. **Make scripts executable:**
```bash
chmod +x calc analysis
```

3. **Install Python dependencies (for thermochemistry):**
```bash
pip install numpy
```

---

## Usage

### Creating Calculation Inputs

1. **Create an input file** based on the template in `inputs/input_calc`:

```bash
cp inputs/input_calc my_molecule_input
# Edit my_molecule_input with your molecule information
```

2. **Generate Gaussian input:**

```bash
./calc my_molecule_input
```

This creates a `.inp` file ready for Gaussian 09 with all G4(MP2) calculation steps.

3. **Run the calculation in Gaussian 09:**

```bash
g09 molecule.inp
```

### Analyzing Results

After the Gaussian calculation completes:

```bash
./analysis molecule.log
```

This script extracts:
- Individual energy components
- G4(MP2) composite energy
- Thermochemical corrections

### Thermochemistry Analysis

For detailed thermochemistry at specific temperatures:

```bash
python thermochemistry.py molecule.log
```

Or for free energy calculations:

```bash
python free_energy_g09.py molecule.log
```

---

## Input File Format

The input file uses a simple key-value format:

```bash
# Software settings
CODE = g09
CORE = 24
MEMORY = 20GB

# Molecule information
NAME = molecule_name
CHARGE = 0
SPIN = 1

# Geometry in Angstrom
BEGIN_GEO
C     0.000000    0.000000    0.000000
H     1.089000    0.000000    0.000000
H    -0.363000    1.027000    0.000000
H    -0.363000   -0.513500    0.889165
H    -0.363000   -0.513500   -0.889165
END_GEO
```

### Parameters

| Parameter | Description                              | Example     |
|-----------|------------------------------------------|-------------|
| `CODE`    | Quantum chemistry software               | `g09`       |
| `CORE`    | Number of CPU cores                      | `24`        |
| `MEMORY`  | Memory allocation                        | `20GB`      |
| `NAME`    | Molecule name (used for output files)    | `methane`   |
| `CHARGE`  | Molecular charge                         | `0`, `-1`   |
| `SPIN`    | Spin multiplicity                        | `1`, `2`    |

---

## Output

### Generated Input File

The `calc` script generates a Gaussian input file with:
- B3LYP/6-31G(2df,p) geometry optimization
- Frequency calculation with GTBas3 basis
- CCSD(T)/GTBas1 single point
- MP2/GTBas2 single point
- MP2/GTBas3 single point
- HF/GTLargeXP single point

### Analysis Output

The `analysis` script provides:
- Core electron count
- Individual method energies
- Final G4(MP2) composite energy
- Thermochemical corrections (ZPE, enthalpy, free energy)

---

## Acknowledgments

**Python thermochemistry code**: The Python scripts for thermochemistry analysis (`readLog.py`, `thermochemistry.py`, `free_energy_g09.py`) were originally developed by **Lucas Cornetta** and can be found in his repository:
- [https://github.com/lmcornetta/vib_g4mp2/](https://github.com/lmcornetta/vib_g4mp2/)

**Bash scripts**: The bash scripts (`calc`, `analysis`) were developed by Ely Miranda.

---

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{g4mp2_toolkit,
  author = {Miranda, Ely},
  title = {G4(MP2) Calculation Toolkit for Gaussian 09},
  year = {2025},
  url = {https://github.com/elyymiranda/g4mp2}
}
```

For the Python thermochemistry scripts, please also cite Lucas Cornetta's original work:
- [https://github.com/lmcornetta/vib_g4mp2/](https://github.com/lmcornetta/vib_g4mp2/)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

**Ely Miranda**
PhD Student, Physics Institute
Universidade de São Paulo
Email: ely.miranda@usp.br

For questions or suggestions, please open an issue on GitHub or contact via email.
