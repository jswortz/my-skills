---
name: Root Cause Tracing
description: Systematically trace bugs backward through call stack to find original trigger
when_to_use: when errors occur deep in execution and you need to trace back to find the original trigger
version: 1.1.0
languages: all
---

# Root Cause Tracing

## Overview

Bugs often manifest deep in the call stack (git init in wrong directory, file created in wrong location, database opened with wrong path). Your instinct is to fix where the error appears, but that's treating a symptom.

**Core principle:** Trace backward through the call chain until you find the original trigger, then fix at the source.


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
