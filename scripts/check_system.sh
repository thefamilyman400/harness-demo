#!/bin/bash
echo "====== System Info ======"
echo "OS: $(uname -a)"
echo "CPU cores: $(nproc)"
echo "Disk: $(df -h / | tail -1)"
echo "========================="
