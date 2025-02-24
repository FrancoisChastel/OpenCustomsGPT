for i in `find . -name "*.py"`; do
    cat - $i > /tmp/f.py <<EOF
# Copyright (C) Francois Chastel - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Francois Chastel <francois@chastel.co>, February 2024
EOF
    mv /tmp/f.py $i
done