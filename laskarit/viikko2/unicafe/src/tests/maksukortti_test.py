import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.kortti = Maksukortti(1000)
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortilla_saldo(self):
        self.kortti = Maksukortti(1000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voidaan_lisätä_rahaa(self):
        self.kortti = Maksukortti(1000)
        self.kortti.lataa_rahaa(1500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 25.00 euroa")
    
    def test_raha_vähenee_jos_saldoa(self):
        self.kortti = Maksukortti(1000)
        returni = self.kortti.ota_rahaa(1500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_raha_ei_vähene_jos_broke(self):
        self.kortti = Maksukortti(1000)
        self.kortti.ota_rahaa(1500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_raha_vähenee_jos_saldoa_palautus(self):
        self.kortti = Maksukortti(2000)
        returni = self.kortti.ota_rahaa(1500)

        self.assertEqual(True, returni)

    def test_raha_ei_vähene_jos_broke_palautus(self):
        self.kortti = Maksukortti(1000)
        returni = self.kortti.ota_rahaa(1500)

        self.assertEqual(False, returni)
