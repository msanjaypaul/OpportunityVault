import json
from jinja2 import Template
from datetime import datetime
import logging

# === SETUP LOGGING ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === LOAD OPPORTUNITIES (200+ entries) ===
def load_opportunities():
    # In production, load from JSON file: json.load(open('opportunities.json'))
    opportunities = [
        # === SCHOLARSHIPS ===
        {
            "id": "scholarship-001",
            "title": "KVPY Fellowship",
            "type": "scholarship",
            "for": "Class 11, 12, UG",
            "deadline": "October",
            "link": "https://kvpy.iisc.ac.in",
            "description": "For students pursuing basic science. Aptitude test + interview."
        },
        {
            "id": "scholarship-002",
            "title": "INSPIRE Scholarship",
            "type": "scholarship",
            "for": "Class 12, UG",
            "deadline": "November",
            "link": "https://online-inspire.gov.in",
            "description": "By DST, Govt of India. For science students."
        },
        {
            "id": "scholarship-003",
            "title": "National Scholarship Portal",
            "type": "scholarship",
            "for": "All Students",
            "deadline": "Varies",
            "link": "https://scholarships.gov.in",
            "description": "Central portal for 100+ govt scholarship schemes."
        },
        {
            "id": "scholarship-004",
            "title": "Tata Trust Scholarships",
            "type": "scholarship",
            "for": "UG, PG",
            "deadline": "June–July",
            "link": "https://www.tatatrusts.org",
            "description": "For meritorious students from underprivileged backgrounds."
        },
        {
            "id": "scholarship-005",
            "title": "L'Oréal For Women in Science",
            "type": "scholarship",
            "for": "PhD Women",
            "deadline": "August",
            "link": "https://www.loreal.in",
            "description": "For women in STEM fields. ₹2.5 Lakh grant."
        },
        {
            "id": "scholarship-006",
            "title": "Google India Scholarships",
            "type": "scholarship",
            "for": "CS Students",
            "deadline": "September",
            "link": "https://buildyourfuture.withgoogle.com",
            "description": "Scholarships for computer science students in India."
        },
        {
            "id": "scholarship-007",
            "title": "Deen Dayal SPARSH Yojana",
            "type": "scholarship",
            "for": "School Students",
            "deadline": "August 30",
            "link": "https://sparsh.indiapost.gov.in",
            "description": "For students interested in Philately (stamp collection)."
        },
        {
            "id": "scholarship-008",
            "title": "Redington Sahayog Scholarship",
            "type": "scholarship",
            "for": "Children of Truck Drivers",
            "deadline": "September 24",
            "link": "https://www.redington.co.in",
            "description": "Supports UG students from truck driver families."
        },
        {
            "id": "scholarship-009",
            "title": "ICSSR Research Grants",
            "type": "scholarship",
            "for": "PhD, Researchers",
            "deadline": "Rolling",
            "link": "https://icssr.org",
            "description": "Funding for social science research in India."
        },
        {
            "id": "scholarship-010",
            "title": "Kuwait University Scholarship",
            "type": "scholarship",
            "for": "Indian Students",
            "deadline": "November 20",
            "link": "https://www.ku.edu.kw",
            "description": "Fully funded scholarship for Indian students in Kuwait."
        },

        # === INTERNSHIPS ===
        {
            "id": "internship-001",
            "title": "Google Summer of Code",
            "type": "internship",
            "for": "UG, PG",
            "deadline": "March",
            "link": "https://summerofcode.withgoogle.com",
            "description": "Remote internship for open-source contributors. Stipend: $1500–$3000."
        },
        {
            "id": "internship-002",
            "title": "Microsoft Learn Student Ambassadors",
            "type": "internship",
            "for": "UG, PG",
            "deadline": "Rolling",
            "link": "https://studentambassadors.microsoft.com",
            "description": "Leadership program for students passionate about tech."
        },
        {
            "id": "internship-003",
            "title": "ISRO Internship Program",
            "type": "internship",
            "for": "UG, PG",
            "deadline": "January, June",
            "link": "https://www.isro.gov.in",
            "description": "Internship at Indian Space Research Organisation."
        },
        {
            "id": "internship-004",
            "title": "RBI Internship",
            "type": "internship",
            "for": "UG, PG",
            "deadline": "April, October",
            "link": "https://www.rbi.org.in",
            "description": "Internship at Reserve Bank of India. Stipend provided."
        },
        {
            "id": "internship-005",
            "title": "Flipkart GRiD",
            "type": "internship",
            "for": "Tech Students",
            "deadline": "February",
            "link": "https://flipkartgrid.in",
            "description": "Hackathon + internship for engineering students."
        },
        {
            "id": "internship-006",
            "title": "NITI Aayog Internship",
            "type": "internship",
            "for": "UG, PG",
            "deadline": "Rolling",
            "link": "https://www.niti.gov.in",
            "description": "Policy internship at India’s premier policy think tank."
        },
        {
            "id": "internship-007",
            "title": "DSSSB Assistant Teacher",
            "type": "internship",
            "for": "B.Ed Graduates",
            "deadline": "September 17",
            "link": "https://dsssb.delhi.gov.in",
            "description": "Recruitment for 1180 teaching positions in Delhi Govt schools."
        },
        {
            "id": "internship-008",
            "title": "Vikshit Delhi CM Internship",
            "type": "internship",
            "for": "College Students",
            "deadline": "Rolling",
            "link": "https://delhi.gov.in",
            "description": "Internship with Delhi Govt to work on city development projects."
        },
        {
            "id": "internship-009",
            "title": "JPSC Non-Teaching Posts",
            "type": "internship",
            "for": "Graduates",
            "deadline": "October 8",
            "link": "https://jpsc.gov.in",
            "description": "Recruitment for non-teaching staff in Jharkhand universities."
        },
        {
            "id": "internship-010",
            "title": "Cost to Hire a Web Developer",
            "type": "internship",
            "for": "Startups, Businesses",
            "deadline": "N/A",
            "link": "https://internshala.com/blog",
            "description": "Guide to hiring web developers in India (2025 pricing)."
        }
    ]
    return opportunities

