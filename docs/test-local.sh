#!/bin/bash

# Simple script to test the GitHub Pages site locally

echo "🚀 Starting local test server..."
echo ""
echo "Your site will be available at:"
echo "👉 http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    cd "$(dirname "$0")"
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    cd "$(dirname "$0")"
    python -m http.server 8000
else
    echo "❌ Python not found. Please install Python to run a local server."
    echo ""
    echo "Alternatively, just open index.html in your browser:"
    echo "open index.html"
fi
