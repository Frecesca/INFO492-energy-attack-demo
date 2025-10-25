# Team 8 – Energy Sector (Attack Posture)

Course: INFO 492 B – Agentic Cybersecurity with AI
Instructor: Professor Frank Martinez
Team members：Frecesca Wang, Kibret Ogale, Vidhya Narayanan

# Project Overview

Our team investigates how AI reconnaissance agents can enhance the speed, precision, and scalability of cyber operations targeting the Pacific Northwest energy grid. We aim to validate whether an AI-driven reconnaissance system can outperform a team of 10–15 human analysts in discovering vulnerabilities while maintaining ethical and explainable control through Human-in-the-Loop (HIL) checkpoints.

Our posture explores offensive APT-style scenarios under controlled academic conditions, focusing on how agentic AI systems can accelerate reconnaissance, simulate phishing, and model nation-state attack behaviors — without deploying any real-world harm.

# Hypothesis (Revisited from Week 2)

Hypothesis:
Our AI recon agent will be able to scan vulnerabilities at a higher rate than a team of 10–15 analysts. For every one energy system that would take a given team 8 hours to scan, our AI would be able to scan 10 simultaneously in approximately one hour with the same depth.

The central question evolved from “Can AI make reconnaissance faster?” to “How can we validate, explain, and ethically govern this speed advantage?”

# First Two Experiments

Experiment #1 – Tabletop Simulation (Wild Horse Wind Farm)

Simulated an AI-led phishing and firmware-update attack on the Wild Horse Wind Farm.

Found that the AI revealed itself too early, triggering SOC countermeasures.

Lesson: Reconnaissance must precede attack execution, and stealth must be maintained.

Validated that speed alone cannot replace strategic restraint.

Experiment #2 – LinkedIn AI Phishing Agent (Regional Scaling)

Integrated the AI agent with the LinkedIn API to identify energy-sector employees.

Generated personalized phishing content and tested email bounce-checks to simulate stealth.

Implemented vulnerability ranking (1–5) and HIL approval dashboard to guide automation.

Expanded the attack surface from a single wind farm to the Bonneville Power Administration, representing a realistic nation-state target.

# Industry Stakeholder Feedback

Alex Reynolds – AI Security Consultant, GridGuardian Inc. (Seattle)

Stressed that AI systems must exhibit predictable behavior and human supervision before any deployment in the energy sector.

Identified three evaluation metrics:

Detection Speed

Precision vs. False-Positive Rate

Operational Risk

Directly inspired our addition of the approval dashboard and explainable-agent rationale log.

Anonymous U.S. Coast Guard Cyber Command Officer

Highlighted the importance of stealth and human vulnerability: “Most attacks begin with people giving up information.”

Warned that Legacy Systems and Remote Access Controls remain exploitable points.

Reinforced our focus on social-engineering realism and HIL oversight.

Stakeholder Impact:
Their insights transformed our hypothesis validation method from purely performance-based to ethically evaluative, emphasizing human judgment as a required layer of control.

# Class Feedback Summary

