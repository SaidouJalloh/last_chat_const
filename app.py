
# Code qui marche mais pas responssive

# import os
# from flask import Flask, request, jsonify
# from constitution_gpt_excellence import ConstitutionGPTWorldClassExcellence

# app = Flask(__name__)

# # Charger la clé API depuis les variables d'environnement
# groq_api_key = os.getenv("GROQ_API_KEY")

# # Chatbot avec la clé API
# chatbot = ConstitutionGPTWorldClassExcellence(groq_api_key)

# chatbot.load_complete_database('constitution_improved_db.pkl')

# @app.route('/')
# def home():
#     return '''<!DOCTYPE html>
# <html lang="fr">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
#     <title>ConstitutionGPT - République de Guinée</title>
#     <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">
#     <style>
#         :root {
#             --primary-color: #1e40af;
#             --primary-dark: #1e3a8a;
#             --secondary-color: #f59e0b;
#             --accent-color: #10b981;
#             --text-primary: #1f2937;
#             --text-secondary: #6b7280;
#             --bg-primary: #ffffff;
#             --bg-secondary: #f8fafc;
#             --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#             --shadow-soft: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
#             --shadow-medium: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
#             --shadow-large: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            
#             /* Variables responsive */
#             --header-padding: clamp(1rem, 4vw, 2rem);
#             --container-padding: clamp(1rem, 3vw, 2rem);
#             --border-radius: clamp(8px, 2vw, 16px);
#             --font-size-base: clamp(0.9rem, 2.5vw, 1rem);
#             --font-size-large: clamp(1.1rem, 3vw, 1.3rem);
#             --font-size-xl: clamp(1.8rem, 5vw, 2.5rem);
#         }

#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         body {
#             font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
#             line-height: 1.6;
#             color: var(--text-primary);
#             background: var(--bg-secondary);
#             font-size: var(--font-size-base);
#             min-height: 100vh;
#             min-height: 100dvh; /* Support pour les navigateurs récents */
#             display: flex;
#             flex-direction: column;
#             overflow-x: hidden;
#         }

#         /* HEADER - Ultra responsive */
#         .header {
#             background: var(--bg-gradient);
#             color: white;
#             padding: var(--header-padding) 0;
#             text-align: center;
#             position: relative;
#             overflow: hidden;
#             min-height: clamp(120px, 20vh, 180px);
#             display: flex;
#             align-items: center;
#         }

#         .header::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             bottom: 0;
#             background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
#             opacity: 0.3;
#         }

#         .header-content {
#             position: relative;
#             z-index: 1;
#             max-width: min(1200px, 95vw);
#             margin: 0 auto;
#             padding: 0 var(--container-padding);
#             width: 100%;
#         }

#         .header h1 {
#             font-family: 'Playfair Display', serif;
#             font-size: var(--font-size-xl);
#             font-weight: 600;
#             margin-bottom: 0.5rem;
#             text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#             line-height: 1.2;
#         }

#         .header p {
#             font-size: var(--font-size-base);
#             opacity: 0.9;
#             font-weight: 300;
#             max-width: 600px;
#             margin: 0 auto;
#         }

#         /* CONTAINER - Adaptive */
#         .container {
#             max-width: min(1000px, 95vw);
#             margin: 0 auto;
#             padding: var(--container-padding);
#             flex: 1;
#             display: flex;
#             flex-direction: column;
#             gap: clamp(1rem, 3vw, 2rem);
#             height: calc(100vh - clamp(120px, 20vh, 180px));
#             height: calc(100dvh - clamp(120px, 20vh, 180px));
#         }

#         /* FEATURES - Grid ultra responsive */
#         .features {
#             display: grid;
#             grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
#             gap: clamp(1rem, 3vw, 1.5rem);
#             margin-bottom: clamp(1rem, 3vw, 2rem);
#             flex-shrink: 0;
#         }

#         .feature-card {
#             background: var(--bg-primary);
#             padding: clamp(1rem, 3vw, 1.5rem);
#             border-radius: var(--border-radius);
#             box-shadow: var(--shadow-soft);
#             text-align: center;
#             transition: transform 0.3s ease, box-shadow 0.3s ease;
#             min-height: clamp(120px, 15vh, 160px);
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#         }

#         .feature-card:hover {
#             transform: translateY(-2px);
#             box-shadow: var(--shadow-medium);
#         }

#         .feature-icon {
#             width: clamp(40px, 8vw, 50px);
#             height: clamp(40px, 8vw, 50px);
#             background: var(--primary-color);
#             color: white;
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             margin: 0 auto 1rem;
#             font-size: clamp(1.2rem, 3vw, 1.5rem);
#         }

#         .feature-title {
#             font-size: var(--font-size-large);
#             font-weight: 600;
#             margin-bottom: 0.5rem;
#             color: var(--text-primary);
#         }

#         .feature-description {
#             font-size: clamp(0.8rem, 2.2vw, 0.9rem);
#             color: var(--text-secondary);
#             line-height: 1.4;
#         }

