# Bloom Filter Implementation

Build a space-efficient, probabilistic data structure.

## What is a Bloom Filter?
* A **space-efficient, probabilistic data structure** used to check if an element might exist in a set without storing the actual elements.

## Why do we need it?
* **Scalable Systems:** Designed for platforms handling 1+ million users to drastically reduce expensive database lookups when verifying if a chosen username is already taken.

## Core Functions
* `set(item)`: Inserts a new element into the filter.
* `exists(item)`: Checks if an element is potentially in the filter.

## Math & Tuning Behavior
Three critical parameters determine the internal behavior of a Bloom Filter:
* `m`: Total array size (in bits)
* `n`: Number of existing items already inserted
* `k`: Number of independent hash functions required

### Approximate False Positive Probability (\(p\))
\[p \approx \left(1 - e^{-\frac{kn}{m}}\right)^k\]

### Optimal Number of Hash Functions (\(k\))
\[k = \left(\frac{m}{n}\right) \ln 2\]

### Determining Bit Array Size (\(m\))
\[m = -\frac{n \cdot \ln(p)}{(\ln 2)^2}\]

* **Example:** For \(n = 1\) item and an acceptable false positive rate of \(p = 0.01\) (1%), the required bit array size resolves to \(m \approx 9.59\) bits.
