---
name: constant-time-analysis
description: Constant-Time Analyzer (ct-analyzer)
---

 Constant-Time Analyzer (ct-analyzer)

A portable tool for detecting timing side-channel vulnerabilities in compiled cryptographic code. Analyzes assembly output from multiple compilers and architectures to detect instructions that could leak secret data through execution timing.

## Background

Timing side-channel attacks exploit variations in execution time to extract secret information from cryptographic implementations. Common sources include:

- **Hardware division** (`DIV`, `IDIV`): Execution time varies based on operand values
- **Floating-point operations** (`FDIV`, `FSQRT`): Variable latency based on inputs
- **Conditional branches**: Different execution paths have different timing

The infamous [KyberSlash](https://kyberslash.cr.yp.to/) attack demonstrated how division instructions in post-quantum cryptographic implementations could be exploited to recover secret keys.


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
