# ruff: noqa: E501

HYBRID_RAG_QUESTIONS = [
    # Source fragment: src/helpers/router_questions_group1.py
        # billing/billing_codes.pdf — Introduction
        "In the MediAssist Insurance Billing Code Reference, what is the difference between ICD-10 diagnosis codes and procedure codes?",
        "According to the billing code reference, why should staff code a diagnosis to the highest level of detail supported by the clinical record?",
        "What does the BILL-CODE-010 guide say about unspecified diagnosis codes and their effect on claim queries or rejections?",
        "Are the package rates in the MediAssist billing code reference guaranteed settlement amounts, or can policy terms change the final payment?",

        # billing/billing_codes.pdf — 1. Top 30 Diagnosis Codes Used at MediAssist
        "In the MediAssist diagnosis-code table, what ICD-10 code and package rate apply to NSTEMI?",
        "Which billing code in BILL-CODE-010 represents type 2 diabetes with renal complications, and is pre-authorisation required?",
        "What are the typical length of stay and package amount for a femoral neck fracture under the MediAssist diagnosis reference?",
        "Which diagnosis codes in the billing reference are associated with oncology packages rather than fixed package prices?",

        # billing/billing_codes.pdf — 2. Common Procedure Codes
        "According to the MediAssist procedure-code table, what code and package rate should be used for coronary angiography?",
        "What is the procedure code for PTCA with a single stent, and is it classified as inpatient or day care?",
        "Which procedure code covers laparoscopic cholecystectomy in the BILL-CODE-010 reference?",
        "What are the package amount and care setting for haemodialysis per session in the MediAssist procedure list?",

        # billing/billing_codes.pdf — 3. Empanelled Insurer Panel
        "In the MediAssist insurer panel, which portal and contact number should be used for a Star Health claim?",
        "Which insurers in BILL-CODE-010 route claims through an external TPA rather than an in-house claims team?",
        "What is the correct claim portal for New India Assurance, and which TPA handles those claims?",
        "Before submitting an insurer claim, what does the billing code reference say staff must confirm about the TPA?",

        # billing/billing_codes.pdf — 4. Exclusions Reference
        "According to the BILL-CODE-010 exclusions table, what does exclusion code EXCL-01 mean and can it be appealed?",
        "Which exclusion code applies when a day-care procedure is incorrectly submitted as an inpatient claim?",
        "What is the usual outcome for EXCL-05 cosmetic or aesthetic procedures in the MediAssist exclusions reference?",
        "How should staff respond to a claim rejected under EXCL-08 for documentation submitted after the deadline?",

        # billing/billing_codes.pdf — 5. Room Rent & Sub-limit Reference
        "In the MediAssist room-rent reference, what room category is typically eligible for a policy with a sum insured below ₹3 lakh?",
        "What proportionate deduction applies when a patient with twin-sharing eligibility upgrades to a higher room category?",
        "According to BILL-CODE-010, what sum-insured range generally supports a single private room?",
        "What should staff verify before assigning a deluxe or suite room under the room-rent and sub-limit rules?",

        # billing/billing_codes.pdf — 6. Common Co-pay & Sub-limits
        "What senior-citizen co-pay percentage is listed in the MediAssist billing reference?",
        "How does the BILL-CODE-010 guide describe zone-based co-pay between metro and non-metro locations?",
        "What cataract sub-limit per eye is shown in the common co-pay and sub-limits table?",
        "What maternity sub-limits are listed for normal delivery and LSCS in the MediAssist billing code reference?",

        # billing/billing_codes.pdf — 7. Pre-authorisation Document Checklist
        "What documents does BILL-CODE-010 require for an insurer pre-authorisation request?",
        "Does the MediAssist pre-auth checklist require an admission note with a provisional diagnosis and ICD-10 code?",
        "Which patient identity and policy documents must be attached to a pre-authorisation submission?",
        "What additional records are required for an accident case under the MediAssist pre-authorisation checklist?",

        # billing/claim_submission_guide.md — Purpose & Scope
        "What is the scope of the MediAssist Claim Submission & Escalation Guide for billing executives?",
        "Which four claim journeys are covered by BILL-OPS-011?",
        "Does the claim submission guide apply to all empanelled insurers, including insurer-specific portal or TPA variations?",
        "What is the “golden rule” in the MediAssist claim operations guide regarding audit trails and MBP logging?",

        # billing/claim_submission_guide.md — How claims flow at MediAssist
        "According to the MediAssist claim-flow diagram, what steps occur between admission and the final bill?",
        "When does a patient move from the cashless route to the reimbursement route in the BILL-OPS-011 workflow?",
        "Where does pre-authorisation enhancement fit into the MediAssist claims process?",
        "What happens in the claim flow when the insurer raises a query or rejection?",

        # billing/claim_submission_guide.md — 1. Cashless Claim Process
        "When should billing staff use the cashless claim process at MediAssist?",
        "What expenses remain payable by the patient under the cashless route described in BILL-OPS-011?",
        "Is cashless insurance available for both planned and emergency admissions under the MediAssist guide?",
        "Who pays the hospital directly when an eligible cashless claim is approved?",

        # billing/claim_submission_guide.md — 1.1 Pre-authorisation timeline
        "According to BILL-OPS-011, how far in advance must staff submit pre-authorisation for a planned admission?",
        "What is the deadline for raising a cashless pre-auth after an emergency admission?",
        "What does the MediAssist guide identify as the most common avoidable reason for emergency cashless denial?",
        "Can staff submit an emergency pre-authorisation with provisional information and enhance it later?",

        # billing/claim_submission_guide.md — 1.2 Documents required for pre-authorisation
        "What documents are required for a cashless pre-authorisation request under the MediAssist claim guide?",
        "Does the pre-auth checklist require an insurer-specific form and a treatment plan with estimated length of stay?",
        "Which diagnosis and coding information must appear in the admission note for a MediAssist pre-auth?",
        "What extra documents are required for an accident-related claim, according to BILL-OPS-011?",

        # billing/claim_submission_guide.md — 1.3 Step-by-step
        "What eligibility checks must a billing executive complete before submitting a cashless claim?",
        "Where in the MediAssist Billing Portal should staff create a new cashless claim?",
        "After submitting through the insurer portal, what reference information must be logged back into MBP?",
        "How quickly must staff respond to an insurer query during the cashless claim process?",

        # billing/claim_submission_guide.md — 1.4 Typical approval turnaround (initial pre-auth)
        "What are the standard initial pre-authorisation SLAs for the insurers listed in BILL-OPS-011?",
        "Which insurer has the fastest typical cashless pre-auth turnaround in the MediAssist guide?",
        "Which insurer is noted for frequent clinical queries on cardiac packages?",
        "What should billing staff do when an insurer does not respond within its stated SLA?",

        # billing/claim_submission_guide.md — 1.5 Worked example
        "In the BILL-OPS-011 NSTEMI example, how quickly was the emergency pre-authorisation raised after admission?",
        "What diagnosis code and package rate were used in the HDFC Ergo chest-pain example?",
        "How was the clinical query about the troponin trend handled in the worked example?",
        "What approved amount and non-payable amount did HDFC Ergo provide in the MediAssist example?",

        # billing/claim_submission_guide.md — 2. Reimbursement Claim Process
        "When should a MediAssist billing executive use the reimbursement claim process instead of cashless?",
        "Who pays the hospital directly in the reimbursement pathway described in BILL-OPS-011?",
        "What situations can lead to a reimbursement claim, such as a non-empanelled insurer or declined cashless request?",
        "What responsibility does the billing executive retain after the patient leaves with a reimbursement claim?",

        # billing/claim_submission_guide.md — 2.1 Documents required
        "What original documents must the patient receive for a reimbursement claim under the MediAssist guide?",
        "Does the reimbursement checklist require a consultant-signed discharge summary and investigation reports?",
        "What banking information must be included with a reimbursement claim submission?",
        "Which KYC, policy, pharmacy, and payment records are required for reimbursement?",

        # billing/claim_submission_guide.md — 2.2 Step-by-step
        "What should billing staff explain to the patient at discharge when the claim is reimbursement rather than cashless?",
        "Which original documents should be issued to the patient and which copies should be retained in MBP?",
        "How should staff verify that ICD-10 and procedure codes match the reimbursement bills?",
        "What is the typical reimbursement submission deadline after discharge, and why must staff confirm it with the insurer?",

        # billing/claim_submission_guide.md — 3. Pre-Authorisation Enhancement
        "When should a billing executive raise an enhancement to an approved cashless amount?",
        "What kinds of treatment changes can require a pre-authorisation enhancement under BILL-OPS-011?",
        "How does an enhancement relate to the original approved pre-auth amount?",
        "Is an enhancement submitted as a new unrelated claim or linked to the original pre-authorisation?",

        # billing/claim_submission_guide.md — 3.1 When to raise
        "According to the MediAssist claim guide, what percentage increase over the approved amount should trigger an enhancement?",
        "Should staff raise an enhancement when a new implant or procedure is added during admission?",
        "What should billing staff do if the patient’s length of stay exceeds the approved package days?",
        "Does ICU escalation qualify as a reason to request pre-authorisation enhancement?",

        # billing/claim_submission_guide.md — 3.2 Documents required
        "What documents must accompany a pre-authorisation enhancement request in BILL-OPS-011?",
        "Why must the enhancement form reference the original pre-auth number?",
        "What clinical information should the treating doctor provide to justify an enhancement?",
        "Are revised cost estimates and updated treatment plans required for an enhancement?",

        # billing/claim_submission_guide.md — 3.3 Process
        "When must staff raise an enhancement relative to exhaustion of the original approved amount?",
        "How should an enhancement be marked and submitted through the insurer portal?",
        "How is an enhancement represented in the MediAssist Billing Portal?",
        "Who should receive an escalation if an enhancement is delayed for more than six hours before discharge?",

        # billing/claim_submission_guide.md — 4. Claim Rejection Response
        "What does the MediAssist guide say about responding to a rejected insurance claim?",
        "Which types of claim rejection are often reversible through an appeal?",
        "Where can billing staff find the rejection-code mapping used for claim responses?",
        "What is the general purpose of the counter-response process in BILL-OPS-011?",

        # billing/claim_submission_guide.md — 4.1 Common rejection codes
        "What does rejection code EXCL-01 mean in the MediAssist claim rejection table?",
        "How should staff respond to EXCL-03 when the treating provider was not empanelled?",
        "What is the correct response to a day-care procedure submitted incorrectly as an inpatient claim?",
        "Which rejection code covers an investigation-only admission, and what supporting document may help?",

        # billing/claim_submission_guide.md — 4.2 Counter-response template
        "What subject line should be used for a reconsideration request under the MediAssist rejection-response template?",
        "Which identifiers must appear in the reconsideration email for a rejected claim?",
        "What documents and consultant clarification should be attached to an EXCL-code appeal?",
        "How does the BILL-OPS-011 template request review within the insurer’s reconsideration window?",

        # billing/claim_submission_guide.md — 4.3 Deadlines
        "How long does the MediAssist guide usually allow for filing a reconsideration or appeal after rejection?",
        "From what event is the 90-day appeal period generally calculated?",
        "Where should staff escalate a denied appeal before approaching the Insurance Ombudsman?",
        "What should billing staff verify because insurer appeal windows may differ?",

        # billing/claim_submission_guide.md — 5. Escalation Matrix
        "Who is the first contact when a cashless pre-auth is delayed under the MediAssist escalation matrix?",
        "What is the escalation path for a clinically rejected claim?",
        "How should staff escalate a payment delayed more than 30 days after discharge?",
        "Who is the final escalation for an enhancement that remains unapproved before discharge?",

        # billing/claim_submission_guide.md — Escalation discipline
        "What claim details must every escalation email include according to BILL-OPS-011?",
        "When should staff move from the first escalation contact to the next escalation level?",
        "Who must be copied on an escalation beyond the first contact?",
        "What is the maximum time a billing executive should allow to pass when an overdue claim response has not been received?",

        # billing/claim_submission_guide.md — 6. Fraud Prevention
        "What is the MediAssist policy position on internal or external claim fraud?",
        "Why are billing executives described as the first line of defence against claim fraud?",
        "What controls does BILL-OPS-011 require before submitting high-value claims?",
        "How long must claim files be retained under the MediAssist fraud-prevention rules?",

        # billing/claim_submission_guide.md — 6.1 Warning signs
        "What diagnosis, procedure, and investigation mismatches are listed as fraud warning signs?",
        "How can inflated or duplicated billing line items indicate possible claim fraud?",
        "What document irregularities should billing executives look for before claim submission?",
        "What does “up-coding” mean in the fraud-warning section of the MediAssist guide?",

        # billing/claim_submission_guide.md — 6.2 Controls
        "When is an independent dual-check required for a MediAssist insurance claim?",
        "What must the second billing executive verify for a claim above ₹2,00,000?",
        "What events and timestamps must be included in the MBP audit trail?",
        "Does BILL-OPS-011 allow billing executives to share insurer portal credentials?",

        # billing/claim_submission_guide.md — 6.3 Reporting
        "Within what time must suspected claim fraud be reported under the MediAssist guide?",
        "Which roles must receive a suspected-fraud report?",
        "Where in MBP should staff report a compliance concern?",
        "Can a fraud report be made confidentially, and does the guide address retaliation against good-faith reporters?",

        # billing/claim_submission_guide.md — 7. Key Performance Indicators (KPIs)
        "Which monthly performance indicators are used to measure MediAssist billing executives?",
        "What target does BILL-OPS-011 set for pre-authorisations raised within SLA?",
        "What query response time target is listed in the claim-operations KPI table?",
        "What rejection-rate and first-pass approval targets are considered indicative for billing staff?",

        # clinical/diagnostic_reference.pdf — 1. Haematology Reference Ranges
        "What normal haemoglobin ranges for male and female patients are listed in the MediAssist diagnostic reference?",
        "Which haematology results are considered critical for white blood cell and platelet counts?",
        "What PT/INR and aPTT values trigger anticoagulant review or bleeding-risk action?",
        "How should staff interpret a marked D-dimer rise according to LAB-DIAG-007?",

        # clinical/diagnostic_reference.pdf — 2. Biochemistry Reference Ranges
        "What sodium and potassium values are outside the critical ranges in the MediAssist biochemistry table?",
        "What action is recommended for a rapid creatinine rise under the diagnostic reference?",
        "Which fasting glucose values require treatment for hypoglycaemia or hyperglycaemia?",
        "What troponin I value is considered significant, and what correlation does the guide recommend?",

        # clinical/diagnostic_reference.pdf — 3. Urine Analysis Interpretation
        "What can a positive urine protein dipstick indicate, and what follow-up does LAB-DIAG-007 recommend?",
        "How should staff interpret glucose detected on urine dipstick testing?",
        "What are the possible causes and next steps for a positive urine blood result?",
        "What does the combination of positive nitrites and leucocytes suggest in the MediAssist urine-analysis guide?",

        # clinical/diagnostic_reference.pdf — 4. ECG Interpretation Quick Guide
        "What heart-rate range is normal in the MediAssist ECG reference, and when are bradycardia or tachycardia indicated?",
        "Which rhythm features distinguish atrial fibrillation, ventricular tachycardia, and SVT in LAB-DIAG-007?",
        "What PR interval indicates first-degree AV block?",
        "What ST-elevation finding triggers the STEMI protocol according to the diagnostic reference?",

        # clinical/diagnostic_reference.pdf — 5. Arterial Blood Gas (ABG) Interpretation
        "What pH range is normal in the MediAssist ABG interpretation guide?",
        "How do PaCO₂ and bicarbonate help identify the respiratory or metabolic component of an ABG abnormality?",
        "What PaO₂ value indicates respiratory failure in LAB-DIAG-007?",
        "What does a lactate level above 4 mmol/L suggest, and what quick ABG interpretation sequence is recommended?",

        # clinical/diagnostic_reference.pdf — 6. Thyroid & Cardiac/Sepsis Markers
        "What TSH and free T4 ranges are listed in the MediAssist diagnostic reference?",
        "Which test is described as the first-line thyroid screen, and which test confirms thyroid status?",
        "What does an elevated BNP or NT-proBNP suggest according to LAB-DIAG-007?",
        "What lactate value triggers a sepsis-6 review?",

        # clinical/diagnostic_reference.pdf — 7. Radiology Reporting Flags
        "Which urgent findings on a chest X-ray require attention under the MediAssist radiology reference?",
        "What CT-head findings are classified as urgent in LAB-DIAG-007?",
        "What abdominal-ultrasound findings should be treated as urgent?",
        "How quickly must a verbal or critical radiology alert be communicated after image acquisition?",

        # clinical/diagnostic_reference.pdf — 8. Microbiology & Culture Turnaround
        "What are the preliminary and final reporting times for blood cultures in the MediAssist diagnostic guide?",
        "How long does a urine culture typically take to produce a final report?",
        "What is the expected turnaround for an urgent CSF Gram stain and the final CSF culture?",
        "When should clinicians de-escalate empirical antibiotics according to the microbiology section?",

        # clinical/diagnostic_reference.pdf — 9. Tumour Markers (interpret with caution)
        "Which tumour marker is associated with prostate disease in LAB-DIAG-007?",
        "What caution does the MediAssist diagnostic reference give about using PSA for screening?",
        "Which tumour marker is associated with ovarian disease, and why can its interpretation be misleading?",
        "How should CEA and AFP results be interpreted according to the tumour-marker section?",

        # clinical/diagnostic_reference.pdf — 10. Critical Value Notification Protocol
        "How soon must the laboratory telephone the treating ward or doctor after identifying a critical value?",
        "Within what time must the doctor acknowledge and document the action for a critical result?",
        "Who should the laboratory contact if the treating doctor cannot be reached?",
        "What is the escalation sequence for unacknowledged critical laboratory values in LAB-DIAG-007?",
    # Source fragment: src/helpers/router_questions_group2.py
        # FILE: clinical/drug_formulary.pdf
        # SECTION: Document Scope and Formulary Purpose
        "What does the MediAssist Approved Drug Formulary say about selecting medicines for use across its hospitals?",
        "According to the Approved Drug Formulary, what should prescribers do when a required medicine is not listed?",
        "What dosing, storage, tier, and substitution information is covered in this MediAssist formulary?",
        "Which staff members are authorised to access the Approved Drug Formulary?",

        # SECTION: Formulary Tier System
        "How are medicines classified into Tiers 1 through 4 in the Approved Drug Formulary?",
        "What approval level is required for a Tier 3 medicine according to the formulary?",
        "Which formulary tier requires approval from the Chief Medical Officer?",
        "What prescribing and subsidy rules apply to Tier 1 generic medicines?",

        # SECTION: 1. Antimicrobials
        "What are the formulary doses, routes, and storage requirements for the listed antimicrobial drugs?",
        "Which antimicrobials in the Approved Drug Formulary require HOD or CMO approval?",
        "What cautions are listed for vancomycin, linezolid, ceftriaxone, and colistin?",
        "Which antimicrobial medicines require therapeutic drug monitoring or close laboratory monitoring?",
        "What are the formulary instructions for amoxicillin in a patient with penicillin allergy?",
        "Which antimicrobial should be de-escalated when culture results are available?",
        "What storage condition applies to reconstituted piperacillin-tazobactam?",
        "What restrictions or safety warnings are listed for metronidazole, ciprofloxacin, clindamycin, and doxycycline?",

        # SECTION: 2. Cardiovascular Drugs
        "What standard doses and routes are listed for the cardiovascular medicines in the Approved Drug Formulary?",
        "Which cardiovascular drugs are contraindicated in pregnancy?",
        "What contraindications are listed for metoprolol and digoxin?",
        "According to the formulary, when should potassium or renal function be considered before using spironolactone?",
        "What dose range is given for furosemide, and when should it be avoided?",
        "Which cardiovascular drugs have bleeding-related contraindications?",
        "What is the formulary dose for clopidogrel, including its loading dose?",
        "What dose and safety warning are provided for atorvastatin?",

        # SECTION: 3. Analgesics & Antipyretics
        "What doses and routes are listed for paracetamol, ibuprofen, and diclofenac in the Approved Drug Formulary?",
        "What is the maximum daily dose of paracetamol stated in the formulary?",
        "Which analgesics are classified as controlled or scheduled medicines?",
        "What narcotic-register requirements apply to morphine and fentanyl?",
        "What dosing guidance is provided for buprenorphine and pregabalin?",
        "Which analgesics can be administered intravenously according to the formulary?",
        "How does the formulary distinguish the controlled status of tramadol, morphine, fentanyl, and pregabalin?",
        "What route options and dosing instructions are given for fentanyl?",

        # SECTION: 4. Respiratory Drugs
        "What are the formulary doses and routes for salbutamol and ipratropium?",
        "What administration cautions are listed for budesonide and montelukast?",
        "Which respiratory medicine requires therapeutic drug monitoring?",
        "What adverse effects are associated with salbutamol and budesonide in the Approved Drug Formulary?",
        "What standard dose is given for theophylline?",
        "Which respiratory drug has a narrow therapeutic index?",
        "What advice is provided about mouth care after using inhaled budesonide?",
        "What is the listed nocturnal dose for montelukast?",

        # SECTION: 5. Gastrointestinal & Endocrine Drugs
        "What doses and routes are listed for pantoprazole, ondansetron, and metoclopramide?",
        "What safety precautions apply to regular insulin in the Approved Drug Formulary?",
        "How should levothyroxine be taken, and how often should TSH be rechecked?",
        "What monitoring advice accompanies IV hydrocortisone?",
        "Which medicines in this section require review for QTc effects or extrapyramidal symptoms?",
        "What is the standard dose of pantoprazole?",
        "What dose range is listed for levothyroxine?",
        "What does the formulary say about glucose monitoring during hydrocortisone stress dosing?",

        # SECTION: 6. Renal Dose Adjustment
        "Which selected medicines require renal dose adjustment in the Approved Drug Formulary?",
        "What metformin guidance is given for eGFR 30–50 and eGFR below 30?",
        "How should meropenem dosing change when eGFR is reduced?",
        "What does the formulary recommend for vancomycin dosing in renal impairment?",
        "How should enoxaparin be adjusted when eGFR is below 30?",
        "What renal precautions apply to digoxin?",
        "Which renal-dose recommendations require therapeutic drug monitoring or specialist input?",
        "What should prescribers confirm before using the illustrative renal dosing table?",

        # SECTION: 7. High-Alert Medications
        "Which medicines are identified as high-alert medications in the Approved Drug Formulary?",
        "What independent double-check procedure is required before administering a high-alert medicine?",
        "How should insulin be stored, labelled, and dose-checked?",
        "What are the formulary safety rules for concentrated potassium chloride?",
        "What storage and documentation requirements apply to morphine?",
        "What special scheduling safeguard is required for methotrexate?",
        "How should heparin be stored and monitored?",
        "Which high-alert medicines are restricted to trained personnel?",

        # SECTION: 8. Substitution Policy
        "When may a pharmacist substitute a Tier 2 medicine with a Tier 1 generic?",
        "What approval is needed for Tier 3 or Tier 4 drug substitutions?",
        "Where must all formulary substitutions be recorded?",
        "Does a Tier 2-to-Tier 1 substitution require a prescription change according to the formulary?",
        "How are substitutions made visible on the patient record?",
        "What is the approved process when the preferred branded medicine is unavailable?",

        # SECTION: 9. Out-of-Formulary Request Process
        "What steps must a prescriber follow to request a medicine outside the Approved Drug Formulary?",
        "What information must be included in an out-of-formulary request?",
        "How quickly must the Pharmacy & Therapeutics Committee review an OOF request?",
        "Who may approve an urgent or life-saving out-of-formulary request on the same day?",
        "What does OOF mean in the formulary request process?",
        "What is the difference between the standard and urgent out-of-formulary approval routes?",

        # SECTION: 10. Look-Alike, Sound-Alike Medications
        "What dispensing checks are required for look-alike, sound-alike medicines?",
        "Which dopamine and dobutamine safety distinction is listed in the Approved Drug Formulary?",
        "How should staff distinguish ephedrine from epinephrine before dispensing?",
        "What is the clinical difference between hydroxyzine and hydralazine in the LASA table?",
        "Which drug pairs require confirmation of spectrum, indication, potency, or haemodynamic effect?",
        "What patient and medicine details must be confirmed before dispensing a LASA medication?",
        "What does Tall Man lettering signify in the formulary’s dispensing-safety guidance?",
        "Which LASA pair includes clonazepam and clonidine?",

        # SECTION: 11. IV Fluids Quick Reference
        "What are the typical uses of 0.9% sodium chloride and Ringer’s lactate in the formulary?",
        "Which IV fluid should be avoided in hyperkalaemia?",
        "How is 5% dextrose described in terms of tonicity and clinical use?",
        "What is DNS, and what use is listed for it?",
        "When is 20% mannitol used according to the Approved Drug Formulary?",
        "Which IV fluids are described as isotonic?",
        "What IV fluid is listed for raised intracranial pressure?",
        "What does the formulary say about the specialist status of mannitol use?",

        # FILE: clinical/treatment_protocols.pdf
        # SECTION: Document Scope and Clinical Use
        "What conditions are covered by the MediAssist Standard Treatment Protocols?",
        "Who is authorised to use the first-line management guidelines in this document?",
        "How should clinicians apply the treatment protocols alongside clinical judgement?",
        "What purpose do the ICD-10 codes serve in the Standard Treatment Protocols?",

        # SECTION: A. Type 2 Diabetes Mellitus
        "What diagnostic criteria for Type 2 Diabetes Mellitus are given in the MediAssist treatment protocols?",
        "What is the first-line metformin regimen for Type 2 Diabetes in this protocol?",
        "When should glipizide be added after metformin therapy?",
        "When should a clinician consider an SGLT2 inhibitor or GLP-1 agonist?",
        "How often should HbA1c be checked before and after diabetes becomes stable?",
        "What glucose, renal, urine ACR, fundus, and foot monitoring is recommended?",
        "When does the protocol recommend endocrinology referral?",
        "What should happen when a patient with Type 2 Diabetes has an eGFR below 45?",

        # SECTION: B. Hypertension — Stage 2
        "What diagnostic blood-pressure criteria define Stage 2 hypertension in the treatment protocols?",
        "What is the recommended first-line drug and dose for Stage 2 hypertension?",
        "When should amlodipine be titrated to 10 mg?",
        "What is the second-line telmisartan regimen in this hypertension protocol?",
        "What monitoring is required after starting an ACE inhibitor or ARB?",
        "What lifestyle targets are recommended for sodium, BMI, alcohol, and exercise?",
        "What cautions apply to telmisartan and hydrochlorothiazide?",
        "How should home blood-pressure monitoring be incorporated into follow-up?",

        # SECTION: C. Community-Acquired Pneumonia
        "How does the treatment protocol use CURB-65 to assess community-acquired pneumonia?",
        "What CURB-65 score supports outpatient management?",
        "When does the protocol recommend general-ward admission or ICU/HDU consideration?",
        "What antibiotic regimen and duration are recommended for outpatient pneumonia?",
        "When should azithromycin be added for atypical outpatient pneumonia?",
        "What inpatient antimicrobial regimen is specified for community-acquired pneumonia?",
        "When can IV therapy be switched to oral therapy?",
        "What SpO₂ monitoring and follow-up chest X-ray schedule are recommended?",

        # SECTION: D. Acute Myocardial Infarction — NSTEMI
        "What immediate treatments are required during the first 60 minutes of NSTEMI management?",
        "What aspirin and clopidogrel loading doses are listed in the NSTEMI protocol?",
        "What is the heparin bolus limit for NSTEMI?",
        "How quickly should a 12-lead ECG and high-sensitivity troponin be obtained?",
        "How is TIMI risk scoring used to determine an early invasive strategy?",
        "What ongoing medicines and doses are recommended after NSTEMI?",
        "What cautions apply to metoprolol and ramipril in the NSTEMI protocol?",
        "How quickly must cardiology on-call be notified after NSTEMI diagnosis?",

        # SECTION: E. Paediatric Fever Management
        "How does the paediatric fever protocol guide treatment by temperature range?",
        "What should staff do for a child with a temperature below 38 °C?",
        "When are oral paracetamol, tepid sponging, or IV paracetamol recommended?",
        "What weight-based oral paracetamol doses are listed for children under 5 kg and 5–10 kg?",
        "Which children should not receive oral ibuprofen according to the dosing table?",
        "What IV paracetamol dose is specified for the different paediatric weight bands?",
        "What paediatric fever danger signs require immediate escalation?",
        "What heart rate threshold is considered a red flag in a child under one year?",

        # SECTION: F. Dengue Fever
        "How does the dengue protocol classify patients without warning signs, with warning signs, and with severe dengue?",
        "What symptoms and laboratory findings indicate dengue with warning signs?",
        "What disposition is recommended for dengue without warning signs?",
        "When should a dengue patient be admitted for IV fluids?",
        "Which antipyretics should be used or avoided in dengue fever?",
        "How should isotonic fluids be titrated in dengue management?",
        "How often should platelet count and haematocrit be monitored?",
        "What combination of rising haematocrit and falling platelets suggests plasma leakage?",
        "When does the protocol recommend platelet transfusion?",
        "What pulse-pressure finding signals impending shock in dengue?",

        # SECTION: G. Acute Exacerbation of COPD
        "What clinical features define an acute exacerbation of COPD in the treatment protocols?",
        "What oxygen saturation target is recommended for an acute COPD exacerbation?",
        "Which bronchodilator combination and nebulised doses are specified?",
        "What corticosteroid regimen is recommended for acute COPD exacerbation?",
        "When should amoxicillin-clavulanate or doxycycline be given?",
        "When should non-invasive ventilation be considered?",
        "What arterial blood gas monitoring schedule is required?",
        "When should a COPD patient be escalated to ICU or HDU?",

        # SECTION: Appendix — Key Drug Interactions & Cautions
        "What interaction risk is associated with azithromycin and other QTc-prolonging medicines?",
        "How should clinicians manage the combination of an ACE inhibitor or ARB with spironolactone?",
        "What is the concern with metformin and iodinated contrast in patients with low eGFR?",
        "How should warfarin be managed with metronidazole or macrolides?",
        "What is the “triple whammy” combination identified in the treatment protocols?",
        "Why is pantoprazole preferred with clopidogrel over a high-dose PPI?",
        "What monitoring or avoidance actions are recommended for the listed drug interactions?",
        "What disclaimer does the Standard Treatment Protocols document give about clinical judgement and adverse drug reactions?",

        # FILE: equipment/equipment_manual.pdf
        # SECTION: Document Scope and Conventions
        "What equipment categories are covered by the MediAssist Equipment Operation & Maintenance Manual?",
        "Who is the intended audience for this equipment manual?",
        "What should staff do if the manufacturer’s instructions are more specific than this manual?",
        "What asset-tag format is used in the equipment manual?",
        "Where do the manual’s fault codes map in the maintenance ticketing system?",
        "What information should be associated with an equipment asset tag?",
        "What safety principle applies before operating any device described in the manual?",
        "Which department owns the Equipment Operation & Maintenance Manual?",

        # SECTION: A. Patient Monitoring System — MediAssist BM-500
        "What parameters does the MediAssist BM-500 patient monitor measure?",
        "What are the BM-500’s display size, battery-backup duration, and serial-number format?",
        "What setup sequence is specified for powering on the BM-500 and connecting its leads?",
        "In what order should ECG leads, the SpO₂ probe, and the BP cuff be connected?",
        "What are the default and adjustable alarm limits for SpO₂ and heart rate?",
        "What does BM-500 fault code E-01, E-02, or E-03 mean, and what action should staff take?",
        "What should staff do when the BM-500 reports fault E-12?",
        "What daily, monthly, and six-monthly maintenance is required for the BM-500?",
        "What tolerance applies to six-monthly NIBP calibration?",
        "When must the BM-500 be removed from service?",

        # SECTION: B. Infusion Pump — DriveFlow IP-200
        "What infusion modes and safety software are available on the DriveFlow IP-200?",
        "What programming steps are required before starting an infusion on the IP-200?",
        "How does the pump use the drug library and patient weight to calculate safe dosing?",
        "What occlusion-pressure settings are recommended for venous and arterial lines?",
        "Which high-alert drugs have hard or soft limits in the DriveFlow drug library?",
        "What do fault codes F-01, F-03, F-05, and F-08 mean on the infusion pump?",
        "What action is required when fault F-12 indicates a drug-library update?",
        "What cleaning and servicing schedule applies to the DriveFlow IP-200?",
        "When should the infusion pump battery be replaced?",
        "Which pump fault requires removal from service and a CMMS entry?",

        # SECTION: C. Autoclave Steriliser — SterilPro 3000
        "What chamber capacity and sterilisation cycles are provided by the SterilPro 3000?",
        "Which autoclave cycle should be used for wrapped sets and porous or hollow loads?",
        "What are the temperature, pressure, and hold time for the Gravity 121 cycle?",
        "What load types are suitable for the Gravity 134 cycle?",
        "When must the Bowie-Dick test be performed?",
        "What should staff do if the Bowie-Dick test fails?",
        "How often is the biological-indicator test required, and what does a positive result mean?",
        "What details must be recorded in the daily autoclave log?",
        "What action is required for SterilPro fault codes E-01, E-04, E-07, and E-11?",
        "Can the pre-vacuum cycle be run when fault E-11 is present?",

        # SECTION: D. Portable X-Ray Unit — RadiPro MX-150
        "What are the main features and serial-number format of the RadiPro MX-150?",
        "What kVp and mAs settings are recommended for an adult chest AP exposure?",
        "What technique chart values apply to paediatric chest, abdomen, pelvis, and knee imaging?",
        "What positioning or shielding notes are listed for the RadiPro technique chart?",
        "How far must personnel stand from the portable X-ray unit during exposure?",
        "What radiation-safety equipment must the operator wear?",
        "What do RadiPro fault codes F-02, F-05, and F-09 mean?",
        "What must staff do when the kV generator fault F-09 occurs?",
        "What battery-care and preventive-maintenance schedule is specified for the RadiPro?",
        "How often are kV/mAs calibration and radiation-leakage testing required?",

        # SECTION: E. Maintenance & Fault-Code Summary
        "Which equipment fault codes require immediate removal from service?",
        "What action is required for BM-500 fault E-12?",
        "What does DriveFlow IP-200 fault F-12 mean, and how should it be escalated?",
        "Which RadiPro fault must appear on an escalated maintenance ticket?",
        "What information should be included in a maintenance ticket for a device removed from service?",
        "Which devices are associated with codes E-12, F-12, and F-09?",
        "What does the manual require biomedical staff to do after recording one of these critical fault codes?",
        "How are escalated maintenance tickets reviewed according to the equipment manual?",

        # SECTION: F. Preventive Maintenance Calendar
        "What daily, weekly, monthly, and annual preventive-maintenance tasks are listed for each device?",
        "What daily checks are required for the BM-500 monitor?",
        "How often are BM-500 SpO₂ verification and NIBP calibration performed?",
        "What are the cleaning, functional-check, service, and battery-replacement intervals for the DriveFlow pump?",
        "What routine testing is required for the SterilPro 3000?",
        "What preventive-maintenance activities apply to the RadiPro MX-150?",
        "What equipment maintenance records must be entered into the CMMS?",
        "Who reviews escalated preventive-maintenance and fault tickets, and how often?",

        # SECTION: Record-Keeping
        "Where must preventive-maintenance activities and equipment faults be recorded?",
        "What types of device events require a CMMS or maintenance-ticket entry?",
        "How are escalated equipment tickets reviewed by Biomedical Engineering?",
        "What information should be retained for maintenance history and fault escalation?",
        "Why is CMMS documentation important for the devices covered in this manual?",

        # SECTION: G. Commissioning & Acceptance Testing
        "What commissioning checks must every new or repaired device pass before clinical use?",
        "What electrical-safety requirement is checked during equipment commissioning?",
        "How are functional tests assessed against manufacturer tolerances?",
        "What calibration documentation must be valid and available?",
        "How should asset tagging be verified during acceptance testing?",
        "What user-training and sign-off evidence is required before a device is released?",
        "Where must commissioning results be recorded?",
        "Who is responsible for conducting commissioning and acceptance testing?",

        # SECTION: H. Decontamination Before Service
        "What must happen before a device is handed to biomedical engineering or an external service engineer?",
        "Is a decontamination certificate required before equipment transport for service?",
        "How should visibly soiled equipment be handled before it leaves the clinical area?",
        "What surface-cleaning method does the manual generally recommend?",
        "Where should the completed decontamination certificate be attached?",
        "Why does the equipment manual require decontamination before service?",
        "What happens if equipment is not decontaminated before a maintenance ticket is raised?",
        "Who must be protected by the pre-service decontamination procedure?",

        # SECTION: I. Common Operator Errors & Troubleshooting
        "What should staff check first when the patient monitor shows no SpO₂ reading?",
        "How should an operator respond when NIBP measurements repeatedly retry?",
        "What are the likely causes and first checks when the infusion pump will not start?",
        "What should staff inspect when an autoclave cycle aborts?",
        "How should an operator troubleshoot a blank X-ray panel image?",
        "What patient or equipment factors can cause repeated NIBP retries?",
        "What first action is recommended for a disconnected or poorly positioned SpO₂ probe?",
        "What checks are advised for a RadiPro DR panel that is not displaying an image?",
    # Source fragment: src/helpers/router_questions_group3.py
        # general/code_of_conduct.pdf — 1. Professional Conduct
        "Under the MediAssist Code of Conduct, what professional behaviour is expected from employees?",
        "What does the Code of Conduct say about punctuality and respectful communication?",
        "How does the Code of Conduct address respect for the clinical and administrative hierarchy?",
        "What happens when verbal or physical abuse against a patient, visitor, or colleague is substantiated?",

        # general/code_of_conduct.pdf — 2. Patient Confidentiality
        "According to the Code of Conduct, who may access or receive patient records, diagnoses, and treatment details?",
        "What confidentiality and data-protection obligations apply to MediAssist staff?",
        "Does the Code of Conduct allow employees to photograph patients or patient charts using personal phones?",
        "What are the rules for sharing patient information outside authorised clinical and billing channels?",

        # general/code_of_conduct.pdf — 3. Conflict of Interest
        "What does the Code of Conduct say about referring patients to facilities in which an employee has a financial interest?",
        "Can staff refer patients to an external laboratory or pharmacy owned by them or their family?",
        "What relationships with pharmaceutical companies must doctors disclose?",
        "How often must doctors report speaking fees, sponsorships, or advisory roles to Compliance?",

        # general/code_of_conduct.pdf — 4. Social Media Policy
        "Under the Code of Conduct’s Social Media Policy, can staff post patient images or case details online?",
        "What restrictions apply to sharing identifiable patient information on social media?",
        "Does MediAssist permit employees to criticise the hospital, colleagues, or competitor hospitals online?",
        "How should employees distinguish personal opinions from MediAssist’s official position?",

        # general/code_of_conduct.pdf — 5. Gifts & Gratuity
        "What gift value is permitted under the MediAssist Code of Conduct?",
        "When must a gift from a patient or vendor be declared to administration?",
        "What should an employee do if they receive a gift worth more than ₹2,000?",
        "How does the Code of Conduct distinguish between gifts up to ₹500, gifts above ₹500, and gifts above ₹2,000?",

        # general/code_of_conduct.pdf — 6. Substance Abuse
        "What is MediAssist’s policy on reporting for duty under the influence of alcohol or drugs?",
        "Does the Code of Conduct allow staff to work while impaired by alcohol or prohibited substances?",
        "When may clinical staff be required to undergo substance testing?",
        "What happens if a clinical employee is involved in an adverse patient event and substance use is suspected?",

        # general/code_of_conduct.pdf — 7. Anti-Harassment Policy (POSH)
        "What does the MediAssist Code of Conduct say about the POSH Committee at each campus?",
        "Who chairs the campus Prevention of Sexual Harassment Committee?",
        "How can an employee file a workplace harassment complaint under the Code of Conduct?",
        "What email address is used for POSH complaints, and what is the internal investigation timeline?",
        "What penalties may apply when a harassment complaint is substantiated?",

        # general/code_of_conduct.pdf — 8. Data & Systems
        "Under the Code of Conduct, may staff install unauthorised software on hospital devices?",
        "Is sharing a MediAssist login password or user credential ever permitted?",
        "How quickly must a suspected data breach be reported to IT Security?",
        "What are the Code of Conduct rules for software installation, login sharing, and breach reporting?",

        # general/code_of_conduct.pdf — 9. Disciplinary Process
        "What are the four stages in MediAssist’s graduated disciplinary process?",
        "How does the Code of Conduct describe the progression from a verbal warning to termination?",
        "Which types of misconduct may lead to immediate termination without completing all disciplinary stages?",
        "Does patient harm, data theft, billing fraud, or assault qualify as gross misconduct under this policy?",
        "Is due process still required when gross misconduct may result in immediate termination?",

        # general/code_of_conduct.pdf — 10. Anti-Bribery & Anti-Corruption
        "What does the Code of Conduct prohibit regarding bribes, kickbacks, and improper inducements?",
        "Are facilitation payments allowed to speed up routine hospital approvals?",
        "What is MediAssist’s policy on referral commissions or ‘cut practice’?",
        "Can an employee accept an improper payment connected with procurement, billing, recruitment, or patient referrals?",
        "What consequences may apply to referral commissions under the anti-corruption rules?",

        # general/code_of_conduct.pdf — 11. Vendor & Procurement Conduct
        "What procurement process must MediAssist staff follow when selecting vendors?",
        "How many quotations are required for purchases above ₹50,000?",
        "What must an employee do if they or a family member has an interest in a vendor?",
        "When must staff recuse themselves from vendor selection or procurement decisions?",
        "Who should receive a declaration of a personal or family vendor interest?",

        # general/code_of_conduct.pdf — 12. Whistleblower Protection
        "How does the MediAssist Code of Conduct protect employees who report genuine ethical or legal concerns?",
        "Where can staff confidentially report suspected unethical or illegal conduct?",
        "Is there an anonymous ethics hotline for whistleblower reports?",
        "What protection is provided to employees who make good-faith reports?",
        "How are knowingly false or malicious whistleblower complaints treated?",

        # general/code_of_conduct.pdf — 13. Acknowledgement
        "What annual declaration must every MediAssist employee sign under the Code of Conduct?",
        "What does the employee acknowledgement confirm?",
        "Where is the signed Code of Conduct declaration retained?",
        "How often must employees confirm that they have read and will follow the Code of Conduct?",

        # general/general_faqs.pdf — Payroll & Benefits
        "According to the MediAssist General Staff FAQs, when is monthly salary credited?",
        "How can an employee download payslips from the HR Portal?",
        "What are the employee and employer Provident Fund contribution rates in the General Staff FAQs?",
        "How does a staff member update their bank account details for salary payments?",
        "What health insurance coverage is provided to permanent employees and their families?",
        "When does an employee become eligible for gratuity, and how is it calculated?",

        # general/general_faqs.pdf — IT & Systems
        "In the General Staff FAQs, how can I reset my MediAssist systems password?",
        "What should staff do if a company laptop is lost or stolen?",
        "How do employees request access to a new hospital system or software module?",
        "Is personal browsing allowed on MediAssist hospital Wi-Fi?",
        "Who should staff contact about a clinical software problem during a shift?",
        "What response time applies to a clinical-system incident reported to IT Support?",

        # general/general_faqs.pdf — Facilities
        "Where is the staff cafeteria located, and what are its opening hours according to the General Staff FAQs?",
        "Are subsidised cafeteria meals available to all staff grades?",
        "Which MediAssist campuses provide a crèche for employees’ children?",
        "What are the age limits and shift arrangements for the staff crèche?",
        "How do I reserve a conference room through the intranet?",
        "How is parking allocated by staff grade, and where are two-wheelers and EVs parked?",

        # general/general_faqs.pdf — HR & Administration
        "How do employees apply for leave according to the General Staff FAQs?",
        "Who approves leave for ICU doctors?",
        "What additional approval is needed when an ICU doctor takes more than five days of leave?",
        "How can I request an experience letter or employment certificate?",
        "What is the resignation notice period for clinical and non-clinical employees?",
        "How can a staff member apply for an internal transfer to another campus?",
        "When are annual appraisals conducted, and how are ratings discussed?",

        # general/general_faqs.pdf — Safety & Emergencies
        "What should staff do when the fire alarm sounds, according to the General Staff FAQs?",
        "Are employees allowed to use lifts during a fire evacuation?",
        "Which internal number activates the Code Blue team for a staff medical emergency?",
        "What should I do if I witness a patient fall?",
        "How should a workplace safety hazard be reported?",
        "Where should urgent hazards such as spills or exposed wiring be reported immediately?",

        # general/leave_policy.pdf — 1. Scope
        "Who is covered by the MediAssist Leave & Attendance Policy?",
        "Does the leave policy apply to permanent employees across all campuses and clinics?",
        "What leave rules apply to contract and locum staff?",
        "What happens if a statutory leave entitlement is more generous than this policy?",

        # general/leave_policy.pdf — 2. Leave Types and Entitlements
        "How many days of Earned Leave do clinical and non-clinical staff receive each year?",
        "What are the annual Sick Leave and Casual Leave entitlements under the Leave & Attendance Policy?",
        "How much maternity, paternity, and bereavement leave is available to employees?",
        "Can clinical employees use Study Leave for CME or certification courses?",
        "What is the maximum Earned Leave carry-forward balance?",
        "How soon must Compensatory Off be used after it accrues?",
        "Can Casual Leave be combined with Earned Leave?",
        "What medical certificate requirement applies when Sick Leave exceeds three consecutive days?",

        # general/leave_policy.pdf — 3. Leave Application Process
        "Where must all MediAssist leave applications be submitted and approved?",
        "Are verbal leave approvals valid under the Leave & Attendance Policy?",
        "How much advance notice is required for Earned Leave?",
        "What is the notice period and approval route for Casual Leave?",
        "How should an employee notify the hospital when taking Sick Leave?",
        "Who approves Earned Leave longer than five days?",
        "Does the HOD approval rule apply to every type of leave lasting more than five consecutive days?",

        # general/leave_policy.pdf — 4. Attendance Tracking
        "How is employee attendance recorded under the Leave & Attendance Policy?",
        "Is there a grace period for shift start times, and how long is it?",
        "What happens when an employee arrives late beyond the ten-minute grace period?",
        "After how many late arrivals in a month is each further late marked as a half-day?",
        "How can a missed biometric punch or mobile check-in be regularised?",
        "What is the deadline for correcting a missed attendance punch?",

        # general/leave_policy.pdf — 5. On-Call & Duty Roster
        "How are doctors’ and nurses’ rotational on-call rosters published?",
        "How far in advance must the unit in-charge publish the on-call roster?",
        "What is the nightly on-call payment for resident doctors?",
        "How much do resident doctors receive for on-call duty on Sundays and public holidays?",
        "What is the standard and holiday on-call compensation for nurses?",
        "Who is covered by the on-call and duty roster rules?",

        # general/leave_policy.pdf — 6. Public Holidays
        "How many fixed national and floating regional holidays are provided each year?",
        "When is the annual public holiday list published?",
        "What compensation do clinical staff receive when they work on a public holiday?",
        "Does working on a public holiday provide both compensatory leave and additional pay?",
        "What pay multiplier applies to clinical staff working on an official public holiday?",

        # general/leave_policy.pdf — 7. Leave Encashment
        "When is Earned Leave above the 30-day carry-forward cap encashed?",
        "How is annual Earned Leave encashment calculated?",
        "What happens to an employee’s Earned Leave balance when they leave MediAssist?",
        "Is Sick Leave eligible for encashment?",
        "Can Casual Leave or Compensatory Off be converted into cash?",
        "Which leave types are excluded from encashment under this policy?",

        # general/leave_policy.pdf — 8. Leave Without Pay (LOP) & Special Cases
        "When may an employee apply for Leave Without Pay under the Leave & Attendance Policy?",
        "What approvals are required for LOP?",
        "Does Leave Without Pay count toward service for salary increments?",
        "Can employees take half-day leave against Casual Leave?",
        "How does the sandwich rule apply to weekly-offs and holidays between two LOP days?",
        "Which leave types may probationers use?",
        "Does Earned Leave accrue during probation, and when can it be taken?",

        # general/leave_policy.pdf — 9. Public Holiday List (illustrative)
        "Which national holidays are included in the Leave Policy’s illustrative public holiday list?",
        "When is the MediAssist public holiday calendar finalised and published?",
        "Which holidays are regional or floating under the illustrative list?",
        "Does the public holiday list include Republic Day, Independence Day, and Gandhi Jayanti?",
        "What dates are listed for Republic Day, May Day, Independence Day, Gandhi Jayanti, and Christmas?",
        "How are campus-state regional holidays added to the fixed national holidays?",

        # general/leave_policy.pdf — 10. Abandonment of Service
        "When is unexplained absence treated as voluntary abandonment of service?",
        "What does the Leave & Attendance Policy say about being absent for ten or more consecutive days without notice?",
        "Can unauthorised extended absence lead to termination?",
        "What should an employee do if an emergency prevents them from informing MediAssist about their absence?",
        "Who should be contacted as soon as possible when an employee cannot report to duty because of an emergency?",
    # Source fragment: src/helpers/router_questions_group4.py
        # general/staff_handbook.pdf
        # Section: 1. About MediAssist Health Network / Welcome
        "According to the MediAssist Staff Handbook’s “About MediAssist Health Network” section, when and where was the organisation founded?",
        "What does the Staff Handbook say about MediAssist’s current hospital, clinic, and diagnostic-centre network?",
        "How many staff members and annual patient visits are described in the “About MediAssist Health Network” section of the MediAssist Staff Handbook?",
        "Which document should take precedence if the Staff Handbook conflicts with a specific MediAssist policy?",
        # Section: 2. Organisational Structure
        "Who does the MediAssist Staff Handbook identify as responsible for network-wide operations and performance?",
        "What are the six reporting levels in the “Organisational Structure” section of the Staff Handbook?",
        "According to the Staff Handbook’s organisational hierarchy, who should staff approach for department-level approvals or escalations?",
        "How are clinical, technology, and finance leadership roles represented in the MediAssist organisational structure?",
        # Section: 3. Our Values
        "What does “Patient First” mean in the MediAssist Staff Handbook’s “Our Values” section?",
        "What standards of honesty and truthfulness does the Staff Handbook require under “Integrity”?",
        "How does the Staff Handbook define clinical excellence at MediAssist?",
        "What does the handbook say about continuous learning, CME, and on-the-job training?",
        "What expectations does the “Team Respect” value place on MediAssist employees?",
        "What conduct does MediAssist consider unacceptable under its team-respect principles?",
        # Section: 4. Facilities & Campuses
        "Which MediAssist campus is described as the multi-speciality flagship with emergency services?",
        "According to the Staff Handbook’s “Facilities & Campuses” section, which location focuses on cardiac sciences and critical care?",
        "Which MediAssist campus specialises in oncology and radiation therapy?",
        "Where are orthopaedics and mother-and-child care identified as the main clinical focus?",
        "What services are associated with the MediAssist Mysuru Clinic Hub?",
        "Does the Staff Handbook allow new hires to be rotated between campuses for training?",
        # Section: 5. Working Hours & Shifts
        "What are the standard office hours for administrative, billing, HR, and IT staff in the MediAssist Staff Handbook?",
        "What are the morning, afternoon, and night clinical shifts listed in the handbook?",
        "What is the weekly-off arrangement for administrative employees?",
        "How are weekly offs scheduled for clinical staff?",
        "What is the maximum number of consecutive days a clinical employee should work according to the Staff Handbook?",
        "Which working-hours rules apply to clinical staff rather than administrative staff?",
        # Section: 6. Staff ID & Access Cards
        "Who issues a new employee’s photo ID and RFID access card according to the Staff Handbook?",
        "What should a staff member do immediately after losing a MediAssist access card?",
        "How quickly is a lost access card deactivated, and how long does replacement normally take?",
        "What replacement fee is specified for a lost staff access card?",
        "Which areas are restricted to clinical staff or authorised personnel?",
        "What does the handbook say about lending access cards or tailgating?",
        # Section: 7. Dress Code
        "What uniform and footwear requirements apply to nurses under the MediAssist Staff Handbook?",
        "What should doctors wear while working at MediAssist?",
        "What clothing and safety-footwear requirements apply to technicians?",
        "What dress standard applies to administrative and billing staff?",
        "Does the Staff Handbook require employees to display their photo ID with their uniform?",
        "What does the handbook say about hair being tied back for nursing staff?",
        # Section: 8. Grievance Redressal
        "Who should a MediAssist employee approach first when raising a workplace grievance?",
        "What is the escalation route if a grievance is unresolved or the immediate supervisor is inappropriate?",
        "Within how many working days must a formal grievance be acknowledged?",
        "What resolution timeline is targeted for staff grievances in the MediAssist Staff Handbook?",
        "Can a grievance be raised confidentially under the handbook?",
        "How does the handbook treat retaliation against an employee who raises a grievance?",
        # Section: 9. IT & Systems Access
        "How does a MediAssist employee request access to an IT system according to the Staff Handbook?",
        "What does the principle of least privilege mean in the handbook’s IT-access rules?",
        "What types of software or data-storage practices are prohibited on MediAssist devices?",
        "What password length and character requirements are specified in the Staff Handbook?",
        "How often must MediAssist passwords be changed?",
        "Which systems require multi-factor authentication?",
        "How quickly must suspected account compromise be reported to IT Security?",
        "Does the handbook permit staff to share login credentials with colleagues or supervisors?",
        # Section: 10. Probation & Confirmation
        "How long is the probation period for clinical employees at MediAssist?",
        "What probation period applies to non-clinical employees?",
        "Under what conditions can probation be extended?",
        "What is the maximum permitted probation extension described in the Staff Handbook?",
        "When do benefits such as study leave begin to accrue?",
        "What notice period applies to either party during probation?",
        "How is successful confirmation communicated to an employee?",
        # Section: 11. Training & Professional Development
        "Which mandatory induction courses must every clinical employee complete within 30 days of joining?",
        "What CME obligations apply to doctors and nurses at MediAssist?",
        "How much study leave is available for approved certification courses?",
        "What training must technicians complete before operating biomedical equipment independently?",
        "Where is the annual MediAssist training calendar published?",
        "How are staff nominations for training routed?",
        # Section: 12. Emergency Codes
        "What does Code Blue mean in the MediAssist Staff Handbook, and what should staff do?",
        "What is the response to Code Pink for an infant or child abduction?",
        "What actions are required when Code Red is announced?",
        "What does Code Orange indicate, and whom should staff contact?",
        "How should employees respond to Code Grey involving a violent or aggressive person?",
        "What does Code Yellow represent, and where should staff report?",
        "What emergency telephone number is used across MediAssist hospitals for internal emergencies?",
        # Section: 13. Key Contacts
        "What is the MediAssist HR Helpdesk telephone number and email address?",
        "How can staff contact IT Support according to the Staff Handbook?",
        "What are the contact details for the Facilities Desk?",
        "Which contact should employees use for the Medical Director’s Office?",
        "What email address is listed for the POSH Committee?",
        "Where does the handbook list the internal emergency extension?",
        # nursing/icu_nursing_procedures.pdf
        # Section: SOP 1 — Central Venous Catheter (CVC) Care
        "According to the ICU Nursing Procedures Manual’s CVC Care SOP, how often should a central-line dressing be changed?",
        "What equipment is required for central venous catheter dressing care in the ICU manual?",
        "How should the insertion site be cleaned during CVC dressing replacement?",
        "How long must chlorhexidine be allowed to air-dry during CVC care?",
        "What details must be written on the new transparent CVC dressing?",
        "What findings require immediate doctor notification during central-line care?",
        "Where should the old CVC dressing be discarded?",
        "What documentation is required after completing CVC dressing care?",
        # Section: SOP 2 — Mechanical Ventilator Management
        "What initial ventilator mode and tidal-volume range are recommended in the ICU Nursing Procedures Manual?",
        "What starting respiratory rate, FiO₂, and PEEP settings are listed for mechanical ventilation?",
        "Which ventilator parameters must be monitored hourly?",
        "What should an ICU nurse check first when the ventilator shows a high-pressure alarm above 40 cmH₂O?",
        "What is the recommended immediate response to low SpO₂ below 90% on a ventilator?",
        "What head-of-bed elevation is required in the ventilator bundle for VAP prevention?",
        "How often should oral care with chlorhexidine be provided under this ICU SOP?",
        "What daily sedation and weaning assessments are included in the ventilator bundle?",
        # Section: SOP 3 — Nasogastric Tube (NGT) Insertion & Management
        "What NGT sizes are recommended for adults in the ICU Nursing Procedures Manual?",
        "How should the tube length be measured before inserting an NGT?",
        "What confirmation methods are required before the first feed through an NGT?",
        "What is the initial feeding rate specified in the NGT management SOP?",
        "How should staff respond when gastric residual volume is below 200 mL?",
        "What action is required for a gastric residual volume between 200 and 400 mL?",
        "What should happen when the NGT gastric residual volume exceeds 400 mL?",
        "Does the ICU manual allow auscultation alone to confirm NGT placement before feeding?",
        # Section: SOP 4 — IV Cannula Insertion
        "What is the preferred order of IV cannula insertion sites in the ICU manual?",
        "When may the legs be used for IV cannulation?",
        "What cannula gauge is recommended for blood transfusion?",
        "Which IV cannula size is advised for rapid fluid resuscitation?",
        "What gauges are listed for routine medication administration?",
        "How many IV cannulation attempts may one nurse make?",
        "Who should be contacted after two failed cannula attempts?",
        "When should an IV cannula be replaced, including when phlebitis is present?",
        # Section: SOP 5 — Patient Restraint Protocol
        "What principle governs the use of restraints in the ICU Nursing Procedures Manual?",
        "In what situations may restraint be considered?",
        "What authorisation is required before applying a patient restraint?",
        "Within what time must a verbal doctor’s restraint order be documented in writing?",
        "How often is restraint re-authorisation required?",
        "What neurovascular checks must be performed while a patient is restrained?",
        "How frequently should range-of-motion exercises be offered?",
        "What information must be recorded in the restraint documentation?",
        # Section: SOP 6 — Endotracheal Suctioning
        "When does the ICU manual recommend endotracheal suctioning?",
        "What clinical signs indicate that an intubated patient may need suctioning?",
        "How long should the patient be pre-oxygenated before endotracheal suctioning?",
        "What catheter-size limit is specified in relation to the ETT internal diameter?",
        "How should suction be applied during catheter withdrawal?",
        "What is the maximum duration of a suction pass?",
        "How many suction passes are permitted before reassessment and recovery?",
        "When must suctioning be stopped immediately?",
        # Section: SOP 7 — Pressure Injury Prevention
        "Which risk-assessment tool is required for ICU patients in the pressure-injury prevention SOP?",
        "When should the Braden Scale be completed?",
        "What Braden score indicates increased pressure-injury risk?",
        "How often should ICU patients be repositioned?",
        "What support surface is recommended for high-risk patients?",
        "Which skin areas should be inspected each shift?",
        "What moisture-management measures are included in the prevention bundle?",
        "How does the ICU manual distinguish Stage 1, Stage 2, Stage 3, and Stage 4 pressure injuries?",
        # nursing/infection_control.pdf
        # Section: 1. Five Moments of Hand Hygiene
        "What are the WHO Five Moments of Hand Hygiene listed in the MediAssist Infection Control Guidelines?",
        "When should staff perform hand hygiene before patient contact?",
        "What hand-hygiene moment applies before an aseptic procedure?",
        "When is hand hygiene required after body-fluid exposure risk?",
        "What duration is required for alcohol-based hand rub?",
        "How long should a soap-and-water handwash take?",
        "When must staff use soap and water instead of alcohol-based hand rub?",
        "What hand-hygiene precautions apply after caring for a patient with C. difficile?",
        # Section: 2. PPE Selection Guide
        "What PPE is required for routine patient contact under the MediAssist Infection Control Guidelines?",
        "Which gloves, gown, mask, and eye protection are needed when blood or body-fluid exposure is possible?",
        "What PPE is required for a suspected respiratory infection?",
        "Which respiratory protection is specified for aerosol-generating procedures?",
        "When is a full face shield required according to the PPE selection table?",
        "What PPE should staff wear before entering a contact-isolation room?",
        "Which procedures are classified as aerosol-generating in the Infection Control Guidelines?",
        "When may a PAPR be used for an aerosol-generating procedure?",
        # Section: 3. Standard Precautions
        "To which patients do standard precautions apply according to the Infection Control Guidelines?",
        "Which body fluids and materials must be treated as potentially infectious?",
        "What infection-control practices are included under standard precautions?",
        "How do standard precautions address non-intact skin and mucous membranes?",
        "Does a patient need a known infection diagnosis before standard precautions are applied?",
        "What do the MediAssist guidelines require regarding safe injection practice?",
        "What sharps and linen-handling practices fall under standard precautions?",
        # Section: 4. Transmission-Based Precautions
        "What precautions are required for a patient with MRSA, VRE, C. difficile, or norovirus?",
        "What are the key measures for droplet precautions in the MediAssist Infection Control Guidelines?",
        "Which organisms are given as examples of airborne-transmitted infections?",
        "What room and mask requirements apply to airborne precautions?",
        "How far from a patient should staff wear a surgical mask under droplet precautions?",
        "When should equipment be dedicated to a contact-precaution patient?",
        "What visitor PPE is required for contact isolation?",
        "What transport restrictions apply to a patient requiring airborne precautions?",
        # Section: 5. Healthcare-Associated Infection (HAI) Surveillance
        "Which four healthcare-associated infections are under active surveillance at MediAssist?",
        "What does CAUTI stand for in the Infection Control Guidelines?",
        "What is the meaning of CLABSI and VAP in the HAI surveillance section?",
        "What does SSI refer to in the MediAssist infection-control document?",
        "Within what timeframe must a suspected HAI be reported?",
        "Who should receive a suspected HAI report?",
        "When is a root-cause analysis conducted?",
        "How are lessons from confirmed HAIs shared with the infection control committee?",
        # Section: 6. Outbreak Management Protocol
        "How does the MediAssist Infection Control Guidelines define an outbreak?",
        "How many linked cases and what timeframe meet the outbreak definition?",
        "What is the notification chain for a suspected outbreak?",
        "Which team should be contacted after the ward in-charge during an outbreak?",
        "What patient-cohorting measures are required during outbreak management?",
        "When should staff and equipment be dedicated to affected patients?",
        "What visitor-control measures may be implemented during an outbreak?",
        "What environmental-cleaning and staff-communication actions are required?",
        # Section: 7. Waste Segregation
        "What waste belongs in the yellow biomedical-waste bin?",
        "Which items should be disposed of in the red contaminated-plastics bin?",
        "What materials go into the blue or translucent white sharps container?",
        "What waste is appropriate for the black general-waste bin?",
        "Where should cytotoxic or chemotherapy waste be discarded?",
        "When must waste be segregated according to the Infection Control Guidelines?",
        "How often should biomedical-waste bins be removed?",
        "What should staff do when a biomedical-waste bin is three-quarters full, and where is collection recorded?",
        # Section: 8. Needlestick & Sharps Injury Management
        "What should a staff member do immediately after a needlestick injury?",
        "How should a sharps wound be washed according to the Infection Control Guidelines?",
        "What must staff avoid doing to a needlestick wound?",
        "How should eye or mouth splashes be managed?",
        "Whom should an injured worker notify after a sharps exposure?",
        "Which infections should be considered during source-patient risk assessment?",
        "What is the preferred timeframe for starting HIV post-exposure prophylaxis?",
        "What reports and follow-up tests are required after a sharps injury?",
        "What does the document say about recapping needles and sharps-container fill levels?",
        # Section: 9. Antimicrobial Stewardship (Nursing Role)
        "Why must nurses administer antimicrobials on time according to the Infection Control Guidelines?",
        "When should nurses prompt the medical team to consider an IV-to-oral antibiotic switch?",
        "When should cultures be collected in relation to the first antibiotic dose?",
        "What antibiotic orders should nursing staff flag to the medical team?",
        "How can nurses support antimicrobial resistance control under this section?",
        "What should a nurse do if an antibiotic continues beyond its review date?",
        "How should staff respond when an antimicrobial has no documented indication?",
        # Section: 10. Isolation Signage
        "What does a yellow contact-precaution door sign mean?",
        "What PPE is required before entering a room with a yellow isolation sign?",
        "What does the blue droplet-isolation sign indicate?",
        "When is a surgical mask required under the blue isolation signage?",
        "What does the red airborne-isolation sign mean?",
        "Which respirator and room type are required for airborne isolation?",
        "How do the colour-coded isolation signs help staff and visitors before entry?",
        "What precautions should staff identify from the door sign before entering an isolation room?",
]

