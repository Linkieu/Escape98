#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
import datetime
from pageshtml import entete, basdepage, chargerech, redir, barretache, croix, scrsaver, barrehaut, discordboutons, imgquest1
from textes import quizz3txt, quizz2txt, quizz1txt, scrsecrettxt, scrbinaire4txt, scrbinaire1txt,scrbinaire2txt, scrsolutiontxt, bienvenuetxt, indextxt

##################################### Permet d'affiché l'heure sur la page. Pour éviter d'écrire à chaque fois page+=heure suivis de page+=basdepage, je s'implifie tout, en une seul ligne: page+=bdpethoraire (basdepageethoraire).

def bdpethoraire():
    
    """
    Prend aucune variable en entrée.
    Renvoi la variable 'heure'
    
    A partir de l'heure de l'ordinateur, il vérifie si c'est au format hh:mm ('12:24', '01,00'...).
    Sinon, il rajoute un ou plusieurs 0 (pour qu'au lieu d'affiché '1:5', il affiche plutôt '01:05')
    
    Puis rassemble les valeurs pour formé l'encart d'heure au format 'hh:mm' (heyres + ':' + minutes).
    """
    
    date = datetime.datetime.now() #Récupère l'heure et la date
    h = str(date.hour) # On récupère les heures, qu'on convertir en chaîne.
    m = str(date.minute) #idem minutes
    
    if len(m)==1: #Pour affiché correctement l'heure au format "hh:mm", il faut qu'il y ai obligatoire 2 caractères pour les minutes (ainsi que les heures). S'il est 13h03, si il n'y avait pas cette partie du code, il affichera "13:3", alors qu'on veut "13:03". C'est seulement estétique.
        m=str(0)+m
    if len(h)==1: #Même explication que pour les minutes.
        h=str(0)+h

    test1="""<div style="position: absolute; left: 1000px; top: 583px; ">""" #Morceau du code HTML 1 - Position de l'heure sur l'écran
    test2="<p>"+h+":"+m+"</p>" #Morceau du code HTML 2 - Affiche l'heure et les minutes sous le format hh:mm
    test3="""</div>""" #Morceau du code HTML 3 - Fin de la mise en place de l'heure
    heure=test1+test2+test3+basdepage #Fusion des morceaux de code HTML et fusion avec le basdepage.
    return heure


#####################################

app = flask.Flask(__name__) # Création de l'application

@app.route('/') # Accueil
def index():   
    page=entete
    page+="""

    
    <form action ="/bienvenue" method="get">\n <!--Créer un bouton "Accéder à Escape98" + Affiche une image de fond + Affiche du texte-->
        <img class="centrer" src="/static/images/autres/écran_accueil.webp" width="776" alt="MacroEspion 2000"> <!--Affiche l'image-->
    """
    page+=indextxt
    page+="""
            <div style="position: absolute; left: 50%; top: 76%;">
            <input type="submit" value="Accéder à ESCAPE 98">\n <!--Bonton-->
            </div>
    </form></div>
    """
    page+=basdepage
    return page






@app.route("/bienvenue") #Affiche le bureau Windows avec rien dessus
def bienvenue():
    page=entete
    page+="""
    <map name="bureau_w98"> <!--Créer une zone cliquable-->
        <area shape="rect" coords="0,580,80,1000" href="/bureau/démarrer/recherche?search=kjhsSDJN44254!?;;HDJhdshç_rsqj²lkds" alt="Bouton Démarrer" /> <!--Ici, la zone sera sur "start" sur l'image, et redirigera vers la page recherche pour redirigé vers le bureau.-->
        <area shape="default" />
        </map>
        <img usemap="#bureau_w98" class="centrer" src="/static/images/autres/bienvenue.webp" width="776" alt="bienvenue"> <!--Affiche l'image et la met en lien avec la zone cliquable créer-->
        </div>
    """
    page+=bienvenuetxt #Récupère le texte dans textes.py
    page+=bdpethoraire() #Affiche l'heure et le bas de page
    return page








@app.route("/bureau") #Affiche le bureau Windows avec rien dessus //// REMARQUE: Vu que les pages suivantes se fonde sur cette page, je ne décrirais pas ce que je décris ici.
def bureau():
    page=entete
    page+=barretache #Place les zones cliquables sur la barre de tâche
    page+="""
        <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Conseil:\nN'hésitez pas à explorer un maximum de pages.\n\nRemarque:\nDes icônes sont intéractives (comme pour fermer une page...)"/>
    
        <!--Bureau-->
        <area shape="rect" coords="10,10,100,70" href="/iexplorer" alt="Internet Explorer" title="Passez à la vitesse supérieur !" /> <!--Zone cliquable sur l'icone IE du bureau-->
        <area shape="rect" coords="120,10,210,70" href="/explorateur?scr=" alt="Poste de travail" title="Affichez les fichiers et dossiers présents sur l'ordinateur."> <!--Zone cliquable sur l'icone Poste de Travail sur le bureau-->
        <area shape="default" />
        </map> <!--Fin de la définition de la zone cliquable-->
        <img usemap="#barre" class="centrer" src="/static/images/ExpW98/bureau_windows.webp" width="776" alt="bureau windows"> <!--Place l'image et la rattache à la zone cliquable "barre"-->
    </div>
    """
    page+=bdpethoraire() #Place l'heure et le basdepage
    return page








