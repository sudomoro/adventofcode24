# Day Three: Multiplication Instruction Analysis

## Objective
Implement a system to process corrupted memory by extracting valid multiplication instructions (`mul`) and respecting enabling/disabling commands (`do()` and `don't()`), focusing on **tokenization** as the core mechanism.

## Key Concept: Tokenization

### What is Tokenization?
- **Definition**: The process of breaking down a stream of text into smaller, meaningful units (tokens).
- **Purpose**: Allows for systematic evaluation of commands and instructions within a corrupted memory block.

### How Tokenization Works in This Program
1. **Splitting the Input**: 
   - The corrupted memory is split into tokens based on patterns for control commands (`do()` and `don't()`) and other text.
   - Regex patterns like `(do\(\)|don't\(\))` separate enable/disable commands from other instructions.

2. **Sequential Processing**:
   - Each token is processed in order to determine its meaning:
     - If it's `do()`, enable subsequent instructions.
     - If it's `don't()`, disable subsequent instructions.
     - If it’s a valid multiplication instruction (`mul(X,Y)`), check the current state (enabled/disabled) before processing.

3. **Maintaining State**:
   - A boolean variable tracks whether instructions are currently enabled or disabled.
   - This state changes only when encountering a `do()` or `don't()` token.

4. **Ignoring Invalid Data**:
   - Tokens that do not match valid patterns (`mul`, `do()`, or `don't()`) are ignored.
---

## Applications of Tokenization

| **Use Case**                  | **Description**                                                                                  | **Examples**                                      |
|-------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------|
| **Natural Language Processing** | Breaking text into words or phrases for sentiment analysis, translation, or chatbots.           | `["Tokenization", "is", "key"]`                 |
| **Programming and Compilers**   | Splitting source code into keywords, operators, and identifiers for syntax checking.            | `["int", "x", "=", "10", ";"]`                  |
| **Data Processing**             | Parsing logs or structured data into analyzable components.                                     | `["2024-12-03", "INFO", "Process", "started"]`  |
| **Search Engines**              | Indexing documents or queries into searchable terms.                                            | `["find", "restaurants", "near", "me"]`         |
| **Security and Cryptography**   | Tokenizing sensitive information into non-sensitive placeholders.                              | OAuth tokens, intrusion detection               |
| **Machine Learning**            | Preparing data for models by extracting tokens for sequence processing.                        | Text to sequences for NLP models                |
| **Data Cleaning and Validation**| Splitting and normalizing messy datasets for analysis.                                          | Parsing addresses into street, city, zip code   |
| **Financial Applications**      | Parsing transactions or invoices into tokens for financial analysis.                           | `["Buy", "100", "XYZ", "$50"]`                  |
| **Legal and Medical Records**   | Tokenizing documents for text mining or diagnosis.                                             | Legal contracts, medical transcripts            |
| **Gaming**                      | Processing player commands or dialogue for in-game actions.                                    | `["move", "player", "north"]`                   |

---

## Takeaways
- Tokenization is the backbone of the analysis process, enabling structured evaluation of mixed commands and data.
- It simplifies state-aware processing by handling one token at a time.
- The combination of tokenization and regex enables powerful and flexible parsing mechanisms for various domains.
