# CRM Fields

Minimum viable CRM can be built in Feishu Base, WeCom SCRM, Jiandaoyun, Airtable, Notion, or a spreadsheet.

## Fields

| Type | Fields |
|---|---|
| basic | customer name, contact, phone, platform handle, company, role, city |
| source | platform, account, content URL, keyword, live session, referral |
| demand | scenario, industry, API needed, estimated monthly usage, current supplier, pain |
| qualification | budget, decision maker, payment entity, contract needed, invoice needed, ordinary invoice or special invoice |
| sales | stage, owner, expected amount, expected gross profit, probability |
| follow-up | last contact, next action, next time, follow-up count |
| quote | quote number, package, quote amount, quote validity, discount approval |
| contract | contract status, payment status, invoice type, invoice title, taxpayer ID, special-invoice info, service dates |
| service | current balance, usage percentage, support tickets, satisfaction, renewal date |
| lost | lost reason, competitor, reactivation potential, next reactivation date |

## Stage Probability

| Stage | Probability |
|---|---:|
| new lead | 5% |
| qualified | 15% |
| diagnosed | 30% |
| quoted | 45% |
| contracting | 70% |
| paid | 100% |

## Required Rule

Every non-lost record must have:

- next action
- next action time
- owner