#         /* CHAT CONTAINER - Parfaitement responsive */
#         .chat-container {
#             background: var(--bg-primary);
#             border-radius: var(--border-radius);
#             box-shadow: var(--shadow-large);
#             overflow: hidden;
#             flex: 1;
#             display: flex;
#             flex-direction: column;
#             min-height: 0;
#             max-height: calc(100vh - clamp(300px, 40vh, 400px));
#             max-height: calc(100dvh - clamp(300px, 40vh, 400px));
#         }

#         .chat-header {
#             background: linear-gradient(90deg, var(--primary-color), var(--primary-dark));
#             color: white;
#             padding: clamp(1rem, 3vw, 1.5rem);
#             display: flex;
#             align-items: center;
#             gap: clamp(0.5rem, 2vw, 1rem);
#             flex-shrink: 0;
#             min-height: clamp(60px, 10vh, 80px);
#         }

#         .chat-header-icon {
#             width: clamp(32px, 6vw, 40px);
#             height: clamp(32px, 6vw, 40px);
#             background: rgba(255, 255, 255, 0.2);
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: clamp(1rem, 2.5vw, 1.2rem);
#             flex-shrink: 0;
#         }

#         .chat-header h2 {
#             font-size: var(--font-size-large);
#             font-weight: 600;
#             white-space: nowrap;
#             overflow: hidden;
#             text-overflow: ellipsis;
#         }

#         .status-indicator {
#             width: clamp(6px, 1.5vw, 8px);
#             height: clamp(6px, 1.5vw, 8px);
#             background: var(--accent-color);
#             border-radius: 50%;
#             margin-left: auto;
#             animation: pulse 2s infinite;
#             flex-shrink: 0;
#         }

#         @keyframes pulse {
#             0% { opacity: 1; }
#             50% { opacity: 0.5; }
#             100% { opacity: 1; }
#         }

#         /* MESSAGES - Responsive et lisible */
#         .chat-messages {
#             flex: 1;
#             padding: clamp(1rem, 3vw, 2rem);
#             background: linear-gradient(to bottom, #fafafa, #ffffff);
#             overflow-y: auto;
#             overflow-x: hidden;
#             display: flex;
#             flex-direction: column;
#             gap: clamp(1rem, 3vw, 1.5rem);
#             min-height: 0;
#             scroll-behavior: smooth;
#         }

#         .message {
#             display: flex;
#             align-items: flex-start;
#             gap: clamp(0.5rem, 2vw, 0.75rem);
#             opacity: 0;
#             animation: slideInFromBottom 0.5s ease-out forwards;
#             width: 100%;
#         }

#         @keyframes slideInFromBottom {
#             from {
#                 opacity: 0;
#                 transform: translateY(20px);
#             }
#             to {
#                 opacity: 1;
#                 transform: translateY(0);
#             }
#         }

#         .message-user {
#             flex-direction: row-reverse;
#             justify-content: flex-start;
#         }

#         .message-avatar {
#             width: clamp(32px, 6vw, 40px);
#             height: clamp(32px, 6vw, 40px);
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: clamp(1rem, 2.5vw, 1.2rem);
#             flex-shrink: 0;
#         }

#         .user-avatar {
#             background: var(--primary-color);
#             color: white;
#         }

#         .bot-avatar {
#             background: var(--accent-color);
#             color: white;
#         }

#         .message-content {
#             max-width: min(75%, calc(100vw - 120px));
#             padding: clamp(0.75rem, 3vw, 1rem) clamp(1rem, 3vw, 1.5rem);
#             border-radius: clamp(12px, 3vw, 18px);
#             font-size: var(--font-size-base);
#             line-height: 1.5;
#             position: relative;
#             word-wrap: break-word;
#             overflow-wrap: break-word;
#         }

#         .user-content {
#             background: var(--primary-color);
#             color: white;
#             border-bottom-right-radius: 6px;
#         }

#         .bot-content {
#             background: #f1f5f9;
#             color: var(--text-primary);
#             border: 1px solid #e2e8f0;
#             border-bottom-left-radius: 6px;
#         }

#         .message-time {
#             font-size: clamp(0.7rem, 2vw, 0.75rem);
#             color: rgba(255, 255, 255, 0.8);
#             margin-top: 0.5rem;
#         }

#         .bot-content .message-time {
#             color: var(--text-secondary);
#         }

#         /* INPUT SECTION - Ultra adaptative */
#         .input-section {
#             padding: clamp(1rem, 3vw, 1.5rem);
#             background: var(--bg-primary);
#             border-top: 1px solid #e5e7eb;
#             flex-shrink: 0;
#             max-width: 100%;
#         }

#         .input-group {
#             display: flex;
#             gap: clamp(0.5rem, 2vw, 1rem);
#             align-items: end;
#             width: 100%;
#         }

#         .input-wrapper {
#             flex: 1;
#             position: relative;
#             min-width: 0;
#         }

#         #question {
#             width: 100%;
#             padding: clamp(0.75rem, 3vw, 1rem) clamp(1rem, 3vw, 1.5rem);
#             border: 2px solid #e5e7eb;
#             border-radius: var(--border-radius);
#             font-size: var(--font-size-base);
#             font-family: inherit;
#             transition: all 0.3s ease;
#             background: var(--bg-primary);
#             resize: none;
#             min-height: clamp(44px, 8vh, 50px);
#             max-height: clamp(100px, 15vh, 120px);
#             line-height: 1.4;
#         }