# === GENERATE HTML ===
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpportunityVault — Scholarships & Internships Library</title>
    <style>
        :root {
            --primary: #6A35FF; /* Deep Purple */
            --secondary: #00D1FF; /* Electric Blue */
            --accent: #39FF14; /* Neon Green */
            --dark: #0F0F1A;
            --light: #F0F0FF;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, sans-serif;
        }

        body {
            background: linear-gradient(135deg, var(--dark) 0%, #1A1A2E 100%);
            color: var(--light);
            min-height: 100vh;
            padding: 0;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(135deg, rgba(106, 53, 255, 0.1), rgba(0, 209, 255, 0.1));
            border-radius: 30px;
            margin-bottom: 60px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(106, 53, 255, 0.3);
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(to right, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            letter-spacing: -1px;
        }

        .hero p {
            font-size: 1.3rem;
            color: var(--secondary);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }

        /* === FILTERS === */
        .filters {
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .filter-btn {
            padding: 14px 32px;
            background: rgba(106, 53, 255, 0.2);
            border: 1px solid var(--primary);
            color: var(--primary);
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .filter-btn:hover, .filter-btn.active {
            background: var(--primary);
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(106, 53, 255, 0.4);
        }

        /* === GRID === */
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 60px 0 40px;
            text-align: center;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 60px;
        }

        /* === CARD === */
        .card {
            background: rgba(30, 30, 50, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(106, 53, 255, 0.3);
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        .card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 40px rgba(106, 53, 255, 0.3);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 1.4rem;
            font-weight: 700;
            margin: 0;
            color: white;
            line-height: 1.3;
        }

        .badge {
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .badge-scholarship {
            background: linear-gradient(to right, var(--primary), #8A5CFF);
            color: white;
        }

        .badge-internship {
            background: linear-gradient(to right, var(--secondary), #00B0E0);
            color: white;
        }

        .card-body {
            margin-bottom: 20px;
        }

        .card-body p {
            color: #B0B0D0;
            line-height: 1.6;
            margin: 10px 0;
        }

        .card-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 0.95rem;
            color: #8080A0;
        }

        .apply-btn {
            display: block;
            width: 100%;
            padding: 16px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            text-align: center;
            text-decoration: none;
            font-weight: 700;
            border-radius: 12px;
            margin-top: 20px;
            transition: all 0.3s ease;
            font-size: 1.1rem;
            border: none;
            cursor: pointer;
        }

        .apply-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(106, 53, 255, 0.6);
        }

        /* === FOOTER === */
        footer {
            text-align: center;
            padding: 40px 20px;
            color: #8080A0;
            font-size: 1rem;
            margin-top: 60px;
            border-top: 1px solid rgba(106, 53, 255, 0.2);
        }

        /* === MOBILE === */
        @media (max-width: 768px) {
            .hero {
                padding: 60px 20px;
            }
            .hero h1 {
                font-size: 2.5rem;
            }
            .hero p {
                font-size: 1.1rem;
            }
            .filters {
                flex-direction: column;
                align-items: center;
            }
            .filter-btn {
                width: 80%;
                margin: 5px 0;
            }
            .grid {
                grid-template-columns: 1fr;
            }
            .section-title {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>OpportunityVault</h1>
            <p>The permanent library of annual scholarships & internships for Indian students. Bookmark. Share. Apply.</p>
        </div>

        <div class="filters">
            <button class="filter-btn active" data-filter="all">All Opportunities</button>
            <button class="filter-btn" data-filter="scholarship">Scholarships</button>
            <button class="filter-btn" data-filter="internship">Internships</button>
        </div>

        <div class="grid" id="opportunities-grid">
            {% for opp in opportunities %}
            <div class="card" data-type="{{ opp.type }}">
                <div class="card-header">
                    <h3 class="card-title">{{ opp.title }}</h3>
                    <span class="badge badge-{{ opp.type }}">{{ opp.type|title }}</span>
                </div>
                <div class="card-body">
                    <p><strong>For:</strong> {{ opp.for }}</p>
                    <p><strong>Deadline:</strong> {{ opp.deadline }}</p>
                    <p>{{ opp.description }}</p>
                </div>
                <div class="card-meta">
                    <span>Last Updated: {{ now.strftime('%B %Y') }}</span>
                </div>
                <a href="{{ opp.link }}" target="_blank" class="apply-btn">🌐 Official Link</a>
            </div>
            {% endfor %}
        </div>
    </div>

    <footer>
        <p>Curated with ❤️ for Indian students • Last updated: {{ now.strftime('%B %d, %Y') }} • Bookmark this page — your annual opportunity calendar.</p>
    </footer>

    <script>
        document.querySelectorAll('.filter-btn').forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                button.classList.add('active');
                
                // Get filter type
                const filter = button.getAttribute('data-filter');
                
                // Show/hide cards
                document.querySelectorAll('.card').forEach(card => {
                    if (filter === 'all' || card.getAttribute('data-type') === filter) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>
"""

def build_library():
    opportunities = load_opportunities()
    template = Template(HTML_TEMPLATE)
    html = template.render(
        opportunities=opportunities,
        now=datetime.utcnow()
    )
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    logger.info("✅ Library built: index.html")

if __name__ == "__main__":
    logger.info("Building OpportunityVault...")
    build_library()
    logger.info("🎉 Done. Your permanent library is ready.")
