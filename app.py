











# app responsive design top sans authentification un peu de souci avec les mobiles
import os
from flask import Flask, request, jsonify
from constitution_gpt_excellence import ConstitutionGPTWorldClassExcellence

app = Flask(__name__)

# Charger la clé API depuis les variables d'environnement
groq_api_key = os.getenv("GROQ_API_KEY")

# Chatbot avec la clé API
chatbot = ConstitutionGPTWorldClassExcellence(groq_api_key)

chatbot.load_complete_database('constitution_improved_db.pkl')

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ConstitutionGPT - République de Guinée</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #1e40af;
            --primary-dark: #1e3a8a;
            --secondary-color: #f59e0b;
            --accent-color: #10b981;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --shadow-soft: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-medium: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-large: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            
            /* Variables responsive */
            --header-padding: clamp(1rem, 4vw, 2rem);
            --container-padding: clamp(1rem, 3vw, 2rem);
            --border-radius: clamp(8px, 2vw, 16px);
            --font-size-base: clamp(0.9rem, 2.5vw, 1rem);
            --font-size-large: clamp(1.1rem, 3vw, 1.3rem);
            --font-size-xl: clamp(1.8rem, 5vw, 2.5rem);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background: var(--bg-secondary);
            font-size: var(--font-size-base);
            min-height: 100vh;
            min-height: 100dvh; /* Support pour les navigateurs récents */
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }

        /* HEADER - Ultra responsive */
        .header {
            background: var(--bg-gradient);
            color: white;
            padding: var(--header-padding) 0;
            text-align: center;
            position: relative;
            overflow: hidden;
            min-height: clamp(120px, 20vh, 180px);
            display: flex;
            align-items: center;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }

        .header-content {
            position: relative;
            z-index: 1;
            max-width: min(1200px, 95vw);
            margin: 0 auto;
            padding: 0 var(--container-padding);
            width: 100%;
        }

        .header h1 {
            font-family: 'Playfair Display', serif;
            font-size: var(--font-size-xl);
            font-weight: 600;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            line-height: 1.2;
        }

        .header p {
            font-size: var(--font-size-base);
            opacity: 0.9;
            font-weight: 300;
            max-width: 600px;
            margin: 0 auto;
        }

        /* CONTAINER - Adaptive */
        .container {
            max-width: min(1000px, 95vw);
            margin: 0 auto;
            padding: var(--container-padding);
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: clamp(1rem, 3vw, 2rem);
            height: calc(100vh - clamp(120px, 20vh, 180px));
            height: calc(100dvh - clamp(120px, 20vh, 180px));
        }

        /* FEATURES - Grid ultra responsive */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
            gap: clamp(1rem, 3vw, 1.5rem);
            margin-bottom: clamp(1rem, 3vw, 2rem);
            flex-shrink: 0;
        }

        .feature-card {
            background: var(--bg-primary);
            padding: clamp(1rem, 3vw, 1.5rem);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-soft);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            min-height: clamp(120px, 15vh, 160px);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-medium);
        }

        .feature-icon {
            width: clamp(40px, 8vw, 50px);
            height: clamp(40px, 8vw, 50px);
            background: var(--primary-color);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-size: clamp(1.2rem, 3vw, 1.5rem);
        }

        .feature-title {
            font-size: var(--font-size-large);
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .feature-description {
            font-size: clamp(0.8rem, 2.2vw, 0.9rem);
            color: var(--text-secondary);
            line-height: 1.4;
        }

        /* CHAT CONTAINER - Parfaitement responsive */
        .chat-container {
            background: var(--bg-primary);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-large);
            overflow: hidden;
            flex: 1;
            display: flex;
            flex-direction: column;
            min-height: 0;
            max-height: calc(100vh - clamp(300px, 40vh, 400px));
            max-height: calc(100dvh - clamp(300px, 40vh, 400px));
        }

        .chat-header {
            background: linear-gradient(90deg, var(--primary-color), var(--primary-dark));
            color: white;
            padding: clamp(1rem, 3vw, 1.5rem);
            display: flex;
            align-items: center;
            gap: clamp(0.5rem, 2vw, 1rem);
            flex-shrink: 0;
            min-height: clamp(60px, 10vh, 80px);
        }

        .chat-header-icon {
            width: clamp(32px, 6vw, 40px);
            height: clamp(32px, 6vw, 40px);
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(1rem, 2.5vw, 1.2rem);
            flex-shrink: 0;
        }

        .chat-header h2 {
            font-size: var(--font-size-large);
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .status-indicator {
            width: clamp(6px, 1.5vw, 8px);
            height: clamp(6px, 1.5vw, 8px);
            background: var(--accent-color);
            border-radius: 50%;
            margin-left: auto;
            animation: pulse 2s infinite;
            flex-shrink: 0;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        /* MESSAGES - Responsive et lisible */
        .chat-messages {
            flex: 1;
            padding: clamp(1rem, 3vw, 2rem);
            background: linear-gradient(to bottom, #fafafa, #ffffff);
            overflow-y: auto;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            gap: clamp(1rem, 3vw, 1.5rem);
            min-height: 0;
            scroll-behavior: smooth;
        }

        .message {
            display: flex;
            align-items: flex-start;
            gap: clamp(0.5rem, 2vw, 0.75rem);
            opacity: 0;
            animation: slideInFromBottom 0.5s ease-out forwards;
            width: 100%;
        }

        @keyframes slideInFromBottom {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message-user {
            flex-direction: row-reverse;
            justify-content: flex-start;
        }

        .message-avatar {
            width: clamp(32px, 6vw, 40px);
            height: clamp(32px, 6vw, 40px);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(1rem, 2.5vw, 1.2rem);
            flex-shrink: 0;
        }

        .user-avatar {
            background: var(--primary-color);
            color: white;
        }

        .bot-avatar {
            background: var(--accent-color);
            color: white;
        }

        .message-content {
            max-width: min(75%, calc(100vw - 120px));
            padding: clamp(0.75rem, 3vw, 1rem) clamp(1rem, 3vw, 1.5rem);
            border-radius: clamp(12px, 3vw, 18px);
            font-size: var(--font-size-base);
            line-height: 1.5;
            position: relative;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        .user-content {
            background: var(--primary-color);
            color: white;
            border-bottom-right-radius: 6px;
        }

        .bot-content {
            background: #f1f5f9;
            color: var(--text-primary);
            border: 1px solid #e2e8f0;
            border-bottom-left-radius: 6px;
        }

        .message-time {
            font-size: clamp(0.7rem, 2vw, 0.75rem);
            color: rgba(255, 255, 255, 0.8);
            margin-top: 0.5rem;
        }

        .bot-content .message-time {
            color: var(--text-secondary);
        }

        /* INPUT SECTION - Ultra adaptative */
        .input-section {
            padding: clamp(1rem, 3vw, 1.5rem);
            background: var(--bg-primary);
            border-top: 1px solid #e5e7eb;
            flex-shrink: 0;
            max-width: 100%;
        }

        .input-group {
            display: flex;
            gap: clamp(0.5rem, 2vw, 1rem);
            align-items: end;
            width: 100%;
        }

        .input-wrapper {
            flex: 1;
            position: relative;
            min-width: 0;
        }

        #question {
            width: 100%;
            padding: clamp(0.75rem, 3vw, 1rem) clamp(1rem, 3vw, 1.5rem);
            border: 2px solid #e5e7eb;
            border-radius: var(--border-radius);
            font-size: var(--font-size-base);
            font-family: inherit;
            transition: all 0.3s ease;
            background: var(--bg-primary);
            resize: none;
            min-height: clamp(44px, 8vh, 50px);
            max-height: clamp(100px, 15vh, 120px);
            line-height: 1.4;
        }

        #question:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1);
        }

        .send-button {
            padding: clamp(0.5rem, 2vw, 0.75rem);
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-soft);
            width: clamp(44px, 8vh, 50px);
            height: clamp(44px, 8vh, 50px);
            flex-shrink: 0;
        }

        .send-button svg {
            width: clamp(18px, 4vw, 24px);
            height: clamp(18px, 4vw, 24px);
        }

        .send-button:hover {
            background: var(--primary-dark);
            transform: translateY(-1px) scale(1.05);
            box-shadow: var(--shadow-medium);
        }

        .send-button:active {
            transform: translateY(0) scale(0.95);
        }

        .send-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        /* LOADING - Responsive */
        .loading {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-secondary);
            font-style: italic;
            font-size: var(--font-size-base);
        }

        .loading-dots {
            display: flex;
            gap: 4px;
        }

        .loading-dot {
            width: clamp(4px, 1.5vw, 6px);
            height: clamp(4px, 1.5vw, 6px);
            background: var(--primary-color);
            border-radius: 50%;
            animation: loadingWave 1.4s ease-in-out infinite both;
        }

        .loading-dot:nth-child(2) { animation-delay: -1.32s; }
        .loading-dot:nth-child(3) { animation-delay: -1.24s; }

        @keyframes loadingWave {
            0%, 80%, 100% {
                transform: scale(0);
                opacity: 0.5;
            }
            40% {
                transform: scale(1);
                opacity: 1;
            }
        }

        /* SCROLLBAR - Responsive */
        .chat-messages::-webkit-scrollbar {
            width: clamp(4px, 1vw, 6px);
        }

        .chat-messages::-webkit-scrollbar-track {
            background: #f1f1f1;
        }

        .chat-messages::-webkit-scrollbar-thumb {
            background: var(--primary-color);
            border-radius: 3px;
        }

        .chat-messages::-webkit-scrollbar-thumb:hover {
            background: var(--primary-dark);
        }

        /* MEDIA QUERIES - Points de rupture spécifiques */
        
        /* Très petits écrans (< 360px) */
        @media (max-width: 359px) {
            .header-content {
                padding: 0 1rem;
            }
            
            .container {
                padding: 0.75rem;
            }
            
            .features {
                grid-template-columns: 1fr;
                gap: 0.75rem;
            }
            
            .message-content {
                max-width: calc(100vw - 80px);
            }
        }

        /* Petits mobiles (360px - 480px) */
        @media (min-width: 360px) and (max-width: 480px) {
            .features {
                grid-template-columns: 1fr;
            }
            
            .chat-header h2 {
                font-size: 1.1rem;
            }
        }

        /* Grands mobiles / Petites tablettes (481px - 768px) */
        @media (min-width: 481px) and (max-width: 768px) {
            .features {
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            }
            
            .container {
                gap: 1.5rem;
            }
        }

        /* Tablettes (769px - 1024px) */
        @media (min-width: 769px) and (max-width: 1024px) {
            .features {
                grid-template-columns: repeat(3, 1fr);
            }
            
            .message-content {
                max-width: 70%;
            }
        }

        /* Desktop (1025px - 1440px) */
        @media (min-width: 1025px) and (max-width: 1440px) {
            .container {
                max-width: 1000px;
            }
            
            .message-content {
                max-width: 65%;
            }
        }

        /* Très grands écrans (> 1440px) */
        @media (min-width: 1441px) {
            .container {
                max-width: 1200px;
            }
            
            .chat-container {
                max-height: 800px;
            }
            
            :root {
                --font-size-xl: 3rem;
                --font-size-large: 1.4rem;
            }
        }

        /* Orientation paysage sur mobile */
        @media (max-height: 500px) and (orientation: landscape) {
            .header {
                min-height: 80px;
                padding: 1rem 0;
            }
            
            .header h1 {
                font-size: 1.5rem;
            }
            
            .header p {
                font-size: 0.9rem;
            }
            
            .features {
                display: none; /* Cache les features en paysage mobile */
            }
            
            .container {
                height: calc(100vh - 80px);
                gap: 0.5rem;
            }
        }

        /* Support pour les écrans haute densité */
        @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
            .feature-icon, .message-avatar {
                transform: translateZ(0); /* Force l'accélération GPU */
            }
        }

        /* Préférences d'accessibilité */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        /* Mode sombre automatique */
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-primary: #1f2937;
                --bg-secondary: #111827;
                --text-primary: #f9fafb;
                --text-secondary: #d1d5db;
            }
            
            .bot-content {
                background: #374151;
                border-color: #4b5563;
                color: #f9fafb;
            }
            
            .chat-messages {
                background: linear-gradient(to bottom, #1f2937, #111827);
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <h1>ConstitutionGPT Guinee</h1>
            <p>Assistant Intelligent pour la Constitution de la République de Guinée</p>
        </div>
    </div>

    <div class="container">
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon">📜</div>
                <div class="feature-title">Constitution</div>
                <div class="feature-description">Consultez les articles et dispositions constitutionnelles</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚖️</div>
                <div class="feature-title">Droits & Devoirs</div>
                <div class="feature-description">Informations sur les droits et devoirs des citoyens</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🏛️</div>
                <div class="feature-title">Institutions</div>
                <div class="feature-description">Organisation et fonctionnement des institutions</div>
            </div>
        </div>

        <div class="chat-container">
            <div class="chat-header">
                <div class="chat-header-icon">🤖</div>
                <h2>Assistant ConstitutionGPT</h2>
                <div class="status-indicator"></div>
            </div>
            
            <div class="chat-messages" id="chatMessages">
                <div class="message message-bot">
                    <div class="message-avatar bot-avatar">🤖</div>
                    <div class="message-content bot-content">
                        <div>👋 Bonjour ! Je suis ConstitutionGPT, votre assistant spécialisé dans la Constitution de la République de Guinée.</div>
                        <div style="margin-top: 0.5rem;">💡 Je peux vous aider avec :</div>
                        <div style="margin-left: 1rem; margin-top: 0.5rem;">
                            • Les articles constitutionnels<br>
                            • Les droits et devoirs des citoyens<br>
                            • L'organisation des institutions<br>
                            • Les procédures légales
                        </div>
                        <div class="message-time" id="welcomeTime"></div>
                    </div>
                </div>
            </div>
            
            <div class="input-section">
                <div class="input-group">
                    <div class="input-wrapper">
                        <textarea 
                            id="question" 
                            placeholder="Posez votre question sur la Constitution de Guinée..."
                            rows="1"
                        ></textarea>
                    </div>
                    <button onclick="ask()" id="sendButton" class="send-button">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="m22 2-7 20-4-9-9-4Z"/>
                            <path d="M22 2 11 13"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Auto-resize textarea avec optimisation
        const textarea = document.getElementById('question');
        let resizeTimeout;
        
        textarea.addEventListener('input', function() {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                this.style.height = 'auto';
                this.style.height = (this.scrollHeight) + 'px';
            }, 10);
        });

        // Handle Enter key (Shift+Enter for new line)
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                ask();
            }
        });

        // Gestion de l'orientation et redimensionnement
        let resizeObserver;
        if (window.ResizeObserver) {
            resizeObserver = new ResizeObserver(() => {
                // Réajuste la hauteur du chat quand la fenêtre change
                const chatMessages = document.getElementById('chatMessages');
                if (chatMessages) {
                    setTimeout(() => {
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                    }, 100);
                }
            });
            resizeObserver.observe(document.body);
        }

        // Gestion de l'orientation
        window.addEventListener('orientationchange', function() {
            setTimeout(() => {
                const chatMessages = document.getElementById('chatMessages');
                if (chatMessages) {
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }
                textarea.style.height = 'auto';
            }, 300);
        });

        // Initialize welcome timestamp
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('welcomeTime').textContent = formatTime();
            
            // Focus initial sur desktop uniquement
            if (window.innerWidth > 768) {
                setTimeout(() => {
                    textarea.focus();
                }, 100);
            }
        });

        function formatTime() {
            return new Date().toLocaleTimeString('fr-FR', { 
                hour: '2-digit', 
                minute: '2-digit' 
            });
        }

        function addMessage(content, isUser = false) {
            const chatMessages = document.getElementById('chatMessages');
            
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'message-user' : 'message-bot'}`;
            
            const avatar = isUser ? '👤' : '🤖';
            const avatarClass = isUser ? 'user-avatar' : 'bot-avatar';
            const contentClass = isUser ? 'user-content' : 'bot-content';
            
            messageDiv.innerHTML = `
                <div class="message-avatar ${avatarClass}">${avatar}</div>
                <div class="message-content ${contentClass}">
                    <div>${content}</div>
                    <div class="message-time">${formatTime()}</div>
                </div>
            `;
            
            chatMessages.appendChild(messageDiv);
            
            // Scroll optimisé avec requestAnimationFrame
            requestAnimationFrame(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
        }

        function addTypingIndicator() {
            const chatMessages = document.getElementById('chatMessages');
            
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message message-bot';
            typingDiv.id = 'typingIndicator';
            
            typingDiv.innerHTML = `
                <div class="message-avatar bot-avatar">🤖</div>
                <div class="message-content bot-content">
                    <div class="loading">
                        <span>ConstitutionGPT réfléchit</span>
                        <div class="loading-dots">
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                        </div>
                    </div>
                </div>
            `;
            
            chatMessages.appendChild(typingDiv);
            
            // Scroll optimisé
            requestAnimationFrame(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
        }

        function removeTypingIndicator() {
            const typingIndicator = document.getElementById('typingIndicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
        }

        async function ask() {
            const question = document.getElementById('question').value.trim();
            const sendButton = document.getElementById('sendButton');
            
            if (!question) return;
            
            // Add user message to chat
            addMessage(question, true);
            
            // Clear input and disable button
            document.getElementById('question').value = '';
            document.getElementById('question').style.height = 'auto';
            sendButton.disabled = true;
            
            // Show typing indicator
            addTypingIndicator();
            
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                });
                
                const data = await response.json();
                
                // Remove typing indicator
                removeTypingIndicator();
                
                // Format and add bot response
                const formattedAnswer = data.answer
                    .replace(/\\n/g, '<br>')
                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                    .replace(/\*(.*?)\*/g, '<em>$1</em>');
                
                addMessage(formattedAnswer, false);
                
            } catch (error) {
                removeTypingIndicator();
                addMessage(
                    '❌ Erreur de connexion. Veuillez réessayer dans quelques instants.', 
                    false
                );
            } finally {
                sendButton.disabled = false;
                
                // Focus sur desktop uniquement
                if (window.innerWidth > 768) {
                    setTimeout(() => {
                        textarea.focus();
                    }, 100);
                }
            }
        }

        // Gestion tactile pour mobile
        let touchStartY = 0;
        let touchEndY = 0;
        
        document.addEventListener('touchstart', function(e) {
            touchStartY = e.changedTouches[0].screenY;
        }, {passive: true});

        document.addEventListener('touchend', function(e) {
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }, {passive: true});

        function handleSwipe() {
            const swipeThreshold = 50;
            const diff = touchStartY - touchEndY;
            
            // Swipe vers le haut pour masquer le clavier sur mobile
            if (Math.abs(diff) > swipeThreshold && diff > 0) {
                if (window.innerWidth <= 768 && document.activeElement === textarea) {
                    textarea.blur();
                }
            }
        }

        // Optimisation des performances
        let ticking = false;
        
        function optimizedScroll() {
            if (!ticking) {
                requestAnimationFrame(() => {
                    // Logique de scroll si nécessaire
                    ticking = false;
                });
                ticking = true;
            }
        }

        // Nettoyage des event listeners
        window.addEventListener('beforeunload', function() {
            if (resizeObserver) {
                resizeObserver.disconnect();
            }
        });

        // Détection du support des fonctionnalités modernes
        const supportsModernFeatures = {
            viewport: CSS.supports('height', '100dvh'),
            flexGap: CSS.supports('gap', '1rem'),
            grid: CSS.supports('display', 'grid')
        };

        // Fallbacks pour les anciens navigateurs
        if (!supportsModernFeatures.viewport) {
            document.body.style.minHeight = '100vh';
        }

        // Amélioration de l'accessibilité
        document.addEventListener('keydown', function(e) {
            // Navigation au clavier
            if (e.key === 'Tab') {
                document.body.classList.add('using-keyboard');
            }
        });

        document.addEventListener('mousedown', function() {
            document.body.classList.remove('using-keyboard');
        });

        // Gestion des erreurs réseau
        let retryCount = 0;
        const maxRetries = 3;

        function handleNetworkError() {
            retryCount++;
            if (retryCount < maxRetries) {
                addMessage(
                    `🔄 Tentative ${retryCount}/${maxRetries}... Reconnexion en cours.`, 
                    false
                );
                return true;
            } else {
                retryCount = 0;
                return false;
            }
        }

        // Performance monitoring (dev only)
        if (window.performance && console.time) {
            let pageLoadStart = performance.now();
            
            window.addEventListener('load', function() {
                let pageLoadEnd = performance.now();
                console.log(`Page chargée en ${Math.round(pageLoadEnd - pageLoadStart)}ms`);
            });
        }
    </script>
</body>
</html>'''

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    answer = chatbot.generate_world_class_response(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    print("Serveur ConstitutionGPT sur http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)









