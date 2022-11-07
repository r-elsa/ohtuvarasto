import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    
    def test_lisays_yli_palautus_tilavuus_nolla(self):
        varasto = Varasto(10,10) 
        varasto.lisaa_varastoon(100)
        self.assertEqual(str(varasto), "saldo = 10, vielä tilaa 0")
        

   
    def test_ottaminen_yli_palautus_saldo_nolla(self):
        varasto = Varasto(10,10)
        varasto.lisaa_varastoon(3)
        saatu_maara = varasto.ota_varastosta(100)
        self.assertAlmostEqual(varasto.saldo, 0.0)


    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-10,10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)
    

    def test_negatiivinen_saldo(self):
        varasto = Varasto(0,-10)
        self.assertAlmostEqual(varasto.saldo, 0.0)
  
    
    def test_lisays_negatiivinen_tilavuus_(self):
        varasto = Varasto(10, 5)
        varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(varasto.tilavuus, 10)


    def test_otavarastosta_negatiivinen(self):
        varasto = Varasto(7)
        varasto.lisaa_varastoon(3)
        saatu_maara = varasto.ota_varastosta(-100)
        self.assertAlmostEqual(varasto.tilavuus, 7)
    
    def test_positiivinen_alkusaldo(self):
        varasto = Varasto(7, 15)
        self.assertAlmostEqual(varasto.saldo, 7)