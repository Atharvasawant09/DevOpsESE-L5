from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsfeed App - Kubernetes Deployment</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            max-width: 1200px;
            width: 100%;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            animation: fadeInDown 0.8s ease;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header h1 {
            color: white;
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }

        .header p {
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
            font-weight: 300;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeInUp 0.8s ease;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }

        .card-icon {
            font-size: 3rem;
            margin-bottom: 15px;
        }

        .card h2 {
            color: #333;
            font-size: 1.5rem;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .card p {
            color: #666;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .status-badge {
            display: inline-block;
            padding: 8px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.85rem;
            margin-top: 10px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }

        .news-section {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            animation: fadeInUp 1s ease;
        }

        .news-section h2 {
            color: #333;
            font-size: 2rem;
            margin-bottom: 25px;
            font-weight: 600;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        .news-item {
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
            border-left: 5px solid #667eea;
        }

        .news-item:hover {
            transform: translateX(10px);
        }

        .news-item h3 {
            color: #333;
            font-size: 1.2rem;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .news-item p {
            color: #555;
            line-height: 1.6;
        }

        .news-date {
            color: #888;
            font-size: 0.85rem;
            margin-top: 10px;
            font-style: italic;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: white;
            font-size: 0.9rem;
            animation: fadeIn 1.5s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5rem;
            }
            
            .header p {
                font-size: 1rem;
            }
            
            .cards-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 Newsfeed App</h1>
            <p>Powered by Kubernetes & Docker</p>
        </div>

        <div class="cards-grid">
            <div class="card pulse">
                <div class="card-icon">🚀</div>
                <h2>Deployment Status</h2>
                <p>Application successfully deployed on Kubernetes cluster with 3 replica pods for high availability.</p>
                <span class="status-badge">✓ Running</span>
            </div>

            <div class="card">
                <div class="card-icon">🌐</div>
                <h2>NodePort Service</h2>
                <p>Exposed via NodePort 30007, making it accessible from outside the Kubernetes cluster.</p>
                <span class="status-badge">Port: 30007</span>
            </div>

            <div class="card">
                <div class="card-icon">⚡</div>
                <h2>Load Balanced</h2>
                <p>Traffic is automatically distributed across all healthy pods for optimal performance.</p>
                <span class="status-badge">3 Replicas</span>
            </div>
        </div>

        <div class="news-section">
            <h2>📋 Latest News Updates</h2>
            
            <div class="news-item">
                <h3>🎯 Kubernetes Deployment Successful</h3>
                <p>Your newsfeed application has been successfully deployed to a Kubernetes cluster using Docker Desktop. All pods are running smoothly with proper health checks.</p>
                <div class="news-date">{{ current_time }}</div>
            </div>

            <div class="news-item">
                <h3>🔧 DevOps Lab Assignment Complete</h3>
                <p>Successfully created a containerized Flask application with YAML manifests for Deployment and NodePort Service. The application demonstrates infrastructure-as-code principles.</p>
                <div class="news-date">{{ current_time }}</div>
            </div>

            <div class="news-item">
                <h3>✨ Modern UI Implementation</h3>
                <p>Enhanced the user interface with animated gradients, responsive card layouts, and smooth animations for an impressive demonstration.</p>
                <div class="news-date">{{ current_time }}</div>
            </div>

            <div class="news-item">
                <h3>🛡️ High Availability Architecture</h3>
                <p>Running with 3 replicas ensures zero-downtime deployments and fault tolerance. If one pod fails, the other two continue serving traffic seamlessly.</p>
                <div class="news-date">{{ current_time }}</div>
            </div>
        </div>

        <div class="footer">
            <p>🎓 DevOps Lab Project | Deployed on Docker Desktop Kubernetes</p>
            <p>Accessed via NodePort Service on port 30007</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    return render_template_string(HTML_TEMPLATE, current_time=current_time)

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "app": "newsfeed-app",
        "version": "2.0",
        "timestamp": datetime.now().isoformat()
    }

@app.route('/api/news')
def api_news():
    return {
        "news": [
            {
                "id": 1,
                "title": "Kubernetes Deployment Successful",
                "content": "Application deployed with 3 replicas",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": 2,
                "title": "NodePort Service Active",
                "content": "Service accessible on port 30007",
                "timestamp": datetime.now().isoformat()
            }
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30007, debug=True)
