import pytest

from yegorcallcenter.CallStatus import BasicCallStatus


@pytest.fixture
def call_status():
    return BasicCallStatus()


def test_call_status_init(call_status):
    # Test that a new call is in progress
    assert call_status.in_progress()

    # Test that the escalation level is initially 0
    assert call_status.escalation_level() == 0


def test_call_escalation(call_status):
    # Test that the escalation level is incremented when a call is escalated
    call_status.escalate_call()
    assert call_status.escalation_level() == 1


def test_call_in_progress(call_status):
    # Test that a call can be set as not in progress
    call_status.stop_call()
    assert not call_status.in_progress()

    # Test that a call can be set back to in progress
    call_status.start_call()
    assert call_status.in_progress()
