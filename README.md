# vuokralaiteSovellus

Sovellusta voi testata [Herokussa](https://vuokralaitesovellus.herokuapp.com)


Sovelluksen avulla pidetään kirjaa vuokratuista laitteista ja niiden huollosta. Sovellus näyttää vuokralaitteet ja vuokrassa olevat laitteet.
 
Sovelluksen ominaisuuksia:
- Käyttäjjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Pääkäyttäjä voi lisätä ja poistaa vuokralaitteita
- Pääkäyttäjä voi lisätä käyttäjälle pääkäyttäjän oikeudet
- Käyttäjä voi lisätä vuokraajan ja vuokrata hänelle laitteen
- Laitteisiin voi merkata huollon
- Käyttäjä voi listata laitteita vuokra-ajan umpeutumisen mukaan
- Käyttäjä voi tutkia tilastoja suosituimmasta vuokrauslaitteesta
- Laitteille voi lisätä tyypin (esimerkiksi ilmanpuhdistin), kuvauksen, mallin (esimerkiksi Lifa Air 352C), huollot ja vuokrausjaksot



### Tämän hetken toiminnallisuudet

Tällä hetkellä sovellukseen voi luoda käyttäjätunnuksen ja kirjautua. Lisäksi on mahdollista lisätä asiakas, joka tallentuu tietokantaan. Sovelluksessa on myös linkki laitteen lisäämiseen, se ei kuitenkaan tee vielä mitään, eli tieto ei tallennu tietokantaan. 

Jos yrität luoda käyttäjätunnuksen, joka on jo olemassa, saat siitä virheviestin, että se ei ole mahdollista. Salasanan ja käytttäjätunnuksen on lisäksi oltava vähintään 3 merkkiä pitkiä. Myös virheellisestä salasanasta tai käyttäjätunnuksesta tulee virheviesti. 

