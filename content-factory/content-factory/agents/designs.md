# Design Overview

## Purpose
ContentFactory is a local-first content automation environment for generating, reviewing, and publishing faceless content through a team of AI agents.

## Main components
- Orchestrator: coordinates the end-to-end workflow
- Agents: specialist roles such as researcher, scriptwriter, producer, publisher, and analyst
- Content folders: pending, approved, and published content storage
- Templates: reusable structures for scripts and calendars

## Runtime flow
1. The orchestrator reads configuration from the project folder.
2. The agent workflow generates content drafts.
3. Approved content moves into the production path.
4. Published output is stored for review and reuse.

## Deployment model
- Best run from a local machine or dev container
- Uses environment variables for secrets
- Designed to be simple to start and easy to extend