@app.route("/bureau/démarrer") #Affiche le Menu Démarré avec le bureau windows
def démarrer():
    page=entete
    page+="""
    <link rel="stylesheet" href="../static/style.css" type="text/css"> <!--Il n'arrive pas à lire cette ligne dans pageshtml.py, il ne cherche pas dans le bon répertoire. Donc je suis obligé de le réécrire ici, en indiquant le vrai répertoire, pour qu'il puisse charger le code css.-->
    <map name="démarrer_w98"> <!--Créer la partie "recherche" du Menu Démarré-->
        <area shape="rect" coords="0,580,80,1000" href="javascript:history.go(-1)" alt="Bouton Démarrer" /> <!--Cette page est accessible sur la majorité des pages du site. Comme sur Windows, quand on ouvre le Menu Démarré, on est censé rester sur la fenêtre ouverte. Si j'avais mis une redirection vers le bureau, ouvrir le menu démarré aurais fait fermer la fenêtre (la page). Et il aurait fallu aller la réouvrir sois même. La partie javascript permet de quand on referme le menu, il réaffiche la page précédente, où la fenêtre était ouverte. (le menu démarré ne se superpose pas à la page précédente)-->
        <area shape="rect" coords="28,295,253,330" href="../../discord?id=&convo=" alt="discord" /> <!--Cette zone, comme ceux en dessous, correspond aux boutons sur le menu démarré.-->
        <area shape="rect" coords="28,335,253,370" href="../../iexplorer/connexion" alt="favoris" />
        <area shape="rect" coords="28,375,253,409" href="../../explorateur/Escape98?scr=" alt="docs" />
        <area shape="rect" coords="28,413,253,448" href="../../explorateur/images?scr=" alt="images" />
        <area shape="rect" coords="28,452,253,487" href="../../explorateur?scr=musique" alt="musique" />
        <area shape="rect" coords="28,495,253,530" href="../../bienvenue" alt="help" />
        <area shape="rect" coords="28,538,253,577" href="../../" alt="shut_down" />
        <!--Barre des tâches-->
        <area shape="rect" coords="85,580,110,1000" href="/iexplorer" alt="Internet Explorer" />
        <area shape="rect" coords="140,580,165,1000" href="/bureau" alt="Bureau" />
        <area shape="default" />
        </map>
    

    <form action ="/bureau/démarrer/recherche" method="get">\n 
        <img usemap="#démarrer_w98" class="centrer" src="/static/images/ExpW98/menu_demarrer.webp" width="776" alt="bureau windows"> <!--Affiche l'image comportant le menu démarré. Le tout racordés aux zones cliquables à l'aide de "usemap".-->
        <div style="position: absolute; left: 27%; top: 270px;"> 
            <input type="text" name="search" size="12">\n <!--"Search" est ce qui va comporté la recherche de l'utilisateur-->
            <input type="submit" value=">">\n <!--Renvoi le formulaire-->
        </div>
    </form>
    </div>
    """
    page+=bdpethoraire()
    return page












@app.route("/bureau/démarrer/recherche", methods = ['GET']) #Ecran de chargement et de redirection vers une autre page.
   
def recherche():
    
    w98search = flask.request.args
    search = w98search['search']
    
    page=redir

    if search=="internet explorer" or search=="iexplorer" or search=="internet": #Si on recherche "internet explorer" (ou ce qui suit) dans le menu démarré
        page+='<meta http-equiv="refresh" content="1; URL=../../iexplorer">' #Redirige vers la page "iexplorer"
        
    elif search=="kjhsSDJN44254!?;;HDJhdshç_rsqj²lkds": #En effet, la recherche est étrange... Mais cela permet d'éviter que l'utilisateur tombe par hasard sur cette page. Vu que cette requête est utilisé par le site pour son fonctionnement.
        page+='<meta http-equiv="refresh" content="0.3; URL=../../bureau">'
        
    elif search=="poste de travail" or search=="explorateur" or search=="explorer.exe": #En effet, la recherche est étrange... Mais cela permet d'éviter que l'utilisateur tombe par hasard sur cette page. Vu que cette requête est utilisé par le site pour son fonctionnement.
        page+='<meta http-equiv="refresh" content="0.3; URL=../../explorateur?scr=">'
       
    elif search=='quizz98russe':
        page+='<meta http-equiv="refresh" content="0.1; URL=../../quizz98?figure=trgsd">'
        
    elif search=='discord':
        page+='<meta http-equiv="refresh" content="0.1; URL=../../discord?id=&convo=">'
        
    elif search=='IMGQUEST' or search=='imgquest':
        page+='<meta http-equiv="refresh" content="0.1; URL=../../quizz98?figure=imgquest">'
        
    
    else: #Si le site ne trouve pas ce qui a été demandé, redirige vers la page d'erreur.
        page+='<meta http-equiv="refresh" content="1; URL=recherche/erreur">'
        
    page+=chargerech
    page+=bdpethoraire()
    return page











