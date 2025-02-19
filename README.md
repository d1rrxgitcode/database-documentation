# Database Documentation Generator

A Python service that automatically generates comprehensive documentation for your database schema using AI-powered descriptions.

## Features

- Automatically scans your PostgreSQL database structure
- Generates descriptions for tables and columns using AI
- Falls back to intelligent pattern-based descriptions when AI is unavailable
- Outputs clean, well-formatted Markdown documentation
- Supports custom comments from database

## Setup and Installation

### Windows

1. Clone the repository:
   ```cmd
   git clone https://github.com/d1rrxgitcode/database-documentation.git
   cd database-documentation
   ```

2. Create and activate virtual environment:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

### Linux/macOS

1. Clone the repository:
   ```bash
   git clone https://github.com/d1rrxgitcode/database-documentation.git
   cd database-documentation
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration

Create `.env` file in the project root with your database credentials:
```env
DB_HOST=your_host
DB_PORT=your_port
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

## Usage

After installation and configuration, run the script:

```bash
# Windows
python main.py

# Linux/macOS
python3 main.py
```

The script will:
1. Connect to your database
2. Scan all tables and columns
3. Generate descriptions using AI (if available) or fallback to pattern-based descriptions
4. Create a `database_documentation.md` file with the results

See [example.md](example.md) for an example of generated documentation.

## AI Description Generation

The service uses a lightweight TinyLlama model for generating column descriptions. If the AI model is unavailable, it falls back to intelligent pattern-based descriptions based on common database naming conventions.