#         #question:focus {
#             outline: none;
#             border-color: var(--primary-color);
#             box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1);
#         }

#         .send-button {
#             padding: clamp(0.5rem, 2vw, 0.75rem);
#             background: var(--primary-color);
#             color: white;
#             border: none;
#             border-radius: 50%;
#             cursor: pointer;
#             transition: all 0.3s ease;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             box-shadow: var(--shadow-soft);
#             width: clamp(44px, 8vh, 50px);
#             height: clamp(44px, 8vh, 50px);
#             flex-shrink: 0;
#         }

#         .send-button svg {
#             width: clamp(18px, 4vw, 24px);
#             height: clamp(18px, 4vw, 24px);
#         }

#         .send-button:hover {
#             background: var(--primary-dark);
#             transform: translateY(-1px) scale(1.05);
#             box-shadow: var(--shadow-medium);
#         }

#         .send-button:active {
#             transform: translateY(0) scale(0.95);
#         }

#         .send-button:disabled {
#             opacity: 0.5;
#             cursor: not-allowed;
#             transform: none;
#         }

#         /* LOADING - Responsive */
#         .loading {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             color: var(--text-secondary);
#             font-style: italic;
#             font-size: var(--font-size-base);
#         }

#         .loading-dots {
#             display: flex;
#             gap: 4px;
#         }

#         .loading-dot {
#             width: clamp(4px, 1.5vw, 6px);
#             height: clamp(4px, 1.5vw, 6px);
#             background: var(--primary-color);
#             border-radius: 50%;
#             animation: loadingWave 1.4s ease-in-out infinite both;
#         }

#         .loading-dot:nth-child(2) { animation-delay: -1.32s; }
#         .loading-dot:nth-child(3) { animation-delay: -1.24s; }

#         @keyframes loadingWave {
#             0%, 80%, 100% {
#                 transform: scale(0);
#                 opacity: 0.5;
#             }
#             40% {
#                 transform: scale(1);
#                 opacity: 1;
#             }
#         }

#         /* SCROLLBAR - Responsive */
#         .chat-messages::-webkit-scrollbar {
#             width: clamp(4px, 1vw, 6px);
#         }

#         .chat-messages::-webkit-scrollbar-track {
#             background: #f1f1f1;
#         }

#         .chat-messages::-webkit-scrollbar-thumb {
#             background: var(--primary-color);
#             border-radius: 3px;
#         }

#         .chat-messages::-webkit-scrollbar-thumb:hover {
#             background: var(--primary-dark);
#         }

#         /* MEDIA QUERIES - Points de rupture spécifiques */
        
#         /* Très petits écrans (< 360px) */
#         @media (max-width: 359px) {
#             .header-content {
#                 padding: 0 1rem;
#             }
            
#             .container {
#                 padding: 0.75rem;
#             }
            
#             .features {
#                 grid-template-columns: 1fr;
#                 gap: 0.75rem;
#             }
            
#             .message-content {
#                 max-width: calc(100vw - 80px);
#             }
#         }

#         /* Petits mobiles (360px - 480px) */
#         @media (min-width: 360px) and (max-width: 480px) {
#             .features {
#                 grid-template-columns: 1fr;
#             }
            
#             .chat-header h2 {
#                 font-size: 1.1rem;
#             }
#         }

#         /* Grands mobiles / Petites tablettes (481px - 768px) */
#         @media (min-width: 481px) and (max-width: 768px) {
#             .features {
#                 grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
#             }
            
#             .container {
#                 gap: 1.5rem;
#             }
#         }

#         /* Tablettes (769px - 1024px) */
#         @media (min-width: 769px) and (max-width: 1024px) {
#             .features {
#                 grid-template-columns: repeat(3, 1fr);
#             }
            
#             .message-content {
#                 max-width: 70%;
#             }
#         }

#         /* Desktop (1025px - 1440px) */
#         @media (min-width: 1025px) and (max-width: 1440px) {
#             .container {
#                 max-width: 1000px;
#             }
            
#             .message-content {
#                 max-width: 65%;
#             }
#         }

#         /* Très grands écrans (> 1440px) */
#         @media (min-width: 1441px) {
#             .container {
#                 max-width: 1200px;
#             }
            
#             .chat-container {
#                 max-height: 800px;
#             }
            
#             :root {
#                 --font-size-xl: 3rem;
#                 --font-size-large: 1.4rem;
#             }
#         }

#         /* Orientation paysage sur mobile */
#         @media (max-height: 500px) and (orientation: landscape) {
#             .header {
#                 min-height: 80px;
#                 padding: 1rem 0;
#             }
            
#             .header h1 {
#                 font-size: 1.5rem;
#             }
            
#             .header p {
#                 font-size: 0.9rem;
#             }
            
#             .features {
#                 display: none; /* Cache les features en paysage mobile */
#             }
            
#             .container {
#                 height: calc(100vh - 80px);
#                 gap: 0.5rem;
#             }
#         }

#         /* Support pour les écrans haute densité */
#         @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
#             .feature-icon, .message-avatar {
#                 transform: translateZ(0); /* Force l'accélération GPU */
#             }
#         }

