# Sales Cross-MCP Workflows

## Sales + CRM: Full Deal Cycle
```
CRM: get_deal(id) → deal data
SALES: create_from_template(template, deal_data)
SALES: send_proposal(id, customer_email)
SALES: request_signature(proposal_id, signers)
CRM: move_deal_stage(stage: "Closed Won")
FINANCE: create_invoice(customer, amount)
```

## Sales + Email: Tracked Outreach
```
SALES: send_tracked_email(to: prospect, subject: "Following up")
SALES: get_email_engagement(email_id) → {opened: true, clicked: true}
CRM: create_activity(type: "email", subject: "Prospect engaged")
```
