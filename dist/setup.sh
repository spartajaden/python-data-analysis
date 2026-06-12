#!/bin/sh

# Setup script for Flask + MySQL application on Alpine/Lightweight Linux
# This script installs all dependencies and prepares the environment

set -e  # Exit on error

echo "=========================================="
echo "Flask + MySQL Setup Script for Lightweight Linux"
echo "=========================================="

# Update system packages
echo ""
echo "[1/5] Updating system packages..."
apk update
apk upgrade

# Install Python and pip
echo ""
echo "[2/5] Installing Python and pip..."
apk add --no-cache python3 py3-pip

# Install pip packages (globally for lightweight Linux)
echo ""
echo "[3/5] Installing Python packages..."
pip install --upgrade pip setuptools wheel
pip install flask==2.3.0
pip install flask-cors==4.0.0
pip install mysql-connector-python==8.0.33
pip install pymysql==1.1.3

# Database setup (optional)
echo ""
echo "[4/5] Database setup..."
echo "MySQL (optional): To install MySQL client, run: apk add --no-cache mysql-client"
echo "For running MySQL server in a separate container, see docker-compose.yml"

# Create requirements.txt
echo ""
echo "Creating requirements.txt..."
cat > requirements.txt << EOF
flask==2.3.0
flask-cors==4.0.0
mysql-connector-python==8.0.33
EOF

# Display setup summary
echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Update MySQL credentials in main.py:"
echo "   - host: 'mysql_container_name' (or your MySQL server address)"
echo "   - user: 'your_username'"
echo "   - password: 'your_password'"
echo "   - database: 'your_database'"
echo "2. Run the application: python3 main.py"
echo ""
echo "To reinstall packages:"
echo "   pip install -r requirements.txt"
echo ""
