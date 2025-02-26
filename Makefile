# Raspberry Pi Workshop Makefile
# This Makefile provides commands for setting up and managing the Raspberry Pi Workshop environment

# Default target - shows help
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make help				- Show this help message"
	@echo "  make os-deps			- Install OS dependencies"
	@echo "  make install-uv		- Install uv package manager if not present"
	@echo "  make setup-venv		- Create Python virtual environment"
	@echo "  make install-deps		- Install Python dependencies from pyproject.toml"
	@echo "  make install-ollama	- Install Ollama"

# Install OS dependencies
.PHONY: os-deps
os-deps:
	@echo "Installing OS dependencies..."
	sudo apt update -y
	sudo apt upgrade -y
	sudo apt install git code python3 python3-dev python3-pip libgpiod2 curl -y
	sudo apt full-upgrade -y
	sudo apt autoremove -y
	@echo "OS dependencies installed successfully."

# Install uv if not present
.PHONY: install-uv
install-uv:
	@echo "Checking if uv is installed..."
	@if ! command -v uv &> /dev/null; then \
		echo "uv not found. Installing..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		echo "uv installed successfully."; \
	else \
		echo "uv is already installed."; \
	fi

# Create Python virtual environment
.PHONY: setup-venv
setup-venv:
	@echo "Creating Python virtual environment..."
	uv venv --python python3.12
	@echo "Virtual environment created successfully."

# Install Python dependencies
.PHONY: install-deps
install-deps:
	@echo "Installing Python dependencies from pyproject.toml..."
	uv sync
	@echo "Python dependencies installed successfully."

.PHONY: install-ollama
install-ollama:
	curl -fsSL https://ollama.com/install.sh | sh
