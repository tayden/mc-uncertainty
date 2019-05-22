# MC Uncertainty

Uncertainty estimation functions for use with Monte Carlo sampled model outputs.

## Installation

`pip install mc-uncertainty`

## Usage

```python
import mc_uncertainty as mcu

# All functions accept data with shape (mc_samples, n, classes)
data = np.array(...

# Variance
print(mcu.variance(data).shape)  # [n, classes]

# Entropy
print(mcu.entropy(data).shape)  # [mc_samples, n]

# Predicted entropy
print(mcu.predicted_entropy(data).shape)  # [n,]

# Mutual information
print(mcu.mutual_information(data).shape)  # [n,]
```