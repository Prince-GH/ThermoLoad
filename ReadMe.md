# ThermoLoad: A Multi-Criteria Load Balancing Algorithm for Sustainable and Carbon-Efficient Data Centers

## 📘 Overview

**ThermoLoad** is a novel load balancing algorithm designed to optimize server workload distribution based on multiple performance and environmental metrics—primarily **server temperature**, **CPU usage**, **response time**, and **hardware weight**.

Unlike traditional algorithms (e.g., Round Robin, Least Connection), ThermoLoad is **thermally aware** and **multi-metric**, aiming to enhance data center sustainability by minimizing hotspots, reducing response time, and improving energy efficiency.

This repository includes:

- ✅ Implementation of ThermoLoad and five benchmark algorithms
- 🧪 A simulated test environment using realistic server conditions
- 📊 Plots and comparison metrics
- 📄 LaTeX source for the research paper (optional)

---

## 🧠 Core Idea

Traditional load balancers ignore real-time server thermals and dynamic performance states. **ThermoLoad** addresses this gap using a **weighted scoring formula**:

```math
\text{Score} = \alpha \cdot T + \beta \cdot C + \gamma \cdot R + \delta \cdot W
```


Where:

- `T` = Normalized temperature (0 to 1)  
- `C` = Normalized active connections  
- `R` = Normalized response time  
- `W` = Normalized server weight (higher = better)  
- `α, β, γ, δ` = Weighting coefficients for each factor

The server with the **lowest score** is selected to handle incoming requests, ensuring performance and thermal stability.


## ⚙️ Experimental Setup

- **Language**: Python 3.11  
- **Packages Used**: `numpy`, `pandas`, `matplotlib`, `random`

### System Configuration

- **CPU**: Intel Core i7-12700H @ 2.30GHz  
- **RAM**: 32 GB  
- **OS**: Ubuntu 22.04 LTS  

### Server Simulation

| Parameter           | Range               |
|---------------------|---------------------|
| Virtual Servers     | 6                   |
| CPU Frequencies     | 2.2 – 3.4 GHz       |
| Temperatures        | 32°C – 61°C         |
| Active Connections  | 20 – 200            |
| Response Times      | 15 ms – 150 ms      |
| Server Weights      | 1 – 5               |

### Workloads Emulated

- CPU-bound (40%)  
- Memory-bound (30%)  
- I/O-heavy (30%)

---

## 🧪 How to Run the Code

### Install Dependencies

```bash
pip install numpy pandas matplotlib
```

## 📚 Cited Works and Influences

This project builds upon and extends ideas from notable works, including:

- **Hassel, W.J.** — *Carbon cost of cooling AI data centers* (2023)  
- **Singhal, A.** — *AI-enhanced load balancing* (2023)  
- **Fan, X.** — *Power provisioning in warehouse-scale data centers* (2007)  
- **Iffländer, L.** — *Heat-aware routing models* (2022)  

See the research paper in the `/report` directory for full citations.

---

## 📜 License

This project is intended for **academic and research use only**.  
Please **cite the associated paper** if used in publications.

---

## 🤝 Acknowledgments

Special thanks to the open-source community and the authors of prior work in:

- 🔥 Thermal-aware computing  
- ☁️ Cloud performance optimization  
- 🌱 Sustainable server architecture  