@app.route("/bureau/démarrer/recherche/erreur", methods = ['GET']) #Affiche l'erreur. Il n'a pas trouvé ce qui a été recherché.
   
def recherche_erreur():
    page=entete
    page+="""
        <link rel="stylesheet" href="../../../static/style.css" type="text/css">
        <map name="barre"> <!--Créer une zone cliquable-->
            <!--Bouton-->
            <area shape="rect" coords="375,300,460,320" href="javascript:history.go(-2)" alt="Retour" /> <!--Vu que la recherche n'a mené à rien, autant que l'utilisateur retourne à l'endroit où il était. Pour peut-être, réessayer.-->
            <!--Barre des tâches-->
            <area shape="rect" coords="0,580,80,1000" href="javascript:history.go(-2)" alt="Bouton Démarrer" /> <!--Vu que la recherche n'a mené à rien, autant que l'utilisateur retourne à l'endroit où il était. Pour peut-être, réessayer.-->
            <area shape="rect" coords="85,580,110,1000" href="/iexplorer" alt="Internet Explorer" />
            <area shape="rect" coords="140,580,165,1000" href="/bureau" alt="Bureau" />
            <area shape="default" />
        </map>
        <img usemap="#barre" class="centrer" src="/static/images/Erreur/erreur_recherche.webp" width="776" alt="erreur_recherche"></div>
    """
    page+=bdpethoraire()
    return page












@app.route("/iexplorer", methods = ['GET']) 
   
def iexplorer(): #Page d'information d'internet explorer.
    page=entete
    page+=barretache
    page+="""
    <area shape="rect" coords="500,430,570,455" href="/iexplorer/connexion/chargement?identifiant=SDJ35&mdp=(èyhjuihud&chien=chat" alt="Ok"/>
    <area shape="rect" coords="572,128,585,140" href="/iexplorer/connexion/chargement?identifiant=SDJ35&mdp=(èyhjuihud&chien=chat" alt="X"/>
    </map>
    <img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/iexplorer_info.webp" width="776" alt="info ie"></div>
    """
    page+=bdpethoraire()
    
    return page












@app.route("/explorateur", methods = ['GET']) 
   
def explorateur(): #Explorateur de fichier Escape

    w98 = flask.request.args
    action = w98['scr']

    page=entete
    page+=barretache+barrehaut
    page+="""
    <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Conseil:\nN'hésitez pas à cliquer sur les icônes.\nVous pouvez aussi refermer les pages."/>
    </map>
    <img usemap="#barre" class="centrer" src="/static/images/explorateur/explorateur.webp" width="776" alt="Poste de travail">
    
    
    
        <!-- Icônes et nom-->
        <div style="position: absolute; left: 40%; top: 100px; display:flex; font-family: windowsfont;">
        
        <a href="/explorateur/Escape98?scr="><img class="centrer" src="/static/images/icons/controlpanel.png" alt="Escape"></a>
        <div style="position:absolute; top:35px; left:0px;"><p>Escape &nbsp; &nbsp; Images &nbsp; Musiques</p></div>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p> 
        <a href="/explorateur/images?scr="><img class="centrer" src="/static/images/icons/docmedias.png" alt="Images"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur?scr=musique"><img class="centrer" src="/static/images/icons/musique.png" alt="Musique"></a>
        
        
        </div>
        
        <!--Titre de la fenêtre-->
        <div style="position: absolute; left: 23%; top: 2px; font-family: windowsfont; font-size: 11px; color:white;">
        <p>Poste de travail</p>
        </div>
        
        <!--Répertoire-->
        <div style="position: absolute; left: 27%; top: 40px; font-family: windowsfont; font-size: 14px;">
        <p>explorateur/</p>
        </div>
        
        <!--Nom de l'onglet-->
        <div style="position: absolute; left: 24%; top: 120px; font-family: arialbl; font-size: 35px;">
        <p>Poste de<br>travail</p>
        </div></div>
    
    
    """
    
    if action=='musique':
        page+=scrsaver
        
        page+="""Musique à écouter (édition .midi, pour votre plus grand plaisir):<br><br><audio controls preload="auto" src="static/musique/envolemoi.mp3"></audio></div></div>"""
    
    page+=bdpethoraire()
    
    return page











@app.route("/explorateur/images", methods = ['GET']) 
   
