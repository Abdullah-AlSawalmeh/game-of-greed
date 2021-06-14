from tests.flow.flo import Flo

def test_bank_one_roll_then_quit():
    Flo.test("tests/flow/bank_one_roll_then_quit.sim.txt")