SQL_RAG_QUESTIONS = [
    # mediassist.db — claims
    # Claim counts and status summaries
    "How many claims are in the claims database?",
    "How many insurance claims are currently pending?",
    "How many claims have been approved, rejected, submitted, or escalated?",
    "What is the count of claims by status?",
    "How many cashless claims are there compared with reimbursement claims?",
    "How many claims were submitted in 2024?",
    "What is the monthly claim volume based on submitted date?",
    "How many claims have not yet been resolved?",

    # Claim amounts and analytical questions
    "What is the total claimed amount across all insurance claims?",
    "What is the total approved amount for approved claims?",
    "What is the difference between the total claimed amount and total approved amount?",
    "What is the average claimed amount per claim?",
    "What is the average approved amount for approved claims?",
    "What percentage of claims have been approved?",
    "What is the approval rate for cashless claims?",
    "Which claims have the largest claimed amounts?",
    "What are the top ten claims by approved amount?",
    "Which claims have a claimed amount above 100000?",
    "How much money is currently tied up in pending claims?",
    "What is the total value of rejected claims?",

    # Claim filters and operational lookups
    "List all pending claims for Star Health.",
    "Show all rejected claims submitted to HDFC Ergo.",
    "Which claims are associated with the cardiology department?",
    "List cashless claims for the orthopaedics department.",
    "Show reimbursement claims for general medicine.",
    "Which claims use diagnosis code I21.4?",
    "Find the claim for a patient named Kavya Pillai.",
    "What are the details of claim CLM-2024-1002?",
    "Which claims were submitted between January and June 2024?",
    "Which claims were resolved in December 2024?",
    "Show claims where the approved amount is lower than the claimed amount.",
    "Which insurers have the most rejected claims?",
    "Which departments have the highest total claimed amount?",
    "What is the total approved amount by insurer?",
    "What is the claim status distribution for each department?",
    "Which diagnosis codes appear most often in the claims table?",
    "How long did each resolved claim take from submission to resolution?",
    "What is the average claim resolution time by insurer?",
    "Which pending claims have been waiting the longest since submission?",

    # mediassist.db — maintenance_tickets
    # Ticket counts and status summaries
    "How many maintenance tickets are in the database?",
    "How many maintenance tickets are currently open or in progress?",
    "How many tickets have been resolved or escalated?",
    "What is the count of maintenance tickets by status?",
    "How many preventive-maintenance tickets are there?",
    "How many tickets were raised in 2024?",
    "What is the monthly maintenance-ticket volume based on raised date?",
    "How many maintenance tickets have no resolved date?",

    # Ticket filters and operational lookups
    "List all open maintenance tickets.",
    "Show escalated maintenance tickets for RadiPro MX-150.",
    "Which maintenance tickets are at MediAssist Hyderabad Central?",
    "List unresolved tickets at the MediAssist Bengaluru Onco Centre.",
    "Show all battery-replacement tickets.",
    "Which tickets have fault code F-09?",
    "Find maintenance tickets for the DriveFlow IP-200.",
    "What are the details of ticket TKT-2024-2001?",
    "Which tickets were raised for calibration due?",
    "Show all sensor-failure tickets by equipment name.",
    "Which equipment has the most maintenance tickets?",
    "Which campus has the highest number of maintenance tickets?",
    "What is the ticket count by equipment category?",
    "What is the ticket count by issue type?",
    "How many tickets are associated with each fault code?",
    "Which unresolved tickets have been open the longest?",
    "What is the average time to resolve maintenance tickets?",
    "What is the average resolution time by equipment category?",
    "Which maintenance tickets were resolved during November 2024?",
    "Show tickets raised between January and March 2024 that are still unresolved.",
    "What resolution notes were recorded for resolved tickets at MediAssist Pune Speciality?",
    "Which users raised the most maintenance tickets?",

    # Cross-table operational analytics
    "Give me a summary of claims and maintenance tickets by status.",
    "Compare the number of unresolved claims with unresolved maintenance tickets.",
    "What are the main operational backlogs in the MediAssist database?",
]


