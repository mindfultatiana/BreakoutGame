#!/bin/bash

# Build script with better error handling
set -e

echo "Starting Buildozer build..."

# Initialize buildozer if needed
if [ ! -f buildozer.spec ]; then
    echo "Initializing buildozer..."
    buildozer init
fi

# Don't clean on first run - let buildozer set up the environment first
echo "Building APK..."
buildozer -v android debug

echo "Build completed!"
echo "APK should be in bin/ directory"