#         /* Préférences d'accessibilité */
#         @media (prefers-reduced-motion: reduce) {
#             * {
#                 animation-duration: 0.01ms !important;
#                 animation-iteration-count: 1 !important;
#                 transition-duration: 0.01ms !important;
#             }
#         }

#         /* Mode sombre automatique */
#         @media (prefers-color-scheme: dark) {
#             :root {
#                 --bg-primary: #1f2937;
#                 --bg-secondary: #111827;
#                 --text-primary: #f9fafb;
#                 --text-secondary: #d1d5db;
#             }
            
#             .bot-content {
#                 background: #374151;
#                 border-color: #4b5563;
#                 color: #f9fafb;
#             }
            
#             .chat-messages {
#                 background: linear-gradient(to bottom, #1f2937, #111827);
#             }
#         }
#     </style>
# </head>
# <body>
#     <div class="header">
#         <div class="header-content">
#             <h1>ConstitutionGPT Guinee</h1>
#             <p>Assistant Intelligent pour la Constitution de la République de Guinée</p>
#         </div>
#     </div>

#     <div class="container">
#         <div class="features">
#             <div class="feature-card">
#                 <div class="feature-icon">📜</div>
#                 <div class="feature-title">Constitution</div>
#                 <div class="feature-description">Consultez les articles et dispositions constitutionnelles</div>
#             </div>
#             <div class="feature-card">
#                 <div class="feature-icon">⚖️</div>
#                 <div class="feature-title">Droits & Devoirs</div>
#                 <div class="feature-description">Informations sur les droits et devoirs des citoyens</div>
#             </div>
#             <div class="feature-card">
#                 <div class="feature-icon">🏛️</div>
#                 <div class="feature-title">Institutions</div>
#                 <div class="feature-description">Organisation et fonctionnement des institutions</div>
#             </div>
#         </div>

#         <div class="chat-container">
#             <div class="chat-header">
#                 <div class="chat-header-icon">🤖</div>
#                 <h2>Assistant ConstitutionGPT</h2>
#                 <div class="status-indicator"></div>
#             </div>
            
#             <div class="chat-messages" id="chatMessages">
#                 <div class="message message-bot">
#                     <div class="message-avatar bot-avatar">🤖</div>
#                     <div class="message-content bot-content">
#                         <div>👋 Bonjour ! Je suis ConstitutionGPT, votre assistant spécialisé dans la Constitution de la République de Guinée.</div>
#                         <div style="margin-top: 0.5rem;">💡 Je peux vous aider avec :</div>
#                         <div style="margin-left: 1rem; margin-top: 0.5rem;">
#                             • Les articles constitutionnels<br>
#                             • Les droits et devoirs des citoyens<br>
#                             • L'organisation des institutions<br>
#                             • Les procédures légales
#                         </div>
#                         <div class="message-time" id="welcomeTime"></div>
#                     </div>
#                 </div>
#             </div>
            
#             <div class="input-section">
#                 <div class="input-group">
#                     <div class="input-wrapper">
#                         <textarea 
#                             id="question" 
#                             placeholder="Posez votre question sur la Constitution de Guinée..."
#                             rows="1"
#                         ></textarea>
#                     </div>
#                     <button onclick="ask()" id="sendButton" class="send-button">
#                         <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
#                             <path d="m22 2-7 20-4-9-9-4Z"/>
#                             <path d="M22 2 11 13"/>
#                         </svg>
#                     </button>
#                 </div>
#             </div>
#         </div>
#     </div>

#     <script>
#         // Auto-resize textarea avec optimisation
#         const textarea = document.getElementById('question');
#         let resizeTimeout;
        
#         textarea.addEventListener('input', function() {
#             clearTimeout(resizeTimeout);
#             resizeTimeout = setTimeout(() => {
#                 this.style.height = 'auto';
#                 this.style.height = (this.scrollHeight) + 'px';
#             }, 10);
#         });

#         // Handle Enter key (Shift+Enter for new line)
#         textarea.addEventListener('keydown', function(e) {
#             if (e.key === 'Enter' && !e.shiftKey) {
#                 e.preventDefault();
#                 ask();
#             }
#         });

#         // Gestion de l'orientation et redimensionnement
#         let resizeObserver;
#         if (window.ResizeObserver) {
#             resizeObserver = new ResizeObserver(() => {
#                 // Réajuste la hauteur du chat quand la fenêtre change
#                 const chatMessages = document.getElementById('chatMessages');
#                 if (chatMessages) {
#                     setTimeout(() => {
#                         chatMessages.scrollTop = chatMessages.scrollHeight;
#                     }, 100);
#                 }
#             });
#             resizeObserver.observe(document.body);
#         }

#         // Gestion de l'orientation
#         window.addEventListener('orientationchange', function() {
#             setTimeout(() => {
#                 const chatMessages = document.getElementById('chatMessages');
#                 if (chatMessages) {
#                     chatMessages.scrollTop = chatMessages.scrollHeight;
#                 }
#                 textarea.style.height = 'auto';
#             }, 300);
#         });

#         // Initialize welcome timestamp
#         document.addEventListener('DOMContentLoaded', function() {
#             document.getElementById('welcomeTime').textContent = formatTime();
            
