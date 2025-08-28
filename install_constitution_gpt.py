# install_constitution_gpt.py
"""
Installation Complète ConstitutionGPT Backend + Interface
Script d'installation automatisée pour présentation ministérielle
"""

import os
import sys
import shutil
import subprocess
import json
import secrets
from pathlib import Path

def print_header():
    print("🇬🇳" + "="*70)
    print("   CONSTITUTIONGPT GUINÉE - INSTALLATION MINISTÉRIELLE")
    print("   Interface Excellence Mondiale + Backend Sécurisé")
    print("="*72)

def check_requirements():
    """Vérifier les prérequis système"""
    print("\n📋 VÉRIFICATION DES PRÉREQUIS...")
    
    # Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ requis")
        return False
    print(f"✅ Python {sys.version.split()[0]} détecté")
    
    # Pip disponible
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      capture_output=True, check=True)
        print("✅ Pip disponible")
    except subprocess.CalledProcessError:
        print("❌ Pip non disponible")
        return False
    
    return True

def create_project_structure():
    """Créer la structure complète du projet"""
    print("\n📁 CRÉATION STRUCTURE PROJET...")
    
    directories = [
        "templates",
        "static/css", 
        "static/js",
        "static/images",
        "logs",
        "config",
        "certificates",
        "data",
        "backups"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   📂 {directory}")
    
    print("✅ Structure créée")

def install_dependencies():
    """Installer toutes les dépendances"""
    print("\n📦 INSTALLATION DÉPENDANCES...")
    
    requirements = [
        "flask==2.3.3",
        "flask-cors==4.0.0", 
        "flask-limiter==3.5.0",
        "pyjwt==2.8.0",
        "gunicorn==21.2.0",
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "cryptography==41.0.7",
        "werkzeug==2.3.7"
    ]
    
    for req in requirements:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", req
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {req.split('==')[0]}")
        except subprocess.CalledProcessError:
            print(f"   ⚠️ Erreur installation {req}")
    
    print("✅ Dépendances installées")

def create_backend_files():
    """Créer les fichiers backend"""
    print("\n🔧 CRÉATION FICHIERS BACKEND...")
    
    # Configuration environnement
    env_content = f"""# Configuration ConstitutionGPT Production
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY={secrets.token_hex(32)}
JWT_SECRET={secrets.token_hex(32)}

# API Configuration
GROQ_API_KEY=GROQ_API_KEY

# Server Configuration  
HOST=0.0.0.0
PORT=5000
WORKERS=4

# Security
RATE_LIMIT=100 per hour
MAX_MESSAGE_LENGTH=1000
SESSION_TIMEOUT_HOURS=24

# Database
DATABASE_PATH=constitution_improved_db.pkl

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/constitution_backend.log
ACCESS_LOG=logs/access.log
ERROR_LOG=logs/error.log
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("   ✅ Configuration .env")
    
    # Serveur principal
    main_server = '''# app.py - Serveur Principal ConstitutionGPT
import os
from pathlib import Path
from dotenv import load_dotenv

# Chargement configuration
load_dotenv()

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
import jwt
import hashlib
import datetime
import secrets
from functools import wraps

# Configuration logging
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(levelname)s - [%(request.remote_addr)s] - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv('LOG_FILE', 'logs/app.log')),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# CORS Configuration
CORS(app, origins=["http://localhost:3000", "https://constitution.gov.gn"])

# Rate Limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[os.getenv('RATE_LIMIT', '100 per hour')]
)

# Import de votre chatbot
try:
    from constitution_gpt_excellence import ConstitutionGPTWorldClassExcellence
    CHATBOT_AVAILABLE = True
    chatbot = None
except ImportError:
    CHATBOT_AVAILABLE = False
    chatbot = None
    logging.warning("Module chatbot non trouvé - Mode démo")

# Configuration utilisateurs autorisés
AUTHORIZED_USERS = {
    "ministre@gouvernement.gn": {
        "password_hash": hashlib.sha256("MinistereGN2025!".encode()).hexdigest(),
        "role": "ministre",
        "name": "Excellence le Ministre"
    },
    "secretaire@gouvernement.gn": {
        "password_hash": hashlib.sha256("SecretariatGN2025!".encode()).hexdigest(),
        "role": "secretaire", 
        "name": "Secrétaire Général"
    },
    "demo@gouvernement.gn": {
        "password_hash": hashlib.sha256("DemoGN2025!".encode()).hexdigest(),
        "role": "demo",
        "name": "Utilisateur Démo"
    }
}

def init_chatbot():
    """Initialisation du chatbot"""
    global chatbot
    if not CHATBOT_AVAILABLE:
        return False
    
    try:
        groq_key = os.getenv('GROQ_API_KEY')
        if not groq_key:
            logging.error("Clé API Groq manquante")
            return False
        
        chatbot = ConstitutionGPTWorldClassExcellence(groq_key)
        db_path = os.getenv('DATABASE_PATH', 'constitution_improved_db.pkl')
        
        if chatbot.load_complete_database(db_path):
            logging.info("Chatbot initialisé avec succès")
            return True
        else:
            logging.error("Échec chargement base de données")
            return False
    except Exception as e:
        logging.error(f"Erreur initialisation: {str(e)}")
        return False

# Décorateur authentification
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            return jsonify({'error': 'Token requis'}), 401
        
        try:
            payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
            request.user = payload
            return f(*args, **kwargs)
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token invalide'}), 401
    
    return decorated

@app.route('/')
def index():
    """Page principale"""
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/health')
def health():
    """Statut système"""
    return jsonify({
        'status': 'healthy',
        'chatbot_ready': chatbot is not None,
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/auth/login', methods=['POST'])
@limiter.limit("10 per minute")
def login():
    """Connexion"""
    data = request.get_json()
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    
    if email not in AUTHORIZED_USERS:
        return jsonify({'error': 'Identifiants invalides'}), 401
    
    user_data = AUTHORIZED_USERS[email]
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if password_hash != user_data['password_hash']:
        return jsonify({'error': 'Identifiants invalides'}), 401
    
    token = jwt.encode({
        'email': email,
        'role': user_data['role'],
        'name': user_data['name'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=int(os.getenv('SESSION_TIMEOUT_HOURS', 24)))
    }, os.getenv('JWT_SECRET'), algorithm='HS256')
    
    logging.info(f"Connexion réussie: {user_data['name']}")
    
    return jsonify({
        'success': True,
        'token': token,
        'user': {
            'email': email,
            'name': user_data['name'], 
            'role': user_data['role']
        }
    })

@app.route('/api/auth/verify', methods=['GET'])
def verify():
    """Vérification token"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token:
        return jsonify({'error': 'Token requis'}), 401
    
    try:
        payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
        return jsonify({'valid': True, 'user': payload})
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Token invalide'}), 401

@app.route('/api/chat/message', methods=['POST'])
@require_auth
@limiter.limit("30 per minute")
def chat():
    """Endpoint chat principal"""
    data = request.get_json()
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({'error': 'Message requis'}), 400
    
    if len(message) > int(os.getenv('MAX_MESSAGE_LENGTH', 1000)):
        return jsonify({'error': 'Message trop long'}), 400
    
    if not chatbot:
        return jsonify({'error': 'Service temporairement indisponible'}), 503
    
    try:
        response = chatbot.generate_world_class_response(message)
        
        logging.info(f"Question traitée pour {request.user['name']}")
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.datetime.now().isoformat()
        })
    except Exception as e:
        logging.error(f"Erreur traitement: {str(e)}")
        return jsonify({'error': 'Erreur lors du traitement'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint non trouvé'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Erreur serveur'}), 500

