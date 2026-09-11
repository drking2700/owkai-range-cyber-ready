from range_app.missions import list_missions, load_manifest

def test_all_16_missions_exist_and_ai_native():
    ms=list_missions()
    assert len(ms)==16
    assert [m['id'] for m in ms]==list(range(1,17))
    for m in ms:
        assert m['ai_native_dimension']
        assert m['verification']
        assert m['aar_questions']

def test_human_review_checkpoints():
    assert load_manifest(8)['human_review_required'] is True
    assert load_manifest(12)['human_review_required'] is True
    assert load_manifest(16)['human_review_required'] is True