#             // Focus initial sur desktop uniquement
#             if (window.innerWidth > 768) {
#                 setTimeout(() => {
#                     textarea.focus();
#                 }, 100);
#             }
#         });

#         function formatTime() {
#             return new Date().toLocaleTimeString('fr-FR', { 
#                 hour: '2-digit', 
#                 minute: '2-digit' 
#             });
#         }

#         function addMessage(content, isUser = false) {
#             const chatMessages = document.getElementById('chatMessages');
            
#             const messageDiv = document.createElement('div');
#             messageDiv.className = `message ${isUser ? 'message-user' : 'message-bot'}`;
            
#             const avatar = isUser ? '👤' : '🤖';
#             const avatarClass = isUser ? 'user-avatar' : 'bot-avatar';
#             const contentClass = isUser ? 'user-content' : 'bot-content';
            
#             messageDiv.innerHTML = `
#                 <div class="message-avatar ${avatarClass}">${avatar}</div>
#                 <div class="message-content ${contentClass}">
#                     <div>${content}</div>
#                     <div class="message-time">${formatTime()}</div>
#                 </div>
#             `;
            
#             chatMessages.appendChild(messageDiv);
            
#             // Scroll optimisé avec requestAnimationFrame
#             requestAnimationFrame(() => {
#                 chatMessages.scrollTop = chatMessages.scrollHeight;
#             });
#         }

#         function addTypingIndicator() {
#             const chatMessages = document.getElementById('chatMessages');
            
#             const typingDiv = document.createElement('div');
#             typingDiv.className = 'message message-bot';
#             typingDiv.id = 'typingIndicator';
            
#             typingDiv.innerHTML = `
#                 <div class="message-avatar bot-avatar">🤖</div>
#                 <div class="message-content bot-content">
#                     <div class="loading">
#                         <span>ConstitutionGPT réfléchit</span>
#                         <div class="loading-dots">
#                             <div class="loading-dot"></div>
#                             <div class="loading-dot"></div>
#                             <div class="loading-dot"></div>
#                         </div>
#                     </div>
#                 </div>
#             `;
            
#             chatMessages.appendChild(typingDiv);
            
#             // Scroll optimisé
#             requestAnimationFrame(() => {
#                 chatMessages.scrollTop = chatMessages.scrollHeight;
#             });
#         }

#         function removeTypingIndicator() {
#             const typingIndicator = document.getElementById('typingIndicator');
#             if (typingIndicator) {
#                 typingIndicator.remove();
#             }
#         }

#         async function ask() {
#             const question = document.getElementById('question').value.trim();
#             const sendButton = document.getElementById('sendButton');
            
#             if (!question) return;
            
#             // Add user message to chat
#             addMessage(question, true);
            
#             // Clear input and disable button
#             document.getElementById('question').value = '';
#             document.getElementById('question').style.height = 'auto';
#             sendButton.disabled = true;
            
#             // Show typing indicator
#             addTypingIndicator();
            
#             try {
#                 const response = await fetch('/ask', {
#                     method: 'POST',
#                     headers: {'Content-Type': 'application/json'},
#                     body: JSON.stringify({question: question})
#                 });
                
#                 const data = await response.json();
                
#                 // Remove typing indicator
#                 removeTypingIndicator();
                
#                 // Format and add bot response
#                 const formattedAnswer = data.answer
#                     .replace(/\\n/g, '<br>')
#                     .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
#                     .replace(/\*(.*?)\*/g, '<em>$1</em>');
                
#                 addMessage(formattedAnswer, false);
                
#             } catch (error) {
#                 removeTypingIndicator();
#                 addMessage(
#                     '❌ Erreur de connexion. Veuillez réessayer dans quelques instants.', 
#                     false
#                 );
#             } finally {
#                 sendButton.disabled = false;
                
#                 // Focus sur desktop uniquement
#                 if (window.innerWidth > 768) {
#                     setTimeout(() => {
#                         textarea.focus();
#                     }, 100);
#                 }
#             }
#         }

#         // Gestion tactile pour mobile
#         let touchStartY = 0;
#         let touchEndY = 0;
        
#         document.addEventListener('touchstart', function(e) {
#             touchStartY = e.changedTouches[0].screenY;
#         }, {passive: true});

#         document.addEventListener('touchend', function(e) {
#             touchEndY = e.changedTouches[0].screenY;
#             handleSwipe();
#         }, {passive: true});

#         function handleSwipe() {
#             const swipeThreshold = 50;
#             const diff = touchStartY - touchEndY;
            
#             // Swipe vers le haut pour masquer le clavier sur mobile
#             if (Math.abs(diff) > swipeThreshold && diff > 0) {
#                 if (window.innerWidth <= 768 && document.activeElement === textarea) {
#                     textarea.blur();
#                 }
#             }
#         }

#         // Optimisation des performances
#         let ticking = false;
        
#         function optimizedScroll() {
#             if (!ticking) {
#                 requestAnimationFrame(() => {
#                     // Logique de scroll si nécessaire
#                     ticking = false;
#                 });
#                 ticking = true;
#             }
#         }

#         // Nettoyage des event listeners
#         window.addEventListener('beforeunload', function() {
#             if (resizeObserver) {
#                 resizeObserver.disconnect();
#             }
#         });

