# Deal Summary Template

Use this structure when presenting sales deal status.

---

## 💰 {deal_name} — {company_name}

**Stage:** {stage_emoji} {stage} | **Value:** ${deal_value} | **Close Date:** {close_date}

### Deal Details

| Field | Value |
|-------|-------|
| Owner | {deal_owner} |
| Pipeline | {pipeline_name} |
| Probability | {win_probability}% |
| Days in Stage | {days_in_stage} |
| Source | {lead_source} |

{stage_emoji mapping: prospecting=🔍, qualification=📋, proposal=📄, negotiation=🤝, closed_won=🎉, closed_lost=❌}

### Contacts

| Name | Role | Engagement |
|------|------|-----------|
| {contact_name} | {contact_role} | {last_contact_date} |

### Activity Summary

| Metric | Count |
|--------|-------|
| Emails | {email_count} |
| Calls | {call_count} |
| Meetings | {meeting_count} |
| Last Activity | {last_activity_date} |

{if days_in_stage > 30: "⚠️ Stalled — deal stuck in stage for 30+ days"}
{if win_probability >= 80: "🌟 High confidence — prioritize for close"}
{if last_activity_date > 14_days_ago: "⚠️ No recent activity — re-engage contacts"}

---

*Generated from mcp-sales | {timestamp}*
