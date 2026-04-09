---
name: defense-in-depth
description: -- name: Defense-in-Depth Validation description: Validate at every layer data passes through to make bugs impossible when_to_use: when invalid data c...
---

--
name: Defense-in-Depth Validation
description: Validate at every layer data passes through to make bugs impossible
when_to_use: when invalid data causes failures deep in execution, requiring validation at multiple system layers
version: 1.1.0
languages: all
---

# Defense-in-Depth Validation

## Overview

When you fix a bug caused by invalid data, adding validation at one place feels sufficient. But that single check can be bypassed by different code paths, refactoring, or mocks.

**Core principle:** Validate at EVERY layer data passes through. Make the bug structurally impossible.


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