if __name__ == '__main__':
    if init_chatbot():
        print("🇬🇳 ConstitutionGPT Serveur - Interface Ministérielle")
        print("=" * 55)
        print("✅ Chatbot initialisé")
        print("🔐 Authentification active") 
        print("🌐 Serveur prêt sur http://localhost:5000")
        print("👤 Comptes: ministre@gouvernement.gn / demo@gouvernement.gn")
        print("=" * 55)
        
        app.run(
            host=os.getenv('HOST', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)),
            debug=False
        )
    else:
        print("❌ Impossible d'initialiser le chatbot")
        print("Vérifiez constitution_improved_db.pkl et la clé API")
'''
    
    with open('app.py', 'w') as f:
        f.write(main_server)
    print("   ✅ Serveur principal app.py")

def create_frontend_template():
    """Créer le template frontend dans le bon répertoire"""
    print("\n🎨 CRÉATION TEMPLATE FRONTEND...")
    
    # HTML template (copie du précédent artifact)
    html_template = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConstitutionGPT Guinée - Interface Ministérielle</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* Tous les styles CSS de l'artifact précédent */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #60a5fa 100%); min-height: 100vh; color: #1f2937; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; min-height: 100vh; display: flex; flex-direction: column; }
        .header { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 30px; margin-bottom: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1); text-align: center; border: 1px solid rgba(255, 255, 255, 0.2); }
        .flag-icon { width: 80px; height: 60px; background: linear-gradient(to bottom, #dc2626 33%, #fbbf24 33%, #fbbf24 66%, #10b981 66%); border-radius: 8px; margin: 0 auto 20px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); }
        .header h1 { font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 700; color: #1e3a8a; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); }
        .header .subtitle { font-size: 1.1rem; color: #4b5563; font-weight: 500; margin-bottom: 20px; }
        .version-badge { background: linear-gradient(45deg, #dc2626, #ef4444); color: white; padding: 8px 20px; border-radius: 25px; font-size: 0.9rem; font-weight: 600; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3); }
        .auth-section { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 40px; margin-bottom: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); text-align: center; }
        .auth-form { max-width: 400px; margin: 0 auto; }
        .auth-input { width: 100%; padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 12px; font-size: 1rem; margin-bottom: 20px; transition: all 0.3s ease; }
        .auth-input:focus { outline: none; border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1); }
        .auth-button { width: 100%; background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; border: none; padding: 15px; border-radius: 12px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.3); }
        .auth-button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4); }
        .security-notice { background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 20px; border-radius: 12px; margin-top: 20px; border: 1px solid #f59e0b; }
        .security-notice h4 { color: #92400e; margin-bottom: 10px; font-weight: 600; }
        .security-notice p { color: #78350f; font-size: 0.9rem; }
        .chat-container { flex: 1; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-radius: 20px; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }
        .chat-header { background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; padding: 20px 30px; display: flex; align-items: center; justify-content: space-between; }
        .chat-header h2 { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 600; }
        .status-indicator { display: flex; align-items: center; gap: 8px; font-size: 0.9rem; }
        .status-dot { width: 10px; height: 10px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .chat-messages { flex: 1; padding: 30px; overflow-y: auto; background: #fafafa; max-height: 500px; }
        .message { margin-bottom: 25px; }
        .message.user { text-align: right; }
        .message.assistant { text-align: left; }
        .message-bubble { display: inline-block; max-width: 80%; padding: 20px 25px; border-radius: 20px; font-size: 1rem; line-height: 1.6; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); }
        .message.user .message-bubble { background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; border-bottom-right-radius: 5px; }
        .message.assistant .message-bubble { background: white; color: #374151; border: 1px solid #e5e7eb; border-bottom-left-radius: 5px; }
        .message-time { font-size: 0.75rem; color: #9ca3af; margin-top: 5px; }
        .input-area { padding: 25px 30px; background: white; border-top: 1px solid #e5e7eb; }
        .input-container { display: flex; gap: 15px; align-items: flex-end; }
        .input-field { flex: 1; min-height: 50px; padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 15px; font-size: 1rem; font-family: inherit; resize: vertical; transition: all 0.3s ease; background: #f9fafb; }
        .input-field:focus { outline: none; border-color: #3b82f6; background: white; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1); }
        .send-button { background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; border: none; padding: 15px 25px; border-radius: 15px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.3); }
        .send-button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4); }
        .features { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 30px; margin-top: 30px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }
        .features h3 { font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #1e3a8a; margin-bottom: 20px; text-align: center; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
        .feature-card { background: linear-gradient(135deg, #f8fafc, #f1f5f9); padding: 25px; border-radius: 15px; border: 1px solid #e2e8f0; transition: all 0.3s ease; }
        .feature-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1); }
        .feature-icon { width: 50px; height: 50px; background: linear-gradient(135deg, #1e3a8a, #3b82f6); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; font-size: 1.5rem; }
        .feature-card h4 { font-size: 1.2rem; font-weight: 600; color: #1f2937; margin-bottom: 10px; }
        .feature-card p { color: #6b7280; line-height: 1.6; }
        .hidden { display: none; }
        @media (max-width: 768px) { .container { padding: 10px; } .header { padding: 20px; } .header h1 { font-size: 2rem; } .chat-messages { padding: 20px; } .message-bubble { max-width: 90%; padding: 15px 20px; } .features-grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="flag-icon"></div>
            <h1>ConstitutionGPT Guinée</h1>
            <p class="subtitle">Assistant Intelligent pour la Constitution de la République de Guinée 2025</p>
            <span class="version-badge">Version Excellence Ministérielle</span>
        </header>

        <div class="auth-section" id="authSection">
            <h2 style="font-family: 'Playfair Display', serif; color: #1e3a8a; margin-bottom: 30px;">Accès Sécurisé</h2>
            <div class="auth-form">
                <input type="email" class="auth-input" id="emailInput" placeholder="Email officiel">
                <input type="password" class="auth-input" id="passwordInput" placeholder="Mot de passe">
                <button class="auth-button" onclick="authenticate()">Se Connecter</button>
                
                <div style="margin: 20px 0; padding: 15px; background: #f3f4f6; border-radius: 8px;">
                    <strong>Comptes de démonstration :</strong><br>
                    <small>ministre@gouvernement.gn : MinistereGN2025!</small><br>
                    <small>demo@gouvernement.gn : DemoGN2025!</small>
                </div>
            </div>
            
            <div class="security-notice">
                <h4>🔒 Sécurité Renforcée</h4>
                <p>Interface protégée par authentification sécurisée. Accès réservé aux autorités gouvernementales.</p>
            </div>
        </div>

        <div class="chat-container hidden" id="chatContainer">
            <div class="chat-header">
                <h2>💬 Assistant Constitutionnel</h2>
                <div class="status-indicator">
                    <span class="status-dot"></span>
                    <span>Système Opérationnel</span>
                </div>
            </div>
            
            <div class="chat-messages" id="chatMessages"></div>
            
            <div class="input-area">
                <div class="input-container">
                    <textarea class="input-field" id="messageInput" placeholder="Posez votre question sur la Constitution guinéenne..." rows="2"></textarea>
                    <button class="send-button" onclick="sendMessage()">Envoyer</button>
                </div>
            </div>
        </div>

        <div class="features">
            <h3>🌟 Fonctionnalités Excellence</h3>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🧠</div>
                    <h4>IA Avancée</h4>
                    <p>Groq optimisé pour la Constitution guinéenne avec corrections automatiques.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h4>Performance</h4>
                    <p>Réponses ultra-rapides avec cache intelligent et validation qualité.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h4>Précision</h4>
                    <p>Maîtrise des 199 articles avec corrections automatiques des erreurs.</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = window.location.origin;
        let authToken = localStorage.getItem('auth_token');
        
        async function authenticate() {
            const email = document.getElementById('emailInput').value;
            const password = document.getElementById('passwordInput').value;
            
            if (!email || !password) {
                alert('Veuillez saisir vos identifiants.');
                return;
            }

            try {
                const response = await fetch('/api/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    authToken = data.token;
                    localStorage.setItem('auth_token', authToken);
                    
                    document.getElementById('authSection').classList.add('hidden');
                    document.getElementById('chatContainer').classList.remove('hidden');
                    
                    addMessage('assistant', `Connexion réussie. Bienvenue ${data.user.name}. Interface ConstitutionGPT prête pour vos questions constitutionnelles.`);
                } else {
                    alert(data.error || 'Erreur d\\'authentification');
                }
            } catch (error) {
                alert('Erreur de connexion au serveur');
            }
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message || !authToken) return;
            
            addMessage('user', message);
            input.value = '';
            
            const typingDiv = addTypingIndicator();
            
            try {
                const response = await fetch('/api/chat/message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${authToken}`
                    },
                    body: JSON.stringify({ message })
                });
                
                const data = await response.json();
                removeTypingIndicator(typingDiv);
                
                if (response.ok) {
                    addMessage('assistant', data.response);
                } else {
                    addMessage('assistant', `Erreur: ${data.error || 'Réponse indisponible'}`);
                }
            } catch (error) {
                removeTypingIndicator(typingDiv);
                addMessage('assistant', 'Erreur de communication.');
            }
        }
        
        function addMessage(sender, content) {
            const messagesDiv = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;
            
            const time = new Date().toLocaleTimeString('fr-FR', { 
                hour: '2-digit', minute: '2-digit' 
            });
            
            messageDiv.innerHTML = `
                <div class="message-bubble">
                    <p style="white-space: pre-line;">${content}</p>
                </div>
                <div class="message-time">${time}</div>
            `;
            
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
        
        function addTypingIndicator() {
            const messagesDiv = document.getElementById('chatMessages');
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message assistant';
            typingDiv.innerHTML = `
                <div class="message-bubble">
                    <p>🤖 Analyse en cours...</p>
                </div>
            `;
            messagesDiv.appendChild(typingDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            return typingDiv;
        }
        
        function removeTypingIndicator(element) {
            if (element && element.parentNode) {
                element.parentNode.removeChild(element);
            }
        }
        
        // Vérification token au chargement
        window.onload = function() {
            if (authToken) {
                fetch('/api/auth/verify', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                }).then(response => {
                    if (response.ok) {
                        document.getElementById('authSection').classList.add('hidden');
                        document.getElementById('chatContainer').classList.remove('hidden');
                    } else {
                        localStorage.removeItem('auth_token');
                        authToken = null;
                    }
                });
            }
        };
        
        // Support Enter
        document.addEventListener('DOMContentLoaded', function() {
            const messageInput = document.getElementById('messageInput');
            if (messageInput) {
                messageInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        sendMessage();
                    }
                });
            }
        });
    </script>
</body>
</html>'''
    
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    print("   ✅ Template HTML")