Source: Week 3 & 4 Feedback Forms (LLM Summarization available）

| Key Takeaways                           | Peer Recommendations                                                 |
| :-------------------------------------- | :------------------------------------------------------------------- |
| **HIL Integration = Major Improvement** | Continue refining human checkpoints for safety and interpretability. |
| **Scaling and Realism Praised**         | Validate differences between PSE and Bonneville security models.     |
| **Strong Industry Alignment**           | Include grounded metrics (speed, accuracy, stealth duration).        |
| **High Detectability Still a Risk**     | Build concealment/detection-resistance test before Demo #3.          |
| **Excellent Presentation Flow**         | Maintain clarity with concise, technical PRD documentation.          |

Peers rated Team 8 with an average of 4.8–4.9/5 for both stakeholder and class feedback incorporation, recognizing our progress from “fast but exposed” to “controlled and explainable.”

# Psychological Dimension

Following Professor Martinez’s midterm meeting, the team explored the psychology of hacking—the pressures, isolation, and responsibility shifts when humans delegate harmful actions to AI.

“When we automate harm, we also automate distance.”

Frecesca’s question about moral accountability in LLM-assisted attacks led to the realization that HIL is not only a technical safeguard but a moral one. Keeping a human in control reinstates accountability and ensures ethical awareness.

We also examined insider threats and loyalty within simulated APT teams, planning to design AI behavioral monitoring tools with strict human oversight for internal risk detection in future iterations.

# Hypothesis Validation Summary

| Validation Aspect | Outcome                                       | Reflection                                                 |
| :---------------- | :-------------------------------------------- | :--------------------------------------------------------- |
| **Speed**         | Proven: AI Recon 200–240× faster than humans. | Efficiency validated, but accuracy must match speed.       |
| **Accuracy**      | In progress: Need human rating calibration.   | Next iteration will compare AI vs. manual ground truth.    |
| **Stealth**       | Not yet achieved; detectability high.         | Concealment metrics and timing refinement needed.          |
| **Ethics / HIL**  | Significant improvement.                      | Human approval flow added; aligns with industry standards. |

Validation is not only about proving that the model works, but understanding its limits, risks, and ethical boundaries.

# Plan for the Second Half of the Quarter

Develop a Grounded Evaluation Model

Compare AI vs. human recon accuracy and false-positive rates.

Implement detection and concealment benchmarks.

Refine Human-in-the-Loop Workflow

Expand approval dashboards and explainability layers.

Introduce visual metrics for human intervention timing.

Ethical & Psychological Expansion

Formalize the “Responsibility Loop” to prevent automation detachment.

Include stakeholder validation on AI accountability framework.

Demo #3 Focus

Shadow test in a simulated digital-twin grid.

Record AI decision logs vs. human oversight checkpoints.

# Repository Structure

```text
├── code/
│   ├── agent_recon_demo.py                # Demo code for AI Reconnaissance agent
│   ├── phishing_llm_experiment.ipynb      # Notebook for Experiment #2 (LinkedIn Phishing Agent)
│   └── dependencies.txt                   # Dependencies used for first two experiments
│
├── data/
│   ├── experiment_outputs.csv             # Collected output data and test metrics
│   ├── feedback_summary.txt               # ← LLM summarization of class feedback
│   ├── stakeholder_transcripts/           # Interview transcripts from industry stakeholders
│   │   ├── alex_reynolds_interview.txt
│   │   └── coast_guard_officer.txt
│   └── metrics_log.json                   # Experiment logs and validation metrics
│
├── prompts/
│   ├── llm_prompts_used.md                # List of all LLM prompts used in Experiments #1–2
│   └── claude_experiments.pdf             # Claude prompt outputs and validation notes
│
├── docs/
│   ├── mid_quarter_analysis.pdf           # Team 8 Mid-Quarter Analysis (1000-word reflection)
│   ├── mid_quarter_reflection.pdf         # Supporting essay draft and feedback summary
│   ├── slides_link.txt                    # Google Slides presentation link
│   └── ethical_diagram.png                # Visualization of HIL and ethical model
│
└── README.md                              # ← You are here (project overview & contents)

# Individual Contributions

| Student                     | Section    | Contribution                                                                                                                                                                                                 |
| :-------------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frecesca (Meixuan) Wang** | INFO 492 B | Led stakeholder interview with Alex Reynolds; designed Human-in-the-Loop logic flow; integrated approval dashboard into Demo #2; authored reflection on psychological dimensions and ethical accountability. |
| **Vidhya Narayanan**        | INFO 492 B | Directed tabletop design and reconnaissance scaling; led stakeholder interview with Coast Guard officer; compiled midterm presentation slides.                                                               |
| **Kibret Ogale**            | INFO 492 B | Built LinkedIn API integration; handled experiment data parsing; contributed to class feedback synthesis and stealth metric planning.                                                                        |