def images(): #Onglet image de l'explorateur de fichier

    w98im = flask.request.args
    image = w98im['scr']

    page=entete
    page+=barretache+barrehaut
    page+="""
    <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Vous pouvez ouvrir les images en\ncliquant sur les icones.\n\nBizarre ces intrus, non ?"/>
        </map>
        <link rel="stylesheet" href="../../../static/style.css" type="text/css">
        <img usemap="#barre" class="centrer" src="/static/images/explorateur/explorateur.webp" width="776" alt="Poste de travail">
    
    
    
        <!-- Icônes et nom-->
        <div style="position: absolute; left: 40%; top: 100px; display:flex; font-family: windowsfont;">
        
        <a href="/explorateur/images?scr=img1"><img class="centrer" src="/static/images/icons/images.png" alt="img1" width="45"></a>
        <div style="position:absolute; top:35px; left:0px; font-size:15px;"><p>image n1 &nbsp; &nbsp; image n2 &nbsp; &nbsp; image n3 &nbsp; &nbsp; image n°4 &nbsp; &nbsp; image n°5 &nbsp; &nbsp; image n6 &nbsp; image n7</p></div>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>  <!--Ce n'est pas très beau, mais pour éviter de devoir mettre plusieurs "div" pour bien espacés les icînes, j'ai préféré mettre des espaces en html.-->
        <a href="/explorateur/images?scr=img2"><img class="centrer" src="/static/images/icons/images.png" alt="img2" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img3"><img class="centrer" src="/static/images/icons/images.png" alt="img3" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img4"><img class="centrer" src="/static/images/icons/images.png" alt="img4" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img5"><img class="centrer" src="/static/images/icons/images.png" alt="img5" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img6"><img class="centrer" src="/static/images/icons/images.png" alt="img6" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img7"><img class="centrer" src="/static/images/icons/images.png" alt="img7" width="45"></a>
        
        </div>
        <div style="position: absolute; left: 40%; top: 200px; display:flex; font-family: windowsfont;">
        <div style="position:absolute; top:35px; left:0px; font-size:15px;"><p>image n8 &nbsp; &nbsp; image 9 &nbsp; &nbsp; image 10</p></div>
        
        <a href="/explorateur/images?scr=img8"><img class="centrer" src="/static/images/icons/images.png" alt="img8" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img9"><img class="centrer" src="/static/images/icons/images.png" alt="img9" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/images?scr=img10"><img class="centrer" src="/static/images/icons/images.png" alt="img10" width="45"></a>
        
        
        
        </div>
        
        <!--Titre de la fenêtre-->
        <div style="position: absolute; left: 23%; top: 2px; font-family: windowsfont; font-size: 11px; color:white;">
        <p>Mes Images</p>
        </div>
        
        <!--Répertoire-->
        <div style="position: absolute; left: 27%; top: 40px; font-family: windowsfont; font-size: 14px;">
        <p>explorateur/images</p>
        </div>
        
        <!--Nom de l'onglet-->
        <div style="position: absolute; left: 24%; top: 120px; font-family: arialbl; font-size: 35px;">
        <p>Mes<br>Images</p>
        </div></div>
    
    
    """
    if image!="":
        page+=scrsaver
    
    if image=="img1": #Affiche l'image 1 dans un pop up
        page+='<img class="centrer" src="/static/images/chiens/ch1.webp" alt="image" width="480"></div>'
    elif image=="img2":
        page+='<img class="centrer" src="/static/images/chiens/ch2.webp" alt="image" width="480"></div>'
    elif image=="img3":
        page+='<img class="centrer" src="/static/images/chiens/pot.webp" alt="image" width="480"></div>'
    elif image=="img4":
        page+='<img class="centrer" src="/static/images/chiens/ch3.webp" alt="image" width="480"></div>'
    elif image=="img5":
        page+='<img class="centrer" src="/static/images/chiens/chat.webp" alt="image" width="480"></div>'
    elif image=="img6":
        page+='<img class="centrer" src="/static/images/chiens/ch4.webp" alt="image" width="480"></div>'
    elif image=="img7":
        page+='<img class="centrer" src="/static/images/chiens/ch5.webp" alt="image" width="480"></div>'
    elif image=="img8":
        page+='<img class="centrer" src="/static/images/chiens/ch6.webp" alt="image" width="480"></div>'
    elif image=="img9":
        page+='<img class="centrer" src="/static/images/chiens/telecommande.webp" alt="image" width="480"></div>'
    elif image=="img10":
        page+='<img class="centrer" src="/static/images/chiens/ch7.webp" alt="image" width="480"></div>'
    elif image=="img83":
        page+="""
        <a href="../../discord?id=umphathi+wenkululeko&convo=222"><img class="centrer" src="/static/images/chiens/ch2.webp" alt="image" width="480"></a></div>
        
        <div style="position: absolute; top: 350px; left: 35.5%; font-family: impact; font-size:20px; color: yellow;">
            <p>j</p>
        </div>

        
        """
    page+=bdpethoraire()
    
    return page

















