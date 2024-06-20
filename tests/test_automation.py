import unittest
from src.automation import enviar_ecd

class TestAutomation(unittest.TestCase):
    def test_enviar_ecd(self):
        # Aqui você pode adicionar testes para a função enviar_ecd
        # Por exemplo, verificar se a função completa sem erros
        try:
            enviar_ecd('12345678000195', '01/2023')
        except Exception as e:
            self.fail(f"enviar_ecd raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