#         // Détection du support des fonctionnalités modernes
#         const supportsModernFeatures = {
#             viewport: CSS.supports('height', '100dvh'),
#             flexGap: CSS.supports('gap', '1rem'),
#             grid: CSS.supports('display', 'grid')
#         };

#         // Fallbacks pour les anciens navigateurs
#         if (!supportsModernFeatures.viewport) {
#             document.body.style.minHeight = '100vh';
#         }

#         // Amélioration de l'accessibilité
#         document.addEventListener('keydown', function(e) {
#             // Navigation au clavier
#             if (e.key === 'Tab') {
#                 document.body.classList.add('using-keyboard');
#             }
#         });

#         document.addEventListener('mousedown', function() {
#             document.body.classList.remove('using-keyboard');
#         });

#         // Gestion des erreurs réseau
#         let retryCount = 0;
#         const maxRetries = 3;

#         function handleNetworkError() {
#             retryCount++;
#             if (retryCount < maxRetries) {
#                 addMessage(
#                     `🔄 Tentative ${retryCount}/${maxRetries}... Reconnexion en cours.`, 
#                     false
#                 );
#                 return true;
#             } else {
#                 retryCount = 0;
#                 return false;
#             }
#         }

#         // Performance monitoring (dev only)
#         if (window.performance && console.time) {
#             let pageLoadStart = performance.now();
            
#             window.addEventListener('load', function() {
#                 let pageLoadEnd = performance.now();
#                 console.log(`Page chargée en ${Math.round(pageLoadEnd - pageLoadStart)}ms`);
#             });
#         }
#     </script>
# </body>
# </html>'''

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.get_json()
#     question = data.get('question', '')
#     answer = chatbot.generate_world_class_response(question)
#     return jsonify({'answer': answer})

# if __name__ == '__main__':
#     print("Serveur ConstitutionGPT sur http://localhost:5000")
#     app.run(host='0.0.0.0', port=5000, debug=True)















# Voici le new code responssive qui marche meme sur mobile

