import pickle
from typing import Any
from typing import Coroutine
from typing import List
from typing import override  # type: ignore

import chainlit as cl
import pandas as pd
from autogen_core import CancellationToken
from autogen_core.code_executor import CodeBlock
from autogen_ext.code_executors._common import CommandLineCodeResult
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from agents import cache


class DataAwareExecutor(DockerCommandLineCodeExecutor):
    def prepare_code(self, code_block: CodeBlock) -> str:
        # Prepend code that loads the DataFrame
        with open(f"{self.work_dir}/df.pkl", "wb") as file:
            pickle.dump(cache.cached_variables["dataframes"][-1], file)

        injection = (
            "import pickle, pandas as pd\n"
            "df = pickle.load(open('df.pkl', 'rb'))\n"
        )
        return injection + code_block.code
    
    @override
    def _execute_code_dont_check_setup(self, code_blocks: List[CodeBlock], cancellation_token: CancellationToken) -> Coroutine[Any, Any, CommandLineCodeResult]:
        for codeblock in code_blocks:
            if codeblock.language == "python":
                codeblock.code = self.prepare_code(codeblock)
        return super()._execute_code_dont_check_setup(code_blocks, cancellation_token)
        return super()._execute_code_dont_check_setup(code_blocks, cancellation_token)
