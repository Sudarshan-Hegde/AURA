#!/bin/bash
# AURA Demonstration Script
# This script demonstrates the AURA relay application

echo "=========================================="
echo "AURA - Armed-forces Unified Relay Application"
echo "Demonstration Script"
echo "=========================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Validate all components
echo "Validating components..."

for file in aura_server.py aura_client.py test_aura.py config.json; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ $file (missing)"
        exit 1
    fi
done

echo ""
echo "All components validated successfully!"
echo ""

echo "To run AURA:"
echo ""
echo "1. Start the server:"
echo "   python3 aura_server.py"
echo ""
echo "2. In separate terminals, start clients:"
echo "   python3 aura_client.py"
echo ""
echo "3. Run tests:"
echo "   python3 test_aura.py"
echo ""
echo "For more information, see README.md"
echo ""
