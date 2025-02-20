#!/bin/bash

# Get the current year
YEAR=$(date +%Y)
# Organization name - change this as needed
ORG_NAME="Francois Chastel"

# License header template
LICENSE_HEADER="# Copyright (C) $YEAR $ORG_NAME
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

"

# Find all Python files recursively
find . -type f -name "*.py" | while read -r file; do
  # Check if file already has the copyright header
  if ! grep -q "Copyright (C)" "$file"; then
    echo "Adding license header to $file"
    # Create a temporary file
    temp_file=$(mktemp)
    # Add the license header followed by the original content
    echo "$LICENSE_HEADER" > "$temp_file"
    cat "$file" >> "$temp_file"
    # Replace the original file with the new content
    mv "$temp_file" "$file"
  else
    echo "License header already exists in $file"
  fi
done