@app.route("/quizz98", methods = ['GET']) 
   
def quizz(): #Partie du site web qui s'occupe des divers quizz

    w98 = flask.request.args

    fig = w98['figure']

    page=entete
    page+=barretache
    
    if fig=='1100010':
        page+='<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Indice:\n\nDes legos, des LETTRES, un globe..."/>'
    elif fig=='opengl':
        page+="""<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="En effet, Google Traduction est conseillé"/>"""
    elif fig=='imgquest':
        page+="""<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Indice:\n\nParmis les images, il y a des intrus.\nSélectionner les,\nen prennant compte du chiffre marqué deçus,\nil faut qu'ils restent en ligne !"/>"""
    elif fig=='imgquestion1':
        page+="""<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Je te donne, donne, donne ce que je suis\n\n... Chanteur très connu"/>"""
    elif fig=='goldman':
        page+="""<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="N'oubliez pas les paroles édition Escape Games\n\nEn cas de soucis avec l'entré de texte,\nn'hésiter pas à vous aider des réponses\ndans le fichier solution."/>"""
    elif fig=="""entre l'ignorance et la violence et l'ennui""":
        page+="""<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Tout est écrit"/>"""
    else:
        page+='<area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Conseil:\n\nRevoir le cours."/>'
    page+="""
    </map>
    <img usemap="#barre" class="centrer" src="/static/images/ExpW98/bureau_gris.webp" width="776" alt="Bureau grisé">
    """
    page+="""
        <map name="fermerfenetre"> <!--Permet de fermer la fenêtre-->
        <area shape="rect" coords="509,5,524,18" href="../bureau" alt="Fermer" /> 
        </map>


        <div style="position: absolute; left: 30%; top: 100px; ;">
        <img usemap="#fermerfenetre" class="centrer" src="/static/images/autres/fenetre.webp" alt="fenêtre" width="530">
        </div>
        <div style="position: absolute; left: 32%; top: 130px; font-family: windowsfont;"> <!--font family permet de choisir une police personnalisé depuis le fichier css-->
    """
    
    if fig=='trgsd':
        page+=quizz1txt
    elif fig=='4':
        page+=quizz2txt
    elif fig=='1100010':
        page+=quizz3txt
    elif fig=='opengl':
        page+="""
        <p>Молодец!<br>
            Вы прошли наши 3 вопроса.<br>
            <br><br>
            Вот подсказка для поиска идентификатора учетной записи<br>администратора:<br>
            « Administrateur des libertés » en Zoulou (tout en minuscule le résultat !).
            <br><br>
            Google Translate - ваш друг.
        </p>
        
        <form action ="../bureau" method="get">
            <input type="submit" value="Quitter">
        </form>
        """
        
    ####PARTI IMGQUEST
    
    elif fig=='imgquest':
        page+="""
        <h3>IMGQUEST - Programme russe, traduit par Agent 9KD2A</h3><hr>
        <p>Des lignes peuvent être vides. Vous ne pouvez pas désélectionner les images.</p><br>
        <p>Ligne n°1
        
        <form action ="/iexplorer/connexion/chargement" method="get"><p>
        """+imgquest1+"""
            <br><input type="submit" value=">">\n
        </form>
        """
        
    elif fig=='imgquestion1':
        page+="""<p>Ecrivez le chanteur de la musique se trouvant dans l'Explorateur Escape 98:</p>
        <p>(la réponse doit être en minuscule, seulement le nom est accepté)</p>
        <br><br><br>
        
        <form action ="/quizz98" method="get">\n 
            <input type="text" name="figure" size="12">\n
            <input type="submit" value="Valider ->">\n
        </form>
        """
        
    elif fig=='goldman':
        page+="""
        <p>Ecriver la phrase manquante. En minuscule... Attention aux espaces !</p>
        
        <pre>
        Minuit se lève en haut des tours
        Les voix se taisent et tout devient aveugle et sourd
        La nuit camoufle pour quelques heures
        La zone sale et les épaves et la laideur
        
        J'ai pas choisi de naître ici
        </pre>
        
        <div style=" position: absolute; left: 13%; top:145px; ">
        <form action ="/quizz98" method="get">\n 
            <input type="text" name="figure" size="30">\n<br> <!--Entrée pour du texte-->
            <br>
            <input type="submit" value="Valider ->">\n
        </form>
        </div>
        
        <div style="position: absolute; top: -30px; left: 40%; font-family: impact; font-size:200px;">
            <p>n</p>
        </div>
        """

    elif fig=="""entre l'ignorance et la violence et l'ennui""":
        page+="""
        <p>Poste de travail > Images > explorateur/images?scr=img[nombre]</p>
        <p>Remplacer "[nombre]" par le nombre formé par les cases que<br>
        vous avez cochés précédemment</p>
        """
        
    elif fig!='':
        page+='<p>Votre réponse est fausse,<br>recommencer en cherchant "quizz98russe" dans le menu démarré.</p></div>'
        
    else:
        page+='<p>Le logiciel a rencontré un problème, veuillez recommencer.</p></div>'
        
    page+='</div></div>'
    page+=bdpethoraire()
    
    return page











