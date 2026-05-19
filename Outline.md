# GitHub Copilot Instructions – Teaching-Agent (BMad-Method)

## Overview
This repository uses the **Teaching-Agent** from the BMad-Method framework.
The agent supports educators in creating complete lecture packages step by step.

## Agent Entry Point
The agent is defined in `.bmad-core/agents/teaching-agent.md`.
Load this file as the system prompt when activating the agent in a web or
IDE context.

## Key Commands
| Command | Description |
|---|---|
| `/create-outline` | Start a new lecture outline |
| `/create-didactics` | Define didactic concept & professor persona |
| `/create-agenda` | Build the session agenda |
| `/create-session {n} {type} {title?}` | Create a session skeleton |
| `/promote-session {n} {type}` | Expand skeleton into full material |
| `/coauthor-materials` | Interactive co-authoring mode |
| `/validate-lecture` | Consistency & quality check |
| `/assemble-bundle` | Package all documents |
| `/help` | Show available commands |
| `/exit` | Exit agent persona |

## Folder Conventions
- `docs/`       → outline, didactics, agenda, validation reports
- `skeletons/`  → session skeletons (`{n}-{type}.md`)
- `materials/`  → full session materials (`{n}-{type}.md`)

## Output Format
All generated materials are **Markdown / LiaScript**.
See `.bmad-core/data/liascript-cheat-sheet.md` for syntax rules.

## Important Notes for Copilot
- Always reference `.bmad-core/` resources before generating content.
- Respect the professor persona defined in `docs/lecture-didactics.md`.
- Use numbered options when choices are open.
- Ask for missing inputs before proceeding.