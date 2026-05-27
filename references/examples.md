# Sales Examples

## Example 1: "Send a proposal to Acme"
```
list_templates() → [{id: "tpl_enterprise"}]
create_from_template(template_id: "tpl_enterprise", variables: {customer: "Acme", value: 75000})
send_proposal(id: "prop_001", recipient: "sarah@acme.com")
```
Response: "✅ Proposal sent to sarah@acme.com"

## Example 2: "What's our forecast?"
```
get_pipeline_forecast() → {weighted: 450000, deals: 12}
get_quota_progress() → {quota: 500000, closed: 320000, pct: 64}
```
Response: "Q1: $450k pipeline, $320k closed (64% of quota)"