# code qui marche bien
import re
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConstitutionGPT - République de Guinée</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 30%, #60a5fa 60%, #93c5fd 100%);
            background-size: 400% 400%;
            animation: gradientShift 25s ease infinite;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Header */
        .header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(25px);
            border-bottom: 1px solid rgba(147, 197, 253, 0.3);
            color: white;
            padding: 2.5rem 1rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(30, 58, 138, 0.2);
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #93c5fd, #ffffff, #93c5fd);
        }

        .header-content {
            max-width: 1000px;
            margin: 0 auto;
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .flag-emblem {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
            filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
        }

        .header h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2rem, 6vw, 3rem);
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            letter-spacing: -0.02em;
        }

        .header .subtitle {
            font-size: clamp(1rem, 3vw, 1.3rem);
            font-weight: 300;
            opacity: 0.95;
            margin-bottom: 1rem;
        }

        .badge-officiel {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* Container */
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem 1rem;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        /* Info Section */
        .info-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .info-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(30, 58, 138, 0.15);
            border: 1px solid rgba(147, 197, 253, 0.4);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .info-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, transparent 0%, rgba(30, 58, 138, 0.03) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .info-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(30, 58, 138, 0.2);
        }

        .info-card:hover::before {
            opacity: 1;
        }

        .info-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 16px rgba(30, 58, 138, 0.3);
        }

        .info-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 0.5rem;
        }

        .info-description {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        /* Chat Container */
        .chat-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(25px);
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(30, 58, 138, 0.15);
            border: 1px solid rgba(147, 197, 253, 0.3);
            overflow: hidden;
            flex: 1;
            display: flex;
            flex-direction: column;
            min-height: 65vh;
        }

        .chat-header {
            background: rgba(30, 58, 138, 0.1);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(147, 197, 253, 0.3);
            color: #1e293b;
            padding: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            position: relative;
        }

        .chat-header::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(147, 197, 253, 0.3), transparent);
        }

        .chat-avatar {
            width: 48px;
            height: 48px;
            background: rgba(30, 58, 138, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            border: 1px solid rgba(147, 197, 253, 0.4);
        }

        .chat-info h2 {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .chat-status {
            font-size: 0.9rem;
            opacity: 0.9;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background: #3b82f6;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Messages */
        .chat-messages {
            flex: 1;
            padding: 2rem;
            overflow-y: auto;
            background: linear-gradient(to bottom, rgba(248, 250, 252, 0.5), rgba(255, 255, 255, 0.8));
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            min-height: 0;
        }

        .message {
            display: flex;
            gap: 1rem;
            animation: slideInMessage 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        @keyframes slideInMessage {
            from {
                opacity: 0;
                transform: translateY(20px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .message-user {
            flex-direction: row-reverse;
        }

        .message-avatar {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .user-avatar {
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
        }

        .bot-avatar {
            background: linear-gradient(135deg, #60a5fa, #93c5fd);
            color: white;
        }

        .message-content {
            max-width: 75%;
            padding: 1rem 1.25rem;
            border-radius: 1.25rem;
            line-height: 1.6;
            word-wrap: break-word;
            position: relative;
            backdrop-filter: blur(10px);
        }

        .user-content {
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            border-bottom-right-radius: 8px;
            box-shadow: 0 4px 16px rgba(30, 58, 138, 0.3);
        }

        .bot-content {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            color: #1e293b;
            border: 1px solid rgba(147, 197, 253, 0.4);
            border-bottom-left-radius: 8px;
            box-shadow: 0 4px 16px rgba(30, 58, 138, 0.1);
        }

        .message-time {
            font-size: 0.8rem;
            opacity: 0.7;
            margin-top: 0.5rem;
            font-weight: 500;
        }

        /* Input Section */
        .input-section {
            padding: 2rem;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(147, 197, 253, 0.2);
            position: relative;
        }

        .input-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 2rem;
            right: 2rem;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(147, 197, 253, 0.3), transparent);
        }

        .input-group {
            display: flex;
            gap: 1rem;
            align-items: flex-end;
            max-width: 100%;
        }

        .input-wrapper {
            flex: 1;
            position: relative;
        }

        .input-label {
            display: block;
            font-size: 0.9rem;
            font-weight: 500;
            color: #64748b;
            margin-bottom: 0.5rem;
        }

        #question {
            width: 100%;
            padding: 1rem 1.25rem;
            border: 2px solid #e2e8f0;
            border-radius: 1rem;
            font-size: 1rem;
            font-family: inherit;
            resize: none;
            min-height: 52px;
            max-height: 140px;
            line-height: 1.5;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: #ffffff;
            color: #1e293b;
        }

        #question:focus {
            outline: none;
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            transform: translateY(-1px);
        }

        #question::placeholder {
            color: #64748b;
        }

        .send-button {
            width: 52px;
            height: 52px;
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            border: none;
            border-radius: 1rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            flex-shrink: 0;
            box-shadow: 0 4px 16px rgba(30, 58, 138, 0.3);
            position: relative;
            overflow: hidden;
        }

        .send-button::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.2) 50%, transparent 70%);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }

        .send-button:hover::before {
            transform: translateX(100%);
        }

        .send-button:hover {
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 8px 25px rgba(30, 58, 138, 0.4);
        }

        .send-button:active {
            transform: translateY(0) scale(0.95);
        }

        .send-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .send-button svg {
            width: 22px;
            height: 22px;
            transition: transform 0.3s ease;
        }

        /* Loading */
        .loading {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            color: #64748b;
            font-style: italic;
            font-weight: 500;
        }

        .loading-dots {
            display: flex;
            gap: 3px;
        }

        .loading-dot {
            width: 6px;
            height: 6px;
            background: #3b82f6;
            border-radius: 50%;
            animation: loadingWave 1.4s ease-in-out infinite both;
        }

        .loading-dot:nth-child(1) { animation-delay: -0.32s; }
        .loading-dot:nth-child(2) { animation-delay: -0.16s; }
        .loading-dot:nth-child(3) { animation-delay: 0s; }

        @keyframes loadingWave {
            0%, 80%, 100% {
                transform: scale(0.8);
                opacity: 0.5;
            }
            40% {
                transform: scale(1.3);
                opacity: 1;
            }
        }

        /* Footer */
        .footer {
            background: #1e293b;
            color: white;
            text-align: center;
            padding: 1.5rem;
            font-size: 0.9rem;
            opacity: 0.9;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                padding: 1rem;
                gap: 1.5rem;
            }
            
            .header {
                padding: 2rem 1rem;
            }
            
            .info-section {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            
            .message-content {
                max-width: 85%;
                padding: 0.875rem 1rem;
            }
            
            .chat-messages {
                padding: 1.5rem;
                gap: 1.25rem;
            }
            
            .input-section {
                padding: 1.5rem;
            }
            
            .flag-emblem {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 480px) {
            .message-content {
                max-width: 90%;
                padding: 0.75rem 0.875rem;
            }
            
            .info-card {
                padding: 1.25rem;
            }
        }

        /* Scrollbar */
        .chat-messages::-webkit-scrollbar {
            width: 6px;
        }

        .chat-messages::-webkit-scrollbar-track {
            background: #f1f5f9;
            border-radius: 3px;
        }

        .chat-messages::-webkit-scrollbar-thumb {
            background: #3b82f6;
            border-radius: 3px;
        }

        .chat-messages::-webkit-scrollbar-thumb:hover {
            background: #1e3a8a;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-content">
            <span class="flag-emblem">🏛️</span>
            <h1>ConstitutionGPT</h1>
            <p class="subtitle">République de Guinée</p>
            <div class="badge-officiel">
                <span>🏛️</span>
                <span>Assistant Institutionnel Officiel</span>
            </div>
        </div>
    </header>

    <!-- Container Principal -->
    <main class="container">
        <!-- Section Informations -->
        <section class="info-section">
            <div class="info-card">
                <div class="info-icon">📜</div>
                <h3 class="info-title">Constitution Nationale</h3>
                <p class="info-description">Accès complet aux articles constitutionnels, dispositions légales et cadre juridique de la République de Guinée.</p>
            </div>
            <div class="info-card">
                <div class="info-icon">⚖️</div>
                <h3 class="info-title">Droits & Libertés</h3>
                <p class="info-description">Guide complet des droits fondamentaux, libertés publiques et devoirs civiques des citoyens guinéens.</p>
            </div>
            <div class="info-card">
                <div class="info-icon">🏛️</div>
                <h3 class="info-title">Institutions Républicaines</h3>
                <p class="info-description">Structure et fonctionnement des institutions étatiques, pouvoirs publics et mécanismes démocratiques.</p>
            </div>
        </section>

        <!-- Interface Chat -->
        <div class="chat-container">
            <div class="chat-header">
                <div class="chat-avatar">🤖</div>
                <div class="chat-info">
                    <h2>Assistant ConstitutionGPT</h2>
                    <div class="chat-status">
                        <div class="status-dot"></div>
                        <span>Service actif - République de Guinée</span>
                    </div>
                </div>
            </div>
            
            <div class="chat-messages" id="chatMessages">
                <div class="message message-bot">
                    <div class="message-avatar bot-avatar">🤖</div>
                    <div class="message-content bot-content">
                        <div><strong>Bonjour !</strong></div>
                        <div style="margin-top: 0.75rem;">Je suis ConstitutionGPT, l'assistant spécialisé dans la Constitution de la République de Guinée. Je suis à votre disposition pour vous fournir des informations précises et détaillées sur :</div>
                        <div style="margin: 0.75rem 0; padding-left: 1rem; border-left: 3px solid #1e3a8a;">
                            • <strong>Articles constitutionnels</strong> et dispositions légales<br>
                            • <strong>Droits fondamentaux</strong> et libertés publiques<br>
                            • <strong>Organisation institutionnelle</strong> et pouvoirs publics<br>
                            • <strong>Procédures administratives</strong> et cadre juridique
                        </div>
                        <div>Comment puis-je vous assister aujourd'hui ?</div>
                        <div class="message-time" id="welcomeTime"></div>
                    </div>
                </div>
            </div>
            
            <div class="input-section">
                <div class="input-group">
                    <div class="input-wrapper">
                        <label for="question" class="input-label">Votre question constitutionnelle</label>
                        <textarea 
                            id="question" 
                            placeholder="Posez votre question sur la Constitution, les institutions ou le droit guinéen..."
                            rows="1"
                        ></textarea>
                    </div>
                    <button onclick="ask()" id="sendButton" class="send-button" title="Envoyer la question">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                            <path d="m22 2-7 20-4-9-9-4Z"/>
                            <path d="M22 2 11 13"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        © 2024 République de Guinée - ConstitutionGPT | Service Institutionnel Officiel 🏛️
    </footer>

    <script>
        const textarea = document.getElementById('question');
        const sendButton = document.getElementById('sendButton');
        const chatMessages = document.getElementById('chatMessages');

        // Auto-resize textarea
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 140) + 'px';
        });

        // Handle Enter key
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                ask();
            }
        });

        // Set welcome time
        document.getElementById('welcomeTime').textContent = new Date().toLocaleTimeString('fr-FR', { 
            hour: '2-digit', 
            minute: '2-digit',
            day: '2-digit',
            month: 'long',
            year: 'numeric'
        });

        function formatTime() {
            return new Date().toLocaleTimeString('fr-FR', { 
                hour: '2-digit', 
                minute: '2-digit' 
            });
        }

        function addMessage(content, isUser = false) {
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
            
            setTimeout(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 100);
        }

        function addTypingIndicator() {
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message message-bot';
            typingDiv.id = 'typingIndicator';
            
            typingDiv.innerHTML = `
                <div class="message-avatar bot-avatar">🤖</div>
                <div class="message-content bot-content">
                    <div class="loading">
                        <span>Analyse constitutionnelle en cours</span>
                        <div class="loading-dots">
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                        </div>
                    </div>
                </div>
            `;
            
            chatMessages.appendChild(typingDiv);
            
            setTimeout(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 100);
        }

        function removeTypingIndicator() {
            const typingIndicator = document.getElementById('typingIndicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
        }

        async function ask() {
            const question = textarea.value.trim();
            if (!question) return;
            
            addMessage(question, true);
            
            textarea.value = '';
            textarea.style.height = 'auto';
            sendButton.disabled = true;
            
            addTypingIndicator();
            
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                });
                
                if (!response.ok) {
                    throw new Error(`Erreur ${response.status}: ${response.statusText}`);
                }
                
                const data = await response.json();
                
                removeTypingIndicator();
                
                const formattedAnswer = data.answer
                    .replace(/\\n/g, '<br>')
                    .re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text))
                    .replace(/\*(.*?)\*/g, '<em>$1</em>');
                
                addMessage(formattedAnswer, false);
                
            } catch (error) {
                removeTypingIndicator();
                addMessage(`❌ <strong>Erreur de service</strong><br>Une difficulté technique est survenue. Veuillez réessayer dans quelques instants.<br><em>Détail : ${error.message}</em>`, false);
            } finally {
                sendButton.disabled = false;
                
                if (window.innerWidth > 768) {
                    setTimeout(() => textarea.focus(), 200);
                }
            }
        }

        setTimeout(() => {
            textarea.focus();
        }, 500);
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
    print("Mobile: http://192.168.1.3:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)









