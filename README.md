# OpenCustomsGPT

OpenCustomsGPT is an advanced open-source tool designed to interact with Sydonia (Customs Management System) data through AI-powered agents. It enables customs officials and analysts to extract, analyze, and visualize customs data efficiently.

## Table of Contents

- [OpenCustomsGPT](#opencustomsgpt)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Examples](#examples)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Production](#production)
    - [Development](#development)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Sydonia Integration:** Direct connection to Sydonia database for real-time data access
- **Data Management:**
  - Support for key Sydonia tables (expandable to full schema)
- **AI-Powered Analysis:**
  - Automated data extraction and processing
  - Advanced analytics and reporting
  - Custom query generation through natural language
- **Flexible Architecture:**
  - Multi-LLM provider support through LiteLLM

## Examples

https://github.com/user-attachments/assets/66016a59-2998-4501-a233-f305d6a86cb9

https://github.com/user-attachments/assets/223cebfa-d602-44eb-baad-e1f763a4ef2d

## Prerequisites

- Python 3.10
- Poetry for dependency management
- PostgreSQL database
- OpenAI API key or other supported LLM provider credentials

## Installation

### Production

For production deployment, please refer to our dedicated installation guide at [OpenCustomsGPT-install](https://github.com/FrancoisChastel/OpenCustomsGPT-install).

### Development

1. **Clone the repository:**
  
   ```bash
   git clone https://github.com/FrancoisChastel/OpenCustomsGPT.git
   cd OpenCustomsGPT
   ```

2. **Install dependencies with Poetry:**

   ```bash
   poetry install
   ```

## Configuration

1. **Set up environment variables:**

   ```bash
   export DB_URI="postgresql+psycopg2://user:password@localhost:5432/dbname"
   export OPENAI_API_KEY="your-api-key"
   export BASE_URL_LITELLM="http://0.0.0.0:4000"
   ```

2. **Configure LLM provider:**
   - Edit `configs/litellm/config.yaml` to set your preferred LLM provider
   - Available configurations include different agent types in `configs/` directory:
     - `coder_agent.yaml`: For code-related tasks
     - `normal_agent.yaml`: For general purpose tasks
     - `small_agent.yaml`: For lightweight operations
     - `thinking_agent.yaml`: For complex reasoning tasks
     - `sql_aent.yaml`: For sql-related tasks

## Usage

1. **Start the LiteLLM proxy:**

   ```bash
   poetry run litellm --config configs/litellm/config.yaml
   ```

2. **Launch the Chainlit interface:**

   ```bash
   poetry run chainlit run src/app.py
   ```

3. Access the application at `http://localhost:8501`

## Project Structure

```markdown
OpenCustomsGPT/
├── LICENSE                 # Project license file
├── README.md               # Project documentation and overview
├── configs/                # Configuration directory
│   ├── coder_agent.yaml    # Configuration for coding-focused AI agent
│   ├── litellm/            # LiteLLM configuration directory
│   │   └── config.yaml     # LiteLLM settings (LLM provider configs)
│   ├── normal_agent.yaml   # Configuration for standard AI agent
│   ├── small_agent.yaml    # Configuration for lightweight AI agent
│   ├── sql_agent.yaml    # Configuration for sql AI agent
│   └── thinking_agent.yaml # Configuration for reasoning-focused AI agent
└── dockerfile              # Container configuration
└── poetry.lock             # Poetry dependency lock file
└── pyproject.toml          # Python project configuration and dependencies
└── src/                    # Source code directory
│   ├── agents/             # AI agents implementation
│   │   ├── cache.py        # Caching mechanism for agents
│   │   ├── config.py       # Agent configuration handling
│   │   ├── executor.py     # Agent execution logic
│   │   ├── prompts.py      # Agent prompt templates
│   │   ├── setup.py        # Agent initialization
│   │   ├── sql.py          # Database interactions
│   │   └── tools.py        # Agent utilities and tools
│   ├── data_schema/        # Data structure definitions
│   │   ├── main.py         # Main schema handling
│   │   └── tmp/            # Temporary schema storage
│   │       └── schema.txt
│   ├── main.py             # Application entry point
│   └── render/             # Output rendering
│       ├── agents.py       # Agent response rendering
│       └── messages.py     # Message formatting
└── work_dir/               # Runtime working directory
    └── helpers/            # Helper functions
        └── tools.py        # Additional utility tools
```

## Roadmap

- [ ] Implement dashboarding solution
- [ ] Enhance SQL query generation
- [ ] Create plugin system for extensions
- [ ] Add verified tooling for LLM used
- [ ] Add targeted data-schema extraction
- [ ] Implement authentification and SSO
- [ ] Add nested agentic behavior
- [ ] Add multi-language support (french as a priority)
- [ ] Add Oracle support

## Contributing

Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and how to submit pull requests.

## License

This project is licensed under the AGPL License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or feedback, please reach out at [francois@chastel.co](mailto:francois@chastel.co).
