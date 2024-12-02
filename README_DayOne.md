# Day One: Reconciliation and Measurement

## Objective
Compare two lists of numbers (location IDs) and evaluate their relationship using numerical and overlap-based metrics.

## Key Concepts

### 1. Numerical Disparity (Total Distance)
- **Definition**: Measures the overall difference between two sorted lists.
- **How it's Calculated**: 
  - Sort both lists.
  - Pair corresponding elements.
  - Compute the absolute difference for each pair and sum them up.
- **Purpose**: Reflects the degree of numerical mismatch between the lists.

### 2. Commonality (Similarity Score)
- **Definition**: Measures how much overlap exists between the two lists.
- **How it's Calculated**:
  - Count how often each number from the first list appears in the second list.
  - Multiply the number by its frequency and sum the results.
- **Purpose**: Highlights shared elements and their significance.

## Applications
- **Data Reconciliation**: Identify mismatches and overlaps between datasets.
- **Similarity and Difference Evaluation**: Quantify relationships in numerical data.

## Takeaways
- Total Distance captures **numerical disparity**.
- Similarity Score highlights **commonality**.
