import unittest
import tests_12_3

suite_st = unittest.TestSuite()
suite_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_st)