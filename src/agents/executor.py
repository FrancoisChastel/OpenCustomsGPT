# Copyright (C) 2025 Francois Chastel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from dataclasses import dataclass
from typing import List

from autogen_core import CancellationToken
from autogen_core.code_executor import CodeBlock
from autogen_ext.code_executors._common import CommandLineCodeResult
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor

from agents import cache


@dataclass
class Message:
    content: str

class DataAwareExecutor(LocalCommandLineCodeExecutor):
    def prepare_code(self, code_block: CodeBlock) -> str:
        injection = (
            "from helpers.tools import serialize_variables\n"
            "import json\n"
            "resulting_data = ''\n"
        )
        end_of_script = (
            "print(resulting_data)\n"
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
