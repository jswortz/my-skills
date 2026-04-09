---
name: condition-based-waiting
description: -- name: Condition-Based Waiting description: Replace arbitrary timeouts with condition polling for reliable async tests when_to_use: when tests have ...
---

--
name: Condition-Based Waiting
description: Replace arbitrary timeouts with condition polling for reliable async tests
when_to_use: when tests have race conditions, timing dependencies, or inconsistent pass/fail behavior
version: 1.1.0
languages: all
---

# Condition-Based Waiting

## Overview

Flaky tests often guess at timing with arbitrary delays. This creates race conditions where tests pass on fast machines but fail under load or in CI.

**Core principle:** Wait for the actual condition you care about, not a guess about how long it takes.


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
