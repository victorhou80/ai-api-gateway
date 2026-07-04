# 01. Compliance And Risk

This section is the gatekeeper. If it fails, do not scale.

## Non-Negotiable Principle

Do not publicly sell foreign model tokens, recharges, API keys, card codes, or account access unless the upstream provider or authorized distributor explicitly permits resale, integration, and end-customer service delivery in writing.

If the channel is only "semi-official" or orally promised, treat it as unverified.

## Upstream Authorization Questions

Ask the supplier for written answers and supporting documents:

1. Who is in the authorization chain: model provider, master distributor, regional agent, technical service provider?
2. Does authorization explicitly include China-based customers or the target geography?
3. Does it allow resale, distribution, API integration, and end-user service delivery?
4. Does it allow quota splitting, second-level pricing, prepaid packaging, and usage pooling?
5. Does it allow using model names, logos, benchmarks, screenshots, or pricing in marketing?
6. Does the supplier provide contracts, invoices, bills, or equivalent tax/cost proofs?
7. What are the data-processing terms: where is data processed, retained, and whether it is used for training?
8. What happens if the upstream model is blocked, throttled, repriced, suspended, or terminated?
9. Who handles customer claims if upstream service fails?
10. Can you produce authorization, order, invoice, data-flow, and customer records during audit?

No written answers means no public launch.

## Red Lines

Do not do these:

- sell or rent accounts, API keys, OAuth tokens, subscriptions, or shared access
- split personal/pro/consumer subscription quota for third-party commercial use
- run a public API relay advertised as a low-price official substitute
- help customers bypass geography, payment, KYC, identity, account, or safety restrictions
- use personal WeChat/Alipay codes for business revenue
- mislabel quota sales as "course material", "consulting", or unrelated invoice items
- claim "official", "semi-official", "highest-level", "lowest price", "unlimited", "no ban", or "internal channel"
- accept unknown gift cards, crypto, offshore personal payers, or third-party money transfers
- process highly sensitive personal data or customer secrets through foreign models without a lawful path
- remove, hide, forge, or alter AI-generated-content labels
- provide services for fraud, spam, pornography, gambling, impersonation, cheating, fake reviews, or illegal content
- copy competitor images, videos, reviews, music, brand assets, or watermarked materials for customer deliverables
- use customer-provided materials without confirming usage rights, especially people, trademarks, music, UGC/KOL, supplier images, or stock assets

## Safer Business Forms

Priority order:

1. Authorized B2B distributor/reseller.
2. Enterprise AI SaaS or workflow product where customers buy your service, not raw quota.
3. Procurement/implementation consultant where customers contract with official channels directly.
4. Authorized enterprise API gateway for whitelisted business customers only.
5. Domestic registered-model solution for compliance-sensitive China customers.

## Data And Customer Restrictions

Default forbidden uploads:

- ID cards and passports
- medical records
- financial accounts
- minors' data
- customer lists without authorization
- private chat logs
- source code or trade secrets unless contractually permitted
- state secrets or important data
- legal, financial, medical, or employment decision data without specialist review

Default permitted low-risk pilots:

- public marketing copy
- product descriptions
- non-sensitive FAQ drafts
- internal training materials
- public-document summaries
- anonymized workflow testing

## Ecommerce Material Rights Rules

For ecommerce content, collect material source and usage rights before production.

Default safer sources:

- customer-owned product photos/videos
- customer-shot product clips
- supplier material with authorization
- licensed commercial stock assets
- authorized UGC/KOL content
- AI-generated material with tool/license/platform review

Use competitor material only for analysis. Do not copy competitor images, videos, reviews, ad screenshots, music, layouts, trademarks, or customer photos into deliverables.

If usage rights are unclear, tag the material as "reference only" or ask the customer for replacement/authorization.

## Cross-Border Model/API Data Rules

For cross-border ecommerce customers, overseas model/API use may be commercially reasonable, but it still needs a controlled data path.

Default safer modes:

1. BYOK: customer brings their own official API key and vendor relationship; you provide routing, logging, prompt workflow, and reporting.
2. Authorized managed access: only if supplier authorization permits integration, resale, and end-customer service delivery in writing.
3. Consulting/procurement support: customer contracts with official provider directly; you provide selection, implementation, and workflow service.

