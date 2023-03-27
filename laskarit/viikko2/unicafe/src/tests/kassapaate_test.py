import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    # Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)
    def test_luotu_kassa_on_olemassa(self):
        self.kassa = Kassapaate()
        self.assertNotEqual(self.kassa, None)

    def test_luotu_kassa_saldo(self):
        self.kassa = Kassapaate()
        self.assertEqual((self.kassa.kassassa_rahaa), 100000)
    
    def test_luotu_kassa_myynnit(self):
        self.kassa = Kassapaate()
        self.assertEqual((self.kassa.edulliset + self.kassa.maukkaat), 0)

    # Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_käteismaksu_edullisesti(self):
        self.kassa = Kassapaate()
        self.kassa.syo_edullisesti_kateisella(241)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100240)
    
    def test_käteismaksu_edullisesti_vaihtoraha(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(100240)

        self.assertEqual(vaihtoraha, 100000)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_käteismaksu_edullisesti_määrä(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(100240)

        self.assertEqual(self.kassa.edulliset, 1)
    
    # maukkaat !!!!!!!!!
    def test_käteismaksu_maukkaat(self):
        self.kassa = Kassapaate()
        self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100400)
    
    def test_käteismaksu_maukkaat_vaihtoraha(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(100400)

        self.assertEqual(vaihtoraha, 100000)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_käteismaksu_maukkaat_määrä(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(100400)

        self.assertEqual(self.kassa.maukkaat, 1)
    
    # Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
    def test_käteismaksu_edullisesti_neg(self):
        self.kassa = Kassapaate()
        self.kassa.syo_edullisesti_kateisella(239)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100000)
    
    def test_käteismaksu_edullisesti_vaihtoraha_neg(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(40)

        self.assertEqual(vaihtoraha, 40)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_käteismaksu_edullisesti_määrä_neg(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassa.edulliset, 0)

    #MAUKKAAT
    def test_käteismaksu_maukkaasti(self):
        self.kassa = Kassapaate()
        self.kassa.syo_maukkaasti_kateisella(239)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100000)
    
    def test_käteismaksu_maukkaasti_vaihtoraha(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(40)

        self.assertEqual(vaihtoraha, 40)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_käteismaksu_maukkaasti_määrä_neg(self):
        self.kassa = Kassapaate()
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassa.edulliset, 0)
    
    # Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_korttimaksu_edullisesti(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        onnistuminen = self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(onnistuminen , True)
    
    def test_korttimaksu_maukkaasti(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        onnistuminen = self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(onnistuminen , True)
    
    # KORTTISALDO
    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    def test_korttimaksu_edullisesti_korttisaldo(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        onnistuminen = self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo , 1000-240)
    
    def test_korttimaksu_maukkaasti_korttisaldo(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        onnistuminen = self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo , 1000-400)
    
    
    
    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    def test_korttimaksu_edullisesti_määrä_neg(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10)
        vaihtoraha = self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttimaksu_edullisesti_määrä(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10000)
        vaihtoraha = self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_korttimaksu_maukkaasti_määrä_neg(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10)
        vaihtoraha = self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttimaksu_maukkaasti_määrä(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10000)
        vaihtoraha = self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.maukkaat, 1)

    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_korttimaksu_edullisesti_kassa_ei_muutu(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100000)
    
    def test_korttimaksu_maukkaasti_kassa_ei_muutu(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual((self.kassa.kassassa_rahaa ), 100000)

    # Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_lataa_rahaa(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(0)

        self.kassa.lataa_rahaa_kortille(self.kortti, 10)

        self.assertEqual((self.kortti.saldo ), 10)
    
    def test_lataa_rahaa_kassa(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(0)

        self.kassa.lataa_rahaa_kortille(self.kortti, 10)

        self.assertEqual(self.kassa.kassassa_rahaa, 100010)
    
    def test_lataa_rahaa_negatiivinen_määrä(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(0)

        self.kassa.lataa_rahaa_kortille(self.kortti, -10)

        self.assertEqual(self.kortti.saldo, 0)
    