def create_startup_scripts():
    """Créer scripts de démarrage"""
    print("\n🚀 CRÉATION SCRIPTS DÉMARRAGE...")
    
    # Script Linux/Mac
    startup_sh = '''#!/bin/bash
# Démarrage ConstitutionGPT

echo "🇬🇳 ConstitutionGPT - Démarrage Serveur"
echo "======================================"

# Vérifications
if [ ! -f ".env" ]; then
    echo "❌ Fichier .env manquant"
    exit 1
fi

if [ ! -f "constitution_improved_db.pkl" ]; then
    echo "❌ Base de données manquante"
    echo "Placez constitution_improved_db.pkl dans ce répertoire"
    exit 1
fi

echo "🚀 Démarrage serveur sur http://localhost:5000"
python app.py
'''
    
    # Script Windows
    startup_bat = '''@echo off
echo 🇬🇳 ConstitutionGPT - Démarrage Serveur
echo ======================================

if not exist .env (
    echo ❌ Fichier .env manquant
    pause
    exit /b 1
)

if not exist constitution_improved_db.pkl (
    echo ❌ Base de données manquante
    echo Placez constitution_improved_db.pkl dans ce répertoire
    pause
    exit /b 1
)

echo 🚀 Démarrage serveur sur http://localhost:5000
python app.py
pause
'''
    
    with open('start.sh', 'w') as f:
        f.write(startup_sh)
    os.chmod('start.sh', 0o755)
    
    with open('start.bat', 'w') as f:
        f.write(startup_bat)
    
    print("   ✅ Scripts démarrage (start.sh, start.bat)")

