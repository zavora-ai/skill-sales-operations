# Sales Operations Skill

> Enterprise sales acceleration for AI agents — proposals, CPQ, outreach sequences, meeting scheduling, e-signatures, and pipeline forecasting via PandaDoc, Apollo.io, Calendly, and Stripe Billing.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--sales-green)](https://github.com/zavora-ai/mcp-sales)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Revenue Impact |
|----------|-------|---------------|
| Proposals | 2-3 | **Direct: sends deal to customer** |
| CPQ | 3-4 | **Direct: accurate pricing** |
| Sequences | 2-3 | Pipeline generation |
| Meetings | 2 | Advance deals faster |
| Signatures | 2-3 | **Direct: close deals** |
| Forecasting | 3 | Revenue visibility |

### Without this skill:
- Proposals take days (manual creation)
- Quotes have pricing errors
- Follow-ups forgotten (no sequences)
- Signature tracking is manual

### With this skill:
- Proposals sent same-day from templates
- CPQ with automatic discount validation
- Automated sequences with engagement tracking
- E-signature with real-time status

## Installation

```bash
git clone https://github.com/zavora-ai/skill-sales-operations.git ~/.skills/skills/sales-operations
```

## Requirements

**Required:** `mcp-sales` (29 tools — PandaDoc, Apollo.io, Calendly, Stripe)

**Cross-MCP:** `mcp-crm` (deal data), `mcp-finance` (invoicing), `mcp-email` (outreach), `mcp-calendar` (meetings)

## Folder Structure

```
sales-operations/
├── SKILL.md                       # 6 workflows + decision tree
├── scripts/
│   └── quote_calculator.py        # Pricing + margin validation
├── references/
│   ├── tool-sequences.md          # 29 tools
│   ├── cross-mcp-workflows.md     # Sales + CRM + Finance + Email
│   └── examples.md                # Proposal, forecast scenarios
├── README.md
└── LICENSE
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Proposal speed | Created + sent in < 3 tool calls |
| Quote accuracy | 100% correct with discount validation |
| Sequence engagement | Track opens/clicks/replies |
| Forecast accuracy | Weighted pipeline within 10% of actual |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
