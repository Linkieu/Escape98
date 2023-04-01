#!/usr/bin/env python3
# -*- coding: utf-8 -*-





entete="""<!DOCTYPE html> <!--Entête de la page HTML-->

<html lang="fr">
    <head>
        <meta charset="UTF-8" >
        <title>Escape 98 - Projet NSI</title>
        <link rel="icon" href="/static/images/autres/w98.png" />
        <link rel="stylesheet" href="static/style.css" type="text/css">
    </head> 
    <div id="contenu">
        
"""

basdepage="""	<!--Bas de la page HTML + Information sur le projet sur le côté-->
<div style="position: absolute; left: 2%; top: 0%; font-family: impact; color: #0F8BFF;">
<h1>Escape 98</h1>
<p class="centrer">Par Matthieu </p>
<p>Projet de NSI sur flask 20/05/21</p>
<br><br>
<p>Ceci est écrit avec<br>la police d'écriture<br>IMPACT.</p>
</div>
</body>
</html>
"""


#############################"""


redir="""<!DOCTYPE html> <!--C'est le début de l'entête de la page, la suite se trouve dans Escape98.py (dans def recherche()). Cela permet d'éviter de créer un entête personnalisé pour chaque recherche depuis le Menu démarré.-->
<!--redir-->
<html lang="fr">
    <head>
        <meta charset="UTF-8" >
        <title>Escape 98 - Projet NSI</title>
        <link rel="icon" href="/static/images/autres/w98.png" />
        <link rel="stylesheet" href="../../static/style.css" type="text/css">
        """    


chargerech=""" <!--S'occupe du reste de la page. Vu que pour cette page, seul la redirection change, cela permet d'éviter de créer un basdepage personnalisé, pour chaque recherche depuis le Menu démarré-->
        <!--chargerech-->        
        </head>
        <div id="contenu">
        <img class="centrer" src="/static/images/ExpW98/search.webp" width="776" alt="search">
        </div>
        """

barretache="""
<!--barretache-->
<!--Zone cliquable de la barre des tâches (permet d'éviter de réécrire à chaque fois...).-->
<map name="barre"> <!--Créer une zone cliquable-->
    <!--Barre des tâches-->
    <area shape="rect" coords="0,580,80,1000" href="/bureau/démarrer" alt="Bouton Démarrer" /> <!--Zone cliquable (ici placé sur le bouton start (remarque: je met dans "alt" ce qui correspond à la zone cliquable), se trouvant sur l'image. Redirige vers la page du Menu Démarré-->
    <area shape="rect" coords="85,580,110,1000" href="/iexplorer" alt="Internet Explorer" title="Ouvrir Internet Explorer"/>
    <area shape="rect" coords="140,580,165,1000" href="/bureau" alt="Bureau" title="Accéder au bureau"/>
    

"""


barrehaut="""
<!--barrehaut-->
<area shape="rect" coords="758,0,800,18" href="/bureau" alt="Bureau"/> <!--A mettre après "page+=barretache" et avant le "</map>"-->
"""


croix="""
    <!--croix-->
    <area shape="rect" coords="760,0,776,15" href="/bureau" alt="[X] Bureau" title="Fermer cette fenêtre"/> <!--Au lieu de copier à chaque fois cette ligne de code, pour que ça soit plus simple pour moi, je la nomme "croix".-->
    """
    
scrsaver="""
        <!--scrsaver (au départ, cette fenêtre était conçus uniquement pour la partie écran de veille. Je l'ai généralisé, par manque de temps, j'ai pas pu modifier le nom de la variable.-->
        <map name="fermerfenetre">
        <area shape="rect" coords="509,5,524,18" href="?scr=" alt="Fermer" />
        </map>


        <div style="position: absolute; left: 30%; top: 100px; ">
        <img usemap="#fermerfenetre" class="centrer" src="/static/images/autres/fenetre.webp" alt="fenêtre" width="530">
        </div>
        <div style="position: absolute; left: 48%; top: 500px; ">
        <form action ="?scr=d" method="get"><input type="hidden" name="scr" value=""><input type="submit" value="Fermer"></form>
        </div>
        
        <div style="position: absolute; left: 32%; top: 130px;">
        """
        
discordboutons="""
            <!--discordboutons-->
            <area shape="rect" coords="0,0,50,50" href="../discord?id=umphathi%20wenkululeko&convo=" alt="Conversation 1" />
            <area shape="rect" coords="60,120,216,150" href="../discord?id=umphathi%20wenkululeko&convo=1" alt="Conversation 1" />
            <area shape="rect" coords="60,160,216,185" href="../discord?id=umphathi%20wenkululeko&convo=2" alt="Conversation 2" />
        </map>
        """
        
imgquest1="""
            <!--imgquest1-->
            <!-- Vu qu'il y a 3 entré, et pour éviter de créer encore une page de chargement, les noms des entrées seront
            les mêmes que ceux de la page de connection sur Internet Explorer. On utilisera comme page de chargement (redirection)
            la page de chargement d'internet explorer. Afin d'être redirigé vers la question suivante.-->

            <!--Ligne 1-->
            <input name="mdp" type="radio" value="img1">Image1
            <input name="mdp" type="radio" value="img2">Image2
            <input name="mdp" type="radio" value="img3">Image3
            <input name="mdp" type="radio" value="img4">Image4
            <input name="mdp" type="radio" value="img7">Image7
            <input name="mdp" type="radio" value="img8">Img8
            <input name="mdp" type="radio" value="img10">Img10
            <input type="hidden" name="mdp" value="vide"> <!-- Valeur par défaut (si l'utilisateur n'a coché aucune case de cette ligne)-->
            <!--Ligne 2--><br><p>Ligne n°2</p>
            <input name="identifiant" type="radio" value="img1">Image1
            <input name="identifiant" type="radio" value="img2">Image2
            <input name="identifiant" type="radio" value="img3">Image3
            <input name="identifiant" type="radio" value="img4">Image4
            <input name="identifiant" type="radio" value="img7">Image7
            <input name="identifiant" type="radio" value="img8">Img8
            <input name="identifiant" type="radio" value="img10">Img10
            <input type="hidden" name="identifiant" value="vide"> <!-- Valeur par défaut (si l'utilisateur n'a coché aucune case de cette ligne)-->
            <!--Ligne 3--><br><p>Ligne n°3</p>
            <input name="chien" type="radio" value="img1">Image1
            <input name="chien" type="radio" value="img2">Image2
            <input name="chien" type="radio" value="img3">Image3
            <input name="chien" type="radio" value="img4">Image4
            <input name="chien" type="radio" value="img7">Image7
            <input name="chien" type="radio" value="img8">Img8
            <input name="chien" type="radio" value="img10">Img10
            <input type="hidden" name="chien" value="vide"> <!-- Valeur par défaut (si l'utilisateur n'a coché aucune case de cette ligne)-->

        """