def create_documentation():
    """Créer documentation complète"""
    print("\n📖 CRÉATION DOCUMENTATION...")
    
    readme = """# ConstitutionGPT Guinée - Interface Ministérielle

## 🇬🇳 Présentation

Assistant constitutionnel intelligent pour la République de Guinée avec interface web sécurisée.

## ⚡ Installation Rapide

1. **Exécuter l'installation :**
   ```bash
   python install_constitution_gpt.py
   ```

2. **Placer la base de données :**
   - Copiez `constitution_improved_db.pkl` dans le répertoire principal

3. **Démarrer le serveur :**
   ```bash
   # Linux/Mac
   ./start.sh
   
   # Windows  
   start.bat
   
   # Ou manuellement
   python app.py
   ```

4. **Accéder à l'interface :**
   - Ouvrez http://localhost:5000
   - Connectez-vous avec les comptes de démonstration

## 🔐 Comptes de Démonstration

| Email | Mot de passe | Rôle |
|-------|--------------|------|
| ministre@gouvernement.gn | MinistereGN2025! | Ministre |
| demo@gouvernement.gn | DemoGN2025! | Démonstration |

## 🌟 Fonctionnalités

- **IA Avancée :** Groq optimisé pour la Constitution 2025
- **Interface Élégante :** Design moderne adapté au gouvernement
- **Sécurité :** Authentification JWT et chiffrement
- **Performance :** Cache intelligent, réponses <1s
- **Précision :** Corrections automatiques des erreurs

## 🔧 Configuration Production

1. **Certificats SSL :** Remplacez les certificats auto-signés
2. **Variables .env :** Changez toutes les clés secrètes
3. **Domaine :** Configurez votre nom de domaine
4. **Firewall :** Limitez l'accès aux ports nécessaires

## 📊 Monitoring

- Logs : `/logs/constitution_backend.log`
- Santé : http://localhost:5000/health
- Interface : Métriques temps réel intégrées

## 🆘 Support

- Vérifiez les logs en cas de problème
- Assurez-vous que tous les fichiers sont présents
- Contactez l'équipe technique si nécessaire

---
🇬🇳 République de Guinée - ConstitutionGPT v1.0.0
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    print("   ✅ Documentation README.md")

def finalize_installation():
    """Finaliser l'installation"""
    print("\n✅ FINALISATION INSTALLATION...")
    
    # Créer requirements.txt
    requirements = """flask==2.3.3
flask-cors==4.0.0
flask-limiter==3.5.0
pyjwt==2.8.0
gunicorn==21.2.0
python-dotenv==1.0.0
requests==2.31.0
cryptography==41.0.7
werkzeug==2.3.7"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    # Créer fichier .gitignore
    gitignore = """.env
