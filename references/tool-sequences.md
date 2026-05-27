# Sales Tool Sequences (29 tools)

## Proposals (7): create, list, get, send, delete, list_templates, create_from_template
## Signatures (5): request_signature, get_signature_status, list_signatures, get_proposal_views, get_proposal_analytics
## CPQ (4): list_products, calculate_quote, apply_discount, create_quote
## Sequences (5): list_sequences, create_sequence, enroll_contact, pause_sequence, get_sequence_stats
## Email (2): send_tracked_email, get_email_engagement
## Meetings (3): get_availability, create_booking_link, list_scheduled_meetings
## Forecasting (3): get_pipeline_forecast, get_quota_progress, get_win_loss_analysis

## Sequence: Proposal → Signature (4 calls)
```
1. create_from_template(template: "enterprise", variables: {customer, value})
2. send_proposal(id, recipient: "buyer@acme.com")
3. request_signature(proposal_id, signers: [{email: "buyer@acme.com"}])
4. get_signature_status(id) → track until complete
```
