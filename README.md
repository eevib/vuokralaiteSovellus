# Vuokralaitesovellus

Sovellusta voi testata [Herokussa](https://vuokralaitesovellus.herokuapp.com)


Sovelluksen avulla pidetään kirjaa vuokratuista laitteista ja niiden huollosta. Sovellus näyttää vuokralaitteet ja vuokrassa olevat laitteet. Sovelluksessa voi luoda tunnuksen ja kirjautua sisään ja ulos, kaikki käyttäjät näkevät kuitenkin samat tiedot. Virheellisiä syötteitä ei sallita ja niistä tulee virheviesti. Toiminnot on sovelluksessa hajautettu omille välilehdille. 
 
Sovelluksen ominaisuuksia:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi lisätä asiakkaan ja vuokrata hänelle laitteen.
- Laitteisiin voi merkata huollon.
- Laitteet listataan vuokra-ajan umpeutumisen mukaan. 
- Asiakkaat listataan aakkosjärjestyksessä
- Asiakkaalta tallennetaan nimi ja sähköpostiosoite.
- Laitteille annetaan tyyppi (esimerkiksi ilmanpuhdistin) ja malli (esimerkiksi Lifa Air 352C), lisäksi on mahdollista lisätä kuvaus.
- Laitetta vuokratessa annetaan asiakkaan ja laitteen id, vuokrauksen aloitus ja lopetuspäivä.
- Huoltoon annetaan laite id, päivämäärä ja kuvaus huollosta. 

  

### Kehitysehdotukset

Sovellusta on mahdollista kehittää vielä huimasti eteenpäin. Tässä muutama jatkokehitysidea: 

- Hakutoiminto asiakkaille, laitteille ja vuokrausjaksoille. 
- Mahdollisuus vuokrata vain vapaana olevia laitteita.
- Eri käyttäjille vain oman / ryhmän tietojen näyttö.
- Pääkäyttäjä, joka huolehtisi omaan ryhmään lisäämisestä.
- Laitteen, asiakkaan, vuokrauksen ja huollon poisto.
- Tilastojen näyttäminen eri laitteille.
- Asiakkaiden, laitteiden, huoltojen ja vuokrausten listaus / haku esimerkiksi laitetyypin mukaan. 
- Mahdollisuus muokata huolto tai vuokraus tapahtumia. 