@app.route("/explorateur/Escape98", methods = ['GET']) 
   
def explorateurescape98(): #"Fichiers système" Comportant les écrans de veille, et les fichiers binaire.

    w98scr = flask.request.args
    scr = w98scr['scr']

    page=entete
    page+=barretache+barrehaut
    page+="""
        <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Conseil:\nL'origine, c'est que des 0 et des 1.\n\nUn traducteur en ligne peut être utile."/>
        </map>
        <link rel="stylesheet" href="../../../static/style.css" type="text/css">
        <img usemap="#barre" class="centrer" src="/static/images/explorateur/explorateur.webp" width="776" alt="Poste de travail">
    
    
    
        <!-- Icônes et nom-->
        <div style="position: absolute; left: 40%; top: 100px; display:flex; font-family: windowsfont;">
        
        <a href="/explorateur/Escape98?scr=3dmaze"><img class="centrer" src="/static/images/icons/scr.png" alt="Labyrinthe 3D" width="45"></a>
        <div style="position:absolute; top:35px; left:0px; font-size:15px;">
        <p>3Dmaze &nbsp; &nbsp; flowerbox &nbsp;&nbsp; windows &nbsp; &nbsp; &nbsp; &nbsp; binaire1 &nbsp; &nbsp; binaire2 &nbsp;&nbsp;&nbsp;&nbsp; solution &nbsp; &nbsp;&nbsp; binaire4</p>
        </div>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p> 
        <a href="/explorateur/Escape98?scr=flowerbox"><img class="centrer" src="/static/images/icons/scr.png" alt="flowerbox" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p> <!--Ce n'est pas très beau, mais pour déplacé les icones, sans êtres obligé de faire plusieurs "div", j'ai préféré mettre des espaces en html pour espacé les icônes.-->
        <a href="/explorateur/Escape98?scr=windows"><img class="centrer" src="/static/images/icons/scr.png" alt="windows" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/Escape98?scr=binaire1"><img class="centrer" src="/static/images/icons/binaire.png" alt="binaire2" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/Escape98?scr=binaire2"><img class="centrer" src="/static/images/icons/binaire.png" alt="binaire3" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/Escape98?scr=solution"><img class="centrer" src="/static/images/icons/binaire.png" alt="solution" width="45"></a>
        
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <a href="/explorateur/Escape98?scr=binaire4"><img class="centrer" src="/static/images/icons/binaire.png" alt="binaire4" width="45"></a>
        
        
        </div>
        
        <!--Titre de la fenêtre-->
        <div style="position: absolute; left: 23%; top: 2px; font-family: windowsfont; font-size: 11px; color:white;">
        <p>Escape98</p>
        </div>
        
        <!--Répertoire-->
        <div style="position: absolute; left: 27%; top: 40px; font-family: windowsfont; font-size: 14px;">
        <p>explorateur/Escape98</p>
        </div>
        
        <!--Nom de l'onglet-->
        <div style="position: absolute; left: 24%; top: 120px; font-family: arialbl; font-size: 35px;">
        <p>Escape 98<br>Système</p>
        </div>
    
    
    """
    
    if scr=="3dmaze": #Affiche l'écran de veille "Labyrinthe 3D"
        page+=scrsaver
        page+='<img class="centrer" src="/static/images/screensaver/3dmaze.gif" alt="3dmaze" width="480"></div>'
    elif scr=="flowerbox": #Affiche l'écran de veille
        page+=scrsaver
        page+='<img class="centrer" src="/static/images/screensaver/flowerbox.gif" alt="flowerbox" width="480"></div>'
    elif scr=="windows": #Affiche l'écran de veille
        page+=scrsaver
        page+='<img class="centrer" src="/static/images/screensaver/windows.gif" alt="windows" width="480"></div>'
    elif scr=="binaire1": #Affiche du texte en binaire
        page+=scrsaver+scrbinaire1txt
    elif scr=="binaire2": #Affiche du texte en binaire
        page+=scrsaver+scrbinaire2txt
    elif scr=="solution": #Affiche du texte en binaire
        page+=scrsaver+scrsolutiontxt
    elif scr=="binaire4": #Affiche du texte en binaire
        page+=scrsaver+scrbinaire4txt
    elif scr=="1975": #Affiche du texte écrit en russe
        page+=scrsaver+scrsecrettxt
        
    page+='</div>'
    page+=bdpethoraire()
    
    return page





