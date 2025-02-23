import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import List

import streamlit as st
from autogen_core import CancellationToken
from autogen_core.code_executor import CodeBlock
from autogen_ext.code_executors._common import CommandLineCodeResult
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor

from agents import cache


@dataclass
class Message:
    content: str

class DataAwareExecutor(LocalCommandLineCodeExecutor):
    def prepare_code(self, code_block: CodeBlock) -> str:
        # Prepend code that loads the DataFrame
        with open(f"{self.work_dir}/df.pkl", "wb") as file:
            pickle.dump(cache.cached_variables["dataframes"][-1], file)

        injection = (
            "import pickle, pandas as pd\n"
            "df = pickle.load(open('df.pkl', 'rb'))\n"
        )
        end_of_script = (
            "import os\n"
            "import uuid\n"
            "from pathlib import Path\n"
            "fig_path = Path('tmp') / f'fig_{uuid.uuid4()}.pkl'\n"
            "fig_path.parent.mkdir(parents=True, exist_ok=True)\n"
            "with open(fig_path, 'wb') as f:\n"
            "    pickle.dump(fig, f)\n"
            "print(f'{fig_path}')\n"
        )
        
        return injection + code_block.code.replace("fig.show()", "") + end_of_script
    
    async def _execute_code_dont_check_setup(self, code_blocks: List[CodeBlock], cancellation_token: CancellationToken) -> CommandLineCodeResult:
        filtered_code_blocks = []
        for codeblock in code_blocks:
            print(codeblock.code)
            if codeblock.language == "python":
                codeblock.code = self.prepare_code(codeblock)
                filtered_code_blocks.append(codeblock)
        return await super()._execute_code_dont_check_setup(filtered_code_blocks, cancellation_token)
