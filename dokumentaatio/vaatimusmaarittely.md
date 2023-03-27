# Vaatimusmäärittely

## PROJEKTI LYHYESTI:
- Käyttäjä voi luoda yksinkertaisen ympäristön ja sen parametrit
- Käyttäjä pystyy määrittelyn jälkeen simuloida ympäristön
- Simuloitu ympäristö sisältää olioita 
- Simuloitujen olioiden toiminta riippuu asetetuista parametreistä, ja soveltuu niihin
- Oliot kokevat mutaatioita lisääntyessään, jotka ajankuluessa aiheuttavat oliolajin soveltumisen ympäristöön

## Toiminta käytännössä:
- ohjelma jakautuu kahteen selvään vaiheeseen: suunnittelu, ja simulaatio
- suunnittelussa käyttäjä voi vaikuttaa olosuhteisiin ennen simulaatiota
- simulaatiossa käyttäjä pystyy seurata simulaatiota ja tallentaa olentoja ja tilanteita
- simulaatio vaihe tarjoaa myös vaihtoethoja olioiden tarkastelemiselle yksityiskohtaisemmin

## Käyttöliittymä
- Ensin yksinkertainen ja tekstipohjainen.
- mahdollista kehittää monimutkaisemmaksi, loppullisesti graaffinen 

## Näkymät
- Alkuun ASCII merkeillä kuvatut olosuhteet helppouden kannalta.
- graaffiset ja kuvitetut kuvakkeet solujen sisällölle

## Käyttäjät
- Käyttäjätyyppejä olisi vain yksi
- Käyttäjä voi tallentaa omia tilanteitaan ja avata muiden omia

## Oliot ja Maailma
- Maailmassa olisi staattisia ja elollisia solutyyppejä.
- Staattiset solut toimisivat typpinsä sääntöjen mukaisesti. (korkea paine pyrkii tasautumaan)
- Elolliset solut kykenisivät monimutkaisempiin toimintoihin ja menehtyvät ilman energiaa, muuttuen staattiseksi.
- Tyhjät Staattiset solut täyttyvät energialla (riippuen olosuhde määrittelystä)
- Mikäli tyhjä solu on täynnä ennergiaa, siihen saattaa syntyä ravintoa
- Eliöt kykenevät keräämään energiaa syömällä ravintoa
- Menehtyneet eliöt muuttuvat staattiseksi ravinnoksi
- Eliöt kykenevät käyttämään huomattavan määrän energiaa itsensä kopioimiseen (mitoosi)
- Eliön kopiointiprosessi ei ole virheetön ja sisältää mutaatioita
- Eliön toiminta riippuu geeneistä, jotka periytyvät kopioille (mahdollisesti mutaatioilla)
- Eliöt kykenevät manipuloimaan ympäristöään
