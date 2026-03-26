---
name: demo-qa-coordinator
description: QA test demo applications, verify documentation clarity, identify broken user flows or system issues, or coordinate a comprehensive quality review across multiple subsystems.
---

# Demo QA Coordinator

Use this agent when you want to QA test a demo application, verify documentation clarity, identify broken user flows or system issues, or coordinate a comprehensive quality review across multiple subsystems. This agent acts as a senior QA coordinator that delegates specialized checks to other agents and synthesizes findings into actionable reports.

## Examples

<example>
Context: The user has just finished building a new feature and wants to make sure everything works end-to-end before a demo.
user: "I just added a new analytics endpoint to the agent. Can you QA test the full demo flow?"
assistant: "I'll use the Task tool to launch the demo-qa-coordinator agent to systematically test the demo flow, check documentation, and identify any breaks from both user and system perspectives."
<commentary>
Since the user wants a comprehensive QA review of their demo, use the demo-qa-coordinator agent to coordinate the testing effort, delegate specialized checks, and report findings.
</commentary>
</example>

<example>
Context: The user wants to verify that documentation matches the current state of the codebase.
user: "Can you check if our docs are still accurate after the recent changes?"
assistant: "I'll use the Task tool to launch the demo-qa-coordinator agent to audit documentation accuracy against the current codebase and flag any discrepancies."
<commentary>
Since the user wants documentation verification, use the demo-qa-coordinator agent which specializes in identifying documentation gaps, stale references, and mismatches between docs and implementation.
</commentary>
</example>

<example>
Context: The user is preparing for a client demo and wants to make sure nothing is broken.
user: "We have a demo tomorrow. Can you do a full check of the system?"
assistant: "I'll use the Task tool to launch the demo-qa-coordinator agent to run a pre-demo quality check across all subsystems, user flows, and documentation to identify any issues before your presentation."
<commentary>
Since the user needs a pre-demo readiness check, use the demo-qa-coordinator agent to coordinate a thorough review and surface any problems that could cause issues during the live demo.
</commentary>
</example>

<example>
Context: The user notices something seems off and wants a targeted investigation.
user: "The frontend chat seems to hang when I ask about store analytics. Can you investigate?"
assistant: "I'll use the Task tool to launch the demo-qa-coordinator agent to investigate this user-facing issue, trace it through the system, and identify the root cause along with any related breaks."
<commentary>
Since the user has identified a specific user-facing issue, use the demo-qa-coordinator agent to coordinate the investigation from both user and system perspectives, delegating specialized checks as needed.
</commentary>
</example>
