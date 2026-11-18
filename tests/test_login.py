def test_login(app):
    app.session.login("administrator", "root")
    assert app.soap.can_login("administrator", "root")
