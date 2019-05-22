# MC Uncertainty
Uncertainty estimation functions for use with Monte Carlo sampled model outputs.

## Installation

`pip install mc-uncertainty`

## Usage

```python
# All functions accept data with shape (mc_samples, n, classes)
data = np.array(...

# Variance
from mc_uncertainty import variance
print(variance(data))  # shape: [n, classes]

# Entropy
from mc_uncertainty import entropy
print(entropy(data))  # shape: [mc_samples, n]

# Predicted entropy
from mc_uncertainty import predicted_entropy
print(predicted_entropy(data))  # shape: [n,]

# Mutual information
from mc_uncertainty import mutual_information
print(mutual_information(data))  # shape: [n,]
```