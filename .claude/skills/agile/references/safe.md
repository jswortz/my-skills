# SAFe (Scaled Agile Framework) Integration

## Program Increment Planning

For multi-team coordination, use a hierarchical agent topology:

```
Release Train Engineer (scrum-master)
├── Team 1 Scrum Master (scrum-master)
│   ├── frontend-dev
│   ├── backend-dev
│   └── qa-engineer
├── Team 2 Scrum Master (scrum-master)
│   ├── frontend-dev
│   ├── backend-dev
│   └── qa-engineer
└── System Architect (tech-lead)
```

## PI Planning Steps

1. Launch Release Train Engineer to coordinate PI scope
2. Each team's scrum-master plans their sprint backlog
3. tech-lead identifies cross-team dependencies
4. product-owner prioritizes PI features across teams

## Cross-Team Dependencies

Track dependencies in the knowledge graph:

```
mcp__memory__create_relations([
  { from: "Team1-Story-Auth", relationType: "blocks", to: "Team2-Story-Dashboard" },
  { from: "Team1-Story-API", relationType: "enables", to: "Team2-Story-Integration" }
])
```

## Innovation Sprint

Reserve 1 sprint per PI for innovation:
- Launch agents with `strategy: "innovation_sprint"` framing
- Cross-functional teams explore new ideas
- Timebox to 1-2 days of agent execution
- Present prototypes in PI review
