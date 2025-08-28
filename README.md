# ConstitutionGPT Guinée - Interface Ministérielle

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
