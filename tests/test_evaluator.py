from harness.evaluator import Evaluator

class FakePassingTask:

    TEST_CASES = [
        {"input": {"x":2}, "expected":4},
        {"input": {"x":3}, "expected":9},
    ]

    @staticmethod
    def solve(x):
        return x * x


class FakeFailingTask:

    TEST_CASES = [
        {"input": {"x":2}, "expected":4},
        {"input": {"x":3}, "expected":100},
    ]

    @staticmethod
    def solve(x):
        return x * x



def test_evaluator_all_pass():
    evaluator = Evaluator()
    result = evaluator.evaluate(FakePassingTask)
    assert result["passed"] ==2
    assert result["total"]==2



def test_evaluator_all_fail():
    evaluator = Evaluator()
    result = evaluator.evaluate(FakeFailingTask)
    assert result["passed"] ==1
    assert result["total"]==2