@app.route("/discord", methods = ['GET']) 
   
def discord(): #Discord

    w98 = flask.request.args
    discordID = w98['id']
    discordCONV= w98['convo']
    
    page=entete
    page+=barretache+barrehaut
    page+="""
    """
    
    if discordID=="umphathi wenkululeko" and discordCONV=="": #Si on a entré le mot de passe, et qu'aucune conversation est choisit, nous affiche le menu Discord 
        page+=discordboutons+"""
        <img usemap="#barre" class="centrer" src="/static/images/discord/accueil.webp" width="776" alt="discord">
        
        <div style="position: absolute; top: 200px; left: 70%; font-family: impact; font-size:20px; color: white;">
            <p>i</p>
        </div>
        
        """
        
    elif discordID=="umphathi wenkululeko" and discordCONV=="1": #Affiche la conversation 1
        page+=discordboutons+"""
        <img usemap="#barre" class="centrer" src="/static/images/discord/convo1.webp" width="776" alt="discord">
        """
        
    elif discordID=="umphathi wenkululeko" and discordCONV=="2": #Affiche la conversation 2
        page+=discordboutons+"""
        <img usemap="#barre" class="centrer" src="/static/images/discord/convo2.webp" width="776" alt="discord">
        """
        
    elif discordID=="umphathi wenkululeko" and discordCONV=="222": #Affiche la conversation caché
        page+=discordboutons+"""
        <img usemap="#barre" class="centrer" src="/static/images/discord/convo222.webp" width="776" alt="discord">
        
        <div style="position: absolute; top: 41px; left: 40%; font-family: impact; font-size:15px; color: blue;">
            <p>a</p>
        </div>

        """
        
    else: #Si l'utilisateur n'est pas connecté, il est diriger vers la page de connexion.
        page+="""
        <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Visiblement,\nl'identifiant demandé est le même que celui\nsur la page de connexion du site russe..."/>
        </map>
        <img usemap="#barre" class="centrer" src="/static/images/discord/connection.webp" width="776" alt="discord">
        
        <form action ="/discord" method="get">\n 
            <div style="position: absolute; left: 30%; top: 240px;"> 
                <input type="text" name="id" size="12">\n
                <input type="HIDDEN" name="convo" value=""> <!--Créer une entrée cacher. Elle me permet de remplire l'input "convo" (avec aucune valeur), et d'éviter que le site plante-->
                <input type="submit" value=">">\n
            </div>
        </form>
        """
        
    
    page+='</div>'+bdpethoraire()
    
    return page

















@app.route("/iexplorer/connexion", methods = ['GET']) 

def ieconnexion(): #La page de connexion du site russe sur Internet Explorer REMARQUE: Même si c'est une page de connexion, le formulaire est envoyer via la méthode GET, et non POST (ce qui aurait plutôt préférable pour une page de connexion). Mais pour éviter tout soucis avec d'autres pages du site (qui aurait de la page de chargement d'internet explorer pour chargé une page), j'ai préféré laisser le formulaire avec la méthode GET.
    page=entete
    page+=barretache+croix
    page+="""
    <area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Pour un monde meilleur,\nUtilisez Deepl plutôt que\nGoogle Traduction."/>
    </map>
    <link rel="stylesheet" href="../static/style.css" type="text/css">
    <img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/siterusse.webp" width="776" alt="site russe">
    <div style="position: absolute; left: 23%; top: 100px;">
        <img class="centrer" src="/static/images/InternetExplorer/logomafia.webp" width="400" alt="Logo mafia russe">
    </div>


    <form action ="/iexplorer/connexion/chargement" method="get">
    <div style="position: absolute; left: 43%; top: 250px; color:white; width:200px;">
    <label>Идентификатор</label> : <input type="text" name="identifiant"><br> <!--Identifiant-->
    <label>Пароль</label> : <input type="password" name="mdp"><br> <!--Mot de passe-->
    </div>
    
                
    <div style="position: absolute; left: 28%; top: 430px; color:white;">
    <input type="radio" id="C1" name="chien" value="chien1" checked="checked">
    <label for="C1">Chien 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                
    <input type="radio" id="C2" name="chien" value="chien2">
    <label for="C2">Chien 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                
    <input type="radio" id="C3" name="chien" value="chien3">
    <label for="C3">Chien 3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                
    <input type="radio" id="C4" name="chien" value="chien4">
    <label for="C4">Chien 4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                
    <input type="radio" id="C5" name="chien" value="chien5">
    <label for="C5">Chien 5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><br>
    </div>
    
    <div style="position: absolute; left: 48%; top: 500px; color:white;">
    <input type="submit" value="Envoyer">\n
    </div></form>

    <div style="position: absolute; left: 27%; top: 350px; display:flex;">
    <img class="centrer" src="/static/images/chiens/ch1.webp" alt="chien 1" width="110">
    <p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
    <img class="centrer" src="/static/images/chiens/ch2.webp" alt="chien 1" width="110">
    <p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
    <img class="centrer" src="/static/images/chiens/ch3.webp" alt="chien 1" width="110">
    <p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
    <img class="centrer" src="/static/images/chiens/ch4.webp" alt="chien 1" width="110">
    <p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
    <img class="centrer" src="/static/images/chiens/ch5.webp" alt="chien 1" width="110">
    </div></div>
    
    
    
   """
    page+=bdpethoraire()
    
    return page











