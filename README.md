# OpenCustomsGPT

OpenCustomsGPT is an open source project that demonstrates the power of agent-based architectures using Sydonia's Data. 
This project empowers autonomous agents to extract data from Sydonia and perform various data-analysis task.
This project is a proof of concept and is not aimed for production.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Agent-Based Architecture:** Leverages autonomous agents to perform distributed tasks.
- **Interactive User Interface:** Uses Streamlit to provide a real-time, dynamic UI.
- **Modular and Extensible:** Designed for easy integration of tools.
- **Open Source Collaboration:** Encourages contributions and community engagement.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/FrancoisChastel/OpenCustomsGPT.git
   cd agentic-streamlit
   ```
2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To launch the Streamlit interface, run:
```bash
streamlit run src/app.py
```
After running the command, open your browser and navigate to the local URL provided by Streamlit.

### Configuration
Customize the project by editing the `config.yaml` file. Adjust agent parameters and UI settings as needed.

## Project Structure
```
OpenCustomsGPT/
├── src
  ├── rag/              # Contains rag logic for data-schema information
  ├── agents/           # Contains agent definitions and logic
  └── app.py            # Main entry point for the app
├── app.py             
├── config.yaml         # Configuration file for agents and UI settings
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Contributing
Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and how to submit pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For questions or feedback, please reach out at [francois@chastel.co](mailto:francois@chastel.co).
