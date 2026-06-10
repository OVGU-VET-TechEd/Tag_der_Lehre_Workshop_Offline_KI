<!--
author:   EduGreenLabs / EU-GREEN University Alliance (OvGU Magdeburg)
email:    workshop@example.org
version:  1.0.0
language: en
narrator: US English Female

comment:  Local AI in Higher Education Teaching — Digital Agency with Offline LLMs,
          LiaScript & Vibe Coding. A 90-minute workshop framed by the UNESCO ICT
          Competency Framework for Teachers and the UNESCO AI Competency Framework
          for Teachers, with a crosswalk from KMK (DE) → DigCompEdu Supplement (EU)
          → UNESCO (global). Works as presentation, self-study tool and workshop toolbox.

logo:     https://raw.githubusercontent.com/LiaScript/docs/master/README/img/logo.png

@style
.lia-slide__content { font-family: system-ui, -apple-system, sans-serif; }
.box { background:#f5f7fa; border-radius:10px; padding:14px 18px; margin:12px 0; border-left:4px solid #2a7ed3; }
.box.warn { border-left-color:#e0832b; background:#fff8f0; }
.box.ok   { border-left-color:#2e9e5b; background:#f1faf4; }
.box.priv { border-left-color:#7c3aed; background:#f7f4fd; }
@end

-->

# Local AI in Higher Education Teaching

**Digital Agency with Offline LLMs, LiaScript & Vibe Coding**

> *Which competencies do teachers need to use AI meaningfully and confidently in
> higher education — without cloud dependency, without data-protection concerns,
> without licence barriers?*

                          --{{0}}--
Welcome. Over the next ninety minutes we explore how local AI applications — offline
large language models — work together with LiaScript and the principle of *Vibe Coding*
to let you build Open Educational Resources at a low threshold. We frame all of this
inside two UNESCO reference documents and trace how teacher AI competencies progress
from the German, to the European, to the global level.

                          {{1}}
<section>

**This resource works three ways:**

| Mode | How to use it |
|------|---------------|
| 🎤 **Presentation** | Project full-screen, use arrow keys, speaker notes are spoken aloud |
| 📖 **Self-study** | Read at your own pace, run every interactive element yourself |
| 🧰 **Workshop toolbox** | Copy code blocks, configs and prompts directly into your own setup |

> 🕐 **Duration:** 90 minutes · **Audience:** Students · **Language:** English
> 📜 **Licence:** CC BY-SA 4.0 — remix and reuse freely.

</section>

                          --{{1}}--
Everything you see in a copyable code block is yours to take. The configuration files,
the prompts, the LiaScript snippets — all of it is released under an open licence so you
can carry it straight into your own teaching practice.

## Agenda

      {{|>}}

1. **Why local AI?** — cloud dependency, data protection, licence barriers *(10 min)*
2. **The three frameworks** — KMK → DigCompEdu Supplement → UNESCO *(15 min)*
3. **🔍 Interactive crosswalk** — explore how the competencies map onto each other *(15 min)*
4. **LiaScript & Vibe Coding** — building OER at a low threshold *(15 min)*
5. **🛠 Hands-on** — Ollama + Gemma 4 + VS Code Copilot Chat *(25 min)*
6. **Wrap-up & toolbox** — what you take home *(10 min)*

--{{|>}}--
The middle of the workshop is the heart of it: an interactive tool that lets you click
through the German, European and global competency frameworks and see, side by side,
how the same underlying ideas are expressed at each level. After that we get our hands
dirty with a fully local AI coding assistant.

## 1 · Why Local AI?

Cloud AI tools are powerful — but in a higher-education context they raise three
recurring problems. This workshop is built around solving all three with **offline LLMs**.

      {{1}}
<div class="box warn">

**☁️ Cloud dependency** — your teaching workflow breaks the moment the service changes its
API, raises its price, or goes down. You are renting, not owning, your tools.

</div>

      {{2}}
<div class="box priv">

**🔒 Data protection** — student work, prompts and assessment data leave your machine and
land on servers you do not control. Under the GDPR (Art. 5, 6, 9) this is a genuine legal
risk, not a hypothetical one.

</div>

      {{3}}
<div class="box">

**💸 Licence barriers** — per-seat pricing and closed models exclude students who cannot
pay, undermining equity and the idea of Open Educational Resources.

</div>

      {{4}}
<div class="box ok">

**✅ The local alternative** — a model like **Gemma** running through **Ollama** on your own
laptop. No data leaves the machine, no subscription, no licence wall. That is what
*digital agency* (*digitale Handlungsfähigkeit*) means in practice.

</div>

--{{1}}--
The first problem is dependency. When your entire teaching workflow sits on top of a
commercial cloud API, you are at the mercy of that provider's pricing and uptime.

--{{2}}--
The second is data protection. Every prompt you send to a cloud model contains
information — sometimes student information — and it leaves your control entirely.

--{{3}}--
The third is licence barriers. Closed, paid models create a two-tier classroom.

--{{4}}--
The answer running through this whole workshop is local inference. A capable open model,
on your own hardware, answering only to you.

### Quick check

What is the single strongest argument for **local** AI in a university classroom that
handles student data?

[( )] It always produces better answers than cloud models.
[(X)] Student data never leaves the machine, which directly addresses GDPR obligations.
[( )] It is faster than every cloud API.
[( )] It requires no hardware at all.
*****************
<div class="box ok">
Correct. Local inference is not always *better* or *faster* — but it keeps data on your
own device, which is decisive when GDPR-relevant student data is involved.
</div>
*****************

## 2 · Three Frameworks, One Direction

Teacher AI competencies are described at three levels. They were written independently,
but they point the same way.

| Level | Document | Scope |
|-------|----------|-------|
| 🇩🇪 **National** | **KMK** *Handlungsempfehlung KI* (2024) + *Lehren und Lernen in der digitalen Welt* (2021) | Recommendations for German education administration |
| 🇪🇺 **European** | **Supplement to the DigCompEdu Framework** (AI Pioneers, Erasmus+, 2023) | 6 competence areas × 6 progression stages |
| 🌍 **Global** | **UNESCO AI Competency Framework for Teachers** (2025) | 5 competency areas × 3 progression levels |

--{{0}}--
Three documents, three levels of governance. The German KMK recommendations, the
European DigCompEdu supplement, and the global UNESCO framework. None of them copied the
others, yet as we will see they describe a strikingly similar set of teacher competencies.

                {{1}}
> 💡 **The key insight:** All three move along the *same axis* — from basic literacy, through
> confident pedagogical application, to ethical leadership and the creation of new
> practice. The labels differ; the destination does not.

### The KMK level (Germany) 🇩🇪

The 2024 KMK *Handlungsempfehlung* devotes its **Themenbereich 3** to teacher
professionalisation. Its core demands:

- AI competence is **embedded in all three phases** of teacher education.
- Teachers must not only *apply* AI but **understand its technical foundations** and judge
  its opportunities, limits and risks.
- **Media literacy, media ethics and critical reflection** sit alongside applied and
  computer-science skills.
- Teachers are **continuous learners** who reflect on and change their own role.

> The 2021 KMK paper already framed this as a **progression of competence development** —
> the seed of the staged models the EU and UNESCO would formalise.

--{{0}}--
Germany's contribution is notable for insisting on three things together: hands-on
application, genuine technical understanding, and critical-ethical reflection. It refuses
to separate "using the tool" from "understanding the tool".

### The European level (DigCompEdu Supplement) 🇪🇺

The **AI Pioneers** project extended the established DigCompEdu framework with AI-specific
competencies, keeping its structure intact: **six competence areas** and a **six-stage
progression** from *Newcomer (A1)* to *Pioneer (C2)*.

      {{1}}
The six areas:

1. **Professional Engagement**
2. **Digital Resources**
3. **Teaching and Learning**
4. **Assessment**
5. **Empowering Learners**
6. **Facilitating Learners' Digital Competence**

      {{2}}
Plus **transversal skills**: digital literacy, critical thinking, problem-solving,
ethical awareness, and lifelong learning.

--{{0}}--
The European supplement is the most granular of the three. It did not reinvent anything —
it took the well-known DigCompEdu structure and asked, for each area, what AI changes.

--{{1}}--
Six areas, ranging from the teacher's own professional networks all the way to helping
students build their own digital competence.

--{{2}}--
And cutting across all six, a set of transversal "soft" skills that make the technical
competencies usable in real classrooms.

### The global level (UNESCO 2025) 🌍

UNESCO's framework organises everything into **five competency areas**, each with **three
progression levels**: **Acquire → Deepen → Create**.

| # | Competency area | Acquire → Deepen → Create |
|---|-----------------|---------------------------|
| 1 | **Human-centred mindset** | Human agency → Human accountability → Social responsibility |
| 2 | **Ethics of AI** | Ethical principles → Safe & responsible use → Co-creating ethical rules |
| 3 | **AI foundations & applications** | Basic techniques → Application skills → Creating with AI |
| 4 | **AI pedagogy** | AI-assisted teaching → AI–pedagogy integration → Pedagogical innovation |
| 5 | **AI for professional development** | Continuous PD → Collaborative PD → Leadership in PD |

--{{0}}--
UNESCO's structure is the cleanest to teach with: five areas, three levels each. Notice
that the very first area is not technical at all — it is a *human-centred mindset*. The
framework deliberately begins with agency and ethics before it touches a single tool.

> 📌 Notice the verbs: **Acquire, Deepen, Create**. That is the same arc the KMK calls a
> "progression of competence development" and DigCompEdu calls *Newcomer → Pioneer*.

## 3 · 🔍 Interactive Framework Crosswalk

The tool below is the centrepiece. Pick a **theme** along the top, then move the
**progression slider** to see how all four frameworks express that competency at a
*beginner*, *intermediate* or *advanced* level — side by side:
🇩🇪 KMK → 🇪🇺 DigCompEdu → 🌐 UNESCO ICT-CFT (2018) → 🌍 UNESCO AI-CFT (2025).

> 🖱️ **How to use it:** click a theme button, drag the slider, and read across the four
> columns. The bottom panel summarises what all four frameworks share at each level.

<div id="crosswalk-app" style="font-family:system-ui,-apple-system,sans-serif;">

  <div style="font-size:13px;font-weight:600;color:#444;margin-bottom:8px;">Choose a competency theme:</div>
  <div id="cw-themes" style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;"></div>

  <div style="background:#f0f4ff;border:1px solid #c8d5f5;border-radius:10px;padding:14px 18px;margin-bottom:18px;">
    <div style="font-size:13px;color:#445;margin-bottom:8px;">Progression level — drag to compare beginner → advanced</div>
    <div id="cw-stagename" style="font-size:20px;font-weight:800;">–</div>
    <input type="range" id="cw-stage" min="0" max="2" step="1" value="0" style="width:100%;accent-color:#2a7ed3;margin-top:6px;">
    <div style="display:flex;justify-content:space-between;font-size:11px;color:#778;margin-top:4px;">
      <span>Beginner</span><span>Intermediate</span><span>Advanced</span>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
    <div id="cw-col-de"  style="border-radius:10px;padding:12px;border-top:5px solid #1a1a2e;background:#fafbfc;"></div>
    <div id="cw-col-eu"  style="border-radius:10px;padding:12px;border-top:5px solid #003399;background:#fafbfc;"></div>
    <div id="cw-col-ict" style="border-radius:10px;padding:12px;border-top:5px solid #2e7d32;background:#fafbfc;"></div>
    <div id="cw-col-un"  style="border-radius:10px;padding:12px;border-top:5px solid #0077c8;background:#fafbfc;"></div>
  </div>

  <div style="margin-top:18px;background:#f1faf4;border:1px solid #b8e3c8;border-left:5px solid #2e9e5b;border-radius:0 10px 10px 0;padding:14px 18px;">
    <div style="font-size:13px;font-weight:700;color:#1e7a44;margin-bottom:6px;">🔗 What all four frameworks share</div>
    <p id="cw-synth" style="font-size:13px;line-height:1.6;margin:0;color:#244;">–</p>
  </div>

</div>

<script>
(function(){

  var STAGES = {
    de:  ['Phase 1 \u2014 Ausbildung', 'Phase 2 \u2014 Referendariat', 'Phase 3 \u2014 Fort-/Weiterbildung'],
    eu:  ['Newcomer / Explorer (A1\u2013A2)', 'Integrator / Expert (B1\u2013B2)', 'Leader / Pioneer (C1\u2013C2)'],
    ict: ['L1 \u2014 Knowledge Acquisition', 'L2 \u2014 Knowledge Deepening', 'L3 \u2014 Knowledge Creation'],
    un:  ['Acquire', 'Deepen', 'Create']
  };
  var STAGECOLOR = ['#2a7ed3', '#7c3aed', '#2e9e5b'];
  var STAGENAMES = ['Beginner \u2014 first contact', 'Intermediate \u2014 confident application', 'Advanced \u2014 leadership & creation'];
  var COLCOLOR   = {de:'#1a1a2e', eu:'#003399', ict:'#2e7d32', un:'#0077c8'};
  var COLS       = ['de', 'eu', 'ict', 'un'];

  var THEMES = [
    {
      id:'mindset', label:'\uD83E\uDDED Human-centred mindset & agency',
      de:[
        {s:'Awareness that learning is social and human-led; AI must not weaken shared learning or undermine the teacher\u2019s irreplaceable central role.', tags:['Medienkompetenz','digitale M\u00FCndigkeit']},
        {s:'Teachers keep the central role in shaping the learning environment; judge chances, limits & risks of AI with genuine critical reflection.', tags:['Lernbegleitung','kritische Reflexion']},
        {s:'Teachers see themselves as continuous learners, actively reflecting on and reshaping their own professional role as AI evolves.', tags:['Selbstreflexion','Rollenwandel']}
      ],
      eu:[
        {s:'Recognise AI as a tool that supports \u2014 not replaces \u2014 the educator; develop basic awareness of how AI influences professional practice.', tags:['Professional Engagement','Newcomer']},
        {s:'Critically evaluate AI outputs and the educator\u2019s evolving role; maintain professional judgement over AI-assisted decisions.', tags:['Critical thinking','Expert']},
        {s:'Lead and advocate for human-centred, responsible AI use across the institution and wider education community.', tags:['Leadership','Pioneer']}
      ],
      ict:[
        {s:'Understand ICT\u2019s role in education reform; align classroom practice with school and national priorities without losing sight of the human relationship at the core of teaching.', tags:['Policy awareness','ICT-CFT Area 1']},
        {s:'Analyse how digital policy affects teaching responsibilities and student agency; maintain the educator\u2019s central role in evidence-based digital practice.', tags:['Policy analysis','ICT-CFT Areas 1\u20133']},
        {s:'Advocate for context-sensitive ICT policies; formulate evidence-based reforms that keep teacher judgement and human relationships central in digital learning.', tags:['Policy advocacy','ICT-CFT L3']}
      ],
      un:[
        {s:'Human agency: understand that AI is human-led; corporate and individual design decisions shape its impact on rights and learner autonomy.', tags:['1.1 Human Agency']},
        {s:'Human accountability: humans remain legally responsible in human\u2013AI decision loops; defend teachers\u2019 pedagogical judgement against AI usurpation.', tags:['1.2 Accountability']},
        {s:'Social responsibility: evaluate AI\u2019s societal implications; actively contribute to inclusive, just, and planet-conscious AI governance in education.', tags:['1.3 Social Responsibility']}
      ],
      synth:'All four frameworks insist that the human stays in charge. Germany frames it as digital M\u00FCndigkeit and the teacher\u2019s irreplaceable role; DigCompEdu as critical evaluation of AI outputs; the ICT-CFT (2018) as policy literacy keeping educators central even in fully digitised schools; and the UNESCO AI-CFT as an explicit three-step progression from human agency, to legal accountability, to social responsibility. The mindset always comes before the tool.'
    },
    {
      id:'ethics', label:'\u2696\uFE0F Ethics, data protection & responsible use',
      de:[
        {s:'Sensitise teachers to legal frameworks (GDPR, EU AI Act) and the possible risks of AI use in school contexts.', tags:['Datenschutz','Medienethik']},
        {s:'Judge the quality and ethical effects of AI outputs; protect students\u2019 personality rights and informational self-determination (informationelle Selbstbestimmung).', tags:['informationelle Selbstbestimmung']},
        {s:'Shape school-level regulation and a positive error culture; safeguard data sovereignty at institutional level (EU AI Act, DSGVO Art. 22).', tags:['Regulierung','Schulaufsicht']}
      ],
      eu:[
        {s:'Ethical awareness: understand privacy, data security, and equity implications of AI tools in educational contexts.', tags:['Ethical awareness','Newcomer']},
        {s:'Identify algorithmic bias; apply responsible-use practices; ensure data privacy throughout the full teaching workflow.', tags:['bias','responsible use','Expert']},
        {s:'Promote a whole-institution culture of responsible AI use; mentor learners and peers on ethical AI practices.', tags:['Empowering Learners','Pioneer']}
      ],
      ict:[
        {s:'Demonstrate awareness of digital citizenship, online safety, and ethical ICT use as core professional responsibility.', tags:['Digital citizenship','ICT-CFT 4.1']},
        {s:'Manage student data responsibly in school digital systems; apply privacy-aware practices throughout classroom ICT workflows.', tags:['Data management','ICT-CFT Area 5']},
        {s:'Lead institutional digital ethics; advocate for responsible data-handling policies and equity in school-wide ICT use.', tags:['Ethics leadership','ICT-CFT L3']}
      ],
      un:[
        {s:'Ethical principles: do-no-harm, proportionality, non-discrimination, sustainability, and transparency/explainability as governing values.', tags:['2.1 Ethical Principles']},
        {s:'Safe & responsible use: data privacy, data sovereignty, IP compliance, and \u201csafety-by-design\u201d vs \u201csafety-by-use\u201d throughout the data lifecycle.', tags:['2.2 Safe Use']},
        {s:'Co-create ethical rules; critically audit AI providers\u2019 guidance; lead multi-stakeholder negotiations on AI ethics in education.', tags:['2.3 Co-creation']}
      ],
      synth:'Data protection is the shared backbone across all four. The ICT-CFT (2018) establishes digital citizenship and privacy responsibility as foundational norms; the KMK names GDPR and the EU AI Act directly; DigCompEdu lists ethical awareness as a transversal skill running through all six areas; and UNESCO AI-CFT devotes an entire competency area to ethics. \u201cData sovereignty\u201d in UNESCO 2.2 is the direct conceptual argument for the local, offline LLMs at the heart of this workshop.'
    },
    {
      id:'foundations', label:'\uD83D\uDD27 AI foundations & technical understanding',
      de:[
        {s:'Basic informatics education: understand the technical functioning of AI; know how LLMs and generative AI differ from earlier systems.', tags:['informatische Grundlagen']},
        {s:'Understand how AI is trained; critically assess the reliability and quality of outputs from a technical perspective.', tags:['Funktionsweise','G\u00FCte der Ergebnisse']},
        {s:'Re-evaluate competence requirements as technology evolves; build institutional evaluation and monitoring procedures for AI tools.', tags:['Evaluation','Weiterentwicklung']}
      ],
      eu:[
        {s:'Digital literacy: basic proficiency in operating AI tools and platforms; understand what AI can and cannot do.', tags:['Digital literacy','Newcomer']},
        {s:'Develop data literacy and computational thinking; curate and critically evaluate AI-generated resources.', tags:['data literacy','Integrator']},
        {s:'Innovate technical solutions; adapt and re-purpose AI tools for novel educational scenarios; contribute to institutional tool evaluation.', tags:['problem-solving','Pioneer']}
      ],
      ict:[
        {s:'Operate essential digital tools (productivity, communication, presentation); develop foundational ICT literacy as the precursor to understanding algorithmic systems.', tags:['Digital literacy','ICT-CFT Area 4']},
        {s:'Apply computational thinking across subjects; develop data literacy and subject-specific digital skills as a foundation for AI understanding.', tags:['Computational thinking','ICT-CFT 4.2']},
        {s:'Create innovative digital learning resources; model advanced ICT use for students and peers; pilot and document emerging digital approaches.', tags:['Digital innovation','ICT-CFT L3']}
      ],
      un:[
        {s:'Basic AI techniques: understand data, algorithms, training, and deployment; operate validated tools \u2014 prefer open-source alternatives.', tags:['3.1 Basics']},
        {s:'Application skills: compare symbolic, predictive, and generative AI; critically assess \u201cethics by design\u201d in candidate tools.', tags:['3.2 Application']},
        {s:'Creating with AI: customise, fine-tune, or assemble AI tools; build institutional repositories of vetted educational AI tools.', tags:['3.3 Creating']}
      ],
      synth:'All four reject black-box use. The ICT-CFT (2018) lays the foundation: computational thinking and digital literacy as prerequisites for AI literacy. The KMK demands genuine informatic understanding of how AI is built; DigCompEdu develops data literacy and curative skills; and UNESCO AI-CFT progresses from operating tools, through comparing AI types, to creating with AI \u2014 with an explicit open-source preference that directly underpins this workshop\u2019s use of Gemma via Ollama.'
    },
    {
      id:'pedagogy', label:'\uD83C\uDF93 AI pedagogy & teaching practice',
      de:[
        {s:'Use AI to support lesson design and preparation; understand AI as an adaptive learning environment and personalised tutor for students.', tags:['Lehr-Lernsituationen']},
        {s:'Make didactically justified decisions about using AI and not using it; apply AI for individualisation and personalised feedback.', tags:['Individualisierung','Feedback']},
        {s:'Develop a rich pedagogical-didactic repertoire combining AI and analogue approaches; co-create education-specific AI solutions in pilot projects.', tags:['Ko-Kreation','Pilotprojekte']}
      ],
      eu:[
        {s:'Teaching & Learning: integrate AI-driven adaptive learning systems and intelligent tutoring to support individual student needs.', tags:['Teaching & Learning','Newcomer']},
        {s:'Assessment: implement AI-assisted adaptive and formative assessment; use analytics to identify learning gaps and provide personalised feedback.', tags:['Assessment','Expert']},
        {s:'Empowering Learners: design personalised, inclusive, learner-centred strategies using AI; foster self-regulated learning and critical AI engagement.', tags:['Empowering Learners','Pioneer']}
      ],
      ict:[
        {s:'Use ICT tools for direct instruction, lesson preparation, and sharing digital resources; apply ICT to support and vary teaching methods.', tags:['Pedagogy L1','ICT-CFT Area 3']},
        {s:'Facilitate collaborative, inquiry-based, and problem-solving learning with ICT; organise group work and foster higher-order cognitive skills.', tags:['Student-centred','ICT-CFT 3.2']},
        {s:'Design transformative ICT-supported learning environments; experiment with emerging tools; mentor peers on innovative digital pedagogy at institutional level.', tags:['Pedagogical innovation','ICT-CFT L3']}
      ],
      un:[
        {s:'AI-assisted teaching: apply a design\u2013implementation\u2013reflection cycle; leverage pedagogical benefits while actively mitigating risks.', tags:['4.1 Assisted']},
        {s:'AI\u2013pedagogy integration: blend AI into student-centred practices; implement human-accountable decision loops in formative and summative assessment.', tags:['4.2 Integration']},
        {s:'Pedagogical innovation: design AI-immersed inquiry- and project-based learning; engineer triangular teacher\u2013student\u2013AI interactions.', tags:['4.3 Innovation']}
      ],
      synth:'Pedagogy is where all four frameworks are richest and most aligned. The ICT-CFT (2018) establishes the student-centred collaborative baseline; the KMK adds the critical demand to decide \u201cwith AND without AI\u201d; DigCompEdu focuses on adaptive assessment and empowering learners; and UNESCO AI-CFT synthesises all of this in a vision of AI-immersed triangular teacher\u2013student\u2013AI interactions. The arc \u2014 direct instruction \u2192 collaborative learning \u2192 innovative design \u2014 runs through all four.'
    },
    {
      id:'profdev', label:'\uD83C\uDF31 Professional development & lifelong learning',
      de:[
        {s:'Embed AI skills in all three phases of teacher education (pre-service, induction, in-service); ongoing AI professionalisation is a structural requirement.', tags:['Lehrkr\u00E4ftebildung']},
        {s:'Adapt PD formats as AI evolves; build regional competence centres that support distributed AI training for teachers.', tags:['Fortbildung','Kompetenzzentren']},
        {s:'Provide teachers with time, resources, and freedom for continuous learning; model a constructive error culture; teachers as permanent learners.', tags:['Ressourcen','Freir\u00E4ume']}
      ],
      eu:[
        {s:'Lifelong learning: commit to continuously updating AI knowledge and skills; treat AI upskilling as a standing professional obligation.', tags:['Lifelong learning','Newcomer']},
        {s:'Collaborate via AI tools and networks; share best practice and co-create materials within communities of practice.', tags:['Professional Engagement','Expert']},
        {s:'Contribute to institutional AI policy; lead CPD initiatives; advocate for responsible AI use at the systemic level.', tags:['policy','Pioneer']}
      ],
      ict:[
        {s:'Identify ICT tools for personal professional development; engage in self-directed digital CPD; recognise ICT as a vehicle for lifelong learning.', tags:['Self-directed CPD','ICT-CFT Area 6']},
        {s:'Participate in ICT-supported communities of practice; use digital tools for reflective peer learning and subject-specific professional growth.', tags:['Communities of practice','ICT-CFT 6.2']},
        {s:'Design and lead ICT-supported professional development programmes; lead professional learning communities; advocate for systemic innovation in teacher education.', tags:['PD leadership','ICT-CFT L3']}
      ],
      un:[
        {s:'Continuous PD: identify AI platforms for personal CPD; use AI for knowledge management and self-directed professional growth.', tags:['5.1 Continuous']},
        {s:'Collaborative PD: connect with peers and mentors via AI platforms; co-create teaching materials; respect IP and data privacy in collaboration.', tags:['5.2 Collaborative']},
        {s:'Leadership in PD: design AI-enhanced CPD programmes; mentor peers; contribute to institution-level policy on AI in teacher professional development.', tags:['5.3 Leadership']}
      ],
      synth:'The teacher as lifelong learner is the most universal idea across all four frameworks. The ICT-CFT (2018) establishes digital CPD and communities of practice as professional norms; the KMK embeds AI learning across all three training phases and demands dedicated time and resources; DigCompEdu names lifelong learning as a transversal skill; and UNESCO AI-CFT crowns this with leadership, mentoring, and institutional policy co-creation. Building an OER artefact in this workshop is exactly this competency in action.'
    }
  ];

  var current  = THEMES[0];
  var stageIdx = 0;

  function flag(w){ return {de:'\uD83C\uDDE9\uD83C\uDDEA', eu:'\uD83C\uDDEA\uD83C\uDDFA', ict:'\uD83C\uDF10', un:'\uD83C\uDF0D'}[w]; }
  function docname(w){ return {de:'KMK (Germany)', eu:'DigCompEdu Supplement (EU)', ict:'UNESCO ICT-CFT (2018)', un:'UNESCO AI-CFT (2025)'}[w]; }

  function renderCol(w){
    var el = document.getElementById('cw-col-' + w);
    var d  = current[w][stageIdx];
    var cc = COLCOLOR[w];
    var h  = '';
    h += '<div style="font-size:20px;line-height:1;margin-bottom:4px;">' + flag(w) + '</div>';
    h += '<div style="font-size:11px;font-weight:700;text-transform:uppercase;color:' + cc + ';letter-spacing:0.04em;margin-bottom:2px;">' + docname(w) + '</div>';
    h += '<div style="font-size:11px;color:#777;font-style:italic;margin-bottom:8px;">' + STAGES[w][stageIdx] + '</div>';
    h += '<span style="display:inline-block;font-size:10px;font-weight:600;color:#fff;background:' + STAGECOLOR[stageIdx] + ';padding:2px 8px;border-radius:20px;margin-bottom:10px;">' + STAGENAMES[stageIdx] + '</span>';
    h += '<p style="font-size:13px;line-height:1.55;margin:0 0 8px 0;color:#233;">' + d.s + '</p>';
    h += '<div>' + d.tags.map(function(t){ return '<span style="display:inline-block;font-size:10px;background:#e8f0fb;color:#2a5eb3;padding:1px 6px;border-radius:4px;margin:2px 1px;">' + t + '</span>'; }).join('') + '</div>';
    el.innerHTML = h;
  }

  function update(){
    document.getElementById('cw-stagename').textContent = STAGENAMES[stageIdx];
    COLS.forEach(function(w){ renderCol(w); });
    document.getElementById('cw-synth').textContent = current.synth;
  }

  var tb = document.getElementById('cw-themes');
  THEMES.forEach(function(t){
    var b = document.createElement('button');
    b.textContent = t.label;
    b.style.cssText = 'padding:6px 14px;border-radius:6px;border:1px solid #d9dee5;background:#fff;color:#334;font-size:12px;cursor:pointer;font-weight:500;';
    b.addEventListener('click', function(){
      current = t;
      Array.prototype.forEach.call(tb.children, function(x){ x.style.background='#fff'; x.style.borderColor='#d9dee5'; x.style.color='#334'; });
      b.style.background='#2a7ed3'; b.style.borderColor='#2a7ed3'; b.style.color='#fff';
      update();
    });
    tb.appendChild(b);
  });
  tb.children[0].style.background  = '#2a7ed3';
  tb.children[0].style.borderColor = '#2a7ed3';
  tb.children[0].style.color       = '#fff';

  document.getElementById('cw-stage').addEventListener('input', function(e){
    stageIdx = parseInt(e.target.value, 10);
    update();
  });

  update();
})();
</script>

--{{0}}--
Take your time with this. Pick the theme that matters most to your own subject, then walk
the slider from beginner to advanced and read across all four columns. The thing to notice
is how often the German, European and two global frameworks produce *almost interchangeable*
wording — four committees, working independently across three decades, converging on the
same competencies. The ICT-CFT column shows exactly how far back these ideas reach;
the AI-CFT column shows where they are heading.

### Reflection

After exploring the crosswalk: which competency theme do *you* feel least prepared in
right now? There is no wrong answer — this is a self-assessment.

[[ Human-centred mindset | Ethics & data protection | AI foundations | AI pedagogy | Professional development ]]

                    {{1}}
> 🎯 Whatever you picked, today's hands-on section touches **AI foundations** (running a
> local model) and **ethics & data protection** (keeping data on your machine) directly —
> and gives you a reusable artefact for **professional development**.


## 4 · LiaScript & Vibe Coding

You are reading this *inside* LiaScript right now. It is a free, open Markdown dialect
that turns a single `.md` file into an interactive course — quizzes, animations, embedded
HTML and code, text-to-speech — all from plain text.

> 📜 **Why it matters for OER:** one human-readable file, version-controllable on GitHub,
> served by any web link, licensable as CC BY-SA. No platform lock-in. That is the
> *low-threshold* path to Open Educational Resources.

      {{1}}
**The same pattern you saw in the crosswalk** — HTML elements written inline in Markdown,
followed by a `<script>` block. No `<!DOCTYPE>`, no wrapper tag:

      {{1}}
``` html
<!-- Write HTML elements directly in the Markdown: -->
<button id="demo-btn" style="padding:8px 20px;background:#2a7ed3;color:white;
  border:none;border-radius:6px;cursor:pointer;font-size:14px;">Click me</button>
<p id="demo-out" style="display:none;color:#2e9e5b;font-weight:600;margin-top:8px;">
  🎉 It works!</p>

<script>
document.getElementById('demo-btn').addEventListener('click', function(){
  document.getElementById('demo-out').style.display = 'block';
});
</script>
```

      {{1}}
<div class="box ok">

**🔴 Live example — the button below is the code above, rendered:**

<button id="sec4-live-btn" style="padding:8px 20px;background:#2a7ed3;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;">✋ Click me</button>
<p id="sec4-live-out" style="display:none;color:#2e9e5b;font-weight:600;margin-top:8px;">🎉 This widget runs entirely from one <code>.md</code> file — no platform, no build step.</p>

</div>

<script>
document.getElementById('sec4-live-btn').addEventListener('click', function(){
  document.getElementById('sec4-live-out').style.display = 'block';
});
</script>

--{{0}}--
LiaScript is the engine running this whole presentation. The crucial point for you as a
future educator is that it is just one text file. You can put it on GitHub, share a link,
and anyone can read it, fork it, or remix it — the definition of an Open Educational
Resource.

--{{1}}--
The pattern is always the same: HTML elements sit directly in the Markdown, a plain script
block wires up the behaviour. No framework, no build step. The live button above is that
exact pattern running inside this course file right now.

### What is *Vibe Coding*?

**Vibe Coding** = describing what you want in plain language and letting an AI assistant
draft the code, while *you* stay the accountable author who reviews and decides.

      {{1}}
<div class="box">

It lowers the threshold dramatically: you do not need to memorise syntax to produce a
working interactive OER element. You need **judgement** — exactly the *human accountability*
competency from UNESCO area 1.2.

</div>

      {{2}}
<div class="box priv">

🔒 **The local twist:** if your coding assistant is a **local Gemma model via Ollama**, then
your "vibe coding" prompts — which may contain student examples or unpublished material —
**never leave your laptop.** Vibe Coding + offline LLM = creativity *and* data protection.

</div>

--{{1}}--
Vibe coding does not remove the human — it relocates the human's job from typing syntax to
exercising judgement. You describe, the model drafts, you review and remain accountable.

--{{2}}--
And here is where the two halves of the workshop meet. If the assistant doing your vibe
coding is a local model, your prompts stay private. You get the creativity of AI assistance
without surrendering a single byte of student data.

## 5 · 🛠 Hands-on: Local AI Coding Assistant

Goal: a fully **offline** AI assistant inside VS Code, powered by **Gemma 4** through
**Ollama**, accessed via the built-in **Copilot Chat** panel. Everything below is copy-paste ready.

> ⚠️ **Before the session:** the four programs in the next section must already be installed.
> Ask your workshop's technical support to prepare the lab machines (checklist provided).

### Step 1 — Pull the model

Ollama downloads and runs the model locally. One command:

``` bash
# Pull Google's Gemma 4 (≈ 8 GB "latest" build used in this workshop)
ollama pull gemma4:latest

# Low-RAM fallback for 8 GB machines (~2 GB):
ollama pull gemma4:2b

# Verify it works — this answer is generated entirely on your machine:
ollama run gemma4:latest "Confirm you are running locally."
```

> 💾 Models are cached in `~/.ollama/models` — you download once, then work offline forever.

### Step 2 — Open the Copilot Chat panel

VS Code 1.99+ auto-detects any Ollama model that is already running. No extension config
file is needed:

1. Start the Ollama service (it runs in the background after install — verify with `ollama list`)
2. Open the Chat panel in VS Code: **`Ctrl+Alt+I`** / **`Cmd+Alt+I`** — or **View → Chat**
3. Click the **model name** at the top of the chat input box to open the model picker
4. Under the *Local* section, select **`gemma4:latest (Ollama)`**

> 💾 VS Code reads `http://localhost:11434/api/tags` to discover all pulled Ollama models
> automatically — no manual entry required.

      {{1}}
<div class="box priv">

🔒 **Privacy check:** once `gemma4:latest (Ollama)` is selected, VS Code routes every
inference call to your own machine. You can verify this with your network adapter switched
off — responses still arrive.

</div>

### Step 3 — Custom instructions live in `.github/copilot-instructions.md`

Copilot Chat reads a plain Markdown file from the project root to set permanent context
rules. Create `.github/copilot-instructions.md` in your workshop folder and paste:

``` markdown
You are a workshop coding assistant for university students building Open
Educational Resources with LiaScript.

Always:
- Prefer fully local, offline-capable solutions (Ollama + Gemma) over cloud APIs.
- Keep all student data on the local machine; never suggest uploading data to a
  third-party service. Flag any GDPR-relevant data handling (cite Art. 5, 6, 9).
- Produce educational output as Markdown or LiaScript, never plain prose dumps.
- Use open licences (MIT for code, CC BY-SA for content) and add a short licence header.
- Explain the code step by step before writing it — students are learning, not just shipping.
- When a decision is open, present numbered options and ask before assuming.
```

> VS Code picks this file up automatically whenever Copilot Chat is active in that workspace —
> no restart required. Add a second project-specific rule by appending a new paragraph.

### Step 4 — Use it

| Action | Shortcut / command |
|--------|--------------------|
| Open Chat panel | `Ctrl+Alt+I` / `Cmd+Alt+I` |
| Add selection to chat | select code → `Ctrl+Alt+I` / `Cmd+Alt+I` |
| Inline edit (quick fix) | select code → `Ctrl+I` / `Cmd+I` |
| Add a file to context | type `#file` in chat, then pick a file |
| Ask about workspace | type `@workspace` in chat |
| Switch model | click model name at top of the Chat panel |
| Toggle Ask / Edit / Agent mode | tabs at top of the Chat panel |

> 🔒 Every response comes from Gemma 4 on `localhost:11434`. **No data leaves the machine** —
> confirm this with your network adapter switched off.

--{{0}}--
This is the moment the whole workshop has been building toward. Four steps: pull the model,
open the Chat panel, point it at the local Gemma 4 model, set your project rules, and start
coding by conversation. And the headline is the privacy callout — you can literally turn off
your wifi and it still works.

### 🧪 Try it yourself

In Copilot Chat (custom instructions are active automatically via `.github/copilot-instructions.md`), try this Vibe Coding prompt:

``` text
Create a LiaScript multiple-choice quiz with three questions about why local
AI protects student data. Use the LiaScript [(X)] correct-answer syntax and add
a short feedback block. Output as Markdown I can paste into a .md file.
```

Then ask Copilot Chat to refine or audit its own output. Notice that it runs **completely
offline** — rules, models, everything stays on `localhost`.

      {{1}}
**Checkpoint quiz:**

Where does inference happen when you use this setup?

[( )] On Google's servers.
[( )] On GitHub's Copilot cloud.
[(X)] Locally, on `http://localhost:11434`, via Ollama.
*****************
<div class="box ok">
Right — Ollama serves the model on your own machine's localhost. That is the entire point.
</div>
*****************

## 6 · 🧰 Technical Support Setup Sheet

> **For the technical support member preparing the lab with me.** Every student PC needs the
> following. Listed with purpose, source and rough footprint so you can plan disk and time.

### Required programs (in install order)

| # | Program | Purpose in this workshop | Source / install | Notes |
|---|---------|--------------------------|------------------|-------|
| 1 | **VS Code** | Editor that hosts the AI assistant and the LiaScript files | code.visualstudio.com | Free. Latest stable (1.99+). |
| 2 | **Ollama** | Runs the local LLM and serves it on `localhost:11434` | ollama.com/download | macOS / Windows / Linux installers. Starts a background service. |
| 3 | **Gemma 4 model** | The actual offline LLM doing the work | `ollama pull gemma4:latest` (~8 GB) | Pull **before** the session over wired LAN. Also pull `gemma4:2b` (~2 GB) as a low-RAM fallback. |
| 4 | **GitHub Copilot** (VS Code built-in) | Provides the Chat panel that connects to the local Gemma 4 model | Built into VS Code 1.99+ — no separate install | A free GitHub account is sufficient. In the Chat model picker, select `gemma4:latest (Ollama)`. No tokens are consumed when using a local model. |

### Supporting tools

| Tool | Why | Notes |
|------|-----|-------|
| **Git** | Clone the workshop repo; version OER files | git-scm.com — often bundled with VS Code on Windows. |
| **A modern web browser** | Render the LiaScript course (`liascript.github.io/course/?<url>`) | Chrome / Firefox / Edge — any current version. |
| **Python 3.10+** *(optional)* | Run the Ollama API examples (`requests`) if you demo scripting | Add `pip install requests`. Only if you show the API. |

### Hardware & prep checklist

<div class="box warn">

- [ ] **RAM:** 16 GB recommended for `gemma4:latest`. On 8 GB machines, switch to `gemma4:2b`.
- [ ] **Disk:** ≥ 12 GB free per machine (model + tools).
- [ ] **Pre-pull the model** on every PC over wired LAN — do **not** rely on 30 students pulling 8 GB over wifi live.
- [ ] **Verify the service:** `curl http://localhost:11434/api/version` returns a version.
- [ ] **Pre-create** `.github/copilot-instructions.md` in the workshop project folder (copy from Section 5, Step 3).
- [ ] **Smoke test:** open VS Code → `Ctrl+Alt+I` → open Chat panel → select `gemma4:latest (Ollama)` → ask a question → confirm a Gemma 4 reply appears.
- [ ] **Offline test:** disable the network adapter and confirm Copilot Chat still answers.
- [ ] **GitHub account:** each machine needs a free GitHub account signed into VS Code (required to activate Copilot Chat).

</div>

> 📦 **One-line install reference (Linux/macOS):** the EU Green Labs `install_ollama.sh`
> pattern — install Ollama, start the service, `ollama pull gemma4:latest`, drop in the
> `.github/copilot-instructions.md`. Windows: run the Ollama `.exe` installer, then the same `ollama pull`.

### Setup verification (run this together)

This shows the model answering locally — no internet required:

``` bash
ollama list                          # gemma4:latest should appear
curl http://localhost:11434/api/version
ollama run gemma4:latest "Reply with exactly: LOCAL OK"
```

## Wrap-up — What You Take Home

      {{|>}}

- 🧭 A **map** of teacher AI competencies across three levels — and the insight that they
  point the same way: KMK → DigCompEdu → UNESCO, *Acquire → Deepen → Create*.
- 🔒 A working argument for **local AI**: no cloud dependency, GDPR-aligned data protection,
  no licence barriers — UNESCO's *data sovereignty* made concrete.
- 🛠 A **reusable setup**: Ollama + Gemma 4 + VS Code Copilot Chat, with the custom instructions file you copied from Section 5.
- 📜 The **LiaScript + Vibe Coding** workflow for building Open Educational Resources at a
  low threshold — and an OER artefact you made yourself.

--{{|>}}--
So what do you walk out with? A mental map of the frameworks, a defensible case for local
AI, a working offline assistant on your own machine, and the skills to build open
educational resources. That last one — building OER yourself — is the professional
development competency from all three frameworks, in action.

                {{1}}
> 🎓 **Digital agency** (*digitale Handlungsfähigkeit*) is not about using the flashiest tool.
> It is about understanding your tools well enough to choose them deliberately — and keeping
> both your data and your pedagogy in your own hands.

### Final reflection

Having built a local AI assistant and seen the frameworks side by side — has your sense of
which competency you're *least* prepared in changed?

[[ Yes, it shifted | No, same as before | I feel more prepared overall ]]

### Further reading

- **UNESCO** — AI Competency Framework for Teachers (2025)
- **AI Pioneers** — Supplement to the DigCompEdu Framework (Erasmus+, 2023)
- **KMK** — *Handlungsempfehlung … Künstliche Intelligenz in schulischen Bildungsprozessen* (2024)
- **LiaScript** — liascript.github.io · **Ollama** — ollama.com · **VS Code Chat** — code.visualstudio.com/docs/copilot/chat
- **EU Green Labs Workshops** — github.com/OVGU-VET-TechEd/EU_Green_Labs_Workshops

> 📜 This resource is released under **CC BY-SA 4.0**. Fork it, translate it, remix it.

**Thank you — now go build something local. 🌿**
