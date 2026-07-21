# ContentFactory

A local-first AI content automation environment for generating, reviewing, and publishing faceless content using a small team of agents.

## What this environment does
- Coordinates a multi-agent workflow for research, scripting, production, publishing, and analysis
- Stores drafts in pending, approved, and published content folders
- Supports local execution and simple setup for development or experimentation

## Requirements
See [requirements.md](requirements.md) for the full list of software, environment variables, and optional tools.

## Design overview
See [designs.md](designs.md) for the architecture, runtime flow, and deployment model.

## Installation

### 1. Prerequisites
Make sure you have:
- Python 3.10 or newer
- Git
- An Anthropic API key

### 2. Clone and enter the repository
```bash
git clone https://github.com/giriva/ContentFactory.git
cd ContentFactory
```

### 3. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set your environment variable
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

## Step-by-step startup instructions
1. Open a terminal in the repository root.
2. Activate the virtual environment.
3. Install the Python dependencies.
4. Export your Anthropic API key.
5. Start the environment with the one-command launcher below.

## One-command startup
Run the following command from the repository root:

```bash
./start.sh
```

The launcher will:
- create the local virtual environment if needed
- install the Python dependencies
- verify that the API key is available
- start the orchestrator workflow

## Project layout
- [content-factory/content-factory/orchestrator](content-factory/content-factory/orchestrator) contains the workflow runner
- [content-factory/content-factory/agents](content-factory/content-factory/agents) contains the agent prompts
- [content-factory/content-factory/content](content-factory/content-factory/content) contains pending, approved, and published content
- [content-factory/content-factory/templates](content-factory/content-factory/templates) stores reusable templates
