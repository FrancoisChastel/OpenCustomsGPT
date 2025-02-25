# OpenCustomsGPT

OpenCustomsGPT is an advanced open-source tool designed to interact with Sydonia (Customs Management System) data through AI-powered agents. It enables customs officials and analysts to extract, analyze, and visualize customs data efficiently.

## Table of Contents

- [OpenCustomsGPT](#opencustomsgpt)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Production](#production)
    - [Development](#development)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Sydonia Integration:** Direct connection to Sydonia database for real-time data access
- **Data Management:**
  - Extract and save customs data
  - Support for key Sydonia tables (expandable to full schema)
  - Data visualization and analytics capabilities
- **AI-Powered Analysis:**
  - Automated data extraction and processing
  - Advanced analytics and reporting
  - Custom query generation through natural language
- **Interactive Interface:**
  - Real-time data visualization
  - User-friendly query builder
  - Export functionality for reports
- **Flexible Architecture:**
  - Modular design for easy extensions
  - Multi-LLM provider support through LiteLLM
  - Scalable for different customs office needs
 
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
   ```

2. **Configure LLM provider:**
   - Edit `configs/litellm/config.yaml` to set your preferred LLM provider
   - Available configurations include different agent types in `configs/` directory:
     - `coder_agent.yaml`: For code-related tasks
     - `normal_agent.yaml`: For general purpose tasks
     - `small_agent.yaml`: For lightweight operations
     - `thinking_agent.yaml`: For complex reasoning tasks

## Usage

1. **Start the LiteLLM proxy:**

   ```bash
   poetry run litellm --config configs/litellm/config.yaml
   ```

2. **Launch the Chainlit interface:**

   ```bash
   poetry run chainlit run src/app.py
   ```

3. Access the application at `http://localhost:8000`

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

## Contributing

Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and how to submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or feedback, please reach out at [francois@chastel.co](mailto:francois@chastel.co).