Before using overseas models/APIs, confirm:

- target countries and languages
- whether personal information is included
- whether buyer messages, orders, phone numbers, addresses, emails, or payment data are included
- whether data must be anonymized or masked
- whether supplier terms allow the use case
- whether the customer has approved cross-border processing
- whether output requires human review before publication

Do not:

- export customer personal information to overseas models without a lawful path
- upload marketplace account passwords, ad account credentials, API keys, or payment data
- offer shared API keys or hidden relays
- help bypass geography, KYC, payment, or platform restrictions
- claim overseas platform approval, ranking, ROI, or GMV guarantees

## API Credential Handling Rules

API credentials are secrets and must be handled as controlled customer/project credentials.

Do:

- create separate keys per customer or project whenever possible
- store keys in server-side environment variables or a secret manager
- mask keys in screenshots, documents, and support chats
- rotate keys after suspected leakage
- record the key owner, package, budget cap, and service period
- revoke or disable keys when the contract ends or abuse occurs

Do not:

- expose API keys in frontend JavaScript
- commit keys to GitHub or shared documents
- send master keys to customers
- reuse one shared key across unrelated customers
- ask customers to send marketplace passwords, ad account passwords, or upstream API keys in plain chat

## Platform Rules

Use platform-approved mechanisms:

- enterprise/professional account
- shop/service listing
- official lead form
- live-stream reservation component
- in-platform private messages
- compliant CRM follow-up after explicit lead consent

Avoid:

- comment-section off-platform transaction bait
- hidden contact methods
- "DM code word to avoid review"
- platform category mismatch
- private payment after platform lead capture when platform rules require closed-loop transaction

## Payment And Invoice Rules

Confirmed capability: ordinary VAT invoices and special VAT invoices can both be issued. This is a real B2B advantage, but it does not remove the need for correct service classification, accurate invoice items, and auditable upstream cost records.

For B2B:

1. quote
2. contract/order
3. confirm invoice type: ordinary invoice, special invoice, or no invoice
4. collect invoice information before payment if the customer requires it
5. company bank account or compliant platform payment
6. service activation after payment
7. issue digital invoice/fapiao according to the real service nature
8. ledger linking customer, contract, payment, invoice, cost, delivery, and refund

Do not:

- accept postpaid terms by default
- maintain large transferrable customer stored-value balances
- use personal payment codes
- issue mismatched invoices
- pay upstream through unexplained third parties

Invoice fields to collect:

| Field | Ordinary invoice | Special invoice |
|---|---|---|
| invoice title | required | required |
| taxpayer identification number | required for company | required |
| address and phone | optional/common | usually required |
| bank and account | optional/common | usually required |
| invoice recipient email | required | required |
| invoice item | must match service | must match service |
| invoice amount | match actual received/contracted amount | match actual received/contracted amount |

Recommended invoice item direction should be confirmed with the accountant based on actual delivery, such as information technology service, technical service, software service, SaaS/service subscription, implementation service, or consulting service. Do not invoice raw "token recharge" as unrelated consulting unless the real delivered service is consulting.

## Contract Clauses To Include

- service nature: resale, technical service, SaaS, implementation, or consulting
- upstream terms and acceptable-use obligations
- prohibited uses
- customer data responsibility
- data processing, retention, deletion, and geography
- AI output review requirement
- upstream price, model, and availability changes
- SLA and compensation boundaries
- invoice and tax handling
- refund and red-invoice process
- termination for abuse, regulatory request, platform request, or upstream suspension

## Sources For Legal Review

- China CAC: Generative AI Services Interim Measures: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
- China CAC: Personal Information Protection Law: https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- China CAC: Data Cross-Border Flow Rules: https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- China CAC: AI Generated/Synthetic Content Labeling Measures: https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm
- OpenAI Services Agreement: https://openai.com/policies/services-agreement/
- OpenAI Service Credit Terms: https://openai.com/policies/service-credit-terms/
- State Tax Administration digital invoice notice: https://fgk.chinatax.gov.cn/zcfgk/c100012/c5236067/content.html
