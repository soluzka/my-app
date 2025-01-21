"""Legacy setup.py for backward compatibility"""
from setuptools import setup, find_packages

# This setup.py is maintained for backward compatibility
# Prefer using pyproject.toml for new installations
setup(
    name="advanced-scraper",
    version="1.0.0",
    description="An advanced web scraper with AI capabilities and real-time updates",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Login',
        'Flask-WTF',
        'Werkzeug',
        'aiohttp',
        'requests>=2.25.1',
        'beautifulsoup4',  # For parsing HTML
        'lxml',           # For parsing HTML and XML
        'matplotlib',      # For data visualization
        'seaborn',        # For statistical data visualization
        'yt-dlp',         # For downloading videos
        'schedule',       # For scheduling tasks
        'asyncio',        # For asynchronous programming
        'tweepy',         # For Twitter API access
        'quart',
        'hypercorn',
        'html2text',
        'python-dotenv',
        'httpx',
        'quart-auth',  # Added for authentication
        "quart>=0.18.4",
        "hypercorn>=0.14.3",
        "aiohttp>=3.8.5",
        "lxml>=4.9.3",
        "httpx>=0.25.2",
        "PyJWT>=2.8.0",
        "bcrypt>=4.1.2",
        "aiosmtplib>=3.0.1",
        "SQLAlchemy>=2.0.23",
        "aiosqlite>=0.19.0",
        "blinker>=1.6.2",
        "websockets>=13.0",  # Updated for yt-dlp compatibility
        "PyQt6==6.4.2",
        "qasync==0.24.0",
        "html2text==2020.1.16",
        'logging',
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "advanced-scraper=advanced_scraper:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
