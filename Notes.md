# WH-347 Form Generator - Project Notes

## MVP Requirements

1. **File Upload**
   - User uploads a simple CSV/Excel timesheet
   - Format: One row per employee per week
   - Required fields: Employee, Trade, Mon-Sun hours, BaseRate, FringeCash

2. **Form Generation**
   - Backend maps fields to WH-347 PDF
   - Calculates gross pay & totals
   - Fills the government form
   - Inserts a digital signature block

3. **Delivery**
   - User downloads completed WH-347
   - 100% compliant, ready to send to prime contractor or agency

## Marketing Copy

**Landing Page:**
- "Stop spending Fridays on WH-347s"
- "Upload your CSV, download a signed certified-payroll form in 60 seconds"
- "Free for early testers – we'll even do the first week manually for you"
- Include 20-second demo video: CSV upload → processing → PDF download

## Competitive Analysis

| Vendor                                                                                                   | Core pitch & target user                                                                                                                                | Typical price point\*                                                                                                                     | Notable strengths                                                                                              | Gaps / opportunities for **your** MVP                                                                                            |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **[LCPtracker](https://lcptracker.com/)**                                                                | Cloud platform for GCs, public agencies and DOT-scale projects; subs upload data through the portal.                                                    | Not public; mid-five-figure SaaS for a prime contract is common. Est. annual revenue **\$18-26 M** ([Growjo][1])                          | rich validation rules, daily logs, workforce analytics, IRA/PWA compliance add-ons ([LCPtracker][2])           | priced + sized for large primes; steep learning curve for a 10-person specialty sub.                                             |
| **[eMars Compliant Client](https://emarsinc.com/)**                                                      | Web-based WH-347 generator + error checker used by primes **and** subs.                                                                                 | “Inexpensive” but opaque; press article notes monthly or flat-fee per project contracts ([Construction Today][3])                         | real-time error flagging; HUD roots; claims “8-minute Friday payroll” ([Construction Today][4])                | no public self-serve signup; pricing discovery by phone demo; brand feels dated.                                                 |
| **[Points North Certified Payroll Reporting](https://www.points-north.com/certified-payroll-reporting)** | Add-on that plugs into ADP, QuickBooks, UKG, etc.  Popular with payroll bureaus & midsize subs.                                                         | Marketplace listing shows **\$175 / mo** base + **\$7.25 per report**; \$995-\$4,995 setup depending on head-count ([ADP Marketplace][5]) | 40+ state & municipal formats; “push-button” exports for agency portals ([points-north.com][6])                | high upfront fee; UI optimised for payroll pros, not owners/foremen; no freemium tier.                                           |
| **[Quantum Project Manager](https://www.quantumss.com/ProjectManager/payroll.asp)**                      | Windows desktop app (one-time licence) that prints WH-347 and 20+ state forms; integrates with QuickBooks Desktop.                                      | **\$349 one-time** for the Certified-Payroll module ([quantumss.com][7])                                                                  | cheap, offline, no subscription; includes tax tables; exports upload files for LCPtracker ([quantumss.com][8]) | PC-only; manual install & updates; no cloud; no collaboration with GC.                                                           |
| **Procore (+ HCM TradeSeal)**                                                                            | Procore itself doesn’t create WH-347; instead it pushes timesheets to payroll/HCM systems that handle certified payroll. TradeSeal sells the connector. | Procore licence + TradeSeal integration (quote only). ([HCM TradeSeal][9])                                                                | already embedded in many GCs; seamless timesheet → payroll sync.                                               | Still requires a **separate** certified-payroll engine; overkill for a small subcontractor that just wants a WH-347 this Friday. |

[1]: https://growjo.com/company/LCPtracker?utm_source=chatgpt.com "LCPtracker: Revenue, Competitors, Alternatives - Growjo"
[2]: https://lcptracker.com/?utm_source=chatgpt.com "LCPtracker | Certified Payroll Reporting Software"
[3]: https://construction-today.com/news/streamlining-compliance-the-power-of-compliant-client-by-emars-in-construction-payroll-management/?utm_source=chatgpt.com "Streamlining Compliance: The Power of Compliant Client by eMars ..."
[4]: https://construction-today.com/news/emars-6/?utm_source=chatgpt.com "The eMars electronic certified payroll system gives construction ..."
[5]: https://apps.adp.com/en-us/apps/253943/points-north-certified-payroll-reporting-for-run-powered-by-adp/configure?utm_source=chatgpt.com "Points North Certified Payroll Reporting for RUN Powered by ADP ..."
[6]: https://www.points-north.com/certified-payroll-reporting?utm_source=chatgpt.com "Certified Payroll Reporting Software - Points North"
[7]: https://www.quantumss.com/productpricing.htm?utm_source=chatgpt.com "Quantum Project Manager - Product Pricing"
[8]: https://www.quantumss.com/ProjectManager/LCPtracker.htm?utm_source=chatgpt.com "Quantum Project Manager Certified Payroll Reports - LCPtracker file ..."
[9]: https://hcmtradeseal.com/erp-systems/procore-certified-payroll-integration/ "Get Procore Certified Payroll Integration with HCM TradeSeal"


## WH-347 Processing Workflow

1. Form is attached to weekly pay application
2. Submission flow: Sub → Prime or Prime → Agency (often via portal)
3. Prime reviews/verifies wage rates, apprentice ratios, signatures
4. Submitted to contracting officer (DOT, Corps of Engineers, VA, municipal agency)
5. Archived for 3 years per federal rule 29 CFR §5.5(a)(3)(i)

**Value Proposition:** A one-click PDF that's already signed and totaled removes friction at every step.

## Go-to-Market Strategy

1. **Target primes first**
   - They can introduce you to their subs if they see value
   - Sample call script: "I saw you just won [PROJECT] ($X M). I'm piloting a tool that lets your subs upload a timesheet and it spits out a signed WH-347 PDF in one minute. Could I do a free run for your first week so your pay-app isn't delayed?"

2. **Demo and expand**
   - Use sample sheet + PDF filler to demonstrate
   - Create a short demo video
   - Ask each prime who else needs this on their project
   - Goal: Land two subs → gather real weekly data to refine MVP

3. **Pricing model**
   - $99/month per sub (<50 employees) 
   - $199/month per prime (unlimited subs)
   - Approximately half the cost of next cheapest option

## Key Terminology
- Certified Payroll
- Fringe Benefits/Fringe Credit

## Sample Data Format

| Employee Name | Last-4 SSN | Work Classification | Sun | Mon | Tue | Wed | Thu | Fri | Sat | Total Hrs | Rate (Straight) | Rate (OT) | Gross Pay | FICA | Federal W/H | State W/H | Other Deduction | Total Deductions | Net Wages |
|---------------|------------|---------------------|-----|-----|-----|-----|-----|-----|-----|-----------|-----------------|-----------|-----------|------|-------------|-----------|-----------------|------------------|-----------|
| Juan Rivera   | 1234       | Electrician         | 0   | 8   | 8   | 8   | 8   | 4   | 0   | 36        | 42.50           | 63.75     | 1,530.00  | 120.15 | 250.00     | 110.00    | 25.00           | 505.15           | 1,024.85  |
| Kelly Smith   | 9876       | Plumber             | 0   | 8   | 8   | 8   | 8   | 8   | 0   | 40        | 38.00           | 57.00     | 1,520.00  | 140.60 | 275.00     | 125.00    | 25.00           | 565.60           | 954.40    |


# Interesting Links
- https://www.quantumss.com/projectmanager/certifiedpayrollreports.htm