UNRELATED_QUESTIONS = [
    # General knowledge
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest ocean on Earth?",
    "Which planet is known as the Red Planet?",
    "Who wrote Romeo and Juliet?",
    "What is the boiling point of water at sea level?",
    "How many continents are there?",
    "What is the currency of Japan?",
    "When did the first Moon landing take place?",
    "What is the tallest mountain in the world?",
    "Who invented the telephone?",
    "What is the square root of 144?",
    "What is the chemical symbol for gold?",
    "Which country has the city of Barcelona?",
    "What is the fastest land animal?",

    # Travel, food, and entertainment
    "What are the best tourist attractions in Paris?",
    "How do I cook a basic vegetable pasta?",
    "What is the weather forecast for tomorrow?",
    "Recommend a science-fiction movie.",
    "What are the rules of chess?",
    "How do I learn to play the guitar?",
    "What is a good recipe for chocolate cake?",
    "Which countries are in South America?",
    "How can I plan a weekend trip?",

    # Technology and programming outside MediAssist
    "How do I create a Python virtual environment?",
    "What is the difference between HTTP and HTTPS?",
    "How do I reset my home Wi-Fi router?",
    "Explain how a blockchain works.",
    "What is the capital of Australia?",
    "How do I write a SQL join?",
    "What is the latest version of JavaScript?",
    "How can I improve my computer performance?",

    # Casual conversation and unrelated requests
    "Tell me a joke.",
    "Write a poem about the ocean.",
    "What time is it?",
    "Can you help me choose a birthday gift?",
    "Translate hello into Spanish.",
    "What should I wear to a wedding?",
    "Tell me an interesting fact.",
    "Can you generate a shopping list for a barbecue?",
    "Who won the last football match?",
    "Help me write a thank-you message.",

    # Non-MediAssist business questions
    "What are today's stock market prices?",
    "How do I file my personal tax return?",
    "Compare the interest rates on home loans.",
    "What is the best smartphone to buy?",
    "Help me create a marketing plan for my shop.",
    "How do I start an online business?",
]
