# Rokotuskanta
Tietokantasovellus kurssin harjoitustehtävä / Rokotuskanta

Sovellus, johon hoitajat kirjaavat asiakkaille annetut koronarokotukset. Lääkärit voivat muokata tietoja. Asiakkaat itse voivat vain katsoa omia tietojaan.
Sovelluksen kautta voi tehdä kattavasti hakuja kantaan.

Sovelluksen ominaisuudet:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen *(tehty)*
- Hoitaja voi kirjata uuden koronarokotuksen (korotuspaikka, pvm, koroteen nimi, 1. vai 2. vaihe, asiakkaan nimi, korottajan nimi) *(tehty)*
- Hoitaja voi jatkaa koronakorotuksen kirjausta, jos esim asiakas tulee 2. vaiheen rokotukseen *(tehty)*
- Lääkäri voi muokata kaikkia tietoja *(tehty)*
- Asiakas voi katsella vain omia tietojaan omilla tunnuksillaan *(tehty)*
- Kantaan voidaan tehdä hakuja (monta rokotusta, missä paikoissa, montako 1. vaiheen, päivämäärä tilasto, yms) *(tehty osaksi)*
- Käyttäjä ja hänen tiedot voidaan poistaa kannasta *(tehty)*

Mahdollisia lisäominaisuuksia:
- asiakas voi antaa palautetta rokotustilanteesta
- asiakas voi tulostaa itselleen rokotustodistuksen

## Lopullinen palautus

Ohjelma on testavissa osoitteessa https://rokotuskanta.herokuapp.com/

Käyttöohjeet:
- Luo uusi käyttäjä
- Kirjaudu sisään (voi käyttää valmiita testitunnuksia)
- Lisää rokotustiedot (Hoitaja ja Lääkäri -oikeudella)
- Katsele rokotusrekisteriä (Hoitaja ja Lääkäri -oikeudella)
- Katsele raporttia

Käyttäjäoikeudet:
- Ohjelmassa on kolme tasoa käyttäjäoikeuksia
- Lääkäri -oikeudella on pääsy kaikkiin tietoihin
- Hoitaja -oikeudella voi kirjata ja muuttaa rokotustietoja
- Käyttäjä -oikeudella voi katsella omia tietoja ja raportteja

Valmiit testikäyttäjät:
- laakari / password1 (Lääkäri -oikeudet)
- hoitaja / password1 (Hoitaja -oikeudet)
- user / password1 (Käyttäjä -oikeudet)

Viimeiseen palautukseen toteutetut toiminnallisuudet:
- Käyttäoikeuksien toteutus
- Palautuksen viimeistely

## Välipalautus 3

Ohjelma on testavissa osoitteessa https://rokotuskanta.herokuapp.com/

Käyttöohjeet:
- Luo uusi käyttäjä
- Kirjaudu sisään
- Lisää rokotustiedot
- Katsele rokotusrekisteriä
- Katsele raporttia

Välipalautuksen tehnyt toiminnallisuudet:
- Palautteissa mainitut puutteet korjattu
- Sivujen ulkoasu muokattu
- Hallintasivua kähitetty (käyttäjän voi poistaa)
- Käyttäjäoikeuksia ei ole toteutettu, kaikilla käyttäjille täydet oikeudet
- Uusi valikko, joka muokkautuu sen mukaan onko kirjautunut
- Kirjautumisen tarkistus jokaisella sivulla

Seuraavaksi toteutettavat toiminnallisuudet:
- Käyttäoikeuksien toteutus
- Palautuksen viimeistely


## Välipalautus 2

Ohjelma on testavissa osoitteessa https://rokotuskanta.herokuapp.com/

Käyttöohjeet:
- Luo uusi käyttäjä
- Kirjaudu sisään
- Lisää rokotustiedot
- Katsele rokotusrekisteriä

Välipalautuksen tilanne:
- Ohjelman päätoiminnallisuudet on toteutettu (rekisteröinti, kirjautuminen, tietojen lisäys, tietojen selaus, hallintasivu)
- Tietokannan rakenne valmiina
- Käyttäjäoikeuksia ei ole toteutettu, kaikilla käyttäjille täydet oikeudet

Seuraavaksi toteutettavat toiminnallisuudet:
- Sivujen ulkoasu
- Käyttäoikeuksien toteutus
- Tietojen muutos -sivun toteutus
- Hallintasivun jatkokehitys
- Käyttäjien poistaminen
- Raportointi -sivun toteutus