@app.route("/iexplorer/connexion/chargement", methods = ['GET']) 
   
def ieconnexionechargement(): #Redirection vers une page.

    iesearch = flask.request.args
    ide = iesearch['identifiant']
    mdp = iesearch['mdp']
    chien = iesearch['chien']

    page=redir
    if ide=="umphathi wenkululeko" and mdp=="Ninja" and chien=="chien2":
        page+='<meta http-equiv="refresh" content="8; URL=../connexion/resultat?scr=54fds"></head>'
    elif ide=="SDJ35" and mdp=="(èyhjuihud" and chien=="chat":
        page+='<meta http-equiv="refresh" content="2; URL=../connexion"></head>'
    elif ide=="Идентификатор" and mdp=="Пароль" and chien=="chien3":
        page+='<meta http-equiv="refresh" content="2; URL=/quizz98?figure=trgsd"></head>'
    elif ide=="vide" and mdp=="img8" and chien=="img3":
        page+='<meta http-equiv="refresh" content="0.1; URL=/quizz98?figure=imgquestion1"></head>'
    else:
        page+='<meta http-equiv="refresh" content="5; URL=../connexion/resultat?scr=echec"></head>'
    
    page+=barretache
    page+="""
    <area shape="rect" coords="680,580,700,1000" href="" alt="lampe" title="Quand on est le meilleur,\non prend le temps de faire correctement\nles choses.\n\n\nInternet Explorer n'a pas planté."/>
    </map>
    <link rel="stylesheet" href="../../static/style.css" type="text/css">
    <img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/siterusse.webp" width="776" alt="fond">
    <div style="position: absolute; left: 44%; top: 250px; color:white; font-family: windowsfont;">
    <img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/ie.gif" width="50" alt="chargement">
    <p>Chargement de la page...</p></div>
    """
    page+=bdpethoraire()
    
    return page










@app.route("/iexplorer/connexion/resultat", methods = ['GET']) 
   
def ieconnexionresultat(): #Affiche en fonction de si vous êtes arriver à vous connecter au compte ou non.

    iesearch = flask.request.args
    res = iesearch['scr']

    page=entete
    page+=barretache
    page+="""
    <area shape="rect" coords="680,580,700,1000" href="" alt="Bureau" title="Je dort !"/>
    </map><link rel="stylesheet" href="../../static/style.css" type="text/css">"""
    
    if res=='54fds': #Si vous avez réussit votre quête, vous serez redirigé ici.
        page+="""<img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/iexplorer_info.webp" width="776" alt="bureau grisé">"""
        page+=scrsaver+"""
        <h1>Macro Espion 2000</h1>
        <p>
        Félicitations !<br>
        Vous avez réussi à nous aider à accéder à ce compte Administrateur !<br>
        <br><br>
        Grâce à cela, nous pouvons désormais fouiller la base de données.<br>
        Cette organisation a déjà fait 6 attaques contre la France, et 16<br>
        tentatives d'attaque.<br>
        <br>
        Merci de nous avoir fait confiance...
        </p><br>
        <h2><i>A bientôt !</i></h2>
        
<pre>L'union des agents secrets vous remercie...</pre>
        </div></div>
        """
    elif res=='echec': #Si vous n'avez pas entrer le bon mot de passe ou le bon identifiant, ou encore si vous n'avez pas choisit la bonne image.
        page+="""<img usemap="#barre" class="centrer" src="/static/images/InternetExplorer/siterusse.webp" width="776" alt="site russe">"""
        page+=scrsaver+"""
        <h1>НАРУШЕНИЕ СОЕДИНЕНИЯ</h1>
        <p>
        Ваше имя пользователя,<br>
        пароль или выбранное изображение не соответствуют действительности.<br>
        <br>
        В случае повторных ошибок мы сохраним ваш IP-адрес в архиве на<br>
        наших серверах.<br>
        Вы рискуете подвергнуться атаке на вашу интернет-сеть или даже<br>
        больше.
        </p></div></div>
        """

    else: #Impossible de faire une redirection depuis cette page, donc j'affiche le bureau grisé, où seulement la barre des tâches est fonctionnel.
        page+="""<img usemap="#barre" class="centrer" src="/static/images/ExpW98/bureau_gris.webp" width="776" alt="bureau grisé"></div>"""
    page+=bdpethoraire()
    
    return page



app.run() 

