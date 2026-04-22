from services.metrics import follow_up_summary


def test_follow_up_summary_tracks_due_and_overdue_leads():
    summary = follow_up_summary()
    assert summary['due_today'] >= 0
    assert summary['overdue'] >= 0
    assert summary['won_this_week'] >= 0
