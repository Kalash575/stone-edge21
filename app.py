from flask import Flask, render_template
import os

app = Flask(__name__)

# Website content data
content = {
    "company_name": "Stonedge Capital",
    "tagline": "New-Age Active Equity Investing",
    "headline": "Precision Investing in Public Markets",
    "description": "Founded in 2023 by Shantanu Jha and Kalash Mendole, Stonedge Capital is an independent hedge fund specializing in high-conviction public equity investing.",
    "philosophy": [
        {
            "icon": "search",
            "title": "Research-Driven, Quant-Enhanced",
            "description": "Combines deep fundamental analysis with quantitative tools to identify high-probability opportunities in the public equity markets."
        },
        {
            "icon": "bolt",
            "title": "Dynamic Strategy",
            "description": "Focuses on momentum trends, technical setups, and undervalued equities to capitalize on market inefficiencies."
        },
        {
            "icon": "chess-knight",
            "title": "Disciplined Execution",
            "description": "Systematic yet adaptive approach to minimize emotional bias and maximize risk-adjusted returns."
        }
    ],
    "edge": [
        {
            "icon": "rocket",
            "title": "Lean & Agile",
            "description": "No bloated teams—just a high-efficiency structure built for speed and precision."
        },
        {
            "icon": "user-tie",
            "title": "Founder-Led",
            "description": "Direct alignment of interests with full focus and capital commitment of founding partners."
        },
        {
            "icon": "bullseye",
            "title": "Pure Equity Focus",
            "description": "Solely dedicated to stock selection and tactical portfolio management."
        }
    ],
    "why_us": [
        {
            "icon": "brain",
            "title": "Next-Gen Active Investing",
            "description": "Blends human insight with data-driven decision-making for a modern edge."
        },
        {
            "icon": "trophy",
            "title": "Built for Performance",
            "description": "Designed to thrive in volatile markets through nimble positioning."
        },
        {
            "icon": "handshake",
            "title": "Transparent & Aligned",
            "description": "Clear, performance-focused partnership with no conflicts."
        }
    ],
    "founders": [
        {
            "name": "Shantanu Jha",
            "role": "Co-Founder & Portfolio Manager",
            "experience": "15+ years in quantitative equity strategies"
        },
        {
            "name": "Kalash Mendole",
            "role": "Co-Founder & Research Director",
            "experience": "Expert in technical and fundamental analysis"
        }
    ],
    "contact_email": "info@stonedgecapital.com"
}

@app.route('/')
def home():
    return render_template('index.html', **content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)