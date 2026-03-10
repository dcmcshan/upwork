#!/bin/bash
# Upwork Job Monitor - Installation Script

set -e

echo "=================================="
echo "Upwork Job Monitor - Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Found Python $PYTHON_VERSION"
echo ""

# Install dependencies
echo "Installing dependencies..."
if pip3 install -r requirements.txt; then
    echo "✓ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Setup environment file
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✓ Created .env file"
        echo ""
        echo "⚠️  IMPORTANT: Edit .env and add your Upwork API credentials"
        echo ""
        echo "To get credentials:"
        echo "1. Visit: https://www.upwork.com/services/api/apply"
        echo "2. Create a new application"
        echo "3. Copy Client ID and Secret to .env"
        echo "4. Run: python get_access_token.py"
        echo ""
    else
        echo "❌ .env.example not found"
        exit 1
    fi
else
    echo "✓ .env file already exists"
    echo ""
fi

# Make scripts executable
echo "Making scripts executable..."
chmod +x upwork upwork_job_monitor.py job_analytics.py examples.py
echo "✓ Scripts are now executable"
echo ""

echo "=================================="
echo "Installation Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Edit .env and add your Upwork API credentials"
echo "   nano .env"
echo ""
echo "2. Generate access token (if you haven't already):"
echo "   python get_access_token.py"
echo ""
echo "3. Test connection:"
echo "   ./upwork test"
echo ""
echo "4. Start monitoring:"
echo "   ./upwork search --query \"your skill\""
echo ""
echo "For help, see:"
echo "  - QUICKSTART.md for quick setup"
echo "  - USER_GUIDE.md for complete documentation"
echo "  - SUMMARY.md for command reference"
echo ""
echo "Run examples:"
echo "  python examples.py"
echo ""