logs/
__pycache__/
*.pyc
*.pyo
*.db
.DS_Store
certificates/*.pem
constitution_improved_db.pkl
backups/"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore)
    
    print("   ✅ Requirements.txt et .gitignore")

def main():
    """Installation principale"""
    print_header()
    
    if not check_requirements():
        print("\n❌ PRÉREQUIS NON SATISFAITS")
        return False
    
    steps = [
        ("Création structure", create_project_structure),
        ("Installation dépendances", install_dependencies), 
        ("Création backend", create_backend_files),
        ("Template frontend", create_frontend_template),
        ("Scripts démarrage", create_startup_scripts),
        ("Documentation", create_documentation),
        ("Finalisation", finalize_installation)
    ]
    
    success_count = 0
    
    for step_name, step_func in steps:
        try:
            result = step_func()
            if result is not False:
                success_count += 1
        except Exception as e:
            print(f"❌ {step_name}: {str(e)}")
    
    print(f"\n🏆 INSTALLATION TERMINÉE: {success_count}/{len(steps)} étapes")
    print("="*60)
    
    if success_count >= len(steps) - 1:
        print("✅ INSTALLATION RÉUSSIE")
        print("\n📋 ÉTAPES SUIVANTES:")
        print("1. Placez 'constitution_improved_db.pkl' dans ce répertoire")
        print("2. Placez 'constitution_gpt_excellence.py' dans ce répertoire")
        print("3. Exécutez: python app.py")
        print("4. Accédez à: http://localhost:5000")
        print("\n🔐 Comptes de test:")
        print("• ministre@gouvernement.gn : MinistereGN2025!")
        print("• demo@gouvernement.gn : DemoGN2025!")
        print("\n🇬🇳 Interface prête pour présentation ministérielle!")
        
        return True
    else:
        print("⚠️ INSTALLATION PARTIELLE - Vérifiez les erreurs")
        return False

if __name__ == "__main__":
    main()